#coding=utf-8

import shelve
 
def CreateData():
    try:
        db = shelve.open('db.dat', 'c')
        # key与value必须是字符串
        db['int'] = 1
        db['float'] = 2.3
        db['string'] = "I like python."
        db['key'] = 'value'
    finally:
        db.close()
 
def LoadData():
    db = shelve.open('db.dat', 'r')
    for item in list(db.items()):
        print(item)
    db.close()
 
if __name__ == '__main__':
    CreateData()
    LoadData()