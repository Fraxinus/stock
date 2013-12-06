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

import re


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
            if int(item['code']) >= 600000:
                list.append(item)
        else:
            list.append(item)
    return list


if __name__ == '__main__':
    print stock_code_SH_perser()
