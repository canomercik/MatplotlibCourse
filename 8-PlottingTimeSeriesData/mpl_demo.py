import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn-v0_8')

#date_format = mpl_dates.DateFormatter('%d %b %Y')
#plt.gca().xaxis.set_major_formatter(date_format)  #getcurrentaxis

data = pd.read_csv('data.csv')

data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

price_date = data['Date']
price_close = data['Close']

plt.plot_date(price_date, price_close, linestyle='solid')

plt.gcf().autofmt_xdate()

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()
plt.savefig('plot.png')
plt.show()
