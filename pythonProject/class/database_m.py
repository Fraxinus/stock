# coding=utf-8
__author__ = 'kk'
__localhost__ = "127.0.0.1"
__testPort__ = 27017


from pymongo import *


class DateBase_Factory:
    def __init__(self, DBName):
        self.DBName = DBName
        self.connect = None
        self.db = None
        print 'DateBase_Factory: init sucess, DBName = %s' % DBName

    def __del__(self):
        if self.connect:
            self.connect.close()
        print('DateBase_Factory: dealloc')

    def __getitem__(self, item):
        if not item:
            print 'DateBase_Factory:Can`t no be None'
            return None
        if not self.connect:
            print 'DateBase_Factory:change db must be doConnect before'
            return None
        return self.changeDB(item)

    def doConnect(self, addr=__localhost__, port=__testPort__):
        if self.connect:
            print 'DateBase_Factory:Connection is existing, Please close it before make another Connection'
            return None
        try:
            self.connect = Connection(addr, port)  # [][].find().sort()
        except Exception, e:
            self.connect = None
            print 'DateBase_Factory:Connect error %s' % e
            return None
        else:
            print 'DateBase_Factory:Connect sucess'
            return self.changeDB(self.DBName)

    def changeDB(self,DBName):
        try:
            self.db = self.connect[DBName]
        except Exception, e:
            self.db = None
            print 'DateBase_Factory:change database error %s' % e
            return None
        else:
            self.DBName = DBName
            print 'DateBase_Factory:change database sucess : %s' % DBName
            return self.db

    def closeConnect(self):
        if self.connect:
            try:
                self.connect.close()
            except Exception, e:
                self.connect = None
                print 'DateBase_Factory:dabase Close error : %s' % e
                return False
            else:
                self.connect = None
                print 'DateBase_Factory:dabase Close sucess'
                return True

    def createCappedCollection(self, collectionName, size):
        if not self.db:
            print 'DateBase_Factory:createCappedCollection, db no connect'
            return False
        try:
            self.db.create_collection(collectionName, capped=True, size=size)
        except Exception, e:
            print 'DateBase_Factory:createCappedCollection error : %s' % e
            return False
        else:
            self.connect = None
            print 'DateBase_Factory:createCappedCollection sucess name = %s' % collectionName
            return True

    def createCollection(self, collectionName):
        if not self.db:
            print 'DateBase_Factory:createCappedCollection, db no connect'
            return False
        try:
            self.db.create_collection(collectionName, capped=False)
        except Exception, e:
            print 'DateBase_Factory:createCappedCollection error : %s' % e
            return False
        else:
            self.connect = None
        print 'DateBase_Factory:createCappedCollection sucess name = %s' % collectionName
        return True

    def createIndex(self, collectionName, key, sort=ASCENDING):
        return self.db[collectionName].create_index([(key, sort)],unique=True)

    def insertDoc(self):
        raise NotImplementedError("insertDoc must be rewrite")

    def resetRewrite(self):
        raise NotImplementedError("insertDoc must be rewrite")