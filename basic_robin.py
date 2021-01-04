import os 
import robin_stocks as rs
import pandas as pd 
from time import sleep 

robin_user = os.environ.get("robinhood_username")
robin_pass = os.environ.get("robinhood_password")

rs.login(username=robin_user,
         password=robin_pass,
         expiresIn=86400,
         by_sms=True)

# rs.orders.order_buy_fractional_by_price(symbol,
#                                        ammountInDollars,
#                                        timeInForce='gtc',
#                                        extendedHours=False) 

# rs.orders.order_buy_limit('AAPL,
#                           5,
#                           450,
#                           timeInForce='gtc',
#                           extendedHours=False)

# while True:
#     try:
#         price = rs.stocks.get_latest_price('MA', includeExtendedHours=True)
#         # assigning price to first (and only) item of list and converting from str to float
#         mastercard_price = float(price[0])
        
#         if mastercard_price < 280:
#             try:
#                 rs.orders.order_buy_fractional_by_price('V', 500)
#                 break
                
#             except Exception as e:
#                 print("Error placing order:", e)
#         else:
#             sleep(15)
                
#     except Exception as e:
#         print("Error fetching latest price:", e)
        
# print("ORDER TRIGGERED at {}".format(pd.Timestamp.now()))

# # firing a pair trade when Dropbox and box diverge more than 3% over the previous day FULL EXAMPLE

# dropbox_data = rs.stocks.get_stock_historicals("DBX", interval="day", span="week")
# dropbox_historical = pd.DataFrame(dropbox_data)

# box_data = rs.stocks.get_stock_historicals("BOX", interval="day", span="week")
# box_historical = pd.DataFrame(box_data)

# price_diff_yesterday = dropbox_historical.iloc[-1]['close_price'] - box_historical.iloc[-1]['close_price']

# while True:
#     try:
#         dropbox_today = float(rs.stocks.get_latest_price('DBX', includeExtendedHours=True)[0])
#         box_today = float(rs.stocks.get_latest_price('BOX', includeExtendedHours=True)[0])
#         print("box today:", box_today)
#         print("dropbox today:", dropbox_today)

#         price_diff_today = dropbox_today - box_today

#         if price_diff_today > 1.03 * price_diff_yesterday:
#             try:
#                 # LONG BOX SHORT DROPBOX
#                 rs.orders.order_buy_fractional_by_price('BOX',
#                                            500,
#                                            timeInForce='gtc',
#                                            extendedHours=False) 

#                 rs.orders.order_sell_fractional_by_price('DBX',            
#                                            500,
#                                            timeInForce='gtc',
#                                            extendedHours=False) 

#                 print("Diverged MORE THAN 3%, YESTERDAY'S DIFFERENCE: {} TODAY'S DIFFERENCE: {} PERCENTAGE CHANGE: {}%\n".format(price_diff_yesterday, price_diff_today, (price_diff_today/price_diff_yesterday - 1)*100))
#                 break
#             except Exception as e:
#                 print("Error placing orders:", e)
#                 sleep(15)


#         else:
#             print("STILL WAITING, YESTERDAY'S DIFFERENCE: {} TODAY'S DIFFERENCE: {} PERCENTAGE CHANGE: {}%\n".format(price_diff_yesterday, price_diff_today, ((price_diff_today/price_diff_yesterday - 1))*100))
#             sleep(15)
#     except Exception as e:
#         print("Error fetching latest prices:", e)
#         sleep(15)

# print("ORDER TRIGGERED at {}".format(pd.Timestamp.now()))

#stop loss order
tick='DOGE'

rs.orders.order_buy_crypto_by_quantity(tick, 3586)

stoploss_order = rs.orders.order_sell_crypto_limit(tick, 3586, .014, 'gtc')

stoploss_order_id = stoploss_order['id']

#doggo=rs.crypto.get_crypto_historicals('DOGE', '10minute', 'week')

while True:
    #price = rs.stocks.get_latest_price(tick, includeExtendedHours=True)
    price = rs.crypto.get_crypto_quote(tick)
    price = float(price[0]) # convert to single float

    if price > .015:
        rs.orders.cancel_crypto_order(stoploss_order_id)
        rs.orders.order_sell_crypto_by_quantity(tick, 3586, 'ask_price')
        print(f"STOP LOSS CANCELLED AND MARKET SELL TRIGGERED, {tick} PRICE: ", price)
        print("ORDER TRIGGERED at {}".format(pd.Timestamp.now()))
        break
    
    print(f"STILL WAITING, {tick} PRICE:", price)
    sleep(15)


