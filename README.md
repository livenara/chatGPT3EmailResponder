# chatGPT3EmailResponder

EメールでchatGPT APIのレスポンスを受け取れます。
コード内に設定したメールアドレスへメールを送るとchatGPTのレスポンスがメールで返信してくれるサンプルコードです。

【使い方】
１、chatGPTのリクエストを受け取るための専用のメールアドレスとメールサーバを用意します。
２、main.pyにOpenAIのAPIキー・メールアドレス・メールサーバの設定を書き込みます。
３、実行します。
４、メール本文にリクエストを書いてプログラム内に設定したメールアドレスに送信します。
５、プログラム実行中は返事が来ます。

※メールチェック間隔は60秒です。　checkTimeで変更できます。

メールが使えればchatGPTが使えます。
メールはIMAPサーバ対応です。ポート番号はサーバに合わせて変更してください。
適宜エラーハンドリングを行なってください。

付記：
GoogleAppScriptでも似たようなものが作れそうかな。



Receive responses from the chatGPT API via email. This is a sample code where if you send an email to the address set in the code, you will receive a reply from chatGPT via email.

Usage
Prepare a dedicated email address and mail server to receive requests for chatGPT.
Fill in your OpenAI API key, email address, and mail server settings in main.py.
Run the program.
Send an email with your request written in the body to the email address configured in the program.
As long as the program is running, you'll get a reply.
Note: The email check interval is set to 60 seconds. You can modify this by adjusting the checkTime variable.

With access to email, you can now leverage chatGPT. The email implementation is compatible with IMAP servers. Please adjust the port number according to your server. Ensure you handle errors appropriately where necessary.
