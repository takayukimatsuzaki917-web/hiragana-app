"""
音声関連のユーティリティ。
- gTTSで日本語テキストを読み上げ（Base64変換してHTMLで再生）
- numpyとscipyでサイン波を合成して効果音を生成（外部ファイル不要）
"""

import io
import base64
import numpy as np
from scipy.io import wavfile
import streamlit as st


# ---- 効果音の生成 ----

def _generate_sine_wave(
    freq: float,
    duration: float,
    sample_rate: int = 44100,
    volume: float = 0.3,
) -> np.ndarray:
    """
    指定した周波数のサイン波を生成する内部関数。

    Args:
        freq: 周波数（Hz）
        duration: 長さ（秒）
        sample_rate: サンプリングレート
        volume: 音量（0.0〜1.0）

    Returns:
        音声データのnumpy配列（int16形式）
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = volume * np.sin(2 * np.pi * freq * t)
    # フェードアウトをかけてクリックノイズを防ぐ
    fade_samples = int(sample_rate * 0.05)  # 最後の50msでフェードアウト
    wave[-fade_samples:] *= np.linspace(1, 0, fade_samples)
    return (wave * 32767).astype(np.int16)


def _wave_to_base64(wave: np.ndarray, sample_rate: int = 44100) -> str:
    """
    numpy配列の音声データをBase64文字列に変換する。

    Args:
        wave: 音声データ（int16形式）
        sample_rate: サンプリングレート

    Returns:
        Base64エンコードされた文字列
    """
    buffer = io.BytesIO()
    wavfile.write(buffer, sample_rate, wave)
    buffer.seek(0)
    return base64.b64encode(buffer.read()).decode("utf-8")


def _make_bell_tone(
    freq: float,
    duration: float,
    sample_rate: int = 44100,
    volume: float = 0.35,
) -> np.ndarray:
    """
    ベル系の音を生成する。
    基音に倍音（2倍・3倍）を重ね、指数的に減衰させてチャイムらしい響きにする。

    Args:
        freq: 基音の周波数（Hz）
        duration: 長さ（秒）
        sample_rate: サンプリングレート
        volume: 音量（0.0〜1.0）

    Returns:
        音声データのnumpy配列（int16形式）
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # 基音 + 倍音を合成（ベル・チャイムらしさを出す）
    wave = (
        0.6 * np.sin(2 * np.pi * freq * t)        # 基音
        + 0.25 * np.sin(2 * np.pi * freq * 2 * t)  # 2倍音
        + 0.15 * np.sin(2 * np.pi * freq * 3 * t)  # 3倍音
    )

    # 指数的な減衰エンベロープ（チャイムのリンと響く感じ）
    decay = np.exp(-4.0 * t / duration)
    wave = wave * decay * volume

    return (wave * 32767).astype(np.int16)


@st.cache_data
def get_correct_sound_b64() -> str:
    """
    正解時のピンポーン音をBase64で返す。
    高音の「ピン」→ 間 → 中音の「ポーン」の2段チャイム。
    """
    sample_rate = 44100

    # 「ピン」：高めのC6（1047Hz）で短く明るく
    pin = _make_bell_tone(1046.50, 0.35, sample_rate, volume=0.38)

    # 間（40ms）
    gap = np.zeros(int(sample_rate * 0.04), dtype=np.int16)

    # 「ポーン」：G5（784Hz）で少し長く余韻を出す
    pon = _make_bell_tone(783.99, 0.55, sample_rate, volume=0.35)

    wave = np.concatenate([pin, gap, pon])
    return _wave_to_base64(wave, sample_rate)


@st.cache_data
def get_retry_sound_b64() -> str:
    """
    再挑戦時のやさしいポップ音をBase64で返す。
    下降する2音でやさしく促す。
    """
    sample_rate = 44100

    # 高めの音から少し低い音へ（やさしい下降）
    part1 = _generate_sine_wave(440.0, 0.15, sample_rate, volume=0.25)  # A4
    silence = np.zeros(int(sample_rate * 0.05), dtype=np.int16)          # 無音50ms
    part2 = _generate_sine_wave(330.0, 0.2, sample_rate, volume=0.2)    # E4

    wave = np.concatenate([part1, silence, part2])
    return _wave_to_base64(wave, sample_rate)


def make_audio_html(b64_data: str, autoplay: bool = True) -> str:
    """
    Base64音声データをHTMLのaudioタグに変換する。

    Args:
        b64_data: Base64エンコードされた音声データ
        autoplay: 自動再生するか（iPhoneではFalseにすること）

    Returns:
        HTML文字列
    """
    autoplay_attr = "autoplay" if autoplay else ""
    return (
        f'<audio {autoplay_attr} style="display:none">'
        f'<source src="data:audio/wav;base64,{b64_data}" type="audio/wav">'
        f"</audio>"
    )


# ---- gTTSによる日本語読み上げ ----

@st.cache_data
def text_to_speech_b64(text: str) -> str | None:
    """
    gTTSで日本語テキストを音声に変換し、Base64で返す。
    失敗した場合はNoneを返す（アプリを止めない）。

    Args:
        text: 読み上げるテキスト（ひらがなや単語）

    Returns:
        Base64エンコードされたMP3データ、失敗時はNone
    """
    try:
        from gtts import gTTS  # gTTSは重いので遅延インポート

        tts = gTTS(text=text, lang="ja", slow=True)  # 子ども向けにゆっくり読む
        buffer = io.BytesIO()
        tts.write_to_fp(buffer)
        buffer.seek(0)
        return base64.b64encode(buffer.read()).decode("utf-8")
    except Exception:
        # ネットワークエラーなどでも無音で続行
        return None


def make_tts_button_html(b64_data: str, button_label: str = "もじをきく🔊") -> str:
    """
    音声再生ボタンのHTMLを生成する。
    iPhoneのSafariはautoplay制限があるため、ボタンクリックで再生する。

    Args:
        b64_data: Base64エンコードされたMP3データ
        button_label: ボタンのラベル文字列

    Returns:
        ボタンとaudioタグのHTML文字列
    """
    audio_id = "tts_audio"
    return f"""
    <audio id="{audio_id}" style="display:none">
        <source src="data:audio/mp3;base64,{b64_data}" type="audio/mp3">
    </audio>
    <button
        onclick="document.getElementById('{audio_id}').play()"
        style="
            font-size: 1.3rem;
            padding: 0.6rem 1.5rem;
            border-radius: 1rem;
            border: 2px solid #4CAF50;
            background-color: #E8F5E9;
            color: #2E7D32;
            cursor: pointer;
            width: 100%;
        "
    >
        {button_label}
    </button>
    """
