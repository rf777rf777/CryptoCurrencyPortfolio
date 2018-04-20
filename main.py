import requests
import json
import os

header = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

requests = requests.get("https://api.coinmarketcap.com/v1/ticker/",headers = header)
json = json.loads(requests.content)

#currencies = ["XRP","EOS","STEEM","BTC"]

my_portfolio = [
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

#time = 0
portfolio_profit_loss = 0

for data in json:
	for currency in my_portfolio:
		#time += 1
		if currency["sym"] == data["symbol"]:
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
			my_portfolio.remove(currency)
			break

print("\r\nPortfolio Profit/Loss: ${0:.2f}".format(portfolio_profit_loss))
#print(time)