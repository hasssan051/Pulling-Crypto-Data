
import pandas as pd
from pycoingecko import CoinGeckoAPI


df = pd.DataFrame(columns=['name', 'usd', 'usd_24h_change', 'btc', 'btc_24h_change', 'last_updated_at'])
cg = CoinGeckoAPI()

data = cg.get_price(ids='ethereum', vs_currencies='usd,btc', include_market_cap='false', include_24hr_vol='false',
                    include_24hr_change='true', include_last_updated_at='true')
df = df.append(data['ethereum'], ignore_index=True)

df['name'] = 'ethereum'
df['last_updated_at'] = (pd.to_datetime(df['last_updated_at'], unit='s'))

df.to_csv('ethereum_data.csv', index=False, encoding='utf-8')

print("CSV file called \'ethereum_data.csv\' succesfully created")
