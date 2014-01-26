# coding=utf-8
__author__ = 'kk'

__test__ = 'function get_alldata(){ \n\
var _t = new Array();\n \
_t.push({val:"600000",val2:"浦发银行",val3:"pfyx"});\n \
_t.push({val:"600004",val2:"白云机场",val3:"byjc"});\n \
_t.push({val:"600005",val2:"武钢股份",val3:"wggf"});\n \
t.push({val:"204028",val2:"GC028",val3:"GC028"});\n \
_t.push({val:"204091",val2:"GC091",val3:"GC091"});\n \
_t.push({val:"204182",val2:"GC182",val3:"GC182"});'

__test2__ = "<tr  class='cls-data-tr' bgcolor='#EEF3F7'><td  class='cls-data-td' style='mso-number-format:\@' align='center' >000011</td><td  class='cls-data-td'  align='center' >深物业A</td><td  class='cls-data-td'  align='left' >深圳市物业发展(集团)股份有限公司</td><td  class='cls-data-td'  align='center' >SHENZHEN PROPERTIES & RESOURCES DEVELOPMENT (GROUP)CO., LTD</td><td  class='cls-data-td'  align='center' >广东省深圳市人民南路国贸大厦39、42层</td><td  class='cls-data-td'  align='center' >000011</td><td  class='cls-data-td'  align='center' >深物业A</td><td  class='cls-data-td'  align='center' >1992-03-30</td><td  class='cls-data-td'  align='center' >528,373,849</td><td  class='cls-data-td'  align='center' >175,831,365</td><td  class='cls-data-td'  align='center' >200011</td><td  class='cls-data-td'  align='center' >深物业B</td><td  class='cls-data-td'  align='center' >1992-03-30</td><td  class='cls-data-td'  align='center' >67,605,243</td><td  class='cls-data-td'  align='center' >67,605,243</td><td  class='cls-data-td'  align='center' >华南</td><td  class='cls-data-td'  align='center' >广东</td><td  class='cls-data-td'  align='center' >深圳市</td><td  class='cls-data-td'  align='left' >K 房地产</td>\n \<td  class='cls-data-td'  align='center' >www.szwuye.com.cn</td></tr>"

import re
import sys


def stock_code_SH_perser(content=__test__, isOnlyStock=True):
    """
    :param content: 'function get_alldata(){
                        var _t = new Array();
                        _t.push({val:"600000",val2:"浦发银行",val3:"pfyx"});
                        _t.push({val:"600004",val2:"白云机场",val3:"byjc"});
                        _t.push({val:"600005",val2:"武钢股份",val3:"wggf"});'
    :return: a list which content dic like this: [{"code":xx, "name":xx, "abbreviation":xx},]
    """
    try:
        iteration = re.findall(r'{\bval\b.*\bval2\b.*\bval3\b.*\b"}', content)
    except Exception, e:
        print 'perser : find all error,check the Format of content', e
        return None

    list = []
    for item in iteration:
        item = re.sub('val:', '"code":', item)
        item = re.sub('val2:', '"name":', item)
        item = eval(re.sub('val3:', '"abbreviation":', item))
        if isOnlyStock:
            if (int(item['code']) >= 600000) and (int(item['code']) < 900000):
                #item['name'] = item['name'].decode(sys.stdin.encoding).encode('utf8')
                list.append(item)
        else:
            list.append(item)
    return list


