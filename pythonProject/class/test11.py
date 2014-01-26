# coding=utf-8
__author__ = 'kk'

import os

print(os.path.split(os.getcwd()))
__fileName__ = os.getcwd()

import sys

#--------------misaka def start--------------
class Misaka:
    def __init__(self, name):
        self.name = name

    def say(self, word):
        print self.name + ":" + word

    def attack(self):
        print self.name + " make an attack"


class Misaka_Imoto(Misaka):
    def __init__(self, name, _id):
        self.name = "%s_%s" % (name, str(_id))

        #def __del__(self):
        #print "%s : yaaaaaaaa" % (self.name)

    def __getitem__(self, item):
        print "%s 持ちないわ" % (item)

    def __len__(self):
        print "嫌だ嫌だ-----見ないで"
        #raise RuntimeError("si si si")
        return sys.getsizeof(self)

    def attack(self):
        print "tututututututu \n \n"

#--------------misaka def end--------------

army = []

for i in range(0, 20001, 1):
    misakaImoto = Misaka_Imoto('misakaIMM', i)
    army.append(misakaImoto)

del army[10000:]
army.reverse()
misakaImoto = army.pop()
misakaImoto.say("xxxx")
misakaImoto["莖"]
print str(len(misakaImoto)) + "kg"

#----------lambda------------------
copyItem = lambda strx: strx * 2
print copyItem("copyed ")

#----------exec----eval--------------
exec "print 'hello'"
print eval("'he'+'llo'")
assert eval("misakaImoto") == misakaImoto  #no would stop
# print misakaImoto
# assert eval(repr(misakaImoto)) == misakaImoto  #no would stop

#---------try-------------------
try:
    print "gogogo"
except:
    print "error"
else:
    print "safe end"
finally:
    print "finish"

    #---------yield-------------------
    def addlist(alist):
        for i in alist:
            yield i + 1

listXX = [0, 1, 2, 3, 4]
# listXX = addlist(list)

for x in addlist(listXX):
    print x


def yieldTest():
    print 'Wen Chuan'
    m = yield 5
    print m
    yield 6


c = yieldTest()
print c.next()
# c.next()
print c.send(777)
print "----------------"


def fab(_max):
    n, a, b = 0, 0, 1
    while n < _max:
        yield b
        # print b 
        a, b = b, a + b
        n += 1


for i in fab(100):
    print i

#-----------search-----------replace------sub----subn----
import re

s = '100 NORTH MAIN ROAD'
# 将字符串结尾的单词“ROAD”替换成“RD.”；该 re.sub() 函数执行基于正则表达式的字符串替换。
print(re.sub(r'\bROAD$', 'RD.', s)) # 打印： 100 NORTH MAIN RD.
## subn() 与 sub() 作用一样，但返回的是包含新字符串和替换执行次数的两元组。
print(re.subn(r'\bROAD$', 'RD.', s)) # 打印： ('100 NORTH MAIN RD.', 1)
r = re.search(r'\bR(OA)(D)\b', s)
print r.groups()  # 返回一个包含字符串的元组,可用下标取元组的内容，打印： ('OA', 'D')
print r.group()  # 返回正则表达式匹配的字符串，打印： ROAD
print r.group(2)  # 返回捕获组对应的内容(用数字指明第几个捕获组)，打印： D
print r.start()  # 返回匹配字符串开始的索引, 打印： 15
print r.end()    # 返回匹配字符串结束的索引，打印： 19
print r.span()  # 返回一个元组包含匹配字符串 (开始,结束) 的索引，打印： (15, 19)

# 匹配多个内容, findall() 返回一个匹配字符串行表
p = re.compile('\d+')
s0 = '12 drummers drumming, 11 pipers piping, 10 lords a-leaping'
print(p.findall(s0))  # 打印： [12, 11, 10]
print(re.findall(r'\d+', s0)) # 也可这样写，打印： [12, 11, 10]

