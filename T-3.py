import json 
import datetime
import matplotlib.pyplot as plt
# Opening JSON file 
f = open('data.json','r') 
l = open('latest-rates.json','r')  
# returns JSON object as  
# a dictionary 
latest = json.load(l)
data = json.load(f) 
  
# Iterating through the json 
# list 

inr = latest['rates']['INR']        #latest rate of INR
gbp = latest['rates']['GBP']        #latest rate of EUR

dates = []  # array to store month dates
for i in data['rates']:     
    dates.append(i)
jan_dates = []
for i in dates:
    datee = datetime.datetime.strptime(i, "%Y-%m-%d")
    if datee.month==1:    # getting all january dates
        jan_dates.append(i)
jan_dates.sort()
INR_EUR_exchange = []
for i in jan_dates:  # getting date wise INR exchenge rate
   INR_EUR_exchange.append(data['rates'][i]['INR'])

GBP_EUR_exchange = []
for i in jan_dates:  # getting date wise GBP exchenge rate
   GBP_EUR_exchange.append(data['rates'][i]['GBP'])

# plotting graph
plt.plot(jan_dates,INR_EUR_exchange,marker='o',color='r')
plt.plot(jan_dates,GBP_EUR_exchange,marker='o',color='b')
plt.xticks(rotation=90)
plt.ylim(min(GBP_EUR_exchange)-1,max(INR_EUR_exchange))

plt.xlabel('January Dates')
plt.ylabel('INR-EUR Exchange Rates')
plt.title('INR Latest Rates : '+str(inr)+' , GBP Latest Rates : '+str(gbp)+'')
plt.show()
# Closing file 
f.close() 