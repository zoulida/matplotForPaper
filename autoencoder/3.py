__author__ = 'zoulida'
#python 画柱状图折线图
#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
a=[1228.3,3.38,63.8,0.07,0.16,6.74,1896.18]  #数据
b=[0.12,-12.44,1.82,16.67,6.67,-6.52,4.04]
wc_cost = [95,100,90,101,105,110]
Random_cost = [99,89,103,109,88,120]
wc_time = [551,546,561,420,356,360]
Random_time = [541,551,579,471,421,409]
l=[i for i in range(6)]
l = np.arange(len(l))

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

fmt='%.2f%%'
yticks = mtick.FormatStrFormatter(fmt)  #设置百分比形式的坐标轴
lx=['0','20','40','60','80','100']

fig = plt.figure()
ax1 = fig.add_subplot(111)
width = 1/4
ax1.bar(l,wc_cost,width,alpha = 0.9,color='orange',label=u'KMCAET-WC代价', zorder=30)
ax1.bar(l + width,Random_cost,width,alpha = 0.9,color='green',label=u'KMCAET-Random代价', zorder=30)

#ax1.yaxis.set_major_formatter(yticks)
#for i,(_x,_y) in enumerate(zip(l,b)):
#    plt.text(_x,_y,b[i],color='black',fontsize=10,)  #将数值显示在图形上
ax1.legend(loc=1)
#ax1.set_ylim([-20, 30]);
ax1.set_ylabel('时间(s)');
ax1.set_xlabel('c Value(%)');
plt.legend(prop={'family':'SimHei','size':8},loc="upper right")  #设置中文
ax2 = ax1.twinx() # this is the important function


#plt.bar(l,a,alpha=0.3,color='blue',label=u'产量')
#plt.bar(l,a,alpha=0.3,color='red',label=u'开心')
ax2.legend(loc=2)
ax2.plot(l, wc_time,'or-',label=u'KMCAET-WC收敛时间', zorder=10);
ax2.plot(l, Random_time,'vb-',label=u'KMCAET-Random收敛时间', zorder=10);
ax2.set_ylabel('代价');
#ax2.set_xlabel('代价');
#ax2.set_ylim([0, 600])  #设置y轴取值范围
plt.legend(prop={'family':'SimHei','size':8},loc="upper left")
plt.xticks(l+1/8,lx)
#plt.xlabel("c Value(%)",fontsize=13,fontweight='bold')
plt.show()