#coding=utf-8
'''
Created on 2015��5��26��

@author: raistlin
'''

import re
import urllib
import os
import time
from multiprocessing import Process
import threading  

mylock = threading.RLock()
num = 20
nFailed = []

def proDownImg(url,fileName):
#     print "url - ", url
#     print "filename - ", fileName
    urllib.urlretrieve(url, fileName)

class thrDown(threading.Thread):
    def __init__(self, name, l, path):
        threading.Thread.__init__(self)
        self.name = name
        self.l = l
        self.path = path
        self.flag = False
        
    def run(self):
        global num
        global nFailed
        l = self.l
        path = self.path
        isfailed = None
        while not self.flag:
            mylock.acquire()
            getNum = num
            num +=1
            if isfailed:
                nFailed.append(isfailed)
                isfailed = None
            mylock.release()
            if getNum >= len(l):
                print "%s - end of list" % self.name
                break
            url = l[getNum]
            if url.find("jpg") >= 0:
                fileName = "%s/%04d.jpg" % (path,getNum)
                print "%s - down %s" % (self.name, url)
                p = Process(target=proDownImg, args=(url,fileName))
                p.start()
                p.join(30)
                if p.is_alive():
                    print "kill pro - ", fileName 
                    p.terminate()
                    isfailed = fileName
        print "thread complete (%s)" % self.name
    
    def stop(self):
        self.flag = True

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def parseHtml(html):
    reg = r'src="([^ <>]+?\.jpg)"><br>' # for xxxurl
#     reg = r'src="([^ <>]+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    reg = r'([^ >]+?)</a><br>'
    addre = re.compile(reg)
    findPic = 0
    result = []
    for line in html.split('\n'): # temporary update, '\n'
        img = re.findall(imgre, line)
        if img:
            result.append(img[0])
            findPic = 1
        elif findPic == 1:
            add = re.findall(addre, line)
            if add:
                result.append(add[0])
                findPic = 0
#     for i, item in enumerate(result):
#         print i, item
    return result


def downloadPic(picList, path, tnum):
    pHash = {}
    for i in range(tnum):
        pHash[i] = thrDown("thr-%d" % i, picList, path)
        pHash[i].start()
#     time.sleep(10)
    for key in pHash.keys():
#         pHash[key].stop()
        pHash[key].join()

def getAll(l, d):
    wdir = "%s\\%s" % (d, time.strftime("%Y-%m-%d"))
    if os.path.isdir(wdir):
        print "dir", wdir, "already exit."
    else:
        os.mkdir(wdir)
    fh = open(wdir + "/list.txt", "w")
    for i,item in enumerate(l):
        fh.write("%03d - %s\n" % (i, item))
        if item.find('.jpg') == -1:
            fh.write("*" *20 + "\n")
    fh.close()
    downloadPic(l, wdir, 3)
#     for i, item in enumerate(l):
#         print "%03d - %s" % (i, item)
#     downloadPic(l, wdir, 3)

def summary():
    print "**** spend time: ", time.clock()
    for i in nFailed:
        print " ", i
    print "failed time - %d" % len(nFailed)

def getImg(url):
    html = getHtml(url)
    l = parseHtml(html)
    getAll(l, r"C:\Users\raistlin\Desktop\program")
    summary()

def parseTopic(html):
    reg = r'src="(.+?\.jpg)" pic_ext='
    imgre = re.compile(reg)
    img = re.findall(imgre, html)
    return img
    
def identifyImg(name):
    if os.path.getsize(name)/1024.0 <10:
        tempDir = os.path.dirname(name) + "\\remove"
        if not os.path.isdir(tempDir):
            os.mkdir(tempDir)
        os.rename(name, "%s\\%s" % (tempDir, os.path.basename(name)))

def getTopic(url, num, path):
    print num, url
    html = getHtml(url)
    for i, item in enumerate(parseTopic(html)):
        name = "%s\\%03d-%02d.jpg" % (path, num, i)
        proDownImg(item, name)
        identifyImg(name)

def traverseForum(url, savePath):
    urlBase = url[:url[7:].index('/')+7]
    html = getHtml(url)
    reg = r'href="(/p/\w+?)" title='
    pageRe = re.compile(reg)
    pages = re.findall(pageRe, html)
#     getTopic("%s/%s" % (urlBase, pages[4]), 0, savePath)
#     getTopic(r'http://tieba.baidu.com//p/3762208718', 0, savePath)
    for i, item in enumerate(pages):
        getTopic("%s/%s" % (urlBase, item), i, savePath)
    summary()
    
if __name__ == '__main__':
    xxurl = "http://www.xqzr777.com/bt.htm"
    testurl = "http://tieba.baidu.com/p/3762208718"
    url_yurisa = "http://tieba.baidu.com/f?kw=yurisa&tp=0"
    print "**** star time ", time.clock()
    # start from here
    
#     getImg(xxurl)

    traverseForum(url_yurisa, r'C:\Users\rgao\Desktop\new\temp')
    
    print "last line"