# 匹配多个内容, finditer() 以迭代器返回
iterator = p.finditer(s0)
# iterator = re.finditer(r'\d+', s0) # 上句也可以这样写
for match in iterator:
    print(match.group()) # 三次分别打印：12、 11、 10

# 记忆组
print(re.sub('([^aeiou])y$', 'ies', 'vacancy'))    # 将匹配的最后两个字母替换掉，打印： vacanies
print(re.sub('([^aeiou])y$', r'\1ies', 'vacancy')) # 将匹配的最后一个字母替换掉，记忆住前一个(小括号那部分)，打印： vacancies
print(re.search('([^aeiou])y$', 'vacancy').group(1))  # 使用 group() 函数获取对应的记忆组内容，打印： c

# 记忆组(匹配重复字符串)
p = re.compile(r'(?P<word>\b\w+)\s+\1') # 注意, re.match() 函数不能这样用，会返回 None
p = p.search('Paris in the the spring')
# p = re.search(r'(?P<word>\b\w+)\s+\1', 'Paris in the the spring') # 这一句可以替换上面两句
print(p.group())  # 返回正则表达式匹配的所有内容，打印： the the
print(p.groups())  # 返回一个包含字符串的元组，打印： ('the',)

# 捕获组
r = re.search(r'\bR(OA)(D)\b', s) # 如过能匹配到，返回一个 SRE_Match 类(正则表达式匹配对象)；匹配不到则返回“None”
# `MatchObject` 实例的几个方法
if r: # 如果匹配不到，则 r 为 None,直接执行下面语句则会报错；这里先判断一下，避免这错误
    print(r.groups()) # 返回一个包含字符串的元组,可用下标取元组的内容，打印： ('OA', 'D')
    print(r.group())  # 返回正则表达式匹配的字符串，打印： ROAD
    print(r.group(2))  # 返回捕获组对应的内容(用数字指明第几个捕获组)，打印： D

# 无捕获组
print(re.match("([abc])+", "abcdefab").groups())   # 正常捕获的结果： ('c',)
print(re.match("(?:[abc])+", "abcdefab").groups())  # 无捕获组的结果： ()

# 命名组
m = re.match(r'(?P<word>\b\w+\b) *(?P<word2>\b\w+\b)', 'Lots of punctuation')
print(m.groups())       # 返回正则表达式匹配的所有内容，打印：('Lots', 'of')
print(m.group(1))       # 通过数字得到对应组的信息，打印： Lots
print(m.group('word2'))  # 通过名称得到对应组的信息，打印： of

# 命名组 逆向引用
p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)') # 与记忆组一样用法, re.match() 函数同样不能这样用，会返回 None
p = p.search('Paris in the the spring')  # r'(?P<word>\b\w+)\s+(?P=word)' 与 r'(?P<word>\b\w+)\s+\1' 效果一样
print(p.group())  # 返回正则表达式匹配的所有内容，打印： the the
print(p.groups())  # 返回一个包含字符串的元组，打印： ('the',)

# 使用松散正则表达式,以判断罗马数字为例
pattern = '''
    ^                   # beginning of string
    (M{0,3})            # thousands - 0 to 3 Ms
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                        #            or 500-800 (D, followed by 0 to 3 Cs)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                        #        or 50-80 (L, followed by 0 to 3 Xs)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                        #        or 5-8 (V, followed by 0 to 3 Is)
    $                   # end of string
    '''
print(re.search(pattern, 'M')) # 这个没有申明为松散正则表达式，按普通的来处理了，打印： None
print(re.search(pattern, 'M', re.VERBOSE).groups()) # 打印： ('M', '', '', '')

# (?iLmsux) 用法
# 以下这三句的写法都是一样的效果，表示忽略大小写，打印： ['aa', 'AA']
print(re.findall(r'(?i)(aa)', 'aa kkAAK s'))
print(re.findall(r'(aa)', 'aa kkAAK s', re.I))
print(re.findall(r'(aa)', 'aa kkAAK s', re.IGNORECASE))
# 可以多种模式同时生效
print(re.findall(r'(?im)(aa)', 'aa kkAAK s'))  # 直接在正则表达式里面写
print(re.findall(r'(aa)', 'aa kkAAK s', re.I | re.M))  # 在参数里面写
print(re.findall(r'(aa)', 'aa kkAAK s', re.I or re.M))

