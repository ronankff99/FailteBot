import requests

url = 'https://failte-bot.herokuapp.com/webhooks/rest/webhook' ##change rasablog with your app

myobj = {
"message": "hi",
"sender": 1,
}
x = requests.post(url, json = myobj)
print(x.text)