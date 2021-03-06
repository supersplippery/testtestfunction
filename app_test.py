from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('/7jKT6yQcneXmnm0HJXQog+LHKsa5VlvC5uj7iejEoEPMjILX5mTn9EU2hHicc9cohTmKdTgIX5unLF6MPFN/IcNowkdKf5AxkgaifTrYN466PtNG+fH4k8EwNr58ExsQCRQXm8411/WlTrAa6fnogdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('12e53fa6ea2cb6af47862ee39543a59f')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

if __name__ == "__main__":
    app.run(debug=True)
