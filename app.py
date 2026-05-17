"""
ひらがな学習アプリ（3歳児向け）
streamlit run app.py で起動する。
"""

import random
import streamlit as st

from data.hiragana_data import HIRAGANA_DATA, HIRAGANA_GROUPS, HIRAGANA_DICT
from utils.audio import (
    get_correct_sound_b64,
    get_retry_sound_b64,
    make_audio_html,
)
from utils.effects import inject_global_css, show_fireworks, show_success_message

# =====================================================================
# ページ設定（一番最初に呼ぶ必要がある）
# =====================================================================
st.set_page_config(
    page_title="ひらがなをおぼえよう！",
    page_icon="🌟",
)

# グローバルCSSを注入
inject_global_css()

# =====================================================================
# セッション状態の初期化（初回起動時のみ実行）
# =====================================================================

def _init_session_state() -> None:
    """セッション変数を初期化する。すでに存在するキーはスキップする。"""

    # 練習対象のひらがなリスト（デフォルトは全46文字）
    if "selected_hiragana" not in st.session_state:
        st.session_state.selected_hiragana = [d["char"] for d in HIRAGANA_DATA]

    # 出題順モード（"ランダム" or "じゅんばん"）
    if "order_mode" not in st.session_state:
        st.session_state.order_mode = "ランダム"

    # 出題キュー（まだ出ていない文字のリスト）
    if "question_queue" not in st.session_state:
        st.session_state.question_queue = _build_queue(
            st.session_state.selected_hiragana,
            st.session_state.order_mode,
        )

    # 現在表示中のひらがな
    if "current_char" not in st.session_state:
        st.session_state.current_char = _pop_next_char()

    # 正解数・挑戦数
    if "correct_count" not in st.session_state:
        st.session_state.correct_count = 0
    if "total_count" not in st.session_state:
        st.session_state.total_count = 0

    # 正解した直後かどうか（花火・音を一度だけ表示するフラグ）
    if "just_correct" not in st.session_state:
        st.session_state.just_correct = False

    # 再挑戦した直後かどうか
    if "just_retry" not in st.session_state:
        st.session_state.just_retry = False

    # 次の文字へ移った直後かどうか（ページ先頭へスクロールするためのフラグ）
    if "scroll_to_top" not in st.session_state:
        st.session_state.scroll_to_top = False


def _build_queue(chars: list[str], mode: str) -> list[str]:
    """
    出題キューを作成する。

    Args:
        chars: 練習対象のひらがなリスト
        mode: "ランダム" or "じゅんばん"

    Returns:
        出題順に並んだリスト
    """
    queue = list(chars)
    if mode == "ランダム":
        random.shuffle(queue)
    # "じゅんばん" の場合はデータ定義の順番（HIRAGANA_DATA の順）を使う
    else:
        # HIRAGANA_DATA の定義順に並べ直す
        order = [d["char"] for d in HIRAGANA_DATA]
        queue = [c for c in order if c in chars]
    return queue


def _pop_next_char() -> str:
    """
    キューから次の文字を取り出す。
    キューが空になったら再構築してシャッフル。
    """
    if not st.session_state.question_queue:
        # 一周したら再度同じリストで出題
        st.session_state.question_queue = _build_queue(
            st.session_state.selected_hiragana,
            st.session_state.order_mode,
        )
    # キューが空のままなら（selected_hiraganaが空）デフォルト文字を返す
    if not st.session_state.question_queue:
        return "あ"
    return st.session_state.question_queue.pop(0)


_init_session_state()

# =====================================================================
# 親モード サイドバー
# =====================================================================

def render_sidebar() -> None:
    """親設定サイドバーを描画する。"""
    with st.sidebar:
        st.markdown("## ⚙️ おやのせってい")
        st.markdown("---")
        st.markdown("### れんしゅうするひらがなをえらんでね")

        # 全選択 / 全解除ボタン
        col_all, col_none = st.columns(2)
        with col_all:
            if st.button("✅ 全部えらぶ", key="btn_select_all"):
                for gname, gchars in HIRAGANA_GROUPS.items():
                    st.session_state[f"sidebar_{gname}"] = list(gchars)
                st.rerun()
        with col_none:
            if st.button("❌ 全部はずす", key="btn_select_none"):
                for gname in HIRAGANA_GROUPS:
                    st.session_state[f"sidebar_{gname}"] = []
                st.rerun()

        # 行ごとにmultiselectを表示
        new_selected: list[str] = []
        for group_name, chars in HIRAGANA_GROUPS.items():
            # デフォルト：現在選択中の文字を初期値にする
            default = [c for c in chars if c in st.session_state.selected_hiragana]
            chosen = st.multiselect(
                group_name,
                options=chars,
                default=default,
                key=f"sidebar_{group_name}",
            )
            new_selected.extend(chosen)

        st.markdown("---")

        # 出題順ラジオボタン
        order = st.radio(
            "でてくるじゅんばん",
            options=["ランダム", "じゅんばん"],
            index=0 if st.session_state.order_mode == "ランダム" else 1,
            key="sidebar_order",
        )

        st.markdown("---")

        # 「きめた！」ボタン
        if st.button("✅ きめた！", key="sidebar_confirm"):
            if len(new_selected) == 0:
                # 1つも選ばれていない場合は警告
                st.warning("1つ以上えらんでね！")
            else:
                # 設定を確定してキューをリセット
                st.session_state.selected_hiragana = new_selected
                st.session_state.order_mode = order
                st.session_state.question_queue = _build_queue(new_selected, order)
                st.session_state.current_char = _pop_next_char()
                st.session_state.just_correct = False
                st.session_state.just_retry = False
                st.rerun()  # サイドバーを閉じてメイン画面を更新


