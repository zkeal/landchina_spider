#!/usr/bin/python  
#encoding:utf-8
import scrapy
import json
import time
from landchina.items import District
from landchina.items import LandchinaItem
from scrapy import log
import sys

class TreeSpider(scrapy.Spider):
	name='DistrictTree'
	allowed_domains = ["www.landchina.com"]
	start_urls = ["http://www.landchina.com/default.aspx?tabid=263"]

	def _init_(self,date='2016-1-1~2016-12-31'):
		self.date=date

	def parse(self,response):
		yield scrapy.Request('http://www.landchina.com/default.aspx?tabid=263',callback=self.parse_node)

 
	def parse_node(self,response):
		log.msg("pase node",level=log.INFO)
		zNodes = [{"id":2,"group":"1","value":"0","name":"行政区划","isParent":True},{"id":1,"group":"1","value":"","name":"中国","pId":2,"isParent":False},{"id":4545,"group":"1","value":"11","name":"北京市","pId":2,"isParent":True},{"id":4624,"group":"1","value":"12","name":"天津市","pId":2,"isParent":True},{"id":4701,"group":"1","value":"13","name":"河北省","pId":2,"isParent":True},{"id":5450,"group":"1","value":"14","name":"山西省","pId":2,"isParent":True},{"id":5991,"group":"1","value":"15","name":"内蒙古","pId":2,"isParent":True},{"id":6354,"group":"1","value":"21","name":"辽宁省","pId":2,"isParent":True},{"id":6597,"group":"1","value":"22","name":"吉林省","pId":2,"isParent":True},{"id":76,"group":"1","value":"23","name":"黑龙江省","pId":2,"isParent":True},{"id":378,"group":"1","value":"31","name":"上海市","pId":2,"isParent":True},{"id":419,"group":"1","value":"32","name":"江苏省","pId":2,"isParent":True},{"id":671,"group":"1","value":"33","name":"浙江省","pId":2,"isParent":True},{"id":885,"group":"1","value":"34","name":"安徽省","pId":2,"isParent":True},{"id":1147,"group":"1","value":"35","name":"福建省","pId":2,"isParent":True},{"id":1345,"group":"1","value":"36","name":"江西省","pId":2,"isParent":True},{"id":1577,"group":"1","value":"37","name":"山东省","pId":2,"isParent":True},{"id":1909,"group":"1","value":"41","name":"河南省","pId":2,"isParent":True},{"id":2279,"group":"1","value":"42","name":"湖北省","pId":2,"isParent":True},{"id":2522,"group":"1","value":"43","name":"湖南省","pId":2,"isParent":True},{"id":2807,"group":"1","value":"44","name":"广东省","pId":2,"isParent":True},{"id":3109,"group":"1","value":"45","name":"广西壮族","pId":2,"isParent":True},{"id":3370,"group":"1","value":"46","name":"海南省","pId":2,"isParent":True},{"id":3424,"group":"1","value":"50","name":"重庆市","pId":2,"isParent":True},{"id":3507,"group":"1","value":"51","name":"四川省","pId":2,"isParent":True},{"id":3927,"group":"1","value":"52","name":"贵州省","pId":2,"isParent":True},{"id":4119,"group":"1","value":"53","name":"云南省","pId":2,"isParent":True},{"id":4410,"group":"1","value":"54","name":"西藏","pId":2,"isParent":True},{"id":4586,"group":"1","value":"61","name":"陕西省","pId":2,"isParent":True},{"id":5079,"group":"1","value":"62","name":"甘肃省","pId":2,"isParent":True},{"id":5509,"group":"1","value":"63","name":"青海省","pId":2,"isParent":True},{"id":5701,"group":"1","value":"64","name":"宁夏回族","pId":2,"isParent":True},{"id":5818,"group":"1","value":"65","name":"新疆维吾尔","pId":2,"isParent":True},{"id":6670,"group":"1","value":"66","name":"新疆建设兵团","pId":2,"isParent":True}];	
		for Nodes in zNodes:
			Node_temp=json.loads(json.dumps(Nodes))
			Node_value=Node_temp['value']
			Node_Name=Node_temp['name']
			Node_is=Node_temp['isParent']
			url='http://www.landchina.com/ExtendModule/WorkAction/EnumHandler.ashx'
			cookies_query={"ASP.NET_SessionId":"btq3snu4jaxxab2abqgpgnn0",
                                "Hm_lpvt_83853859c7247c5b03b527894622d3fa": "1498471253",
                                "Hm_lvt_83853859c7247c5b03b527894622d3fa": "1498379824"}
			yield scrapy.FormRequest(url,formdata={'id': Node_value, 'group': '1'},cookies=cookies_query,callback=self.parse_tree,meta={'district_':Node_Name})
			# yield  scrapy.Request(url,callback=self.parse_tree,method='POST',body='id=11&group=1',cookies={'ASP.NET_SessionId':'mw3mg10xfwf4t4vsmiotygb3','Hm_lvt_83853859c7247c5b03b527894622d3fa':'1496338131','Hm_lpvt_83853859c7247c5b03b527894622d3fa':cooietime_end})	
	
	def parse_tree(self,response):
		nodes=json.loads(response.body_as_unicode())
		for node in nodes:
			if node['isParent']:
				url='http://www.landchina.com/ExtendModule/WorkAction/EnumHandler.ashx'
				value_id=node['value']
				forest_name=response.meta['district_']+','+node['name']
				cookies_query={"ASP.NET_SessionId":"btq3snu4jaxxab2abqgpgnn0",
                                "Hm_lpvt_83853859c7247c5b03b527894622d3fa": "1498471253",
                                "Hm_lvt_83853859c7247c5b03b527894622d3fa": "1498379824"}	
				yield scrapy.FormRequest(url,formdata={'id': value_id, 'group': '1'},cookies=cookies_query,callback=self.parse_tree,meta={'district_':forest_name})
			else:
				import sys
				reload(sys)
				sys.setdefaultencoding('utf8')
				print sys.getdefaultencoding()
				url='http://www.landchina.com/default.aspx?tabid=263'
				select_data=self.date
				query_date='9f2c3acd-0256-4da2-a659-6949c4671a2a'+':'+select_data
				#▓
				log.msg(node['name'],level=log.INFO)
				select_district=node['value']+'▓~'+node['name']
				forest_name=response.meta['district_']
				#select_district='110101▓~东城区'
				log.msg(node['name'],level=log.INFO)
				quert_distric='42ad98ae-c46a-40aa-aacc-c0884036eeaf:'+select_district.decode('UTF-8').encode('GBK')
				sum_query=query_date+'|'+str(quert_distric)
							
				cookies_query={"ASP.NET_SessionId":"btq3snu4jaxxab2abqgpgnn0",
                                "Hm_lpvt_83853859c7247c5b03b527894622d3fa": "1498471253",
                                "Hm_lvt_83853859c7247c5b03b527894622d3fa": "1498379824"} 
				
				param={
				'__VIEWSTATE':'/wEPDwUJNjkzNzgyNTU4D2QWAmYPZBYIZg9kFgICAQ9kFgJmDxYCHgNzcmMFLFVzZXIvZGVmYXVsdC9VcGxvYWQvc3lzRnJhbWVJbWcvZ3VvcTY4em4uanBnZAIBD2QWAgIBDxYCHgVzdHlsZQUgQkFDS0dST1VORC1DT0xPUjojZjNmNWY3O0NPTE9SOjtkAgIPZBYCAgEPZBYCZg9kFgJmD2QWAmYPZBYEZg9kFgJmD2QWAmYPZBYCZg9kFgJmD2QWAmYPFgQfAQUgQ09MT1I6I0QzRDNEMztCQUNLR1JPVU5ELUNPTE9SOjseB1Zpc2libGVoFgJmD2QWAgIBD2QWAmYPDxYCHgRUZXh0ZWRkAgEPZBYCZg9kFgJmD2QWAmYPZBYEZg9kFgJmDxYEHwEFhwFDT0xPUjojRDNEM0QzO0JBQ0tHUk9VTkQtQ09MT1I6O0JBQ0tHUk9VTkQtSU1BR0U6dXJsKGh0dHA6Ly93d3cubGFuZGNoaW5hLmNvbS9Vc2VyL2RlZmF1bHQvVXBsb2FkL3N5c0ZyYW1lSW1nL3hfdGRzY3dfc3lfamhnZ18wMDAuZ2lmKTseBmhlaWdodAUBMxYCZg9kFgICAQ9kFgJmDw8WAh8DZWRkAgIPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmD2QWAmYPZBYEZg9kFgJmDxYEHwEFIENPTE9SOiNEM0QzRDM7QkFDS0dST1VORC1DT0xPUjo7HwJoFgJmD2QWAgIBD2QWAmYPDxYCHwNlZGQCAg9kFgJmD2QWBGYPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmD2QWAmYPFgQfAQUgQ09MT1I6I0QzRDNEMztCQUNLR1JPVU5ELUNPTE9SOjsfAmgWAmYPZBYCAgEPZBYCZg8PFgIfA2VkZAICD2QWBGYPZBYCZg9kFgJmD2QWAmYPZBYCAgEPZBYCZg8WBB8BBYYBQ09MT1I6I0QzRDNEMztCQUNLR1JPVU5ELUNPTE9SOjtCQUNLR1JPVU5ELUlNQUdFOnVybChodHRwOi8vd3d3LmxhbmRjaGluYS5jb20vVXNlci9kZWZhdWx0L1VwbG9hZC9zeXNGcmFtZUltZy94X3Rkc2N3X3p5X2pnZ2dfMDEuZ2lmKTsfBAUCNDYWAmYPZBYCAgEPZBYCZg8PFgIfA2VkZAIBD2QWAmYPZBYCZg9kFgJmD2QWAgIBD2QWAmYPFgQfAQUgQ09MT1I6I0QzRDNEMztCQUNLR1JPVU5ELUNPTE9SOjsfAmgWAmYPZBYCAgEPZBYCZg8PFgIfA2VkZAIDD2QWAgIDDxYEHglpbm5lcmh0bWwFgwc8cCBhbGlnbj0iY2VudGVyIj48c3BhbiBzdHlsZT0iZm9udC1zaXplOiB4LXNtYWxsIj4mbmJzcDs8YnIgLz4NCiZuYnNwOzxhIHRhcmdldD0iX3NlbGYiIGhyZWY9Imh0dHA6Ly93d3cubGFuZGNoaW5hLmNvbS8iPjxpbWcgYm9yZGVyPSIwIiBhbHQ9IiIgd2lkdGg9IjI2MCIgaGVpZ2h0PSI2MSIgc3JjPSIvVXNlci9kZWZhdWx0L1VwbG9hZC9mY2svaW1hZ2UvdGRzY3dfbG9nZS5wbmciIC8+PC9hPiZuYnNwOzxiciAvPg0KJm5ic3A7PHNwYW4gc3R5bGU9ImNvbG9yOiAjZmZmZmZmIj5Db3B5cmlnaHQgMjAwOC0yMDE0IERSQ25ldC4gQWxsIFJpZ2h0cyBSZXNlcnZlZCZuYnNwOyZuYnNwOyZuYnNwOyA8c2NyaXB0IHR5cGU9InRleHQvamF2YXNjcmlwdCI+DQp2YXIgX2JkaG1Qcm90b2NvbCA9ICgoImh0dHBzOiIgPT0gZG9jdW1lbnQubG9jYXRpb24ucHJvdG9jb2wpID8gIiBodHRwczovLyIgOiAiIGh0dHA6Ly8iKTsNCmRvY3VtZW50LndyaXRlKHVuZXNjYXBlKCIlM0NzY3JpcHQgc3JjPSciICsgX2JkaG1Qcm90b2NvbCArICJobS5iYWlkdS5jb20vaC5qcyUzRjgzODUzODU5YzcyNDdjNWIwM2I1Mjc4OTQ2MjJkM2ZhJyB0eXBlPSd0ZXh0L2phdmFzY3JpcHQnJTNFJTNDL3NjcmlwdCUzRSIpKTsNCjwvc2NyaXB0PiZuYnNwOzxiciAvPg0K54mI5p2D5omA5pyJJm5ic3A7IOS4reWbveWcn+WcsOW4guWcuue9kSZuYnNwOyZuYnNwO+aKgOacr+aUr+aMgTrmtZnmsZ/oh7vlloTnp5HmioDogqHku73mnInpmZDlhazlj7gmbmJzcDvkupHlnLDnvZE8YnIgLz4NCuWkh+ahiOWPtzog5LqsSUNQ5aSHMDkwNzQ5OTLlj7cg5Lqs5YWs572R5a6J5aSHMTEwMTAyMDAwNjY2KDIpJm5ic3A7PGJyIC8+DQo8L3NwYW4+Jm5ic3A7Jm5ic3A7Jm5ic3A7PGJyIC8+DQombmJzcDs8L3NwYW4+PC9wPh8BBWRCQUNLR1JPVU5ELUlNQUdFOnVybChodHRwOi8vd3d3LmxhbmRjaGluYS5jb20vVXNlci9kZWZhdWx0L1VwbG9hZC9zeXNGcmFtZUltZy94X3Rkc2N3MjAxM195d18xLmpwZyk7ZGSNceUY8jR2bvh6reI4SVrxj1MCCt5oiPzALkErSq1tYw==',
				'__EVENTVALIDATION':'/wEWAgK+pP7ZDwLN3cj/BOiYHg454ZqWIO8Eyw1drSbDWm2BwAja7CsM+xsueevC',
				'hidComName':'default',
				'TAB_QueryConditionItem':['9f2c3acd-0256-4da2-a659-6949c4671a2a','42ad98ae-c46a-40aa-aacc-c0884036eeaf'],
				'TAB_QuerySortItemList':'282:False',
				'TAB_QuerySubmitConditionData':sum_query,
				'TAB_QuerySubmitOrderData':'282:False',
				'TAB_RowButtonActionControl':'',
				'TAB_QuerySubmitPagerData':'1',
				'TAB_QuerySubmitSortData':''
				}
				log.msg(sum_query,level=log.INFO)
				yield scrapy.FormRequest(url,formdata=param,cookies=cookies_query,callback=self.parse_info,meta={'data':sum_query,'page':'1','cookie':cookies_query,'district_':forest_name})		
			

	def parse_info(self,response):
		fast_dict = response.request.meta
		cookies_query=response.meta['cookie']
		for tr_line in response.selector.xpath('(//tr[contains(@onmouseover,"rowClass=this.className")])'):
			item=LandchinaItem()
			item['number']=tr_line.xpath('td[1]/text()').extract_first()
			if tr_line.xpath('td[2]/text()').extract_first():
				item['district']=tr_line.xpath('td[2]/text()').extract_first()
			else:
				item['district']=tr_line.xpath('td[2]/span/@titile').extract_first()
			if tr_line.xpath('td[3]/a/text()').extract_first():
				item['location']=tr_line.xpath('td[3]/a/text()').extract_first()
			else:
				item['location']=tr_line.xpath('td[3]/a/span/@title').extract_first()
			item['ahref']='http://www.landchina.com/'+tr_line.xpath('td[3]/a/@href').extract_first()
			item['area']=tr_line.xpath('td[4]/text()').extract_first()
			item['purpose']=tr_line.xpath('td[5]/text()').extract_first()
			item['mode']=tr_line.xpath('td[6]/text()').extract_first()
			item['date']=tr_line.xpath('td[7]/text()').extract_first()
			item['dis_link'] = fast_dict.get('district_1')
			ahref_detail=item['ahref']
			log.msg(ahref_detail,level=log.INFO)
			yield scrapy.Request(ahref_detail,cookies=cookies_query,callback=self.parse_detail_Info,meta={'item':item,'cookie':cookies_query}) 
		next_tag=len(response.selector.xpath('//td[contains(@class,"pager")]/a[contains(@onclick,"QueryAction.GoPage")]').extract())
		if next_tag!=0:
			url='http://www.landchina.com/default.aspx?tabid=263'
			sum_query=response.meta['data']
			page=int(response.meta['page'])+1
			param={'__VIEWSTATE':'/wEPDwUJNjkzNzgyNTU4D2QWAmYPZBYIZg9kFgICAQ9kFgJmDxYCHgdWaXNpYmxlaGQCAQ9kFgICAQ8WAh4Fc3R5bGUFIEJBQ0tHUk9VTkQtQ09MT1I6I2YzZjVmNztDT0xPUjo7ZAICD2QWAgIBD2QWAmYPZBYCZg9kFgJmD2QWBGYPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmDxYEHwEFIENPTE9SOiNEM0QzRDM7QkFDS0dST1VORC1DT0xPUjo7HwBoFgJmD2QWAgIBD2QWAmYPDxYCHgRUZXh0ZWRkAgEPZBYCZg9kFgJmD2QWAmYPZBYEZg9kFgJmDxYEHwEFhwFDT0xPUjojRDNEM0QzO0JBQ0tHUk9VTkQtQ09MT1I6O0JBQ0tHUk9VTkQtSU1BR0U6dXJsKGh0dHA6Ly93d3cubGFuZGNoaW5hLmNvbS9Vc2VyL2RlZmF1bHQvVXBsb2FkL3N5c0ZyYW1lSW1nL3hfdGRzY3dfc3lfamhnZ18wMDAuZ2lmKTseBmhlaWdodAUBMxYCZg9kFgICAQ9kFgJmDw8WAh8CZWRkAgIPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmD2QWAmYPZBYEZg9kFgJmDxYEHwEFIENPTE9SOiNEM0QzRDM7QkFDS0dST1VORC1DT0xPUjo7HwBoFgJmD2QWAgIBD2QWAmYPDxYCHwJlZGQCAg9kFgJmD2QWBGYPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmD2QWAmYPFgQfAQUgQ09MT1I6I0QzRDNEMztCQUNLR1JPVU5ELUNPTE9SOjsfAGgWAmYPZBYCAgEPZBYCZg8PFgIfAmVkZAICD2QWBGYPZBYCZg9kFgJmD2QWAmYPZBYCAgEPZBYCZg8WBB8BBYYBQ09MT1I6I0QzRDNEMztCQUNLR1JPVU5ELUNPTE9SOjtCQUNLR1JPVU5ELUlNQUdFOnVybChodHRwOi8vd3d3LmxhbmRjaGluYS5jb20vVXNlci9kZWZhdWx0L1VwbG9hZC9zeXNGcmFtZUltZy94X3Rkc2N3X3p5X2pnZ2dfMDEuZ2lmKTsfAwUCNDYWAmYPZBYCAgEPZBYCZg8PFgIfAmVkZAIBD2QWAmYPZBYCZg9kFgJmD2QWAgIBD2QWAmYPFgQfAQUgQ09MT1I6I0QzRDNEMztCQUNLR1JPVU5ELUNPTE9SOjsfAGgWAmYPZBYCAgEPZBYCZg8PFgIfAmVkZAIDD2QWAgIDDxYEHglpbm5lcmh0bWwFgwc8cCBhbGlnbj0iY2VudGVyIj48c3BhbiBzdHlsZT0iZm9udC1zaXplOiB4LXNtYWxsIj4mbmJzcDs8YnIgLz4NCiZuYnNwOzxhIHRhcmdldD0iX3NlbGYiIGhyZWY9Imh0dHA6Ly93d3cubGFuZGNoaW5hLmNvbS8iPjxpbWcgYm9yZGVyPSIwIiBhbHQ9IiIgd2lkdGg9IjI2MCIgaGVpZ2h0PSI2MSIgc3JjPSIvVXNlci9kZWZhdWx0L1VwbG9hZC9mY2svaW1hZ2UvdGRzY3dfbG9nZS5wbmciIC8+PC9hPiZuYnNwOzxiciAvPg0KJm5ic3A7PHNwYW4gc3R5bGU9ImNvbG9yOiAjZmZmZmZmIj5Db3B5cmlnaHQgMjAwOC0yMDE0IERSQ25ldC4gQWxsIFJpZ2h0cyBSZXNlcnZlZCZuYnNwOyZuYnNwOyZuYnNwOyA8c2NyaXB0IHR5cGU9InRleHQvamF2YXNjcmlwdCI+DQp2YXIgX2JkaG1Qcm90b2NvbCA9ICgoImh0dHBzOiIgPT0gZG9jdW1lbnQubG9jYXRpb24ucHJvdG9jb2wpID8gIiBodHRwczovLyIgOiAiIGh0dHA6Ly8iKTsNCmRvY3VtZW50LndyaXRlKHVuZXNjYXBlKCIlM0NzY3JpcHQgc3JjPSciICsgX2JkaG1Qcm90b2NvbCArICJobS5iYWlkdS5jb20vaC5qcyUzRjgzODUzODU5YzcyNDdjNWIwM2I1Mjc4OTQ2MjJkM2ZhJyB0eXBlPSd0ZXh0L2phdmFzY3JpcHQnJTNFJTNDL3NjcmlwdCUzRSIpKTsNCjwvc2NyaXB0PiZuYnNwOzxiciAvPg0K54mI5p2D5omA5pyJJm5ic3A7IOS4reWbveWcn+WcsOW4guWcuue9kSZuYnNwOyZuYnNwO+aKgOacr+aUr+aMgTrmtZnmsZ/oh7vlloTnp5HmioDogqHku73mnInpmZDlhazlj7gmbmJzcDvkupHlnLDnvZE8YnIgLz4NCuWkh+ahiOWPtzog5LqsSUNQ5aSHMDkwNzQ5OTLlj7cg5Lqs5YWs572R5a6J5aSHMTEwMTAyMDAwNjY2KDIpJm5ic3A7PGJyIC8+DQo8L3NwYW4+Jm5ic3A7Jm5ic3A7Jm5ic3A7PGJyIC8+DQombmJzcDs8L3NwYW4+PC9wPh8BBWRCQUNLR1JPVU5ELUlNQUdFOnVybChodHRwOi8vd3d3LmxhbmRjaGluYS5jb20vVXNlci9kZWZhdWx0L1VwbG9hZC9zeXNGcmFtZUltZy94X3Rkc2N3MjAxM195d18xLmpwZyk7ZGRgck5Fo6pq6VZKO/BZJV3IaSndNmX3b/ACh/e9v+aSJA==',
					'__EVENTVALIDATION':'/wEWAgK+pP7ZDwLN3cj/BOiYHg454ZqWIO8Eyw1drSbDWm2BwAja7CsM+xsueevC',
					'hidComName':'default',
					'TAB_QueryConditionItem':['9f2c3acd-0256-4da2-a659-6949c4671a2a','42ad98ae-c46a-40aa-aacc-c0884036eeaf'],
					'TAB_QuerySortItemList':'282:False',
					'TAB_QuerySubmitConditionData':sum_query,
					'TAB_QuerySubmitOrderData':'282:False',
					'TAB_RowButtonActionControl':'',
					'TAB_QuerySubmitPagerData':str(page),
					'TAB_QuerySubmitSortData':''
					}
			yield scrapy.FormRequest(url,formdata=param,cookies=cookies_query,callback=self.parse_info,meta={'data':sum_query,'page':str(page),'cookie':cookies_query,'district_1':fast_dict.get('district_1')})

	def parse_detail_Info(self,response):
		item=response.meta['item']
		item['detail_district']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r1_c2_ctrl')]/text()").extract()		
		item['detail_name']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r17_c2_ctrl')]/text()").extract()
		item['detail_location']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r16_c2_ctrl')]/text()").extract()
		item['detail_area']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r2_c2_ctrl')]/text()").extract()
		item['detail_source']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r2_c4_ctrl')]/text()").extract()
		item['detail_use']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r3_c2_ctrl')]/text()").extract()
		item['detail_method']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r3_c4_ctr')]/text()").extract()
		item['detail_years']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r19_c2_ctrl')]/text()").extract()
		item['detail_class']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r19_c4_ctrl')]/text()").extract()
		item['detail_level']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r20_c2_ctrl')]/text()").extract()
		item['detail_price']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r20_c4_ctrl')]/text()").extract()
		price1_result=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f3_r2_c3_')]/text()").extract()
		if len(price1_result)!=0:
			del price1_result[0]
			for temp_price in price1_result:
				item['detail_price1']=temp_price+';'
		else:
			item['detail_price1']=[]
		item['detail_owner']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r9_c2_ctrl')]/text()").extract()
		item['detail_volume1']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f2_r1_c2_ctrl')]/text()").extract()
		item['detail_volume2']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f2_r1_c4_ctrl')]/text()").extract()
		item['detail_date1']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r21_c4_ctrl')]/text()").extract()
		item['detail_date2']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r22_c2_ctrl')]/text()").extract()
		item['detail_date3']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r22_c4_ctrl')]/text()").extract()
		item['detail_gov']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r14_c2_ctrl')]/text()").extract()
		item['detail_date4']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r14_c4_ctrl')]/text()").extract()
		yield item