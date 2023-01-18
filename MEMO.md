## メモ

### サーバー起動

```shell
python manage.py runserver
```

### プロジェクトに新しいアプリケーションを作成

```shell
python manage.py startapp tutorial
```

### 遭遇したエラー ①

```
AADSTS50194: Application '186a4da8-dbaf-40f2-a194-1eedcdd03b18'(msal-django) is not configured as a multi-tenant application. Usage of the /common endpoint is not supported for such applications created after '10/15/2018'. Use a tenant-specific endpoint or configure the application to be multi-tenant.
```

#### 原因

`oauth_settings.yml` で、本アプリをマルチテナントとして定義していることによる。

```yaml
authority: https://login.microsoftonline.com/common
```

#### 解決策

`oauth_settings.yml` を以下のように修正

```yaml
authority: https://login.microsoftonline.com/<tenant_id>
```

### 遭遇したエラー ②

```
AADSTS50011: The redirect URI 'http://localhost:8000/callback' specified in the request does not match the redirect URIs configured for the application '186a4da8-dbaf-40f2-a194-1eedcdd03b18'. Make sure the redirect URI sent in the request matches one added to your application in the Azure portal. Navigate to https://aka.ms/redirectUriMismatchError to learn more about how to fix this.
```

#### 原因

Azure AD アプリケーション登録時の callback URI を指定していないことによる。

#### 解決策

登録したアプリケーションのリダイレクト URI (Web) に、以下を指定する。

```
http://localhost:8000/callback
```

### 遭遇したエラー ③

```
Reverse for 'home' not found. 'home' is not a valid view function or pattern name.
```

#### 原因

リダイレクト先 `home` で指定される view が存在しない。

#### 解決策

`home` ビューを作成（サンプルサイトにあったような凝ったものではなく、Azure AD から取得した ID トークンを表示するだけの簡易的な実装とする）。
画面に表示されたトークン（JWT）を、[https://jwt.ms](https://jwt.ms)にコピペしてみると、解析結果が取得できる。
