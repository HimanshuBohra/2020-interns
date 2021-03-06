import json 
import datetime
import matplotlib.pyplot as plt
# Opening JSON file 
f = open('data.json','r') 
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 
  
# Iterating through the json 
# list 
dates = []
for i in data['rates']: 
    dates.append(i)
jan_dates = []
for i in dates:
    datee = datetime.datetime.strptime(i, "%Y-%m-%d")
    if datee.month==1:
        jan_dates.append(i)
jan_dates.sort()
INR_EUR_exchange = []
for i in jan_dates:
   INR_EUR_exchange.append(data['rates'][i]['INR'])
plt.plot(jan_dates,INR_EUR_exchange,marker='o')
plt.xticks(rotation=90)
plt.ylim(min(INR_EUR_exchange)-0.5,max(INR_EUR_exchange)+0.5)

plt.xlabel('January Dates')
plt.ylabel('INR-EUR Exchange Rates')
plt.title('INR exchange rate against EUR from 1 Jan 2019 to 31 Jan 2019')
plt.show()
# Closing file 
f.close() 
