#coding:utf-8
#!/usr/bin/python
# '''
# Created on May 12, 2015
# 
# @author: rgao
# 
# this util uses for auto rename the storytelling
# '''
import os
import re

dirPath = "C:/Users/rgao/Desktop/ykc/烈火金刚"
p1 = "C:/Users/rgao/Desktop/ykc/封神演义-200"
b1 = 0
n1 = "封神演义"
p2 = "C:/Users/rgao/Desktop/ykc/水泊梁山_袁阔成-100"
b2 = 200
n2 = "水泊梁山"
p3 = "C:/Users/rgao/Desktop/ykc/袁阔成 碧眼金蟾 全100回"
b3 = 300
n3 = "碧眼金蟾"
p4 = "C:/Users/rgao/Desktop/ykc/袁阔成 薛刚反唐 全100回"
b4 = 400
n4 = "薛刚反唐"
p5 = "C:/Users/rgao/Desktop/ykc/三国演义-袁阔成-365"
b5 = 500
n5 = "三国演义"
p6 = "C:/Users/rgao/Desktop/ykc/林海雪原_袁阔成-45"
b6 = 865
n6 = "林海雪原"
p7 = "C:/Users/rgao/Desktop/ykc/西楚霸王-袁阔成-50"
b7 = 910
n7 = "西楚霸王"
p8 = "C:/Users/rgao/Desktop/ykc/袁阔成 金钱镖 全52回"
b8 = 1798
n8 = "金钱镖"
p9 = "C:/Users/rgao/Desktop/ykc/袁阔成评书_春秋五霸.袁田(全100回)"
b9 = 1850
n9 = "春秋五霸"
p10 = "C:/Users/rgao/Desktop/ykc/袁阔成 野火春风斗古城 全80回"
b10 = 1950
n10 = "野火春风斗古城"
p11 = "C:/Users/rgao/Desktop/ykc/袁阔成 彭公案 全86回"
b11 = 2030
n11 = "彭公案"
p12 = "C:/Users/rgao/Desktop/ykc/烈火金刚-袁阔成-33"
b12 = 2116
n12 = "烈火金刚"

def changeFile(path, base, name):
    if not os.path.exists(path):
        print "the path is not exst"
        return
    cur = os.getcwd()
    os.chdir(path)
    files = os.listdir(".")
    mp3 = {}
    for i in range(len(files)):
        #print files[i]
        m = re.search(r"[^\d]*(\d+)[^\d]*\.[mM][pP]3$", files[i])
        if m:
            num = int(m.group(1))
            mp3[num] = files[i]
    for key in mp3.keys():
        #print key, mp3[key]
        newName = "%05d-%s-%03d.mp3" % (int(key)+base, name, int(key))
        print newName, '-', mp3[key]
        os.rename(mp3[key], newName)
    os.chdir(cur)
        

if __name__ == '__main__':
    print "start------"
    changeFile(dirPath, 100, n1)
#     changeFile(p7, b7, n7)
#     changeFile(p8, b8, n8)
#     changeFile(p9, b9, n9)
#     changeFile(p10, b10, n10)
#     changeFile(p11, b11, n11)
#     changeFile(p12, b12, n12)
    
    
    