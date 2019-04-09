__author__ = 'zoulida'



# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif']=['SimHei']  #如果要显示中文字体，则在此处设为：SimHei
plt.rcParams['axes.unicode_minus']=False  #显示负号

x = np.array([2,4,6,8,10])
A = np.array([10,21,30,43,41])
B= np.array([29,18,9,3,2.6])
C=np.array([14.87179487,19.38461538,13.84615385,5.608695652,4.889908257])
#D=np.array([0.9664, 0.6701, 0.9884, 0.7929, 0.8790, 0.6072, 0.9352, 0.7920, 0.9170, 0.9254])

#label在图示(legend)中显示。若为数学公式，则最好在字符串前后添加"$"符号
#color：b:blue、g:green、r:red、c:cyan、m:magenta、y:yellow、k:black、w:white、、、
#线型：-  --   -.  :    ,
#marker：.  ,   o   v    <    *    +    1
plt.figure(figsize=(10,5))
plt.grid(linestyle = "--")      #设置背景网格线为虚线
ax = plt.gca()
ax.spines['top'].set_visible(False)  #去掉上边框
ax.spines['right'].set_visible(False) #去掉右边框

plt.plot(x,A,color="black",label="查全率",linewidth=1.5)
plt.plot(x,B,"k--",label="查准率",linewidth=1.5)
plt.plot(x,C,color="red",label="F1 Score",linewidth=1.5)
#plt.plot(x,D,"r--",label="D algorithm",linewidth=1.5)

#group_labels=['dataset1','dataset2','dataset3','dataset4','dataset5',' dataset6','dataset7','dataset8','dataset9','dataset10'] #x轴刻度的标识
#plt.xticks(x,group_labels,fontsize=12,fontweight='bold') #默认字体大小为10
plt.xticks(x, fontsize=12,fontweight='bold') #默认字体大小为10
plt.yticks(fontsize=12,fontweight='bold')
#plt.title("example",fontsize=12,fontweight='bold')    #默认字体大小为12
plt.xlabel("p Value(%)",fontsize=13,fontweight='bold')
plt.ylabel("Score",fontsize=13,fontweight='bold')
#plt.xlim(3,21)         #设置x轴的范围
#plt.ylim(0.5,1)

#plt.legend()          #显示各曲线的图例
plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize=12,fontweight='bold') #设置图例字体的大小和粗细

plt.savefig('D:\\filename.svg',format='svg')  #建议保存为svg格式，再用inkscape转为矢量图emf后插入word中
plt.show()

