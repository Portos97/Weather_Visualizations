import csv
from datetime import datetime
import matplotlib.pyplot as plt

data = 'data/death_valley_2018_simple.csv'
with open(data) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Select of the highest temperatures
    dates, highs, lows = [], [], []
    for row in reader:
        current_day = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f'Missing data for {current_day}')
        else:
            dates.append(current_day)
            highs.append(high)
            lows.append(low)

# Chart data
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Chart format
ax.set_title("Highest and lowest temperatures in Death Valley in 2018", fontsize=25)
ax.set_xlabel('', fontsize=12)
fig.autofmt_xdate()
ax.set_ylabel('Temperature', fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
