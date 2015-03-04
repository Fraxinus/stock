# coding=utf-8
__author__ = 'kk'

import StockData
import StockNetwork
import loader_CVS
import data_parser


def callback_stockDetail_newFromCode_list(code, exchangeName):
    """
    按代码更新的回调
    stockData.callback_stockDetail的rewrite需求
    """
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
    """
    按数据库最后时间更新code的内容的回调
    stockData.callback_stockDetail的rewrite需求
    """
    content = None
    if exchangeName == StockData.ShangHaiStockDB:
        content = StockNetwork.getHistoryByStartDate(code, StockNetwork.history_extentName_SH, date_last)

    if exchangeName == StockData.ShenZhenStockDB:
        content = StockNetwork.getHistoryByStartDate(code, StockNetwork.history_extentName_SZ, date_last)

    if not content:
        return None

    loader = loader_CVS.Loader_CVS(content=content)
    # ret = loader.load_file_safe()
    # if not ret:
    #     return None
    parse_list = loader.parse_content(2, True, True)
    # loader.loader_file_close()
    return parse_list


def callback_stockIndex_list(exchangeName):
    """
    更新index表的回调
    StockData.callback_stockDetail的rewrite需求
    """
    content = None
    content_persered = None
    if exchangeName == StockData.ShangHaiStockDB:
        content = StockNetwork.getAllCode_SH()
        content_persered = data_parser.stock_code_SH_perser(content, isOnlyStock=True)

    if exchangeName == StockData.ShenZhenStockDB:
        content = StockNetwork.getAllCode_SZ()
        content_persered = data_parser.stock_code_SZ_perser(content, isOnlyStock=False)

    if not content or not content_persered:
        print 'callback_stockIndex_list:not content or not content_persered'
        return None
    print 'callback_stockIndex_list:return content_persered'
    return content_persered



stockData = StockData.StockDataClass(StockData.ShangHaiStockDB)
# stockData.changeStockExchange(StockData.ShenZhenStockDB)
# print "collection_names:", stockData.db.collection_names()

# print 'stockIndexUpdate'
# stockData.callback_stockDetail = callback_stockIndex_list
# print "resualt:", stockData.stockIndexUpdate()

# print "getAllStockCollectionsName_list:", stockData.getAllStockCollectionsName_list()
# print "getAllStockCode_list:", stockData.getAllStockCode_list()

# print "initNewStockDetail:"
# stockData.callback_stockDetail = callback_stockDetail_newFromCode_list
# print "resualt:", stockData.initNewStockDetail()

# stockData.stock_test()

# print 'insertNewDateStockDetail'
# code_list = stockData.getAllStockCollectionsName_list()
# print code_list
# for code in code_list:
#     stockData.callback_stockDetail = callback_stockDetail_newFromCodeAndLastDate_list
#     print "results:", stockData.insertFreshDateStockDetail_auto(code)


# print 'insertNewDateStockDetail'
# stockData.callback_stockDetail = callback_stockDetail_newFromCodeAndLastDate_list
# print "resualt:", stockData.insertFreshDateStockDetail_auto("600000")

