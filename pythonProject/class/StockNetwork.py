# coding=utf-8
__author__ = 'kk'

__timeout__ = 30
__history_cvs_addr__ = 'table.finance.yahoo.com'
__history_cvs_port__ = 80
__history_SH_exchange_extentName__ = 'ss'
__history_SZ_exchange_extentName__ = 'sz'

import httplib
from HTMLParser import HTMLParser
import time
import data_parser
import chardet
import re
##
history_extentName_SH = __history_SH_exchange_extentName__
history_extentName_SZ = __history_SZ_exchange_extentName__

# 公司代码	公司简称	公司全称	英文名称	注册地址	A股代码	A股简称	A股上市日期	A股总股本	A股流通股本
# B股代码	B股 简 称	B股上市日期	B股总股本	B股流通股本	地 区	省 份	城 市	所属行业	公司网址

class MyParser(HTMLParser):
    """一个简单的HTMLparser的例子"""

    def handle_decl(self, decl):
        """处理头文档"""
        # HTMLParser.handle_decl(self, decl)
        print"处理头文档",  decl

    def handle_starttag(self, tag, attrs):
        """处理起始标签"""
        # HTMLParser.handle_starttag(self, tag, attrs)
        # if not HTMLParser.get_starttag_text(self).endswith("/>"):
        print "处理起始标签", "<",tag,">", attrs

    def handle_data(self, data):
        """处理文本元素"""
        # HTMLParser.handle_data(self, data)
        print "处理文本元素", data.decode('gbk').encode('utf8'),

    def handle_endtag(self, tag):
        """处理结束标签"""
        # HTMLParser.handle_endtag(self, tag)
        # if not HTMLParser.get_starttag_text(self).endswith("/>"):
        print "处理结束标签", "</",tag,">"

    def handle_startendtag(self, tag, attrs):
        """处理自闭标签"""
        # HTMLParser.handle_startendtag(self, tag, attrs)
        print "处理自闭标签", HTMLParser.get_starttag_text(self)

    def handle_comment(self, data):
        """处理注释"""
        # HTMLParser.handle_comment(self, data)
        print "处理注释", data

    def close(self):
        HTMLParser.close(self)
        print "parser over"

def test():
    httpClient = None
    response_status = None
    response_content = None
    try:
        # http://www.szse.cn/szseWeb/FrontController.szse?ACTIONID=8&CATALOGID=1110&TABKEY=tab2&ENCODE=1
        httpClient = httplib.HTTPConnection('www.szse.cn', 80, timeout=30)
        httpClient.request('GET', '/szseWeb/FrontController.szse?ACTIONID=8&CATALOGID=1110&TABKEY=tab2&ENCODE=1')
        #response是HTTPResponse对象
        response = httpClient.getresponse()
        response_status = response.status
        print 'StockNetwork: response.status = %s' % response_status
        print 'StockNetwork: response.reason = %s' % response.reason
        response_content = response.read()

        # detect_dict = chardet.detect(response_content)
        # print detect_dict
        # confidence, encoding = detect_dict['confidence'], detect_dict['encoding']
        # if 0.9 > confidence or encoding == None:
        #     print u"无法准确识别编码"
        # if encoding == 'GB2312':
        response_content = response_content.decode('gbk').encode('utf8')

        # hp = MyParser()
        # hp.feed(response_content)
        # hp.close()
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

def getAllCode_SH():
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

    content_persered = data_parser.stock_code_SH_perser(response_content, isOnlyStock=True)
    print 'StockNetwork: stock_code_SH_perser = ' , content_persered

    if httpClient:
        httpClient.close()

    if response_status != 200:
        return None
    else:
        return content_persered


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


def getAllHistory(code, history_extentName):
    requestStr = '/table.csv?s=%s.%s' % (code, history_extentName)
    return _httpBase_Get(__history_cvs_addr__, __history_cvs_port__, __timeout__, requestStr)


def getHistoryByStartDate(code, history_extentName, start_date):
    struct_time = time.strptime(start_date, '%Y-%m-%d')
    requestStr = 'http://table.finance.yahoo.com/table.csv?s=%s.%s&b=%d&a=%d&c=%s&g=d' % \
                 (code, history_extentName,
                  int(struct_time.tm_mday), int(struct_time.tm_mon) - 1, struct_time.tm_year)
    return _httpBase_Get(__history_cvs_addr__, __history_cvs_port__, __timeout__, requestStr)

if __name__ == '__main__':
    test()
    # print "resualt:",getAllHistory('600003', history_extentName_SH)
    # print "resualt:",getHistoryByStartDate('600000', history_extentName__SH, "2013-1-1")