#!/usr/bin/env python
import re
import urllib
import datetime

url8191 = r'http://www.cmbchina.com/CFWEB/Personal/productdetail.aspx?code=8191&type=prodvalue'
url8192 = r'http://www.cmbchina.com/CFWEB/Personal/productdetail.aspx?code=8192&type=prodvalue'

def getDate(strD):
    return datetime.date(int(strD[:4]), int(strD[4:6]), int(strD[6:]))

class fund(object):
    __value_91 = 0
    __value_92 =0
    __date_91 = datetime.date(2014,1,1)
    __date_92 = datetime.date(2014,1,1)
    def __init__(self, buyDate, buyValue, buyType = 8192):
        self.date = buyDate
        self.value = buyValue
        self.type = buyType
        self.count = 0
    def setCount(self, val):
        self.count = val/self.value
    def getDuration(self):
        if self.type == 8191:
            duration = fund.__date_91 - self.date
        elif self.type == 8192:
            duration = fund.__date_92 - self.date
        return duration.days
    def getIncome(self):
        if self.type == 8191:
            return fund.__value_91 - self.value
        elif self.type == 8192:
            return fund.__value_92 - self.value
    def show(self):
        print "buy: ", self.date, " -- ", self.value
        if self.type == 8191:
            print "now: ", fund.__date_91, " -- ", fund.__value_91
            print " -"*4, "money = ", fund.__value_91 * self.count,
        elif self.type == 8192:
            print "now: ", fund.__date_92, " ---- ", fund.__value_92
            print " -"*4, "money = ", fund.__value_92 * self.count,
        print "  ---- ratio: ", (self.getIncome()*36500)/(self.value * self.getDuration())
    @staticmethod
    def update91(dat, val):
        fund.__value_91 = val
        fund.__date_91 = dat
    @staticmethod
    def update92(dat, val):
        fund.__value_92 = val
        fund.__date_92 = dat

def html2table(html, useid=False):
    trs = re.findall(r'<tr align="left" valign="middle">.*</tr>', html, re.DOTALL)
    rows = []
    for tr in trs:
        x = re.findall(r'<td align="center" valign="middle">([^<>]*)</td>', tr, re.DOTALL)
        x = map(lambda t: t.strip(), x)
        rows.append(x)
    return rows

def getLastValue(name, html):
    rows = html2table(urllib.urlopen(html).read())
    print "%s ---- %s value is: %s" % (name, rows[0][3], rows[0][2])
    date = []
    value = []
    i = 0
    for r in rows:
        for c in r:
            if i==2:
                value.append(c)
            elif i==3:
                date.append(c)
                i-=4
            i+=1
    days = getDate(date[0]) - getDate(date[-1])
    gain = float(value[0]) - float(value[-1])
    print "\t %d days increase %f" % (days.days, gain)
    print "\t 1w increase (%f) last day" % ((float(value[0]) - float(value[1])) * 10000/float(value[1]))
    print "\t increase ratio is ----> %f" % (gain/float(value[-1])/float(days.days) *365 *100)
    return (getDate(date[0]), float(value[0]))

if __name__ == "__main__":
    (d8191, v8191) = getLastValue("8191", url8191)
    (d8192, v8192) = getLastValue("8192", url8192)
    fund.update91(d8191,v8191)
    fund.update92(d8192,v8192)
    f1 = fund(getDate("20140311"), 1.0877)
    f1.setCount(100000)
    f2 = fund(getDate("20140313"), 1.0881)
    f2.setCount(20000)
    f3 = fund(getDate("20140325"), 1.1564, 8191)
    f3.setCount(50000)
    f4 = fund(getDate("20140401"), 1.0915)
    f4.setCount(130000)
    print
    f1.show()
    print
    f2.show()
    print
    f3.show()
    print
    f4.show()
    
    raw_input()