# 预编译正则表达式解析的写法
# romPattern = re.compile(pattern)  # 如果不是松散正则表达式,则这样写,即少写 re.VERBOSE 参数
romPattern = re.compile(pattern, re.VERBOSE)
print(romPattern.search('MCMLXXXIX').groups())  # 打印： ('M', 'CM', 'LXXX', 'IX')
print(romPattern.search('MMMDCCCLXXXVIII').groups())  # 打印： ('MMM', 'DCCC', 'LXXX', 'VIII')
# match()、search()、sub()、findall() 等等都可以这样用

#match() 函数只检查 RE 是否在字符串开始处匹配，而 search() 则是扫描整个字符串。记住这一区别是重要的。
#match() 只报告一次成功的匹配，它将从 0 处开始；如果匹配不是从 0 开始的， match() 将不会报告它。
#search() 将扫描整个字符串，并报告它找到的第一个匹配。
#例：
print(re.match('super', 'superstition').span())  # 打印： (0, 5)
print(re.match('super', 'insuperable'))          # 打印： None
print(re.search('super', 'superstition').span()) # 打印： (0, 5)
print(re.search('super', 'insuperable').span())  # 打印： (2, 7)
#------------search----------replace------sub----subn----end-----

#-----------list-------------------
class test:
    def __init__(self, a, b):
        self.a = a
        self.b = b


test1 = test(5, 25)
test2 = test(50, 35)
test3 = test(10, 15)
tests = [test1, test2, test3]
# 以 cmp 来指定排序方式, python3不可以这样写(没有cmp参数及cmp函数)
result = sorted(tests, cmp=lambda x, y: cmp(x.a, y.a))
print result[1].a, result[1].b
result2 = sorted(tests, key=lambda d: d.a)
print result[1].a, result[1].b

#set():  将元组，列表 转化成没有重复项的集合
#map(func,list):将list的每一个元素传递给func的函数，这个函数有一个参数，且返回一个值，map将每一次调用函数返回的值组成一个新列表返回
#filter(func,list):将list的每一个元素传递给func的函数，这个函数有一个参数，返回bool类型的值，filter将返回True的元素组成新列表返回
#reduce(func,list):将list的元素，挨个取出来和下一个元素通过func计算后将结果和再下一个元素继续计算

books = [
    {"name": "C#从入门到精通", "price": 23.7, "store": "卓越"},
    {"name": "ASP.NET高级编程", "price": 44.5, "store": "卓越"},
    {"name": "C#从入门到精通", "price": 24.7, "store": "当当"},
    {"name": "ASP.NET高级编程", "price": 45.7, "store": "当当"},
    {"name": "C#从入门到精通", "price": 26.7, "store": "新华书店"},
    {"name": "ASP.NET高级编程", "price": 55.7, "store": "新华书店"},
]

#2.1 求《ASP.NET高级编程》价格最便宜的店：
storename = min([b for b in books if b['name'] == "ASP.NET高级编程"], key=lambda b: b['price'])["store"]
print [b for b in books if b['name'] == "ASP.NET高级编程"]
print min([b for b in books if b['name'] == "ASP.NET高级编程"], key=lambda b: b['price'])
print storename
#过程：先用列表解析取出《ASP.NET高级编程》的列表，通过min函数，比较字典的price键获取price最小的项

#2.2 求在新华书店购买两本书一样一本要花的钱：
price = sum([b['price'] for b in books if b['store'] == "新华书店"])
print price

#2.3 求列表中有那几本书：
booknames = list(set([b['name'] for b in books]))

#2.4 列表里的书都打5折：
bookss = map(lambda b: dict(name=b['name'], price=b['price'] * 0.5, store=b['store']), books)

