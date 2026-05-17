# ひらがなをおぼえよう！🌟

3歳の子ども向けひらがな学習Webアプリ。iPhone Safariでも快適に動作します。

## 機能

- ひらがな46文字をランダムまたは順番に出題
- 各文字に3つの単語（絵文字）を表示
- gTTSによる日本語読み上げ（「もじをきく」ボタン）
- 正解時に花火エフェクト＋効果音
- 親がサイドバーから練習する文字を選択可能
- Pixabay APIキーを設定すると絵文字から写真に切り替わる

## セットアップ

### 1. 仮想環境を作成して依存パッケージをインストール

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### 2. 環境変数を設定（任意）

`.env.example` をコピーして `.env` を作成します。

```bash
cp .env.example .env
```

`.env` を開き、Pixabay APIキーを設定します。

```
PIXABAY_API_KEY=your_api_key_here
```

> **Pixabay APIキーの取得方法**
> 1. [https://pixabay.com/](https://pixabay.com/) で無料アカウントを作成
> 2. [https://pixabay.com/api/docs/](https://pixabay.com/api/docs/) にアクセス
> 3. ページ上部に表示されているAPIキーをコピー

APIキーがなくても、絵文字フォールバックでアプリは動作します。

### 3. アプリを起動

```bash
streamlit run app.py
```

ブラウザで `http://localhost:8501` を開きます。

## ディレクトリ構成

```
hiragana-app/
├── app.py                  # メインUI
├── data/
│   └── hiragana_data.py    # ひらがな46文字のデータ定義
├── utils/
│   ├── audio.py            # gTTS読み上げ・効果音生成
│   ├── effects.py          # CSSアニメーション・花火エフェクト
│   └── image_fetcher.py    # Pixabay API連携
├── assets/
│   └── sounds/             # （音声ファイル保存用）
├── .env.example            # 環境変数テンプレート
├── requirements.txt
└── README.md
```

## iPhone Safariでの使い方

1. PCでアプリを起動し、LAN内のIPアドレスを確認（例：`192.168.1.10`）
2. iPhoneのSafariで `http://192.168.1.10:8501` を開く
3. 音声はSafariのautoplay制限のため「もじをきく🔊」ボタンをタップして再生

> **外部公開する場合** は `streamlit run app.py --server.address 0.0.0.0` で起動してください。

## 操作方法

| ボタン | 内容 |
|--------|------|
| ✅ いえる！ | 正解申告（花火エフェクト） |
| 🔄 もういちど | 再挑戦（同じ文字をもう一度） |
| ➡️ つぎのもじ | 次の文字へ進む |
| 🔊 もじをきく | ひらがなを音声で読み上げ |
| ⚙️ おやのせってい | サイドバーを開いて練習文字を選択 |
