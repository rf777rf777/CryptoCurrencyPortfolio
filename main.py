from tkinter import *
import requests
import json
import os

root =  Tk()
root.title("CryptoCurrency")

#name = Label(root,text = "ABCDEF",bg = "blue",fg = "white")
#name.grid(row=0,column=0,sticky=N+S+E+W)

#title = ["Name" , "Rank" , "Current Price" , "Price Paid" , "P/L Per" , "1-Hour Change" , "24-Hour Change" , "7-Day Change" , "Current Value" , "P/L Total"]
title_name = Label(root,text="Name",bg="white",font="Verdana 8 bold") 
title_name.grid(row=0,column=0,sticky=N+S+E+W)

title_rank = Label(root,text="Rank",bg="silver",font="Verdana 8 bold") 
title_rank.grid(row=0,column=1,sticky=N+S+E+W)

title_current_price = Label(root,text="Current Price",bg="white",font="Verdana 8 bold") 
title_current_price.grid(row=0,column=2,sticky=N+S+E+W)

title_price_paid = Label(root,text="Price Paid",bg="silver",font="Verdana 8 bold") 
title_price_paid.grid(row=0,column=3,sticky=N+S+E+W)

title_profit_loss_per = Label(root,text="Profit/Loss Per",bg="white",font="Verdana 8 bold") 
title_profit_loss_per.grid(row=0,column=4,sticky=N+S+E+W)

title_1_hr_change = Label(root,text="1 HR Change",bg="silver",font="Verdana 8 bold") 
title_1_hr_change.grid(row=0,column=5,sticky=N+S+E+W)

title_24_hr_change = Label(root,text="24 HR Change",bg="white",font="Verdana 8 bold") 
title_24_hr_change.grid(row=0,column=6,sticky=N+S+E+W)

title_7_day_change = Label(root,text="7 Day Change",bg="silver",font="Verdana 8 bold") 
title_7_day_change.grid(row=0,column=7,sticky=N+S+E+W)

title_current_value = Label(root,text="Current Value",bg="white",font="Verdana 8 bold") 
title_current_value.grid(row=0,column=8,sticky=N+S+E+W)

title_profit_loss_total = Label(root,text="Profit Loss Total",bg="silver",font="Verdana 8 bold") 
title_profit_loss_total.grid(row=0,column=9,sticky=N+S+E+W)

#currencies = ["XRP","EOS","STEEM","BTC"]

#time = 0

def lookup():	

	json = getDatafromApi()

	my_portfolio = [
		{
			"sym":"BTC",
			"amount_owned":1,
			"price_paid_per": 12000
		},
		{
			"sym":"STEEM",
			"amount_owned":3000,
			"price_paid_per": .80
		},
		{
			"sym":"XRP",
			"amount_owned":5000,
			"price_paid_per": .20
		},
		{
			"sym":"XLM",
			"amount_owned":2000,
			"price_paid_per": .10
		},
		{
			"sym":"EOS",
			"amount_owned":1000,
			"price_paid_per": 2.00
		}
	]

	portfolio_profit_loss = 0
	row_count = 0
	for data in json:
		column = 0
		for currency in my_portfolio:
			#time += 1
			if currency["sym"] == data["symbol"]:
				row_count += 1
				total_paid = currency["amount_owned"] * currency["price_paid_per"]
				current_value = currency["amount_owned"] * float(data["price_usd"])
				profit_loss = current_value - total_paid
				profit_loss_per_coin = float(data["price_usd"]) - currency["price_paid_per"]
				portfolio_profit_loss += profit_loss


				print("\r\n{0}\nCurrent Price: ${1:.2f}\nProfit/Loss per coin: ${2:.2f}\nRank: {3}\nTotal Paid: ${4:.2f}\nCurrent Value: ${5:.2f}\nProfit/loss: ${6:.2f}".format(
						data["name"],
						float(data["price_usd"]),
						profit_loss_per_coin,
						data["rank"],
						total_paid,
						current_value,
						profit_loss
					))

				name = Label(root,text=data["name"],bg="white") 
				name.grid(row=row_count,column=column,sticky=N+S+E+W)

				rank = Label(root,text=data["rank"],bg="silver") 
				rank.grid(row=row_count,column=column+1,sticky=N+S+E+W)

				current_price = Label(root,text="${0:.2f}".format(float(data["price_usd"])),bg="white") 
				current_price.grid(row=row_count,column=column+2,sticky=N+S+E+W)

				price_paid = Label(root,text="${0:.2f}".format(float(currency["price_paid_per"])),bg="silver") 
				price_paid.grid(row=row_count,column=column+3,sticky=N+S+E+W)

				profit_loss_per = Label(root,text="${0:.2f}".format(float(profit_loss_per_coin)),bg="white") 
				profit_loss_per.grid(row=row_count,column=column+4,sticky=N+S+E+W)

				one_hr_change = Label(root,text="{0:.2f}%".format(float(data["percent_change_1h"])),bg="silver") 
				one_hr_change.grid(row=row_count,column=column+5,sticky=N+S+E+W)

				twentyfour_hr_change = Label(root,text="{0:.2f}%".format(float(data["percent_change_24h"])),bg="white") 
				twentyfour_hr_change.grid(row=row_count,column=column+6,sticky=N+S+E+W)

				seven_day_change = Label(root,text="{0:.2f}%".format(float(data["percent_change_7d"])),bg="silver") 
				seven_day_change.grid(row=row_count,column=column+7,sticky=N+S+E+W)

				current_value = Label(root,text="${0:.2f}".format(float(current_value)),bg="white") 
				current_value.grid(row=row_count,column=column+8,sticky=N+S+E+W)

				profit_loss_total = Label(root,text="${0:.2f}".format(float(profit_loss)),bg="silver") 
				profit_loss_total.grid(row=row_count,column=column+9,sticky=N+S+E+W)

				my_portfolio.remove(currency)
				break

#print("\r\nPortfolio Profit/Loss: ${0:.2f}".format(portfolio_profit_loss))
#print(time)


def getDatafromApi():
	header = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
	}

	req = requests.get("https://api.coinmarketcap.com/v1/ticker/",headers = header)
	jsonResult = json.loads(req.content)

	return jsonResult

lookup()

root.mainloop()
