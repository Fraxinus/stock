# coding=utf-8
__author__ = 'kk'

__timeout__ = 30
__history_cvs_addr__ = 'table.finance.yahoo.com'
__history_cvs_port__ = 80
__history_SH_exchange_extentName__ = 'ss'
__history_SZ_exchange_extentName__ = 'sz'
__proxy_addr__ = '127.0.0.1'
__proxy_port__ = 1080
__proxy_mode__ = False

import sys
import httplib
from HTMLParser import HTMLParser
import time
import chardet
import re
import httplib2
import socks
##
history_extentName_SH = __history_SH_exchange_extentName__
history_extentName_SZ = __history_SZ_exchange_extentName__

# 公司代码	公司简称	公司全称	英文名称	注册地址	A股代码	A股简称	A股上市日期	A股总股本	A股流通股本
# B股代码	B股 简 称	B股上市日期	B股总股本	B股流通股本	地 区	省 份	城 市	所属行业	公司网址

def getAllCode_SZ():
    httpClient = None
    response_status = None
    response_content = None
    try:
        # http://www.szse.cn/szseWeb/FrontController.szse?ACTIONID=8&CATALOGID=1110&TABKEY=tab2&ENCODE=1
        # httpClient = httplib.HTTPConnection('www.szse.cn', 80, timeout=30)
        # httpClient.request('GET', '/szseWeb/FrontController.szse?ACTIONID=8&CATALOGID=1110&TABKEY=tab2&ENCODE=1')
        #response是HTTPResponse对象
        response = httpClient.getresponse()
        response_status = response.status
        print 'StockNetwork: response.status = %s' % response_status
        print 'StockNetwork: response.reason = %s' % response.reason
        response_content = response.read()

        detect_dict = chardet.detect(response_content)
        print detect_dict
        confidence, encoding = detect_dict['confidence'], detect_dict['encoding']
        if 0.9 > confidence or encoding == None:
            print u"无法准确识别编码"
        # if encoding == 'GB2312':
        response_content = response_content.decode(encoding, 'ignore').encode('utf-8')

    except Exception, e:
        print 'StockNetwork: error', e
    finally:
        print("StockNetwork: response finish")

    if httpClient:
        httpClient.close()

    if response_status != 200:
        return None
    else:
        return response_content


def getAllCode_SH():
    """
    :param
   :return: a list which content dic like this: [{'abbreviation': 'pfyx', 'code': '600000', 'name': '\xe6\xb5\xa6\xe5\x8f\x91\xe9\x93\xb6\xe8\xa1\x8c'},]
   """
    httpClient = None
    response_status = None
    response_content = None
    try:
        httpClient = httplib.HTTPConnection('www.sse.com.cn', 80, timeout=30)
        httpClient.request('GET', '/js/common/ssesuggestdataAll.js')
        ##response是HTTPResponse对象
        response = httpClient.getresponse()
        response_status = response.status
        print 'StockNetwork: response.status = %s' % response_status
        print 'StockNetwork: response.reason = %s' % response.reason
        response_content = response.read()
        print 'StockNetwork: response.content = %s' % response_content
    except Exception, e:
        print 'StockNetwork: error', e
    finally:
        print("StockNetwork: response finish")

    if httpClient:
        httpClient.close()

    if response_status != 200:
        return None
    else:
        return response_content


def _httpBase_Get(addr, port, timeout, extendStr):
    httpClient = None
    response_status = None
    response_content = None
    try:
        httpClient = httplib.HTTPConnection(addr, port, timeout=timeout)
        print 'StockNetwork: request %s%s' % (addr, extendStr)
        httpClient.request('GET', extendStr)

        #response是HTTPResponse对象
        response = httpClient.getresponse()
        response_status = response.status
        print 'StockNetwork: response.status = %s' % response_status
        print 'StockNetwork: response.reason = %s' % response.reason
        response_content = response.read()
        print 'StockNetwork: response.content = %s' % response_content
    except Exception, e:
        print 'StockNetwork: error', e
    finally:
        print("StockNetwork: response finish")
        if httpClient:
            httpClient.close()

    if response_status != 200:
        return None
    else:
        return response_content


def _httpBase_Get_Proxy(url):
    httpClient = None
    response_response = None
    response_content = None
    try:
        httpClient = httplib2.Http(proxy_info=httplib2.ProxyInfo(socks.PROXY_TYPE_SOCKS5, __proxy_addr__, __proxy_port__))
        print 'StockNetwork: request %s' % url
        response_response, response_content = httpClient.request(url)

        print 'StockNetwork: response_response = %s' % response_response
        print 'StockNetwork: response_content = %s' % response_content
    except Exception, e:
        print 'StockNetwork: error', e
    finally:
        print("StockNetwork: response finish")
        if httpClient:
            httpClient = None

    if response_response['status'] != '200':
        print 'StockNetwork:not 200'
        return None
    else:
        return response_content


def getAllHistory(code, history_extentName):
    requestStr = '/table.csv?s=%s.%s' % (code, history_extentName)
    if __proxy_mode__:
        return _httpBase_Get_Proxy('http://' + __history_cvs_addr__ + requestStr)
    else:
        return _httpBase_Get(__history_cvs_addr__, __history_cvs_port__, __timeout__, requestStr)



def getHistoryByStartDate(code, history_extentName, start_date):
    struct_time = time.strptime(start_date, '%Y-%m-%d')
    requestStr = 'http://table.finance.yahoo.com/table.csv?s=%s.%s&b=%d&a=%d&c=%s&g=d' % \
                 (code, history_extentName,
                  int(struct_time.tm_mday), int(struct_time.tm_mon) - 1, struct_time.tm_year)
    if __proxy_mode__:
        return _httpBase_Get_Proxy(requestStr)
    else:
        return _httpBase_Get(__history_cvs_addr__, __history_cvs_port__, __timeout__, requestStr)


if __name__ == '__main__':
     print "resualt:", getAllCode_SH()
    # for item in getAllCode_SZ():
    #     print item['companyCode']
    #     print item['companyShortName']
    #     print item['companyFullName']
    #     print item['engName']
    #     print item['ACode']
    #     print item['AName']
    #     print item['BName']
    #     print item['province']
    #     print item['HP']
    #     print item['businessClassify']
    #     print item['AStockCount']
    #     print item['ACirculate']
    # print "resualt:",getAllHistory('600003', history_extentName_SH)
    # print "resualt:",getHistoryByStartDate('600000', history_extentName__SH, "2013-1-1")