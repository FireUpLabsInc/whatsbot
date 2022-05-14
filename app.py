from flask import Flask, request
import requests
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
account = "ACbf0d1f34d6a20c5ae91ac541b87e3999"
token = "a71041bfe3d469782de71062caf9f56c"
client = Client(account, token)

@app.route("/")
def hello():
    return "Hello, World!"


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')
    return str(resp)

@app.route('/sendMsg', methods=['POST'])
def send_msg():





if __name__ == '__main__':
    app.run(debug=True ,port=8080,use_reloader=False)