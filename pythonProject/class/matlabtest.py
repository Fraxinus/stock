#_*_coding:utf-8_*_

from PyQt4 import QtGui, QtCore, uic
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as figureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import sys

import prettyplotlib as ppl


class DrawWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(DrawWidget, self).__init__(parent)

        figure = plt.gcf()
        x = [1, 2, 3, 3]
        y = [4, 5, 5, 6]
        t = np.arange(0., 5., 0.2)
        # plt.plot(t, t, 'g--', t, t*2, 'bs', t, t**2, 'r^')
        # plt.axis([-2, 10, -2, 30])
        # #  是指定xy坐标的起始范围，它的参数是列表[xmin, xmax, ymin, ymax]。
        # plt.text(2, .25, r'$\mu=100,\ \sigma=15$')
        # plt.title('example')
        # plt.xlabel('x')
        # plt.ylabel('y')

        self.xxlineH = None
        self.xxlineV = None
        self.xxax = figure.gca()
         # fig, ax = plt.subplots(1)
        # np.random.seed(14)
        x = ppl.plot(figure.gca(), t, t, '--', color=(255/255.,150/255.,250/255.), label=str('t, t'), pickradius=28.0)
        ppl.plot(figure.gca(),  t, t*2, label=str(' t, t*2'), pickradius=8.0)
        ppl.plot(figure.gca(), t, t**2, label=str('t, t**2'), pickradius=8.0)
        ppl.legend(figure.gca(), loc='upper left', ncol=3)

        # figure.gca().lines.remove(x[0])

        # ax = plt.gca()#移动坐标轴
        # ax.spines['right'].set_color('none')#去除右边的轴
        # ax.spines['top'].set_color('none')#去除顶轴
        # ax.xaxis.set_ticks_position('bottom')
        # #下轴移至数据0点，理想状态下0点为中心点，具体跟数据位置有关
        # ax.spines['bottom'].set_position(('data', 0))
        # ax.yaxis.set_ticks_position('left')
        # ax.spines['left'].set_position(('data', 0))

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

        # 'button_press_event':鼠标按键按下时触发
        # 'button_release_event':鼠标按键释放时触发
        # 'motion_notify_event':鼠标移动时触发
        # 当前的所有注册的响应函数可以通过Figure.canvas.callbacks.callbacks
        for key, funcs in figure.canvas.callbacks.callbacks.iteritems():
            print key
            for cid, wrap in sorted(funcs.items()):
                func = wrap.func
                print "    {0}:{1}.{2}".format(cid, func.__module__, func)

        self.text = figure.gca().text(0.5, 10.5, "event", ha="center", va="center", fontdict={"size":20})
        self.canvas = figureCanvas(figure)

        self.canvas.setFocusPolicy( QtCore.Qt.ClickFocus) ##qt4需要加这两句，否者信号被qt拦截，无法到达matplot
        self.canvas.setFocus()
        figure.canvas.mpl_connect('key_press_event', self.on_key_press)
        # figure.canvas.mpl_disconnect(figure.canvas.manager.key_press_handler_id)
        figure.canvas.mpl_connect('motion_notify_event', self.on_mouse_move)
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

        # import prettyplotlib as ppl
        # fig, ax = plt.subplots(1)
        # np.random.seed(14)
        # n = 10
        # ppl.bar(plt.gca(), np.arange(n), np.abs(np.random.randn(n)), annotate=True, grid='y')



        layout = QtGui.QHBoxLayout(self)
        layout.addWidget(self.canvas)
        layout.addWidget(self.canvas2)

        self.canvas2.draw()

    def on_mouse_move(self, event):
        print event.name, ',', event.x, ',', event.y, ',', event.xdata, ',', event.ydata
        if event.xdata and event.ydata:
            info = "{}\nButton:{}\nFig x,y:{}, {}\nData x,y:{:3.2f}, {:3.2f}".format(
                event.name, event.button, event.x, event.y, event.xdata, event.ydata)
            self.text.set_text(info)

        for line in self.xxax.lines:
            if line.contains(event)[0]:
                self.highlight(line)
                break
            else:
                self.highlight(None)

            #绘制准心
            if not self.xxlineH:
                print 'draw line'
                self.xxlineH = self.xxax.plot([0, event.xdata], [event.ydata, event.ydata], 'k')[0]
                self.xxlineV = self.xxax.plot([event.xdata, event.xdata], [0, event.ydata], 'k')[0]
            else:
                self.xxax.lines.remove(self.xxlineH)
                self.xxax.lines.remove(self.xxlineV)
                self.xxlineH = self.xxax.plot([0, event.xdata], [event.ydata, event.ydata], 'k')[0]
                self.xxlineV = self.xxax.plot([event.xdata, event.xdata], [0, event.ydata], 'k')[0]
                self.text.set_x(event.xdata)
                self.text.set_y(event.ydata)
            self.canvas.draw()

    def on_key_press(self, event):
            print event.key
            # sys.stdout.flush()
            if event.key == 'escape':
                self.close()

    def highlight(self, target):
        need_redraw = False
        if target is None:
            for line in self.xxax.lines:
                line.set_linewidth(1.0)
                need_redraw = True
        else:
            for line in self.xxax.lines:
                line.set_alpha(1.0)
            need_redraw = True
            target.set_linewidth(20.0)

        if need_redraw:
            self.xxax.figure.canvas.draw_idle()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ui = DrawWidget()
    ui.show()
    ui.raise_()
    sys.exit(app.exec_())