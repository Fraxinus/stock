# coding=utf-8
__author__ = 'kk'
__data_dir__ = 'dataFile'

import StockData
import StockNetwork
import loader_CVS
import data_parser
import csv


stockData = StockData.StockDataClass(StockData.ShangHaiStockDB)
stockData.changeStockExchange(StockData.ShenZhenStockDB)

# data = stockData.loadStockDayDataByDate("000001", "2014-01-01", "2016-12-31")
# print data
# header = ['date', 'volume', 'low', 'high', 'adj_close', 'close', 'open']
# f = file(__data_dir__ + "/" + "sh000001.csv", "wb")
# writer = csv.DictWriter(f, header)
# writer.writeheader()
# writer.writerows(data)
# f.close()

stock_cursor = stockData.db[stockData.stockIndexCollectionName].find({}, {"code": 1, "name": 1, "_id": 0})
for stock in stock_cursor:
    print stock['code'], stock['name']