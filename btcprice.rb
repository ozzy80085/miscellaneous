require "uri"
require "net/http"
require "json"

uri = URI("https://api.coindesk.com/v1/bpi/currentprice.json")
res = Net::HTTP.get_response(uri)
data = JSON.parse(res.body)

price = data["bpi"]["USD"]["rate"]

print "The Current BTC Price is: ", price, " USD", "\n"
