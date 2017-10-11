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
	row0=[u'序号',u"地区",u"行政区",u"土地坐落",u"超链接",u"抵押面积",u"抵押土地用途",u"宗地标识",u"宗地编号",u"宗地座落",u"土地面积",u"土地他项权利人证号",u"土地使用权证号",u"土地抵押人名称",u"土地抵押人性质",u"土地抵押权人",u"抵押土地用途",u"抵押土地权性质与使用权类型",u"抵押面积",u"评估金额",u"抵押金额",u"抵押起始时间",u"抵押结束时间"]
	for i in range(0,len(row0)):
		self.info.write(0,i,row0[i])

    def process_item(self, item, spider):
	print "begin_wirte"
	num=0
	for number in range(0,23):
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
	                self.info.write(self.lines,num,item['area'])
		if number==6:
                        self.info.write(self.lines,num,item['use'])
		if number==7:
                        self.info.write(self.lines,num,item['detail_flag'])
		if number==8:
                        self.info.write(self.lines,num,item['detail_num'])
		if number==9:
                        self.info.write(self.lines,num,item['detail_location'])
		if number==10:
			self.info.write(self.lines,num,item['detail_area'])
		if number==11:
                        self.info.write(self.lines,num,item['detail_othernumber'])
		if number==12:
                        self.info.write(self.lines,num,item['detail_countrynumber'])
		if number==13:
                        self.info.write(self.lines,num,item['detail_mortgager'])
		if number==14:
                        self.info.write(self.lines,num,item['detail_mortgage'])
		if number==15:
                        self.info.write(self.lines,num,item['detail_profit'])
		if number==16:
                        self.info.write(self.lines,num,item['detail_use'])
		if number==17:
                        self.info.write(self.lines,num,item['detail_class'])
		if number==18:
                        self.info.write(self.lines,num,item['detail_area'])
		if number==19:
                        self.info.write(self.lines,num,item['detail_Fprice'])
		if number==20:
                        self.info.write(self.lines,num,item['detail_Tprice'])
		if number==21:
                        self.info.write(self.lines,num,item['detail_starttime'])
		if number==22:
                        self.info.write(self.lines,num,item['detail_endtime'])
		num=num+1
	self.lines = self.lines+1
    	return item

    def close_spider(self,spider):
	print 'close in'
	self.myexcel.save("info.xls")
        
