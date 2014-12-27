#_*_coding:utf-8_*_

from PyQt4 import QtGui, QtCore, uic
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as figureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import sys


class DrawWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(DrawWidget, self).__init__(parent)

        figure = plt.gcf()
        x = [1, 2, 3, 3]
        y = [4, 5, 5, 6]
        t = np.arange(0., 5., 0.2)
        plt.plot(t, t, 'g--', t, t*2, 'bs', t, t**2, 'r^')
        plt.axis([-2, 10, -2, 30])
        #  是指定xy坐标的起始范围，它的参数是列表[xmin, xmax, ymin, ymax]。
        plt.text(2, .25, r'$\mu=100,\ \sigma=15$')
        plt.title('example')
        plt.xlabel('x')
        plt.ylabel('y')

        ax = plt.gca()#移动坐标轴
        ax.spines['right'].set_color('none')#去除右边的轴
        ax.spines['top'].set_color('none')#去除顶轴
        ax.xaxis.set_ticks_position('bottom')
        #下轴移至数据0点，理想状态下0点为中心点，具体跟数据位置有关
        ax.spines['bottom'].set_position(('data', 0))
        ax.yaxis.set_ticks_position('left')
        ax.spines['left'].set_position(('data', 0))

        # plt.xlim(t.min()*1.1, t.max()*1.1)#X轴的范围
        # plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],#从新定义刻度
        #            [r'$-\pi$',r'$-\pi/2$',r'$0$',r'$\pi/2$',r'$\pi$'])#X轴的刻度值
        # plt.ylim(s.min()*1.1,s.max()*1.1)#Y轴的范围
        # plt.yticks([-1,0,1],[r'$-1$',r'$0$',r'$+1$']) #设置Y轴的刻度值,第二个参数对其进行格式化

        plt.annotate(r'$sin(\frac{2\pi}{3})=(\frac{\sqrt{3}}{2})$',
                     xy=(5,  5), xycoords='data',
                     xytext=(15, 200), textcoords='offset points', fontsize=16,
                     arrowprops = dict(arrowstyle='->', connectionstyle='arc3,rad=.1'))

        plt.plot([5, 5], [0, 5], 'ro', color='black', linewidth=1.0, linestyle='--', label='$cos(x)$')
        # plt.plot([5, 5], [0, 5],'ro',  linewidth=5.0, label='$sin(x)$')
        # plt.scatter([5, 5], [0, 5], 50, color='red')

        # for i in ax.get_xticklabels() + ax.get_yticklabels():#从新设置所有bbox
        #     i.set_fontsize(15)
        #     i.set_bbox(dict(facecolor='white',edgecolor='none',alpha=0.65))

        self.canvas = figureCanvas(figure)
        self.canvas.draw()

        figure2 = plt.figure(2, figsize=(8, 4), facecolor='green', edgecolor='red')
        #figsize = (8,4)表示figure的大小，屏幕显示 640 * 320 ， 输出显示 800*400，这个要注意。
        #显示色和外框线条颜色设置。
        self.canvas2 = figureCanvas(figure2)

        plt.subplot(311)# 子区，3行，1列, 第1个
        y = [1, 2, 3, 4]
        x = [4, 5, 5, 6]
        plt.plot(x, y, 'bo', x, y, 'r')
        plt.title('examrple2')
        plt.xlabel('x')
        plt.ylabel('y')

        plt.subplot(323)# 子区，3行，2列, 第3个
        x = [1, 2, 3]
        y = [4, 5, 6]
        plt.bar(x, y)
        plt.title('Example3')
        plt.xlabel('x')
        plt.ylabel('y')

        plt.subplot(336)# 子区，3行，3列, 第6个
        x = [1, 2, 3]
        y = [4, 5, 6]
        plt.scatter(x, y)
        plt.title('Example4')
        plt.xlabel('x')
        plt.ylabel('y')

        plt.subplot(313)# 子区，3行，1列, 第3个
        mu, sigma = 100, 15
        x = mu + sigma*np.random.randn(10000)
        # the histogram of the data
        n, bins, patches = plt.hist(x, 150, normed=1, facecolor='g', alpha=0.75)
        plt.xlabel('Smarts')
        plt.ylabel('Probability')
        plt.title('Histogram of IQ')
        plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
        plt.axis([40, 160, 0, 0.03])
        plt.grid(True)

        self.canvas2.draw()

        layout = QtGui.QHBoxLayout(self)
        layout.addWidget(self.canvas)
        layout.addWidget(self.canvas2)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ui = DrawWidget()
    ui.show()
    sys.exit(app.exec_())