from twilio.rest import Client 
from dotenv import load_dotenv
import requests
import os


def send_messages(persons, joke): 
    for person in persons:
        message_body =   f"""
Hello {person[0]}! 👋
You seem to be a great programmer👨‍💻

So I decided to send you a programming joke daily I hope you are happy with that.

_{joke}_
        """
        send_message(fromN='whatsapp:+14155238886',toN=f'whatsapp:{person[1]}',message_body=message_body)

def send_message(fromN,toN,message_body):
    message = client.messages.create( 
                from_=fromN,
                body=message_body,      
                to=toN )
    print(message.body, message.price, message.price_unit)

def get_random_programming_joke():
    response = requests.get("https://backend-omega-seven.vercel.app/api/getjoke").json()
    #print(response)
    return response[0]["question"]+" "+response[0]["punchline"]

# load enviroment variables
load_dotenv(verbose=True)

# init twilio client
twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID")
client = Client(twilio_account_sid, twilio_auth_token) 

# parse persons from env file. they are in format => name:number,name:number..etc
persons = list(map(lambda p:p.split(':'),os.getenv("TO_NUMBERS").split(",")))

joke = get_random_programming_joke()

send_messages(persons, joke)
 