render_sidebar()

# =====================================================================
# メイン画面
# =====================================================================

# ---- ページ先頭へスクロール（つぎのもじ押下後に一度だけ実行） ----
if st.session_state.scroll_to_top:
    st.markdown(
        "<script>window.parent.scrollTo({top: 0, behavior: 'smooth'});</script>",
        unsafe_allow_html=True,
    )
    st.session_state.scroll_to_top = False

# ---- 進捗表示 ----
progress_html = (
    f'<div class="progress-display">'
    f"⭐ {st.session_state.correct_count}もじ せいかい！　"
    f"（{st.session_state.total_count}かい ちょうせん）"
    f"</div>"
)
st.markdown(progress_html, unsafe_allow_html=True)

# ---- 正解・再挑戦時の効果音（autoplay はPC向け、iPhoneは制限あり） ----
if st.session_state.just_correct:
    sound_html = make_audio_html(get_correct_sound_b64(), autoplay=True)
    st.markdown(sound_html, unsafe_allow_html=True)

if st.session_state.just_retry:
    sound_html = make_audio_html(get_retry_sound_b64(), autoplay=True)
    st.markdown(sound_html, unsafe_allow_html=True)

# ---- ひらがな大文字表示 ----
current_char = st.session_state.current_char
char_data = HIRAGANA_DICT.get(current_char, HIRAGANA_DATA[0])

st.markdown(
    f'<div class="prompt-text">よんでみよう！</div>',
    unsafe_allow_html=True,
)
st.markdown(
    f'<div class="hiragana-display">{current_char}</div>',
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

# ---- 単語カード（3つ）を横並び表示 ----
st.markdown("### この もじ の ことば")

cols = st.columns(3)
for idx, word_data in enumerate(char_data["words"]):
    word: str = word_data["word"]
    emoji: str = word_data["emoji"]

    with cols[idx]:
        # 単語の先頭1文字を赤・太字で強調
        first_char = word[0]
        rest_chars = word[1:]
        word_html = (
            f'<span class="word-first-char">{first_char}</span>'
            f'<span class="word-rest-chars">{rest_chars}</span>'
        )

        # emoji + 単語テキスト
        st.markdown(
            f'<div class="word-card">'
            f'<span class="word-emoji">{emoji}</span>'
            f"{word_html}</div>",
            unsafe_allow_html=True,
        )

st.markdown("<br>", unsafe_allow_html=True)

# ---- 正解時の花火・メッセージ表示 ----
if st.session_state.just_correct:
    show_success_message("やったー！すごい！🎉")
    show_fireworks()
    st.balloons()

# =====================================================================
# アクションボタン（正解 / 再挑戦 / 次へ）
# 中央寄せ：左右に余白カラムを置き、中央エリアにボタンをまとめる
# =====================================================================

_, btn_area, _ = st.columns([1, 3, 1])

with btn_area:
    # 上段：「いえる！」と「もういちど」を横並び
    col_correct, col_retry = st.columns(2)

    with col_correct:
        if st.button("✅ いえる！", key="btn_correct"):
            st.session_state.correct_count += 1
            st.session_state.total_count += 1
            st.session_state.just_correct = True
            st.session_state.just_retry = False
            st.rerun()

    with col_retry:
        if st.button("🔄 もういちど", key="btn_retry"):
            st.session_state.total_count += 1
            st.session_state.just_retry = True
            st.session_state.just_correct = False
            st.rerun()

    # 下段：「つぎのもじ」は上段と同じ幅で横長に
    if st.button("➡️ つぎのもじ", key="btn_next"):
        st.session_state.current_char = _pop_next_char()
        st.session_state.just_correct = False
        st.session_state.just_retry = False
        st.session_state.scroll_to_top = True
        st.rerun()

# =====================================================================
# フッター：おやのせってい ボタン（サイドバーを開くヒント）
# =====================================================================
st.markdown("---")
st.markdown(
    '<div style="text-align:center; color:#888; font-size:0.9rem;">'
    "⬅️ 左のメニューから「おやのせってい」で れんしゅうする もじを えらべるよ"
    "</div>",
    unsafe_allow_html=True,
)
