import imaplib
mail = imaplib.IMAP4_SSL('mail.gandi.net')
mail.login('thinkpad@antoilonappan.in', 'AntoThinkpad')
mail.list()
mail.select("inbox")
import email
import os
s =0

while True:
    result, data = mail.uid('search', None, "ALL")
    latest_email_uid = data[0].split()[-1]
    if s == 0:
         saved_last = latest_email_uid
         #print 'saved_last = latest_email_uid'
         s=1
    if latest_email_uid > saved_last:
       #print 'messege'
       result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
       raw_email = data[0][1]

       email_message = email.message_from_string(raw_email)
       pri = 'Hello Anto, you have received a mail from %s'%email.utils.parseaddr(email_message['From'])[0] 
       os.system("echo %s | festival --tts --pipe"%pri)
       saved_last = latest_email_uid
     
