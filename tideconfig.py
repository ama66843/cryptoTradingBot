#!/usr/bin/env python
import os

robin_user = os.environ.get("robinhood_username")
robin_pass = os.environ.get("robinhood_password")

rh={
    "username": robin_user,
    "password": robin_pass
}

#robin_user = os.environ.get("robinhood_username")
#robin_pass = os.environ.get("robinhood_password")

config = {
    "statusEmailAddress": "xxxxxxxxxx@vtext.com",
    #percent below ma to buy
    "buyLimit": 0.01,
    #percent above purchase to sell
    "sellLimit": 0.015,
    "movingAverageWindows": 24,    # 4 hours * 6 samples per hour
    "runMinute": [5,15,25,35,45,55],
    "coinList": ["BCH", "ETH"],
    "tradesEnabled": False,
    "rsiWindow": 48,
}




