from twilio.rest import TwilioRestClient
import sys
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC8c0bd10e151a6850ff742e308ec22d15"
auth_token  = "71cd6024d2a89b19a532f6e83b37b907"
client = TwilioRestClient(account_sid, auth_token)

callerId = sys.argv[1] 

message = client.messages.create(body="Here is your photo",
    to="+1%s" % callerId,    # Replace with your phone number
    from_="+12017305222",
    media_url=['http://104.131.171.117/voiceselfi/%s.png' % callerId])
print message.sid