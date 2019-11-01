__author__ = 'zoulida'
import numpy as np
import matplotlib.pyplot as plt

##-----读取数据----------
data = open("E:/ss.csv").readlines()
name = []
VI = []
VC = []
for i in range(len(data)):
    data[i] = data[i].strip('\n').split(',')
    name.append(data[i][0])
    VI.append(eval(data[i][1]))
    VC.append(eval(data[i][2]))

##-----绘制右边柱子----------
##w是柱子的宽度
w = 1
##生成绘图对象
fig = plt.figure()
##将画布划分成1行1列，在第一个方格中绘制
ax1 = fig.add_subplot(111)
##隐藏上边框
ax1.spines['top'].set_color('none')
##设置刻度范围
ax1.set_ylim(-max(VC), max(VC))
##设置x轴为下边框
ax1.xaxis.set_ticks_position('bottom')
##将x轴移动至0刻度处
ax1.spines['bottom'].set_position(('data', 0))
##设置x轴的标签，3个单位长度间隔，和柱子间距一致
##ax1.set_xticks(np.arange(0,len(name)*3,3))
ax1.set_xticklabels(name, ha='left', fontsize=9)
##设置柱子间距
idx = np.arange(w, len(name) * 3 + w, 3)
##生成柱状图，VI是数据列，width是柱子宽度
plt.bar(idx, VC, width=w, color='red')

##-----绘制左边柱子----------
##共享x坐标，这是关键
ax2 = ax1.twinx()
ax2.spines['bottom'].set_position(('data', 0))
ax2.set_ylim(-max(VI), max(VI))
ax2.set_xticks(np.arange(0, len(name) * 3, 3))
ax2.set_xticklabels(name, ha='left', fontsize=9)

plt.bar(idx - w, VI, width=w)
plt.show()