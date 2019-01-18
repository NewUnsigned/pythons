import csv
from matplotlib import pyplot as plt

# python使用datetime模块创建日期对象，然后调用方法strptime('2014-7-1', '%Y-%m-%d')，即可
# 第一个参数是字符串类型的日期，第二个参数是日期格式，各种格式对照如下
# %A 星期的名称，如：Monday
# %B 月份名，如：January
# %m 用数字表示的月份（01~12)
# %d 用数字表示月份中的一天（01~31）
# %Y 四位的年份，如：2015
# %y 两位的年份，如：15
# %H 24小时制的小时数（00~23）
# %I 12小时制的小时数（01~12）
# %p am或pm
# %M 分钟数（00~59）
# %S 秒数（00~59）
# firstdate = datetime.strptime('2014-7-1', '%Y-%m-%d')
# print(firstdate)

from datetime import datetime


def show_temperature(file):
    filename = file

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        print(header_row)

        # for index, column_header in enumerate(header_row):
        # print(index, column_header)

        highs, dates, lows = [], [], []
        for row in reader:
            try:
                date = datetime.strptime(row[0], '%Y-%m-%d')
                high = int(row[1])
                low = int(row[2])
            except ValueError:
                print(date, 'missing data')
            else:
                dates.append(date)
                highs.append(high)
                lows.append(low)

        plt.figure(dpi=128, figsize=(10, 6))
        plt.plot(dates, highs, c='red', alpha=0.5)
        plt.plot(dates, lows, c='blue', alpha=0.5)


# filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'

plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

# show_temperature('sitka_weather_2014.csv')
show_temperature('death_valley_2014.csv')

plt.show()
