# -*- coding: utf-8 -*-

__author__ = 'kk'

# Created: Wed Feb 28 16:05:47 2015

import sys
import datetime

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as figureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import prettyplotlib as ppl


class StocksGraphView(object):
    def __init__(self, parent):
        # super(StocksGraphView, self).__init__(parent)
        self.fatherHandle = parent

        self.figure = plt.gcf()
        self.ax = self.figure.gca()
        self.canvas = figureCanvas(self.figure)
        self.hintText = self.ax.text(-.5, -.5, "", ha="right", va="baseline", fontdict={"size": 15})

        self.figure.canvas.mpl_connect('key_press_event', self._on_key_press)
        self.figure.canvas.mpl_connect('button_press_event', self._on_button_press)
        # figure.canvas.mpl_disconnect(figure.canvas.manager.key_press_handler_id)
        self.figure.canvas.mpl_connect('motion_notify_event', self._on_mouse_move)

        self._lines = {}
        self._hHintLine = None
        self._vHintLine = None

        self.ax.fmt_date = matplotlib.dates.DateFormatter('%Y-%m-%d')
        self.strpdate2num = matplotlib.dates.strpdate2num('%Y-%m-%d')

        plt.subplots_adjust(left=.04, bottom=.0, right=.98, top=.97,
                      wspace=.0, hspace=.0)
        plt.minorticks_on()

        self.ax.grid()

        self.ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%y\n-\n%m\n-\n%d'))


    def setFocus(self, focus):
        """
        qt4 need this, or matplot can't get signal because qt.
        :param focus: QtCore.Qt.ClickFocus
        """
        self.canvas.setFocusPolicy(focus)
        self.canvas.setFocus()

    def _on_mouse_move(self, event):
        # print event.name, ',', event.x, ',', event.y, ',', event.xdata, ',', event.ydata
        # if event.xdata and event.ydata:
        #     info = "{}\nButton:{}\nFig x,y:{}, {}\nData x,y:{:3.2f}, {:3.2f}".format(
        #         event.name, event.button, event.x, event.y, event.xdata, event.ydata)
        #     self.hintText.set_text(info)
        #     self.hintText.set_x(event.xdata)
        #     self.hintText.set_y(event.ydata)
        #     self.canvas.draw()
        for line in self.ax.lines:
            if line.contains(event)[0]:
                self.highlight(line)
                if event.xdata and event.ydata:
                    code = str(line).replace('Line2D(', '').replace(')', '')
                    dateTime = matplotlib.dates.num2date(event.xdata)
                    date_str = dateTime.strftime('%Y-%m-%d')
                    info = "{}\n{}\n{:3.2f}".format(code, date_str, event.ydata)
                    self.hintText.set_text(info)
                    self.hintText.set_x(event.xdata)
                    self.hintText.set_y(event.ydata)
                break
            else:
                self.hintText.set_x(-100)
                self.highlight(None)

    def _on_key_press(self, event):
        print 'graphView keyPress', event.key
        if event.key == 'escape':
            self.fatherHandle.close()

    def _on_button_press(self, event):
        print 'graphView buttonPress'
        # print event.name, ',', event.x, ',', event.y, ',', event.xdata, ',', event.ydata
        if event.xdata and event.ydata:
            for line in self.ax.lines:
                if line.contains(event)[0]:
                    if event.xdata and event.ydata:
                        code = str(line).replace('Line2D(', '').replace(')', '')
                        self.fatherHandle.selectStockItem(code)
                    break

    def addDateLine(self, x_array, y_array, code, color_r, color_g, color_b, needRedrawXLabel=True):
        date_list = []
        for date in x_array:
            date_list.append(self.strpdate2num(date))

        lines = plt.plot(date_list, y_array,
                         color=(color_r / 255., color_g / 255., color_b / 255.),
                         linestyle='-', label=code, pickradius=0.6)

        # lines = plt.scatter(date_list, y_array, color=(color_r / 255., color_g / 255., color_b / 255.), label=code, pickradius=0.6)

        self._lines[code], = lines

        if needRedrawXLabel:
            locs = self.ax.xaxis.get_ticklocs()
            range = locs[len(locs) - 1] - locs[0]
            if 100 <= range < 1000:
                self.ax.xaxis.set_major_locator(
                    matplotlib.ticker.MultipleLocator(range / 10))
            if 1000 <= range < 8000:
                self.ax.xaxis.set_major_locator(
                    matplotlib.ticker.MultipleLocator(range / 20))
            if range >= 8000:
                self.ax.xaxis.set_major_locator(
                    matplotlib.ticker.MultipleLocator(range / 30))
            self.figure.autofmt_xdate()
            for label in self.ax.xaxis.get_ticklabels():
                label.set_ha('center')
                label.set_rotation(0)


    def draw(self):
        self.canvas.draw_idle()

    def removeLineByCode(self, code):
        self.ax.lines.remove(self._lines[code])
        del self._lines[code]
        # for k, v in self._lines.iteritems():
        #     print k, v

    def removeAllLine(self):
        for k, v in self._lines.iteritems():
            self.ax.lines.remove(v)
        del self._lines

    def highlight(self, target):
        need_redraw = False
        if target is None:
            for line in self.ax.lines:
                line.set_linewidth(1.0)
                need_redraw = True
        else:
            for line in self.ax.lines:
                line.set_alpha(1.0)
            need_redraw = True
            target.set_linewidth(1.5)

        if need_redraw:
            self.ax.figure.canvas.draw_idle()

    def __del__(self):
        print 'graph view dealloc'
        plt.close()