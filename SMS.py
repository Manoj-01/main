
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
def code():
    account_sid ='AC5bfb4aee56ba55e525e0d31ab5762ed2'
    auth_token ='8a0e7f078a0483ceca7b29b84e11819a'
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(body="Hey!! Manoj",
                from_='+15028379552',
                to='+918248607955'
                 )
    print(message.sid)

