# 🤖 Simple Chatbot

OpenAI API（GPT-3.5）を使った、シンプルなチャットボットアプリです。  
StreamlitでWebアプリ化しており、インストールも操作もとても簡単です。

---

## 🚀 機能

- GPT-3.5による自然な質問応答
- 履歴を保持した対話（セッション中）
- シンプルで直感的なUI（Streamlit製）

---

## 🔧 インストール方法

### ✅ 前提条件

- Python 3.8以上
- OpenAI APIキー（[こちらから取得](https://platform.openai.com/account/api-keys)）

### 📦 セットアップ手順（Windows想定）

```bash
git clone https://github.com/Kensyo731/simple_chatbot.git
cd simple_chatbot
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
🔐 .env ファイルの作成
プロジェクトのルートに .env ファイルを作成し、以下を記入してください：

ini
コピーする
編集する
OPENAI_API_KEY=your_api_key_here
▶️ 実行方法
仮想環境が有効な状態で、以下を実行：

bash
コピーする
編集する
streamlit run chatbot.py
ブラウザで http://localhost:8501 が開きます。

📁 フォルダ構成
bash
コピーする
編集する
simple_chatbot/
├── chatbot.py          # アプリ本体
├── .env                # OpenAI APIキー（Gitには含めない）
├── requirements.txt    # 必要なライブラリ一覧
├── .gitignore          # 無視ファイル設定
└── README.md           # このファイル
📄 ライセンス
MIT License

🙋‍♂️ 作者情報
Created by Kensyo731
GitHubでのスター・フォーク大歓迎です ⭐