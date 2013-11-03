# coding=utf-8
__author__ = 'kk'

import StockData
import StockNetwork
import loader_CVS


def callback_stockDetail_newFromCode_list(code, exchangeName):
    content = None
    if exchangeName == StockData.ShangHaiStockDB:
        content = StockNetwork.getAllHistory(code, StockNetwork.history_extentName_SH)

    if exchangeName == StockData.ShenZhenStockDB:
        content = StockNetwork.getAllHistory(code, StockNetwork.history_extentName_SZ)

    if not content:
        return None

    loader = loader_CVS.Loader_CVS(content=content)
    # ret = loader.load_file_safe()
    # if not ret:
    #     return None
    parse_list = loader.parse_content(1, True, True)
    # loader.loader_file_close()
    return parse_list


def callback_stockDetail_newFromCodeAndLastDate_list(code, exchangeName, date_last):
    content = None
    if exchangeName == StockData.ShangHaiStockDB:
        content = StockNetwork.getHistoryByStartDate(code, StockNetwork.history_extentName__SH, date_last)

    if exchangeName == StockData.ShenZhenStockDB:
        content = StockNetwork.getHistoryByStartDate(code, StockNetwork.history_extentName__SZ, date_last)

    if not content:
        return None

    loader = loader_CVS.Loader_CVS(content=content)
    # ret = loader.load_file_safe()
    # if not ret:
    #     return None
    parse_list = loader.parse_content(2, True, True)
    # loader.loader_file_close()
    return parse_list





stockData = StockData.StockDataClass(StockData.ShangHaiStockDB)
# stockData.changeStockExchange(StockData.ShenZhenStockDB)
# print "collection_names:", stockData.db.collection_names()
# print "getAllStockCollectionsName_list:", stockData.getAllStockCollectionsName_list()
# print "getAllStockCode_list:", stockData.getAllStockCode_list()

print "initNewStockDetail:"
stockData.callback_stockDetail = callback_stockDetail_newFromCode_list
print "resualt:",stockData.initNewStockDetail()

# stockData.stock_test()

# print 'insertNewDateStockDetail'
# stockData.callback_stockDetail = callback_stockDetail_newFromCodeAndLastDate_list
# print "resualt:", stockData.insertFreshDateStockDetail_auto("600000")
#
#
if stockData:
    stockData
    stockData = None


    # from Tkinter import *
    # def helllllo():
    #     print "hello world"
    # win = Tk()
    # win.title('hello world')
    # win.geometry('200x300+500+200')
    # btn = Button(win, text='hello', command=helllllo)
    # btn.pack(expand=YES, fill=BOTH)
    # mainloop()