def stock_code_SZ_perser(content=__test2__, isOnlyStock=True, list_tmp=None):
    """
    :param content format:公司代码
                        公司简称
                        公司全称
                        英文名称
                        注册地址
                        A股代码
                        A股简称
                        A股上市日期
                        A股总股本
                        A股流通股本
                        B股代码
                        B股 简 称
                        B股上市日期
                        B股总股本<
                        B股流通股本
                        地区
                        省份
                        城市
                        所属行业
                        公司网址
    :param content example:<tr  class='cls-data-tr' bgcolor='#FFFFFF'><td  class='cls-data-td' style='mso-number-format:\@' align='center' >000001</td>
                        <td  class='cls-data-td'  align='center' >平安银行</td>
                        <td  class='cls-data-td'  align='left' >平安银行股份有限公司</td>
                        <td  class='cls-data-td'  align='center' >Ping An BANK CO.,LTD</td>
                        <td  class='cls-data-td'  align='center' >广东省深圳市罗湖区深南东路5047号</td>
                        <td  class='cls-data-td'  align='center' >000001</td>
                        <td  class='cls-data-td'  align='center' >平安银行</td>
                        <td  class='cls-data-td'  align='center' >1991-04-03</td>
                        <td  class='cls-data-td'  align='center' >9,520,745,656</td>
                        <td  class='cls-data-td'  align='center' >5,571,282,976</td>
                        <td  class='cls-data-td'  align='center' ></td>
                        <td  class='cls-data-td'  align='center' ></td>
                        <td  class='cls-data-td'  align='center' ></td>
                        <td  class='cls-data-td'  align='center' >0</td>
                        <td  class='cls-data-td'  align='center' >0</td>
                        <td  class='cls-data-td'  align='center' >华南</td>
                        <td  class='cls-data-td'  align='center' >广东</td>
                        <td  class='cls-data-td'  align='center' >深圳市</td>
                        <td  class='cls-data-td'  align='left' >J 金融业</td>
                        <td  class='cls-data-td'  align='center' >www.sdb.com.cn</td>
    :return: a list which content dic like this: [{"code":xx, "name":xx, "abbreviation":xx},]
    """
    try:
        iteration = re.findall(r'<td[^>]*?>.*?</td>', content)
    except Exception, e:
        print 'stock_code_SZ_perser : find all error,check the Format of content', e
        return None

    list = []
    list_tmp = []
    count = 0
    for item in iteration:
        # print item
        count += 1
        if count <= 20:
            continue

        try:
            p = re.compile('<[^>]+>')
            print item
            list_tmp.append(p.sub("", item).replace("\"", "\'"))
            if count % 20 == 0:
                print list_tmp
                stockInfo_str = '{"companyCode":"%s", "companyShortName":"%s", "companyFullName":"%s", "engName":"%s", "regAddr":"%s", \
                "ACode":"%s", "AName":"%s", "AOrgDate":"%s", "AStockCount":"%s", "ACirculate":"%s", \
                "BCode":"%s", "BName":"%s", "BOrgDate":"%s", "BStockCount":"%s", "BCirculate":"%s", \
                "area":"%s", "province":"%s", "city":"%s", "businessClassify":"%s", "HP":"%s"}' \
                                %\
                                (list_tmp[0], list_tmp[1], list_tmp[2], list_tmp[3], list_tmp[4],
                                 list_tmp[5], list_tmp[6], list_tmp[7], list_tmp[8], list_tmp[9],
                                 list_tmp[10], list_tmp[11], list_tmp[12], list_tmp[13], list_tmp[14],
                                 list_tmp[15], list_tmp[16], list_tmp[17], list_tmp[18], list_tmp[19]
                                )
                count = 0
                # print stockInfo_str
                list.append(eval(stockInfo_str))
                list_tmp = []
        except Exception, e:
            print 'perser : find </td> error,check the Format of content:', e
            return None

    return list

            #     item = re.sub('val:', '"code":', item)
            #     item = re.sub('val2:', '"name":', item)
            #     item = eval(re.sub('val3:', '"abbreviation":', item))
            #     if isOnlyStock:
            #         if int(item['code']) >= 600000:
            #             #item['name'] = item['name'].decode(sys.stdin.encoding).encode('utf8')
            #             list.append(item)
            #     else:
            #         list.append(item)
            # return list


if __name__ == '__main__':
    # print stock_code_SH_perser()
    f = open('/Users/kk/Downloads/xxxxx2.xls', "rb") # 以二进制读取
    storedlist2 = f.read().decode('GB2312', 'ignore').encode('utf-8')
    # print(storedlist2)
    for item in stock_code_SZ_perser(storedlist2):
        print item['companyCode']
        print item['companyShortName']
        print item['companyFullName']
        print item['engName']
        print item['ACode']
        print item['AName']
        print item['BName']
        print item['province']
        print item['HP']
        print item['businessClassify']
        print item['AStockCount']
        print item['ACirculate']
        print item['BStockCount']
        print item['BCirculate']
    f.close()
