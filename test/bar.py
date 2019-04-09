__author__ = 'zoulida'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def bar():

    df = pd.DataFrame(
    {'HEIGHT': [175, 165, 162, 158, 180], 'AGE': [23, 30, 27, 21, 35], 'SCORE': [80, 100, 70, 85, 65]},
         columns = ['HEIGHT', 'AGE', 'SCORE'],
         index = ['jack', 'leo', 'james', 'Lily', 'David'])


    df_plot = df.plot(kind='bar', rot=-45)


    df_plot.legend(df.columns, loc=2)
    df_plot.set_yticks([x for x in range(1, 180, 10)])
    df_plot.set_ylabel('Longdian')


    plt.savefig('test.jpg')
    plt.show()

def weather():


    df = pd.DataFrame({'2018-8': [30, 29, 34, 23, 45, 12, 23, 34, 36, 37, 38, 39, 30, 23, 25, 27, 28, 33, 34, 36, 21,
                                  24, 26, 46, 30, 36, 56, 23, 35, 32]})
    ax = df.plot(kind='line', marker='v', rot=-45, ylim=[10, 60])
    date_range = pd.date_range('8/1/2018', '8/31/2018', freq='d')
    ax.set_xticks(date_range.day)


    plt.savefig('test.jpg')
    plt.show()

if __name__ == '__main__':
    bar()
    #weather()