print stockData.stockIndexInsertOne('000002','Ａ股指数')
print stockData.stockIndexInsertOne('000003','Ｂ股指数')
print stockData.stockIndexInsertOne('000004','工业指数')
print stockData.stockIndexInsertOne('000005','商业指数')
print stockData.stockIndexInsertOne('000006','地产指数')
print stockData.stockIndexInsertOne('000007','公用指数')
print stockData.stockIndexInsertOne('000008','综合指数')
print stockData.stockIndexInsertOne('000010','上证180')
print stockData.stockIndexInsertOne('000011','基金指数')
print stockData.stockIndexInsertOne('000012','国债指数')
print stockData.stockIndexInsertOne('000013','企债指数')
print stockData.stockIndexInsertOne('000015','红利指数')
print stockData.stockIndexInsertOne('000016','上证50')
print stockData.stockIndexInsertOne('000017','新综指')
print stockData.stockIndexInsertOne('000018','180金融')
print stockData.stockIndexInsertOne('000019','治理指数')
print stockData.stockIndexInsertOne('000020','中型综指')
print stockData.stockIndexInsertOne('000021','180治理')
print stockData.stockIndexInsertOne('000022','沪公司债')
print stockData.stockIndexInsertOne('000023','沪分离债')
print stockData.stockIndexInsertOne('000025','180基建')
print stockData.stockIndexInsertOne('000026','180资源')
print stockData.stockIndexInsertOne('000027','180运输')
print stockData.stockIndexInsertOne('000028','180成长')
print stockData.stockIndexInsertOne('000029','180价值')
print stockData.stockIndexInsertOne('000030','180R成长')
print stockData.stockIndexInsertOne('000031','180R价值')
print stockData.stockIndexInsertOne('000032','上证能源')
print stockData.stockIndexInsertOne('000033','上证材料')
print stockData.stockIndexInsertOne('000034','上证工业')
print stockData.stockIndexInsertOne('000035','上证可选')
print stockData.stockIndexInsertOne('000036','上证消费')
print stockData.stockIndexInsertOne('000037','上证医药')
print stockData.stockIndexInsertOne('000038','上证金融')
print stockData.stockIndexInsertOne('000039','上证信息')
print stockData.stockIndexInsertOne('000040','上证电信')
print stockData.stockIndexInsertOne('000041','上证公用')
print stockData.stockIndexInsertOne('000042','上证央企')
print stockData.stockIndexInsertOne('000043','超大盘')
print stockData.stockIndexInsertOne('000044','上证中盘')
print stockData.stockIndexInsertOne('000045','上证小盘')
print stockData.stockIndexInsertOne('000046','上证中小')
print stockData.stockIndexInsertOne('000047','上证全指')
print stockData.stockIndexInsertOne('000048','责任指数')
print stockData.stockIndexInsertOne('000049','上证民企')
print stockData.stockIndexInsertOne('000054','上证海外')
print stockData.stockIndexInsertOne('000055','上证地企')
print stockData.stockIndexInsertOne('000056','上证国企')
print stockData.stockIndexInsertOne('000057','全指成长')
print stockData.stockIndexInsertOne('000058','全指价值')
print stockData.stockIndexInsertOne('000059','全R成长')
print stockData.stockIndexInsertOne('000060','全R价值')
print stockData.stockIndexInsertOne('000061','沪企债30')
print stockData.stockIndexInsertOne('000062','上证沪企')
print stockData.stockIndexInsertOne('000063','上证周期')
print stockData.stockIndexInsertOne('000064','非周期')
print stockData.stockIndexInsertOne('000065','上证龙头')
print stockData.stockIndexInsertOne('000066','上证商品')
print stockData.stockIndexInsertOne('000067','上证新兴')
print stockData.stockIndexInsertOne('000068','上证资源')
print stockData.stockIndexInsertOne('000069','消费80')
print stockData.stockIndexInsertOne('000070','能源等权')
print stockData.stockIndexInsertOne('000071','材料等权')
print stockData.stockIndexInsertOne('000072','工业等权')
print stockData.stockIndexInsertOne('000073','可选等权')
print stockData.stockIndexInsertOne('000074','消费等权')
print stockData.stockIndexInsertOne('000075','医药等权')
print stockData.stockIndexInsertOne('000076','金融等权')
print stockData.stockIndexInsertOne('000077','信息等权')
print stockData.stockIndexInsertOne('000078','电信等权')
print stockData.stockIndexInsertOne('000079','公用等权')
print stockData.stockIndexInsertOne('000300','沪深300')
print stockData.stockIndexInsertOne('000901','小康指数')
print stockData.stockIndexInsertOne('000902','中证流通')
print stockData.stockIndexInsertOne('000903','中证100')
print stockData.stockIndexInsertOne('000904','中证200')
print stockData.stockIndexInsertOne('000905','中证500')
print stockData.stockIndexInsertOne('000906','中证800')
print stockData.stockIndexInsertOne('000907','中证700')
print stockData.stockIndexInsertOne('000908','300能源')
print stockData.stockIndexInsertOne('000909','300材料')
print stockData.stockIndexInsertOne('000910','300工业')
print stockData.stockIndexInsertOne('000911','300可选')
print stockData.stockIndexInsertOne('000912','300消费')
print stockData.stockIndexInsertOne('000913','300医药')
print stockData.stockIndexInsertOne('000914','300金融')
print stockData.stockIndexInsertOne('000915','300信息')
print stockData.stockIndexInsertOne('000916','300电信')
print stockData.stockIndexInsertOne('000917','300公用')
print stockData.stockIndexInsertOne('000918','300成长')
print stockData.stockIndexInsertOne('000919','300价值')
print stockData.stockIndexInsertOne('000920','300R成长')
print stockData.stockIndexInsertOne('000921','300R价值')
print stockData.stockIndexInsertOne('000922','中证红利')
print stockData.stockIndexInsertOne('000925','基本面50')
print stockData.stockIndexInsertOne('000957','300运输')
print stockData.stockIndexInsertOne('000958','创业成长')
print stockData.stockIndexInsertOne('000960','中证龙头')
print stockData.stockIndexInsertOne('000961','中证上游')
print stockData.stockIndexInsertOne('000968','300周期')
print stockData.stockIndexInsertOne('000969','300非周')
print stockData.stockIndexInsertOne('888880','新标准券')

#
if stockData:
    print stockData
    stockData = None

