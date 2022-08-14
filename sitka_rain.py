import csv
from datetime import datetime
import matplotlib.pyplot as plt

data = 'data/sitka_weather_2018_simple.csv'
with open(data) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Select of the highest temperatures
    dates, rains = [], []
    for row in reader:
        current_day = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            rain = float(row[3])
        except ValueError:
            print(f'Missing data for {current_day}')
        else:
            dates.append(current_day)
            rains.append(rain)


# Chart data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, rains, c='blue', alpha=0.5)
plt.fill_between(dates, rains, facecolor='blue', alpha=0.2)

# Format plot.
title = "Daily rainfall amounts in Sitka in 2018"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
