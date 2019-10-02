from cryptocompy import price

bitcoin = price.get_current_price("BTC", ["EUR"])
litecoin = price.get_current_price("LTC", ["EUR"])
zcash = price.get_current_price("ZEC", ["EUR"])


print("H τιμή του bitcoin ειναι:",bitcoin['BTC']['EUR'])
print("H τιμή του litecoin ειναι:",litecoin['LTC']['EUR'])
print("H τιμή του zcash ειναι:",zcash['ZEC']['EUR'])
