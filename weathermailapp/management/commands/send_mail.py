from django.core.management.base import BaseCommand
import schedule
import time
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import ssl
from django.contrib.auth import get_user_model
User = get_user_model()
import requests


url = 'http://weather.livedoor.com/forecast/webservice/json/v1?'




class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        FROM_ADDRESS = 'appofweathermail@gmail.com'
        MY_PASSWORD = 'weathermail8310'
        #TO_ADDRESS = user.email
        BCC = ''
        SUBJECT = '今日の天気予報です。'
        #BODY = '送信テストです'


        def create_message(from_addr, to_addr, bcc_addrs, subject, body):
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = from_addr
            msg['To'] = to_addr
            msg['Bcc'] = bcc_addrs
            msg['Date'] = formatdate()
            return msg


        def send(from_addr, to_addrs, msg):
            #context = ssl.create_default_context()
            smtpobj = smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10)
            smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
            smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
            smtpobj.close()

        """
        for user in User.objects.all():
            query_params = {'city': user.location}
            data = requests.get(url, params=query_params).json()


            to_addr = user.email
            subject = SUBJECT
            #body = BODY
            body = '今日の天気は' + data['forecasts'][0]['telop'] + 'です。'



            msg = create_message(FROM_ADDRESS, to_addr, BCC, subject, body)
            send(FROM_ADDRESS, to_addr, msg)

            #schedule.every(1/60).minutes.do(send, FROM_ADDRESS, to_addr, msg)
            schedule.every().day.at("13:20").do(send, FROM_ADDRESS, to_addr, msg)
        """

        def main():
            for user in User.objects.all():
                query_params = {'city': user.location}
                data = requests.get(url, params=query_params).json()


                to_addr = user.email
                subject = SUBJECT
                #body = BODY
                body = '今日の天気は' + data['forecasts'][0]['telop'] + 'です。'



                msg = create_message(FROM_ADDRESS, to_addr, BCC, subject, body)
                send(FROM_ADDRESS, to_addr, msg)

                #schedule.every(1/60).minutes.do(send, FROM_ADDRESS, to_addr, msg)
                
        schedule.every().day.at("12:16").do(main)
        
        while True:
            schedule.run_pending()
            time.sleep(1)



"""
class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for user in User.objects.all():
            print(int(user.location))
"""
