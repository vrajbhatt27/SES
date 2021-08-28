from django.core.mail import EmailMessage
import time
def mail(to, fname):
   mail = EmailMessage(
       'Registered Successfully',
       'Smart Enterance System',
       'barry.tmp10@gmail.com',
       [to],
   )
#    time.sleep(5)
   print("STARTING TO SEND MAIL--------------")
   mail.attach_file('media/qrcodes/{f}.png'.format(f=fname))
   mail.send()

   print("DONE ~~~~~~~~~~~~~~~~~~~~~~~~~~~")
