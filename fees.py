# Reselling Fee Calculator by milesb#0001
print("Hello!")

print("What is the amount you would like to convert?")
amount = float(input())

print("What platform are you using?")
print("Options are ebay, goat, stockx, grailed or paypal?")
platform = input()

if platform == "ebay":
    ebayConversion = amount*.1
    paypalConversion = amount*.029
    paypalConversion = paypalConversion + .30
    ebayFee = ebayConversion + paypalConversion
    ebayTotal = amount - ebayFee
    ebayTotal = round(ebayTotal, 2)
    ebayTotal = str(ebayTotal)
    print("You will receive $" + ebayTotal + " after eBay fees are taken out.")

elif platform == "goat":
    goatConversion = amount*.095 + 5
    paypal2Conversion = amount*.029 + .30
    goatFee = goatConversion + paypal2Conversion
    goatTotal = amount - goatFee
    goatTotal = round(goatTotal, 2)
    goatTotal = str(goatTotal)
    print("You will receive $" + goatTotal + " after Goat fees are taken out.")

elif platform == "stockx":
    stockxConversion = amount*.09
    paypal3Conversion = amount*.03
    stockxFee = stockxConversion + paypal3Conversion
    stockxTotal = amount - stockxFee
    stockxTotal = round(stockxTotal, 2)
    stockxTotal = str(stockxTotal)
    print("You will receive $" + stockxTotal + " after StockX fees are taken out.")

elif platform == "grailed":
    grailedConversion = amount*.06
    paypal4Conversion = amount*.029 + .3
    grailedFee = grailedConversion + paypal4Conversion
    grailedTotal = amount - grailedFee
    grailedTotal = round(grailedTotal, 2)
    grailedTotal = str(grailedTotal)
    print("You will receive $" + grailedTotal + " after Grailed fees are taken out.")

elif platform == "paypal":
        paypal5Conversion = amount*.029 + .3
        invoiceFee = paypal5Conversion
        invoiceTotal = amount - invoiceFee
        invoiceTotal = round(invoiceTotal, 2)
        invoiceTotal = str(invoiceTotal)
        print("You will receive $" + invoiceTotal + " after Paypal fees are taken out.")

else:
    print("Sorry. That platform is not currently supported or you typed a supported platform incorrectly. Please try again, thanks!")
