# Talk to @BotFather(https://t.me/BotFather). Send /newbot to them and follow the prompts. In response you will get an HTTP API token 
# It will look something like 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11

# Talk to your newly created bot, it is enough to just /start it.

# Immediately open https://api.telegram.org/bot<token>/getMe in your web-browser , 
# literally paste the token you received from the BotFather, complete with all the letters and punctuation.
# Copy the chat id from the returned JSON object. Sample response from above call looks like below.

# Example
"""
Request :- https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMe
reseponse :-
{
  "ok": true,
  "result": {
    "id": 1112078030,
    "is_bot": true,
    "first_name": "bot name",
    "username": "bot user name",
    "can_join_groups": true,
    "can_read_all_group_messages": false,
    "supports_inline_queries": false
  }
}
"""

import requests

def telegram_bot_sendtext(bot_message, bot_token, chat_id):

   BOT_TOKEN = bot_token
   # Telegram bots can't send messages to other bots by design, so you should specify chat ID of non-bot user, group or channel. 
   # You could obtain your account ID using @userinfobot bot, just search this bot, click start and send one messsage it gives you your ID.
   CHAT_ID = chat_id
   SEND_TEXT = 'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage?chat_id=' + BOT_CHAT_ID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(SEND_TEXT)
   return response.json()
  
test = telegram_bot_sendtext("Testing Telegram bot",'123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11','1112078030')
print(test)
