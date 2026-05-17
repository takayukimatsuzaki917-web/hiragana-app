"""
CSSアニメーションや視覚エフェクトのユーティリティ。
正解時の花火・星降りエフェクトなどを提供する。
"""

import streamlit as st


def inject_global_css() -> None:
    """
    アプリ全体に適用するCSSをHTMLとして注入する。
    iPhone Safariでも快適に使えるサイズ・色設定を行う。
    """
    css = """
    <style>
    /* ===== 全体レイアウト ===== */
    .stApp {
        background-color: #FFF9C4;  /* 明るいパステルイエロー */
    }

    /* ===== ボタン（子どもが押しやすい大きさ） ===== */
    .stButton > button {
        font-size: 1.5rem !important;
        padding: 1rem 2rem !important;
        border-radius: 1rem !important;
        width: 100% !important;
        font-weight: bold !important;
        transition: transform 0.1s ease !important;
    }

    /* ボタンを押したときのアニメーション */
    .stButton > button:active {
        transform: scale(0.95) !important;
    }

    /* 正解ボタン（緑） */
    .stButton > button[data-testid="correct-btn"] {
        background-color: #4CAF50 !important;
        color: white !important;
        border: none !important;
    }

    /* 再挑戦ボタン（オレンジ） */
    .stButton > button[data-testid="retry-btn"] {
        background-color: #FF9800 !important;
        color: white !important;
        border: none !important;
    }

    /* 次の文字ボタン（青） */
    .stButton > button[data-testid="next-btn"] {
        background-color: #2196F3 !important;
        color: white !important;
        border: none !important;
    }

    /* ===== ひらがな大文字表示 ===== */
    .hiragana-display {
        font-size: 200px;
        font-weight: bold;
        text-align: center;
        color: #1A237E;
        line-height: 1.1;
        font-family: 'Noto Sans JP', 'Hiragino Rounded Gothic Pro', 'Yu Gothic', sans-serif;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.15);
    }

    /* ===== 進捗表示 ===== */
    .progress-display {
        font-size: 1.3rem;
        font-weight: bold;
        text-align: center;
        color: #5D4037;
        padding: 0.5rem;
        background-color: rgba(255,255,255,0.7);
        border-radius: 1rem;
        margin-bottom: 0.5rem;
    }

    /* ===== 促しテキスト ===== */
    .prompt-text {
        font-size: 1.5rem;
        text-align: center;
        color: #6A1B9A;
        font-weight: bold;
        margin: 0.3rem 0;
    }

    /* ===== 単語カード ===== */
    .word-card {
        background-color: white;
        border-radius: 1rem;
        padding: 0.8rem;
        text-align: center;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        margin: 0.3rem;
    }

    /* 単語の先頭文字（赤・太字で強調） */
    .word-first-char {
        color: #D32F2F;
        font-weight: bold;
        font-size: 1.4rem;
    }

    /* 単語の残りの文字 */
    .word-rest-chars {
        font-size: 1.3rem;
        color: #333;
    }

    /* 絵文字の大きさ */
    .word-emoji {
        font-size: 3rem;
        display: block;
    }

    /* ===== 正解メッセージ ===== */
    .success-message {
        font-size: 2rem;
        font-weight: bold;
        text-align: center;
        color: #FF6F00;
        animation: pop-in 0.4s ease-out;
    }

    /* ===== ポップインアニメーション ===== */
    @keyframes pop-in {
        0%   { transform: scale(0.5); opacity: 0; }
        70%  { transform: scale(1.1); opacity: 1; }
        100% { transform: scale(1.0); opacity: 1; }
    }

    /* ===== 花火エフェクト（CSS星降り） ===== */
    .firework-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;  /* クリックを透過させる */
        z-index: 9999;
        overflow: hidden;
    }

    /* 星のパーティクル */
    .firework-particle {
        position: absolute;
        font-size: 2rem;
        animation: fall-down 2s ease-in forwards;
        opacity: 1;
    }

    /* 星が上から落ちてくるアニメーション */
    @keyframes fall-down {
        0%   { transform: translateY(-50px) rotate(0deg); opacity: 1; }
        100% { transform: translateY(110vh) rotate(720deg); opacity: 0; }
    }

    /* ===== サイドバー（親モード）の文字サイズ ===== */
    .stSidebar .stMarkdown {
        font-size: 1.1rem !important;
    }

    .stSidebar .stMultiSelect label,
    .stSidebar .stRadio label {
        font-size: 1.1rem !important;
    }

    .stSidebar .stButton > button {
        font-size: 1.2rem !important;
        padding: 0.8rem 1.5rem !important;
    }

    /* ===== iPhone Safariのズーム防止 ===== */
    input, select, textarea {
        font-size: 16px !important;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


def show_fireworks() -> None:
    """
    正解時に花火エフェクト（CSSアニメーション）を表示する。
    st.balloons() と組み合わせて使う。
    """
    # 絵文字パーティクルをランダムな位置に配置
    particles_html = ""
    emojis = ["⭐", "🌟", "✨", "🎉", "🎊", "🌈", "💫", "🎈", "🏆", "💖"]
    positions = [
        (5, 0.3), (15, 0.8), (25, 0.2), (35, 1.0), (45, 0.5),
        (55, 0.1), (65, 0.7), (75, 0.4), (85, 0.9), (92, 0.6),
    ]

    for i, (left_pct, delay) in enumerate(positions):
        emoji = emojis[i % len(emojis)]
        particles_html += (
            f'<div class="firework-particle" '
            f'style="left:{left_pct}%; animation-delay:{delay:.1f}s;">'
            f"{emoji}</div>"
        )

    html = f"""
    <div class="firework-container" id="firework-container">
        {particles_html}
    </div>
    <script>
        // 2.5秒後にエフェクトを自動削除
        setTimeout(function() {{
            var el = document.getElementById('firework-container');
            if (el) el.remove();
        }}, 2500);
    </script>
    """
    st.markdown(html, unsafe_allow_html=True)


def show_success_message(message: str = "やったー！すごい！🎉") -> None:
    """
    正解時の祝福メッセージをポップインアニメーションで表示する。

    Args:
        message: 表示するメッセージ
    """
    html = f'<div class="success-message">{message}</div>'
    st.markdown(html, unsafe_allow_html=True)