#2.5 《C#从入门到精通》的平均价格：
avg = (lambda ls: sum(ls) / len(ls))([b['price'] for b in books if b['name'] == "C#从入门到精通"])

#2.6 求每本书的平均价格：
book_avg = map(lambda bookname: dict(name=bookname, avg=(lambda ls: sum(ls) / len(ls))(
    [b['price'] for b in books if b['name'] == bookname])), list(set([b['name'] for b in books])))

#-----------**
def parament(**arg):
    print arg;


parament(name=1, key=2)

#-----------with
class WITHTEST:
    def __enter__(self):
        print 'in enter'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print 'in exit'


with WITHTEST() as www:
    print 'in with'

from contextlib import contextmanager
#from __future__ import with_statement   2.6以下使用
@contextmanager
def context():
    print 'entering the zone'
    try:
        yield
    except Exception, e:
        print 'with an error %s' % e
        raise e
    else:
        print 'with no error'


with context():
    print '----in context call------'

#----------------time---date
import time, datetime

print(time.strftime('%Y-%m-%d %H:%M:%S')) # 打印如: 2011-04-13 18:30:10
print(time.strftime('%Y-%m-%d %A %X %Z', time.localtime(time.time()))) # 显示当前日期； 打印如: 2011-04-13 Wednesday 18:30:10 CST
print(time.strftime("%Y-%m-%d %A %X", time.localtime())) # 显示当前日期； 打印如: 2011-04-13 Wednesday 18:30:10
print(time.time()) # 以浮点数形式返回自Linux新世纪以来经过的秒数； 打印如: 1302687844.7
print(time.ctime(1150269086.6630149))  # time.ctime([sec]) 把秒数转换成日期格式，如果不带参数，则显示当前的时间。打印如: Wed Apr 13 21:13:11 2011

# 得到今天的日期
print(datetime.date.today()) # 打印如: 2011-04-13
# 得到前一天的日期
print(datetime.date.today() + datetime.timedelta(days=-1))  # 打印如: 2011-04-12
print(datetime.date.today() - datetime.timedelta(days=1))  # 打印如: 2011-04-14
# 得到10天后的时间
print(datetime.date.today() + datetime.timedelta(days=10))  # 打印如: 2011-04-23
# 得到10小时后的时间，上面的 days 换成 hours
print(datetime.datetime.now() + datetime.timedelta(hours=10))  # 打印如: 2011-04-14 04:30:10.189000

#两日期相减(也可以大于、小于来比较):
d1 = datetime.datetime(2005, 2, 16)
d2 = datetime.datetime(2004, 12, 31)
print((d1 - d2).days)  # 打印： 47

#运行时间：
starttime = datetime.datetime.now()
time.sleep(1) # 暂停1秒
endtime = datetime.datetime.now()
print((endtime - starttime).seconds)  # 秒, 打印： 1
print((endtime - starttime).microseconds)  # 微秒； 打印： 14000


#-------------对象写 文件
# import pickle as p # 这里使用 as 简称,方便更改模块时只需改一行代码
import cPickle as p  # Python 2.x 有这个模块(比pickle快1000倍)

# 将会把资料保存在这个文件里面
shoplistfile = 'shoplist.data'

# 需要保存的资料
shoplist = ['apple', 'mango', 'carrot', 2, 5]

# 写入文件
f = open(shoplistfile, "wb") # 以二进制写入,Python2.x时可不用二进制,但3.x必须
p.dump(shoplist, f) # dump the object to a file
f.close()

# 取出资料
f = open(shoplistfile, "rb") # 以二进制读取
storedlist2 = p.load(f)
print(storedlist2)
f.close()

# 删除文件
# os.remove(shoplistfile)

#---------------url编码操作--------------
import urllib

