# coding=utf-8
__author__ = 'kk'

__stockIndexCollection__ = 'stock_index'
__serviceAddr__ = "127.0.0.1"
__servicePort__ = 37017
__cappedSize__ = 1572864  # 1.5Mb
ShangHaiStockDB = 'SH'
ShenZhenStockDB = 'SZ'
import database_m
import time
import datetime

__isTest__ = True  # #--正式环境时更改此变量为False
import pprint


def insertStock(db, collectionName, date, open, high, low, close, volume, adj_close):
        return db[collectionName].insert({"date":date, "open":open, "high":high, "low":low, "close":close,
                                          "volume":volume, "adj_close":adj_close})


def insertStockIndex(db, code, name,
                     companyShortName, companyFullName, engName, regAddr,
                     ACode, AName, AOrgDate, AStockCount, ACirculate,
                     BCode, BName, BOrgDate, BStockCount, BCirculate,
                     area, province, city, businessClassify, HP):
        AStockCount_ = 0
        ACirculate_ = 0
        BStockCount_ = 0
        BCirculate_ = 0
        if AStockCount and len(AStockCount) != 0:
            AStockCount_ = int(AStockCount.replace(',', ""))
        if ACirculate and len(ACirculate) != 0:
            ACirculate_ = int(BCirculate.replace(',', ""))
        if BStockCount and len(BStockCount) != 0:
            BStockCount_ = int(BStockCount.replace(',', ""))
        if BCirculate and len(BCirculate) != 0:
            BCirculate_ = int(BCirculate.replace(',', ""))

        return db[__stockIndexCollection__].insert({"code":code, "name":name, "count":0, "date_origin":"", "date_last":"",
                                          "price_highest":0.0, "price_last":0.0, "flag3":None, "flag4":None,
                                          "flag5":None, "companyShortName":companyShortName, "companyFullName":companyFullName, "engName":engName,
                                          "regAddr":regAddr, "ACode":ACode, "AName":AName, "AOrgDate":AOrgDate,
                                          "AStockCount":AStockCount_, "ACirculate":ACirculate_, "BCode":BCode, "BName":BName,
                                          "BOrgDate":BOrgDate, "BStockCount":BStockCount_, "BCirculate":BCirculate_, "area":area,
                                          "province":province, "city":city, "businessClassify":businessClassify, "HP":HP})


