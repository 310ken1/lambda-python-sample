## 開発環境の準備

### アプリケーションのインストール

```cmd
winget install -e --id Git.Git
winget install -e --id Microsoft.VisualStudioCode
winget install -e --id suse.RancherDesktop
winget install -e --id Amazon.AWSCLI
```

### ソースコードの取得

```cmd
https://github.com/310ken1/lambda-python-sample.git
cd lambda-python-sample
```

### Python の開発環境準備

```cmd
python -m venv .venv
.venv\Scripts\activate
python -m pip install pipenv
pipenv shell
pipenv sync --dev
```

### Node.js の開発環境準備

```cmd
winget install -e --id jasongin.nvs
nvs add lts
nvs lts
npm ci
```

### Visual Studio Code の拡張機能のインストール

拡張機能の検索欄に以下を入力し、「ワークスペースの推奨事項」に表示される拡張機能をインストールする

```
@recommended
```

---

## 開発環境の実行方法

### 開発環境のアクティブ化

```
cd lambda-python-sample
nvs use lts
pipenv shell
```

### docker デーモン起動とコンテナ起動

```cmd
"c:\Program Files\Rancher Desktop\Rancher Desktop.exe"
docker compose -f "docker-compose.yml" up -d --build
```

#### pgAdmin の接続設定

- ログイン設定
  http://localhost:8080
  |設定|値|
  |-|-|
  |user|example@example.com|
  |pass|password|

- DB 接続設定
  |設定|値|
  |-|-|
  |ホスト名/アドレス|postgres|
  |ユーザ名|postgres|
  |パスワード|postgres|

### ローカル実行

```cmd
sls invoke local -f <関数名>
```

### リモート実行

```cmd
sls invoke -f <関数名>
```

### デプロイ

```cmd
sls deploy
```

### テストの実行

```cmd
lambda-python-sample>python -m pytest -s tests\hello\test_hello.py
```

---

## 開発環境の構築

### Serverless Framework

#### インストール

```cmd
npm install -g serverless
```

#### サービス作成

```cmd
sls create --template aws-python3 --name test --path lambda-python-sample
cd lambda-python-sample
sls plugin install -n serverless-python-requirements
```
