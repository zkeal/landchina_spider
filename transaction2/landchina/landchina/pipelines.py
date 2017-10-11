# coding=utf-8
import csv
import xlwt

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class LandchinaPipeline(object):

    def __init__(self):
	self.myexcel = xlwt.Workbook()
	self.info = self.myexcel.add_sheet("info",cell_overwrite_ok=False)
	self.lines=1
	row0=[u'序号',u"地区",u"行政区",u"土地坐落",u"超链接",u"土地用途",u"签订日期",u"宗地标识",u"宗地编号",u"宗地座落",u"土地使用权证号",u"土地面积",u"土地用途",u"土地级别",u"土地利用状况",u"出租期限",u"到期时间",u"到期时间",u"年租总金额"]
	for i in range(0,len(row0)):
		self.info.write(0,i,row0[i])

    def process_item(self, item, spider):
	print "begin_wirte"
	num=0
	for number in range(0,18):
		if number==0:
			self.info.write(self.lines,num,item['number'])
			print self.lines,num,item['number'],number
		if number==1:
			self.info.write(self.lines,num,item['dis_link'])
		if number==2:
                        self.info.write(self.lines,num,item['district'])
		if number==3:
			#n = 'HYPERLINK'
			#content='("'+item['ahref']+'";"'+item['location']+'")'
			#print item['location']
			#self.info.write(self.lines,num,xlwt.Formula('HYPERLINK("http://www.google.com";"Google")'))			
                       	self.info.write(self.lines,num,item['location'])
		if number==4:
                        self.info.write(self.lines,num,item['ahref'])
		if number==5:
	                self.info.write(self.lines,num,item['use'])
		if number==6:
                        self.info.write(self.lines,num,item['date'])
		if number==7:
                        self.info.write(self.lines,num,item['detail_flag'])
		if number==8:
                        self.info.write(self.lines,num,item['detail_num'])
		if number==9:
                        self.info.write(self.lines,num,item['detail_location'])
		if number==10:
			self.info.write(self.lines,num,item['detail_usenumber'])
		if number==11:
                        self.info.write(self.lines,num,item['detail_use'])
		if number==12:
                        self.info.write(self.lines,num,item['detail_level'])
		if number==13:
                        self.info.write(self.lines,num,item['detail_status'])
		if number==14:
                        self.info.write(self.lines,num,item['detail_years'])
		if number==15:
                        self.info.write(self.lines,num,item['detail_date'])
		if number==16:
                        self.info.write(self.lines,num,item['detail_date2'])
		if number==17:
                        self.info.write(self.lines,num,item['detail_price'])
		num=num+1
	self.lines = self.lines+1
    	return item

    def close_spider(self,spider):
	print 'close in'
	self.myexcel.save("info.xls")
        