class StockDataClass:
    def __init__(self, DBName, stockIndexCollectionName=__stockIndexCollection__):
        self.stockIndexCollectionName = stockIndexCollectionName
        self.db = None
        self.curExchangeName = DBName
        self.db_factory = database_m.DateBase_Factory(DBName)
        if self.db_factory:
            if __isTest__:
                self.db = self.db_factory.doConnect()
            else:
                self.db = self.db_factory.doConnect(addr=__serviceAddr__, port=__servicePort__)

    def __del__(self):
        if self.db:
            self.db = None
        if self.db_factory:
            self.db_factory.closeConnect()
            self.db_factory = None
        print('StockDataClass: dealloc')

    def callback_stockDetail(self):
        """
        获取数据的回调，需要执行数据更新时必须先重载
        获取外部数据统一的接口
        根据实际情况自行设计
        """
        print('StockDataClass: warning, callback hasn`t rewrite')
        raise NotImplementedError("callback hasn`t rewrite")

    def callback_reset(self):
        """
        重置回调到未重载状态
        """
        print('StockDataClass: warning, callback hasn`t rewrite')
        raise NotImplementedError("callback hasn`t rewrite")

    def changeStockExchange(self, stockExchangeName):
        """
        更换交易所
        :param stockExchangeName:
        """
        self.db = self.db_factory[stockExchangeName]
        self.curExchangeName = stockExchangeName

    def isConnectSuccess(self):
        if self.db:
            return True
        return False

    def getServerIP(self):
        if __isTest__:
            return __serviceAddr__ + ':27017'
        return __serviceAddr__ + ':' + __servicePort__

    #-------------stock---function----------------------------------
    def stockIndexUpdate(self):
        """
        更新股票元数据
        所更新的内容取决于self.stockIndexCollectionName（或__stockIndexCollection__）表中code还不存在的
        需要以foo(exchangeName) 重载callback_stockDetail()，结果是返回metadataList列表，
        重载了self.db_factory.insertDoc = insertStock
        所有重载函数完成后reset
        :return: codes in a list which has been insert into DB
        """
        if not self.db:
            print 'StockDataClass: has no connection'
            return None

        metadataList = self.callback_stockDetail(self.curExchangeName)

        self.db_factory.insertDoc = insertStockIndex

        insert_success_List = []
        for data in metadataList:
            if self.curExchangeName == ShangHaiStockDB:
                isExist = self.db[__stockIndexCollection__].find({"code":data['code']}).count()
            else:
                isExist = self.db[__stockIndexCollection__].find({"code":data['companyCode']}).count()

            if isExist:
                if self.curExchangeName == ShangHaiStockDB:
                    print 'isExist :', data['code']
                else:
                    print 'isExist :', data['companyCode']

                continue

            try:
                if self.curExchangeName == ShangHaiStockDB:
                    ret = self.db_factory.insertDoc(self.db, data['code'], data['name'], data['abbreviation'],
                                                    '', '', '',
                                                    '', '', '', 0, 0,
                                                    '', '', '', 0, 0,
                                                    '', '', '', '', '')
                else:
                    ret = self.db_factory.insertDoc(self.db, data['companyCode'], data['companyShortName'], data['companyShortName'],
                                                    data['companyFullName'], data['engName'], data['regAddr'],
                                                    data['ACode'], data['AName'], data['AOrgDate'], data['AStockCount'], data['ACirculate'],
                                                    data['BCode'], data['BName'], data['BOrgDate'], data['BStockCount'], data['BCirculate'],
                                                    data['area'], data['province'], data['city'], data['businessClassify'], data['HP'])
            except Exception, e:
                ret = False
                print 'StockDataClass stockIndexUpdate:', e

            if not ret:
                if self.curExchangeName == ShangHaiStockDB:
                    print 'StockDataClass stockIndexUpdate: %s -- %s insert error,' % (data['code'], data['name'])
                else:
                    print 'StockDataClass stockIndexUpdate: %s -- %s insert error,' % (data['companyCode'], data['companyShortName'])
                insert_success_Flag = False
                break
            if self.curExchangeName == ShangHaiStockDB:
                insert_success_List.append(data['code'])
            else:
                insert_success_List.append(data['companyCode'])

        # #--reset callback function
        self.callback_stockDetail = self.callback_reset
        self.db_factory.insertDoc = self.db_factory.resetRewrite
        print len(insert_success_List)
        return insert_success_List

    def stockIndexInsertOne(self, code, name,
                            shortName='', fullName='', engName='',
                            regAddr='', ACode='', AName='',
                            AOrgDate='', AStockCount=0,
                            ACirculate=0, BCode='', BName='',
                            BOrgDate='', BStockCount=0, BCirculate=0,
                            area='', province='', city='',
                            businessClassify='', HP=''):

        if self.curExchangeName == ShangHaiStockDB:
            isExist = self.db[__stockIndexCollection__].find({"code": code}).count()
        else:
            isExist = self.db[__stockIndexCollection__].find({"code": name}).count()

        if isExist:
            return 0

        self.db_factory.insertDoc = insertStockIndex
        ret = self.db_factory.insertDoc(self.db, code, name, shortName,
                                        fullName, engName, regAddr,
                                        ACode, AName, AOrgDate, AStockCount, ACirculate,
                                        BCode, BName, BOrgDate, BStockCount, BCirculate,
                                        area, province, city, businessClassify, HP)

        self.db_factory.insertDoc = self.db_factory.resetRewrite

        return ret

    def getAllStockCollectionsName_list(self):
        """
        取得所有股票文件的集合名
        :return: list
        """
        if not self.db:
            print 'StockDataClass: has no connection'
            return None

        collection_list = self.db.collection_names()
        collection_list.remove('system.indexes')
        collection_list.remove(self.stockIndexCollectionName)
        return collection_list

    def getAllStockCode_list(self):
        """
        取得所有股票代码
        :return: list
        """
        if not self.db:
            print 'StockDataClass: has no connection'
            return None

        stock_list = []
        stock_cursor = self.db[self.stockIndexCollectionName].find({}, {"code": 1, "_id": 0})
        for stock in stock_cursor:
            stock_list.append(stock['code'])
        return stock_list

    def getStockInfo_dicORList(self, code=None, name=None):
        """
        取得股票整体信息
        当code未设置时，返回全部信息
        :return: list or dic
        """
        if not self.db:
            print 'StockDataClass: has no connection'
            return None

        stock_list = []

        if not code and not name:
            stock_cursor = self.db[self.stockIndexCollectionName].find({}, {"_id": 0})

        if code:
            stock_cursor = self.db[self.stockIndexCollectionName].find({"code":  {'$regex': code}}, {"_id": 0})

        if name:
            stock_cursor = self.db[self.stockIndexCollectionName].find({"name": {'$regex': name, '$options': 'i'}}, {"_id": 0})

        for stock in stock_cursor:
            stock_list.append(stock)
        return stock_list


    def initNewStockDetail(self):
        """
        更新新增股票(新股票)内容
        所更新的内容取决于self.stockIndexCollectionName（或__stockIndexCollection__）表中count数量为0的股票代码
        需要以foo(code, exchangeName) 重载callback_stockDetail(code)，结果是返回data列表，
        需要确保数据日期无重复，否则将会报错
        重载了self.db_factory.insertDoc = insertStock
        所有重载函数完成后reset
        每项股票内容顺序为date, open, high, low, close, volume, adj_close
        :param code:
        :return: the list of insert stock code
        """
        if not self.db:
            print 'StockDataClass: has no connection'
            return None

        need2CreateCollection_Flag = False
        insert_success_Flag = True
        updated_stock_list = []

        self.db_factory.insertDoc = insertStock

        # #--find the stock which doesn`t has stockdetail
        stock_cursor = self.db[self.stockIndexCollectionName].find({"count":0},{"_id":0})

        # #--take the list of stock detail, and find out which stock detail collection hasn`t created
        stock_collection_list = self.getAllStockCollectionsName_list()
        print 'StockDataClass: all stock list :', stock_collection_list

        for stock in stock_cursor:
            insert_success_Flag = True
            print "StockDataClass:", stock
            code = stock['code']
            try:
                stock_collection_list.index(code)
            except Exception, e:
                print 'StockDataClass: find Collection error : %s' % e
                print 'StockDataClass: it means %s is not Existing ' % code
                need2CreateCollection_Flag = True
            else:
                print 'StockDataClass: %s is Existing' % code
                need2CreateCollection_Flag = False
            if need2CreateCollection_Flag:
                # #--Create a collection()
                # ret = self.db_factory.createCappedCollection(code, __cappedSize__)
                ret = self.db_factory.createCollection(code)
                if not ret:
                    print 'StockDataClass: createCappedCollection false,continue'
                    continue
                # #--ceateIndex for date
                print 'StockDataClass: %s:  create index = %s' % (code, self.db_factory.createIndex(code, "date"))

            # #--request the stock detail from a callback funtion,
            # self.callback_stockDetail must be rewrited
            newStockDetail_list = self.callback_stockDetail(code, self.curExchangeName)
            if not newStockDetail_list:
                print 'StockDataClass: %s is load data error' % code
                continue
            # pprint.pprint(newStockDetail_list)

            # #--inset new stock detail into collection
            # #--date, open, high, low, close, volume, adj_close
            for stock in newStockDetail_list:
                # print 'StockDataClass: stock:', stock
                try:
                    ret = self.db_factory.insertDoc(self.db, code, stock[0], float(stock[1]),float(stock[2]),
                                                    float(stock[3]), float(stock[4]), int(stock[5]), float(stock[6]))
                except ValueError:
                    print 'StockDataClass: %s -- changeValueError,' % code
                    print stock
                    break
                # ret = self.db_factory.insertDoc(self.db, code, stock[0], stock[1],stock[icons],
                #                                 stock[3], stock[4], stock[5], stock[6])
                if not ret:
                    print 'StockDataClass: %s -- %s insert error,' % (code, stock[0])
                    insert_success_Flag = False
                    break
                # print 'StockDataClass: insert sucess %s -- %s' % (code,stock[0])
            # #--update stock_index: count,updateTime ect
            count = self.db[code].count()
            if count > 0:
                # #--update stock_index
                date_origin = self.db[code].find({},{"date":1,"_id":0}).sort("date", database_m.ASCENDING).limit(1).next()["date"]
                last = self.db[code].find({},{"date":1,"close":1,"_id":0}).sort("date", database_m.DESCENDING).limit(1).next()
                date_last = last["date"]
                price_last = last["close"]
                price_highest = self.db[code].find({},{"close":1,"_id":0}).sort("close", database_m.DESCENDING).limit(1).next()["close"]
                highest_highest = self.db[code].find({},{"high":1,"_id":0}).sort("high", database_m.DESCENDING).limit(1).next()["high"]
                if highest_highest > price_highest:
                    price_highest = highest_highest
                self.db[self.stockIndexCollectionName].update(
                    {"code":code},
                    {"$set":{"count":count, "date_origin":date_origin, "date_last":date_last,
                             "price_last":price_last, "price_highest":price_highest}}
                )
            if insert_success_Flag:
                updated_stock_list.append({"code":code, "count":count})  # #--resualt record
         # #--reset callback function
        self.callback_stockDetail = self.callback_reset
        self.db_factory.insertDoc = self.db_factory.resetRewrite

        return updated_stock_list

    def insertFreshDateStockDetail_auto(self, code):
        """
        更新股票新增内容
        需要重载callback_stockDetail(code, curExchangeName, date_last)，返回股票信息列表，
        重载了self.db_factory.insertDoc = insertStock
        所有重载函数结束后reset重载状态
        返回信息必须保证全部新于数据库中的最后日期，并且无重复、日期递增排序
        每项股票内容顺序为date, open, high, low, close, volume, adj_close
        :return insert date list, 包括部分错误信息（如果有的话）
        """
        # #--get the date of last update
        stockInfo = self.db[self.stockIndexCollectionName].find(
            {"code":code},{"date_last":1, "count":1, "_id":0}
        ).next()
        date_last = stockInfo["date_last"]
        if not date_last or date_last == "0":
            print 'StockDataClass: %s  load data_last error, you need to run init first' % code
            return None
        # #--get  the data of new stock detail
        newStockDetail_list = self.callback_stockDetail(code, self.curExchangeName, date_last)
        if newStockDetail_list is None:
            print 'StockDataClass: %s  loads data error' % code
            # #--reset callback function
            self.callback_stockDetail = self.callback_reset
            return None
        if len(newStockDetail_list) == 0:
            print 'StockDataClass: %s has not new data' % code
            # #--reset callback function
            self.callback_stockDetail = self.callback_reset
            return None

        # #--insert new data into database
        insertCount = 0
        count_last = stockInfo["count"]
        insertNewDateList = []
        insertAllSuccessFlag = True
        self.db_factory.insertDoc = insertStock

        for stock in newStockDetail_list:
            # print 'StockDataClass: stock:', stock
            try:
                ret = self.db_factory.insertDoc(self.db, code, stock[0], float(stock[1]),float(stock[2]),
                                                float(stock[3]), float(stock[4]), int(stock[5]), float(stock[6]))
            except ValueError:
                print 'StockDataClass: %s -- changeValueError,' % code
                print stock
                insertAllSuccessFlag = False
                break
            if not ret:
                print 'StockDataClass: %s -- %s insert error,' % (code, stock[0])
                insertAllSuccessFlag = False
                break
            insertCount += 1
            insertNewDateList.append(stock[0])
            # print 'StockDataClass: insert sucess %s -- %s' % (code,stock[0])

        if insertCount == 0:
            insertNewDateList.append("not all error")
            self.db_factory.insertDoc = self.db_factory.resetRewrite
            return insertNewDateList

        # #--校验插入条目数量,只提出警告，不影响
        final_db_count = self.db[code].count()
        local_finally_count = count_last + insertCount
        if final_db_count == local_finally_count:
            print 'StockDataClass: %s success insert %d' % (code, insertCount)
        else:
            print 'StockDataClass: warning:%s insertCount: %d ,count_last: %d ,final_db_count: %d,' \
                  'it should be %d' % (code, insertCount, count_last, final_db_count, local_finally_count)

        # #--update stock_index
        last = self.db[code].find({},{"date":1,"close":1,"_id":0}).sort("date", database_m.DESCENDING).limit(1).next()
        date_last = last["date"]
        price_last = last["close"]
        price_highest = self.db[code].find({},{"close":1,"_id":0}).sort("close", database_m.DESCENDING).limit(1).next()["close"]
        highest_highest = self.db[code].find({},{"high":1,"_id":0}).sort("high", database_m.DESCENDING).limit(1).next()["high"]
        if highest_highest > price_highest:
            price_highest = highest_highest
            self.db[self.stockIndexCollectionName].update(
                {"code":code},
                {"$set":{"count":final_db_count, "date_last":date_last,
                         "price_last":price_last, "price_highest":price_highest}}
            )

        # #--reset callback function
        self.callback_stockDetail = self.callback_reset
        self.db_factory.insertDoc = self.db_factory.resetRewrite

        if not insertAllSuccessFlag:
            insertNewDateList.append("not all success, process break out")
        return insertNewDateList

    def loadStockDayDataByDate(self, code, startDate=None, endDate=None):
        """
        :return:A list,stock day data between the startDate and endDate
        :param code:Stock'code
        :param startDate: if None, load from the origin
        :param endDate:if None, load to the last
        :raise: date string format error or endDate larger then startDate
        """
        if (not startDate) and (not endDate):
            stock_cursor = self.db[code].find({}, {"_id": 0})\
                .sort("date", database_m.ASCENDING)
        elif startDate and endDate:
            try:
                t = time.strptime(startDate, "%Y-%m-%d")
                originDateTime = datetime.date(t.tm_year, t.tm_mon, t.tm_mday)
                t2 = time.strptime(endDate, "%Y-%m-%d")
                endDateTime = datetime.date(t2.tm_year, t2.tm_mon, t2.tm_mday)
            except Exception, e:
                print 'StockData: the string of date is format error'
                raise e
            finally:
                if originDateTime >= endDateTime:
                    raise 'StockData: originDate >=endDate'
            stock_cursor = self.db[code].find({"date": {"$gte": startDate, "$lte": endDate}},
                                              {"_id": 0})\
                .sort("date", database_m.ASCENDING)
        elif startDate:
            try:
                t = time.strptime(startDate, "%Y-%m-%d")
            except Exception, e:
                print 'StockData: the string of date is format error'
                raise e
            stock_cursor = self.db[code].find({"date": {"$gte": startDate}}, {"_id": 0})\
                .sort("date", database_m.ASCENDING)
        elif endDate:
            try:
                t = time.strptime(endDate, "%Y-%m-%d")
            except Exception, e:
                print 'StockData: the string of date is format error'
                raise e
            stock_cursor = self.db[code].find({"date": {"$lte": endDate}}, {"_id": 0})\
                .sort("date", database_m.ASCENDING)

        stock_list = []
        for stock in stock_cursor:
            stock_list.append(stock)
        return stock_list

    def stockIndexCollectionCheckAndRepair(self):
        """
        Compare the Collections and stock Index,
        find out the wrong data in stockIndexCollection.
        And let them be right.
        """
        # logs = []
        codes = self.getAllStockCode_list()
        for code in codes:
            stockInfo = self.db[self.stockIndexCollectionName].find(
                    {"code":code},{"_id": 0}
                ).next()
            if stockInfo['count'] < 5:
                # logs.append("%s: count less, break" % code)
                print "%s: count less, break" % code
                continue

            count = self.db[code].count()
            org = self.db[code].find({},{"date":1,"close":1,"_id":0}).sort("date", database_m.ASCENDING).limit(1).next()
            date_org = org["date"]
            last = self.db[code].find({},{"date":1,"close":1,"_id":0}).sort("date", database_m.DESCENDING).limit(1).next()
            date_last = last["date"]
            price_last = last["close"]
            price_highest = self.db[code].find({},{"close":1,"_id":0}).sort("close", database_m.DESCENDING).limit(1).next()["close"]
            highest_highest = self.db[code].find({},{"high":1,"_id":0}).sort("high", database_m.DESCENDING).limit(1).next()["high"]
            if highest_highest > price_highest:
                price_highest = highest_highest

            haveError = False

            if stockInfo['date_origin'] != date_org:
                # logs.append("%s: date_origin error, index:%s, doc:%s " % code, stockInfo['date_origin'], date_org)
                haveError = True
                print "%s: date_origin error" % code
                print stockInfo['date_origin'], date_org
            elif stockInfo['date_last'] != date_last:
                # logs.append("%s: date_last error, index:%s, doc:%s " % code, stockInfo['date_last'], date_last)
                haveError = True
                print "%s: date_last error " % code
                print stockInfo['date_last'], date_last
            if stockInfo['count'] != count:
                # logs.append("%s: count error, index:%s, doc:%s " % code, stockInfo['count'], count)
                haveError = True
                print "%s: count error " % code
                print stockInfo['count'], count
            if stockInfo['price_highest'] != price_highest:
                # logs.append("%s: price_highest error, index:%s, doc:%s " % code, stockInfo['price_highest'], price_highest)
                haveError = True
                print "%s: price_highest error" % code
                print stockInfo['price_highest'], price_highest
            if stockInfo['price_last'] != price_last:
                # logs.append("%s: price_last error, index:%s, doc:%s " % code, stockInfo['price_last'], price_last)
                haveError = True
                print "%s: price_last error" % code
                print stockInfo['price_last'], price_last

            if haveError:
                print self.db[self.stockIndexCollectionName].update(
                    {"code":code},
                    {"$set":{"count":count, "date_last":date_last, "date_origin":date_org,
                             "price_last":price_last, "price_highest":price_highest}}
                )
            else:
                print "%s: no error" % code

        # for str in logs:
        #     print str


    def stock_test(self):
        # StopIteration
        # print self.db["600001"].find({},{"date":1,"_id":0}).sort("date", database_m.ASCENDING).limit(1).next()["date"]
        # print self.db["600000"].find({},{"date":1,"_id":0}).sort("date", database_m.DESCENDING).limit(1).next()["date"]
        # print self.db["600000"].find({"date":{"$gt":"2013-03-02","$lt":"2013-09"}}).next()
        isExist = self.db[__stockIndexCollection__].find({"code":"600000"}).count()
        if isExist:
            print 'cunzai'
        else:
            print 'no cun zai '
        print isExist
        pass

