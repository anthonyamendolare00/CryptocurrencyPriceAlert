from bs4 import BeautifulSoup # Beautiful Soup - library for pulling data out of HTML files
import requests # allows user to send http requests easy
import time # handles time-related tasks
import smtplib # allows the actual sending function
import ssl # Secure Socket Layer - designed to create a secure connection between the client and server
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Multipurpose Internal Mail Extensions - Internet standard that extends the format of email messages to support text
# ,and other attachments
# Multipart - allows more than one attachment

# function to get the price of a coin
def get_price(coin):
    url = "https://www.google.com/search?q=" + coin + "+price" # url
    HTML = requests.get(url) # make requests to website
    soup = BeautifulSoup(HTML.text, 'html.parser') # extracts the html text
    text = soup.find("div", attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text # finds the current price in the text
    return text # returns the text to get the price

receiver = 'receiver@gmail.com' # receiver email address
sender = 'sender@gmail.com' # sender email address
sender_pwd = 'sender password' # sender password

# function for sending the email
def send_email(receiver, sender, sender_pwd, text_price):
    message = MIMEMultipart() # allows attachments
    message['Subject'] = 'Alert! New Ethereum Price!!!' # subject of email
    message['From'] = sender # from the sender
    message['To'] = receiver # to the receiver

# message inside the email with HTML
    HTML = """ 
        <html>
            <body>
                <h1> New Ethereum Price Alert :) </h1>
                <h2>"""+text_price+"""
                </h2>
            </body>
        </html>
    """

    MTObj = MIMEText(HTML, "html") # make the MIMEText for the HTML code that is an object in Python
    message.attach(MTObj) # adds the MTObj into the email
    SSL_context = ssl.create_default_context() # create the SSL object
    server = smtplib.SMTP_SSL(host="smtp.gmail.com", port=465, context=SSL_context) # create the connection for the SMTP
    server.login(sender, sender_pwd) # logs into the sender's email
    server.sendmail(sender, receiver, message.as_string()) # sends email to receiver with email attached as a string in Python

send_email(receiver, sender, sender_pwd, 'TEST') # sends the email

def send_alerts(): # function for sending alerts
    some_price = -1 # fixed price
    while True: # loop
        coin = 'ethereum' # coin
        price = get_price(coin) # get the price of the coin
        if price != some_price: # if the price is not equal to -1 then
            print(coin.capitalize()+ 'price:', price) # print the coin price
            price_text = coin.capitalize() + 'is' + price
            send_email(sender, receiver, sender_pwd, price_text) # send email
            time.sleep(30) # 30 second then email will be sent again

send_alerts() # sends the alerts

