from matplotlib import pyplot as plt
from read_data import read_date_max_min_temp

# filename = './data/sitka_weather_07-2014.csv'
filename_sitka = './data/sitka_weather_2014.csv'
filename_death_valley = './data/death_valley_2014.csv'
(dates_sitka,highs_sitka,lows_sitka) = read_date_max_min_temp(filename_sitka)
(dates_dv,highs_dv,lows_dv) = read_date_max_min_temp(filename_death_valley)

fig = plt.figure(dpi=128,figsize=(10,12))
plt.subplot(2,1,1)
plt.plot(dates_sitka,highs_sitka,c='red',linewidth=1)
plt.plot(dates_sitka,lows_sitka,c='blue',linewidth=1)
plt.fill_between(dates_sitka,highs_sitka,lows_sitka,facecolor='yellow',alpha=0.5)  # alpha - transparency
plt.grid(axis='both',which='both')
fig.autofmt_xdate()
plt.title('Daily high and low temperatures, Sitka, 2014',fontsize=18)
plt.xlabel('Date',fontsize=16)
plt.ylabel('Temperature(F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.subplot(2,1,2)
plt.plot(dates_dv,highs_dv,c='red',linewidth=1)
plt.plot(dates_dv,lows_dv,c='blue',linewidth=1)
plt.fill_between(dates_dv,highs_dv,lows_dv,facecolor='yellow',alpha=0.5)  # alpha - transparency
plt.grid(axis='both',which='both')
fig.autofmt_xdate()
plt.title('Daily high and low temperatures, Death Valley, 2014',fontsize=18)
plt.xlabel('Date',fontsize=16)
plt.ylabel('Temperature(F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()
