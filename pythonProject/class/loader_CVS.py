# coding=utf-8
__author__ = 'kk'

__text1__ = "D:\\"
__text2__ = '600000.ss.csv'  # 平安银行


class Loader_CVS:
    def __init__(self, dir=None, filename=None, file_handle=None, content=None):
        """
        :param dir:
        :param filename: 配合load_file使用,前两个参数需配合file_close
        :param file_handle: 相当于直接传入前两个所做的工作结果
        :param content: 直接传入完整数据字符串，同时去掉最后一个\n
        """
        self.filename = filename
        self.dir = dir
        self.file_handle = file_handle
        if content:
            self.content = content.strip("\n")

    def load_file_safe(self, beginIndex=1):
        if (not self.dir) or (not self.filename):
            print 'Loader_CVS: not dir or filename'
            return False
        if beginIndex < 1:
            print 'Loader_CVS: beginIndex false'
            return False
        if self.file_handle:
            self.file_handle.close()

        try:
            self.file_handle = open(self.dir + self.filename, "r")
        except Exception, e:
            self.file_handle = None
            print 'Loader_CVS: load file error %s' % e
            return False
        else:
            for i in range(0, beginIndex - 1):
                self.file_handle.readline()
            return True

    def loader_file_close(self):
        if not self.file_handle:
            print "Loader_CVS: error,not filehandle"
            return
        print "Loader_CVS: ",self.dir + self.filename + " : Close"
        self.file_handle.close()
        self.file_handle = None

    def parse_file_list_left_all(self):
        if not self.file_handle:
            print "Loader_CVS: error,not filehandle"
            return None
        list = []
        for line in self.file_handle:
            if line:
                items = line.split("\n")[0].split(",")
                list.append(items)
                print items
        return list

    def parse_file_list_all(self):
        if not self.file_handle:
            print "Loader_CVS: error,not filehandle"
            return None
        list = []
        self.file_handle.seek(0)
        for line in self.file_handle:
            if line:
                items = line.split("\n")[0].split(",")
                list.append(items)
        return list

    def _parse_file_list_lineItem(self):
        item = self.file_handle.readline()
        if not item:
            print "Loader_CVS: error,not more line"
            return None
        list = item.split(",")
        return list

    def parse_file_next(self):
        if not self.file_handle:
            print "Loader_CVS: error,not file"
            return None
        return self._parse_file_list_lineItem()

    def parse_file_reset(self):
        """
        重置文件流位置
        """
        if not self.file_handle:
            print "Loader_CVS: error,not file"
            return
        self.file_handle.seek(0)

    def parse_content(self, beginIndex=1, isRemoveTitle=False, reverseFlag=False):
        """
        从字符串中解析数据
        :param beginIndex: 从第几个开始，下标最小为1
        :param reverseFlag: 数据是否逆序
        :return:
        """
        # self.content = self.file_handle.read().strip("\n")
        if not self.content:
            print "Loader_CVS: error,not content"
            return None
        if 1 > beginIndex:
            print "Loader_CVS: error,beginIndex false"
            return None
        lists = []
        splitLine = self.content.split("\n")
        splitLineCount = len(splitLine)
        if splitLineCount == 0:
            print "Loader_CVS: error,splitLine false"
            return None

        if isRemoveTitle:
            splitLine.pop(0)
        if reverseFlag:
            splitLine.reverse()
        for row in range(beginIndex - 1, splitLineCount - 1):
            items = []
            for item in splitLine[row].split(","):
                items.append(item)
            lists.append(items)
        return lists

    def parse_contentEX_stock(self, isRemoveTitle, beginDate, endDate=None, reverseFlag=False):
        """
        从字符串中根据日期区间读取数据

        初始数据默认为时间倒序，如果endDate为空或未找到，查找beginDate至最新数据
        本函数不对日期格式及前后有效性进行审查
        :return: 返回结果列表，以时间逆续形式
        """
        # self.content = self.file_handle.read().strip("\n")
        if not self.content:
            print "Loader_CVS: error,not content"
            return None
        if not beginDate:
            print "Loader_CVS: error,beginDate false"
            return None

        lists = []
        splitLine = self.content.split("\n")
        if isRemoveTitle:
            print "Loader_CVS: remove: ", splitLine.pop(0)

        splitLineCount = len(splitLine)
        beginIndex = splitLineCount
        endIndex = 0
        if endDate:
            for index in range(0,splitLineCount):
                line = splitLine[index]
                if line.split(",")[0] == endDate:
                    endIndex = index
                    break

        if beginDate:
            for index in range(0,splitLineCount):
                line = splitLine[index]
                if line.split(",")[0] == beginDate:
                    beginIndex = index
                    break
            if beginIndex == splitLineCount:
                print "Loader_CVS: beginDate data nofound"
                return None
        print "Loader_CVS: beginIndex", endIndex, beginIndex
        for row in range(endIndex, beginIndex + 1):
            items = []
            for item in splitLine[row].split(","):
                items.append(item)
            lists.append(items)
        if reverseFlag:
            lists.reverse()
        return lists


if __name__ == '__main__':
    loader = Loader_CVS(__text1__, __text2__)
    loader.load_file_safe()
    # # loader.parse_file_next()
    # # loader.parse_file_next()
    # # loader.parse_file_reset()
    # # loader.parse_file_next()
    #
    import pprint
    # # pprint.pprint(loader.parse_file_list_all())
    pprint.pprint(loader.parse_content(1,True))
    # pprint.pprint(loader.parse_contentEX_stock(True, "1999-11-10"))
    #
    # loader.loader_file_close()