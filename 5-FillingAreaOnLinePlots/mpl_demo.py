import pandas as pd
from matplotlib import pyplot as plt

#plt.style.use('fivethirtyeight')

data = pd.read_csv('data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color='#444444',
		 linestyle='--', label='All_Devs')

plt.plot(ages, py_salaries, label='Python')

overall_median = 57287

plt.fill_between(ages, py_salaries, js_salaries, where=(py_salaries > js_salaries), interpolate=True, alpha=0.25, label='Above Avg')
plt.fill_between(ages, py_salaries, js_salaries, where=(py_salaries <= js_salaries), interpolate=True, color='r', alpha=0.25, label='Below Avg')  # also can add color

plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()
plt.savefig('plot.png')
plt.show()
