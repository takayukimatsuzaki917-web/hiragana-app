"""
Pixabay APIを使って画像URLを取得するユーティリティ。
APIキーがない場合やエラー時はNoneを返し、呼び出し元でemoji fallbackに切り替える。
"""

import os
import requests
import streamlit as st
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()


@st.cache_data(ttl=3600)  # 1時間キャッシュして、API呼び出し回数を最小化
def fetch_image(keyword_en: str) -> str | None:
    """
    Pixabay APIから画像URLを取得する。

    Args:
        keyword_en: 英語の検索キーワード（例: "apple", "cat"）

    Returns:
        画像URL文字列、取得できない場合はNone
    """
    api_key = os.getenv("PIXABAY_API_KEY", "")

    # APIキーが設定されていない場合はNoneを返す
    if not api_key:
        return None

    try:
        # Pixabay APIエンドポイント
        url = "https://pixabay.com/api/"
        params = {
            "key": api_key,
            "q": keyword_en,         # 検索キーワード
            "image_type": "photo",   # 写真のみ
            "orientation": "horizontal",  # 横向き優先
            "safesearch": "true",    # 子ども向けなので安全フィルタON
            "per_page": 5,           # 5件取得して最初の1件を使う
            "lang": "ja",            # 日本語設定
        }

        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()  # HTTPエラーがあれば例外を発生させる

        data = response.json()

        # 検索結果があれば最初の画像のURLを返す
        if data.get("hits") and len(data["hits"]) > 0:
            # webformatURL: 中サイズの画像（表示に適したサイズ）
            return data["hits"][0]["webformatURL"]

        return None

    except requests.exceptions.Timeout:
        # タイムアウトした場合はNoneを返す（アプリを止めない）
        return None
    except requests.exceptions.RequestException:
        # その他のネットワークエラーもNoneを返す
        return None
    except Exception:
        # 予期しないエラーも安全にNoneを返す
        return None