addddd = '杭州'
print(urllib.quote(addddd))  # url 转码,打印如: %E6%9D%AD%E5%B7%9E
print(urllib.unquote('%E6%9D%AD%E5%B7%9E'))  # url 解码,打印如: 杭州
# 按所用的编码来转码
print(urllib.quote(addddd.decode(sys.stdin.encoding).encode('utf8')))  # 打印如: %E6%9D%AD%E5%B7%9E
print(urllib.quote(addddd.decode(sys.stdin.encoding).encode('gbk')))  # 打印如: %BA%BC%D6%DD
print(urllib.quote(addddd.decode('utf8').encode('gbk')))  # 指定编码来转码
addddd22 = addddd.decode(sys.stdin.encoding).encode('gbk')
print(urllib.quote(addddd22.decode('gbk').encode('utf8')))  # 指定编码来转码
print(urllib.quote(u'中国'.encode('utf8')))  # unicode编码的，需encode一下；否则中文会出错
# decode就是把其他编码转换为unicode，等同于unicode函数；encode就是把unicode编码的字符串转换为特定编码。
# 一些不希望被编码的url
print urllib.quote("http://localhost/index.html?id=1") # 打印: http%3A//localhost/index.html%3Fid%3D1
print urllib.quote("http://localhost/index.html?id=1", ":?=/") # 打印: http://localhost/index.html?id=1
# 查看
print(u'中国'.__class__)  # 打印: <type 'unicode'>
print('中国'.__class__)  #  打印: <type 'str'>


def cc(a, b=time.time()):
    print('%s  %s' % (a, b))


lili1 = [1, 2, 3, 4, 5]
lili2 = ['e', 'a', 'c', 'b']
lili1[2:2] = lili2
print lili1

import string

transTabel = string.maketrans('s', 't')
print 'sdsds'.translate(transTabel, 'd')

phoneBook = {'abc': '123', 'vvv': '224'}
print "abc no tel wa: %(abc)s" % phoneBook  # 非常有用，特别是在输入类似xml和html的时候配合字符串模版使用

from Tkinter import *
def helllllo():
    print "hello world"

win = Tk()
win.title('hello world')
win.geometry('200x300+500+200')
btn = Button(win, text='hello', command=helllllo)
btn.pack(expand=YES, fill=BOTH)

mainloop()

# jobs = set()
# jobs.add('%s:%s' % (a,b))
# print '\n'.join(sorted(jobs, key=lambda s:s.lower()))

# from urllib import urlopen
# htmlText = urlopen(r"http://bbs.saraba1st.com/2b/thread-955062-1-1.html").read()
# sys.stdout.write(htmlText)
# print 'close'

for i in range(0, 0):
    print i
list =[ ['2013-9-12', '12.52', '13.86', '12.4', '13.47', '183054000', '13.47'],
        ['2013-9-13', '13.23', '13.7', '13.03', '13.21', '119131900', '13.21'],
        ['2013-9-16', '13.22', '13.64', '12.67', '13.2', '143436600', '13.2'],
         ['2013-9-17', '13.15', '13.37', '12.75', '12.79', '94002600', '12.79'],
        ['2013-9-18', '12.75', '12.99', '12.51', '12.79', '61700200', '12.79']]
list2 =['2013-9-18', '12.75', '12.99', '12.51', '12.79', '61700200', '12.79']
# print list.index(['20132-9-12', '12.52', '13.86', '12.4', '13.47', '183054000', '13.47'])
print list2.index('12.75')

import time

a = '2013-9-17'
b = time.strptime(a, '%Y-%m-%d')
print b.tm_year
print b.tm_mon
print b.tm_mday
print time.mktime(time.strptime(a, '%Y-%m-%d'))

x = time.localtime(time.mktime(time.strptime(a, '%Y-%m-%d')))
print x
print time.strftime('%Y-%m-%d', x)

import datetime
print datetime.datetime.strptime(a, '%Y-%m-%d')

a ="12.5"
b="12.52"

if b > a:a = b
print a

# import chardet
# detect_dict = chardet.detect('sdsdsdsdsdsd')
# confidence, encoding = detect_dict['confidence'], detect_dict['encoding']
# print detect_dict
B = {"name": "C#从入门到精通", "price": "23,7", "store": "卓越"}
print B['price']
c = B['price']
print int((B['price'] or "0").replace(',', ""))
