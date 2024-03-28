import requests
from bs4 import BeautifulSoup
import pandas as pd
import gspread


temp_list = []
forecasts_list = []
humidity_list = []

url = "https://weather.com/en-PK/weather/hourbyhour/l/087c91e31e8ea01975990342c0180df07ad2a75a1e0897cde90bd0f77ed502ad#detailIndex4"
r = requests.get(url)
# print(r)
soup = BeautifulSoup(r.text,"html")
# print(soup)
# --------------- temperature

temp = soup.find_all("span",class_ = "DetailsSummary--tempValue--jEiXE")
# print(temp)
for i in temp:
    n = i.text.strip()
    temp_list.append(n)

# print(len(temp_list))

# ---------------- forecasts
forecasts = soup.find_all("span",class_ = "DetailsSummary--extendedData--307Ax")
# print(forecasts)
for i in forecasts:
    n = i.text.strip()
    forecasts_list.append(n)

# print(len(forecasts_list))

# --------------- humidity

humidity = soup.find_all("span",class_ = "DetailsTable--value--2YD0-",attrs={'data-testid': 'PercentageValue'})
# print(humidity)

for i in humidity[0:48]:
    n = i.text.strip()
    humidity_list.append(n)

# print(len(humidity_list))





df = pd.DataFrame({"Temperature":temp_list,"forecasts": forecasts_list,"Humidity":humidity_list})

# print(df)

# df.to_csv("Weather Report.csv")

gc = gspread.service_account(filename='Weather.json')
sh = gc.open("Weather_Report").sheet1
sh = df