from datetime import datetime
import matplotlib.dates as mdates
from matplotlib import pyplot as plt


if __name__ == '__main__':
    plt.rcParams['font.family'] = 'SimHei,STHeiti'

    with open('log.txt', 'r') as f:
        x = f.readlines()

    x = [datetime.strptime(i.strip(), '%Y-%m-%d %H:%M:%S') for i in x]
    bins = 100

    fig, ax = plt.subplots()

    plt.hist(x, bins=bins)
    fig.autofmt_xdate()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    # ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
    ax.xaxis.set_label_text('时间点')
    ax.yaxis.set_label_text('有号次数')

    plt.show()
