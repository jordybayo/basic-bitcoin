# import modules
# Make sure to copy the exchanges from https://github.com/dursk/bitcoin-price-api
# to the same location as this script
from exchanges.bitfinex import Bitfinex
import smtplib

# Function to send email
def trigger_email(msg):
    # Change these to your email details
    email_user = "jordii.bayo@gmail.com"
    email_password = "wxswgcrymwggaduc"
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    email_from = "jordii.bayo@gmail.com"
    email_to = "jordii.bayo@gmail.com"

    # login to the email server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_user, email_password)
    # send email
    server.sendmail(email_from, email_to, msg)
    server.quit()


# define buy and sell thresholds for Bitcoin. These values you have to change according to the
buy_thresh = 6500
sell_thresh = 6500

# get Bitcoin prices
btc_sell_price = Bitfinex().get_current_bid()
btc_buy_price = Bitfinex().get_current_ask()

print(btc_buy_price)

# Trigger Buy email if buy price is lower than threshold
if btc_buy_price < buy_thresh:
    email_msg = """
    Bitcoin Buy Price is {} which is lower than
    threshold price of {}.
    Good time to buy!""".format(btc_buy_price, buy_thresh)
    trigger_email(email_msg)
    

# Trigger sell email if sell price is higher than threshold
if btc_sell_price > sell_thresh:
    email_msg = """
    Bitcoin sell Price is {} which is higher than
    threshold price of {}.
    Good time to sell!""".format(btc_sell_price, sell_thresh)
    trigger_email(email_msg)