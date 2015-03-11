from twilio.rest import TwilioRestClient
import sys
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "YOUR_ACCOUNT"
auth_token  = "YOUR_TOKEN"
client = TwilioRestClient(account_sid, auth_token)

callerId = sys.argv[1] 

message = client.messages.create(body="Here is your photo",
    to="+1%s" % callerId,    # Replace with your phone number
    from_="+PHONE_NUMBER",
    media_url=['http://SERVER/FOLDER/%s.png' % callerId])
print message.sid
