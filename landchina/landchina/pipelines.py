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
	row0=[u'序号',u"地区",u"行政区",u"土地坐落",u"链接",u"总面积",u"土地用途",u"供应方式",u"签订日期",u"项目名称",u"项目位置",u"面积(公顷)",u"土地来源",u"土地用途",u"供地方式",u"土地使用年限",u"行业分类",u"土地级别",u"成交价格",u"分期支付",u"土地使用权人",u"约定容积率(上限)",u"约定容积率(下限)",u"约定交地时间",u"约定开工时间",u"约定竣工时间",u"批准单位",u"合同签订日期"]
	for i in range(0,len(row0)):
		self.info.write(0,i,row0[i])

    def process_item(self, item, spider):
	print "begin_wirte"
	num=0
	for number in range(0,28):
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
                        self.info.write(self.lines,num,item['purpose'])
		if number==7:
                        self.info.write(self.lines,num,item['mode'])
		if number==8:
                        self.info.write(self.lines,num,item['date'])
		if number==9:
			self.info.write(self.lines,num,item['detail_name'])
		if number==10:
                        self.info.write(self.lines,num,item['detail_location'])
		if number==11:
                        self.info.write(self.lines,num,item['detail_area'])
		if number==12:
                        self.info.write(self.lines,num,item['detail_source'])
		if number==13:
                        self.info.write(self.lines,num,item['detail_use'])
		if number==14:
                        self.info.write(self.lines,num,item['detail_method'])
		if number==15:
                        self.info.write(self.lines,num,item['detail_years'])
		if number==16:
                        self.info.write(self.lines,num,item['detail_class'])
		if number==17:
                        self.info.write(self.lines,num,item['detail_level'])
		if number==18:
                        self.info.write(self.lines,num,item['detail_price'])
		if number==19:
                        self.info.write(self.lines,num,item['detail_price1'])
		if number==20:
                        self.info.write(self.lines,num,item['detail_owner'])
		if number==21:
                        self.info.write(self.lines,num,item['detail_volume1'])
		if number==22:
                        self.info.write(self.lines,num,item['detail_volume2'])
		if number==23:
                        self.info.write(self.lines,num,item['detail_date1'])
		if number==24:
                        self.info.write(self.lines,num,item['detail_date2'])
		if number==25:
                        self.info.write(self.lines,num,item['detail_date3'])
		if number==26:
                        self.info.write(self.lines,num,item['detail_gov'])
		if number==27:
                        self.info.write(self.lines,num,item['detail_date4'])
		num=num+1
	self.lines = self.lines+1
    	return item

    def close_spider(self,spider):
	print 'close in'
	self.myexcel.save("info.xls")
        
