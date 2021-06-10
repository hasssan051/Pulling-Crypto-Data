# Pulling-Ethereum-Data
Data Engineering Intern Trial Task

##Desclaimer##
_I was not able to scrap 10 latest prices of ethereum from coingecko because after much exploration of the API I was not able to find a query that would give me the latest prices with all the information that was required for the CSV. If there is a way to do this, please inform me._

##Description##
This program uses the CoinGecko API to pull the latest ethereum price in usd and btc (US-Dollars and Bitcoin). The information retrieved is then saved into a csv file on your computer.

##Usage##
Since this program is Dockerized, its usage is pretty straigtforward. 
After pulling from this github repo, go to your terminal and write:
- docker build -t python-ethereum-data .
- docker run python-ethereum-data

