#!/usr/bin/python  
#encoding:utf-8
import scrapy
import json
import time
from landchina.items import District
from landchina.items import LandchinaItem
from scrapy import log
import sys
import pdb

class TreeSpider(scrapy.Spider):
	name='transaction2'
	allowed_domains = ["www.landchina.com"]
	start_urls = ["http://www.landchina.com/default.aspx?tabid=264&ComName=default"]

	def _init_(self,date='2016-1-1~2016-12-31'):
		self.date=date

	def parse(self,response):
		yield scrapy.Request('http://www.landchina.com/default.aspx?tabid=264&ComName=default',callback=self.parse_node)


	def parse_node(self,response):
		log.msg("pase node",level=log.INFO)
		import sys
		reload(sys)
		sys.setdefaultencoding('utf8')
		print sys.getdefaultencoding()
		zNodes = [{"id":1,"group":"1","value":"","name":"中国","pId":2,"isParent":False}]
		for Nodes in zNodes:
			Node_temp=json.loads(json.dumps(Nodes))
			Node_value=Node_temp['value']
			Node_Name=Node_temp['name']
			Node_is=Node_temp['isParent']
			url='http://www.landchina.com/ExtendModule/WorkAction/EnumHandler.ashx'
			cookies_query={"ASP.NET_SessionId":"btq3snu4jaxxab2abqgpgnn0",
                                "Hm_lpvt_83853859c7247c5b03b527894622d3fa": "1498471253",
                                "Hm_lvt_83853859c7247c5b03b527894622d3fa": "1498379824"}
			url = 'http://www.landchina.com/default.aspx?tabid=264&ComName=default'
			select_data = self.date
			query_date = '8ede234a-9e5a-4bef-8d51-8157dceb471c' + ':' + select_data
			sum_query = query_date
			cookies_query = {"ASP.NET_SessionId": "btq3snu4jaxxab2abqgpgnn0",
							 "Hm_lpvt_83853859c7247c5b03b527894622d3fa": "1498471253",
							 "Hm_lvt_83853859c7247c5b03b527894622d3fa": "1498379824"}
			log.msg(sum_query,level=log.INFO)
			param = {
				'__VIEWSTATE': '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FgJmD2QWAmYPZBYCAgEPZBYCZg8WBB8BBSdDT0xPUjojRDNEM0QzO0JBQ0tHUk9VTkQtQ09MT1I6IzMzNjZmZjsfAmgWAmYPZBYCAgEPZBYCZg8PFgIfA2VkZAIDD2QWAgIDDxYEHglpbm5lcmh0bWwFgwc8cCBhbGlnbj0iY2VudGVyIj48c3BhbiBzdHlsZT0iZm9udC1zaXplOiB4LXNtYWxsIj4mbmJzcDs8YnIgLz4NCiZuYnNwOzxhIHRhcmdldD0iX3NlbGYiIGhyZWY9Imh0dHA6Ly93d3cubGFuZGNoaW5hLmNvbS8iPjxpbWcgYm9yZGVyPSIwIiBhbHQ9IiIgd2lkdGg9IjI2MCIgaGVpZ2h0PSI2MSIgc3JjPSIvVXNlci9kZWZhdWx0L1VwbG9hZC9mY2svaW1hZ2UvdGRzY3dfbG9nZS5wbmciIC8+PC9hPiZuYnNwOzxiciAvPg0KJm5ic3A7PHNwYW4gc3R5bGU9ImNvbG9yOiAjZmZmZmZmIj5Db3B5cmlnaHQgMjAwOC0yMDE0IERSQ25ldC4gQWxsIFJpZ2h0cyBSZXNlcnZlZCZuYnNwOyZuYnNwOyZuYnNwOyA8c2NyaXB0IHR5cGU9InRleHQvamF2YXNjcmlwdCI+DQp2YXIgX2JkaG1Qcm90b2NvbCA9ICgoImh0dHBzOiIgPT0gZG9jdW1lbnQubG9jYXRpb24ucHJvdG9jb2wpID8gIiBodHRwczovLyIgOiAiIGh0dHA6Ly8iKTsNCmRvY3VtZW50LndyaXRlKHVuZXNjYXBlKCIlM0NzY3JpcHQgc3JjPSciICsgX2JkaG1Qcm90b2NvbCArICJobS5iYWlkdS5jb20vaC5qcyUzRjgzODUzODU5YzcyNDdjNWIwM2I1Mjc4OTQ2MjJkM2ZhJyB0eXBlPSd0ZXh0L2phdmFzY3JpcHQnJTNFJTNDL3NjcmlwdCUzRSIpKTsNCjwvc2NyaXB0PiZuYnNwOzxiciAvPg0K54mI5p2D5omA5pyJJm5ic3A7IOS4reWbveWcn+WcsOW4guWcuue9kSZuYnNwOyZuYnNwO+aKgOacr+aUr+aMgTrmtZnmsZ/oh7vlloTnp5HmioDogqHku73mnInpmZDlhazlj7gmbmJzcDvkupHlnLDnvZE8YnIgLz4NCuWkh+ahiOWPtzog5LqsSUNQ5aSHMDkwNzQ5OTLlj7cg5Lqs5YWs572R5a6J5aSHMTEwMTAyMDAwNjY2KDIpJm5ic3A7PGJyIC8+DQo8L3NwYW4+Jm5ic3A7Jm5ic3A7Jm5ic3A7PGJyIC8+DQombmJzcDs8L3NwYW4+PC9wPh8BBWRCQUNLR1JPVU5ELUlNQUdFOnVybChodHRwOi8vd3d3LmxhbmRjaGluYS5jb20vVXNlci9kZWZhdWx0L1VwbG9hZC9zeXNGcmFtZUltZy94X3Rkc2N3MjAxM195d18xLmpwZyk7ZGR8R2Hf96YNnf6j1YMeSz+J5BPeYgyae/XkhbQJa7VIXQ==',
				'__EVENTVALIDATION': '/wEWAgLV6oKLBALN3cj/BO464ABoybQPHOdzQf2ngEaxl8Vo30d+g02QfNizQ7Ge',
				'hidComName': 'default',
				'mainModuleContainer_492_1114_495_TabMenu1_selected_index': '1',
				'top1_QuerySubmitConditionData': '',
				'top1_QuerySubmitOrderData': '',
				'top1_RowButtonActionControl': '',
				'top1_QuerySubmitPagerData': '1',
				'top1_QuerySubmitSortData': '',
				'top2_QueryConditionItem': '8ede234a-9e5a-4bef-8d51-8157dceb471c',
				'top2_QuerySubmitConditionData': sum_query,
				'top2_QuerySubmitOrderData': '',
				'top2_RowButtonActionControl': '',
				'top2_QuerySubmitPagerData': '1',
				'top2_QuerySubmitSortData': '',
				'top3_QuerySubmitConditionData': '',
				'top3_QuerySubmitOrderData': '',
				'top3_RowButtonActionControl': '',
				'top3_QuerySubmitPagerData': '1',
				'top3_QuerySubmitSortData': ''
			}
			log.msg(sum_query, level=log.INFO)
			yield scrapy.FormRequest(url, formdata=param, cookies=cookies_query, callback=self.parse_info,
									 meta={'data': sum_query, 'page': '1', 'cookie': cookies_query,
										   'district_1': Node_Name})

	def parse_info(self,response):
		fast_dict = response.request.meta
		cookies_query=response.meta['cookie']
		for tr_line in response.selector.xpath('//table[contains(@id,"top2_contentTable")]//tr[contains(@onmouseover,"rowClass=this.className")]'):
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
			item['use']=tr_line.xpath('td[4]/text()').extract_first()
			item['date']=tr_line.xpath('td[5]/text()').extract_first()
			item['dis_link'] = fast_dict.get('district_1')
			ahref_detail=item['ahref']
			yield scrapy.Request(ahref_detail,cookies=cookies_query,callback=self.parse_detail_Info,meta={'item':item,'cookie':cookies_query})
		next_tag=len(response.selector.xpath('//td[contains(@class,"pager")]/a[contains(@onclick,"QueryAction.GoPage")]').extract())
		if next_tag!=0:
			url='http://www.landchina.com/default.aspx?tabid=264'
			sum_query=response.meta['data']
			page=int(response.meta['page'])+1
			param={'__VIEWSTATE':'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FgJmD2QWAmYPZBYCAgEPZBYCZg8WBB8BBSdDT0xPUjojRDNEM0QzO0JBQ0tHUk9VTkQtQ09MT1I6IzMzNjZmZjsfAmgWAmYPZBYCAgEPZBYCZg8PFgIfA2VkZAIDD2QWAgIDDxYEHglpbm5lcmh0bWwFgwc8cCBhbGlnbj0iY2VudGVyIj48c3BhbiBzdHlsZT0iZm9udC1zaXplOiB4LXNtYWxsIj4mbmJzcDs8YnIgLz4NCiZuYnNwOzxhIHRhcmdldD0iX3NlbGYiIGhyZWY9Imh0dHA6Ly93d3cubGFuZGNoaW5hLmNvbS8iPjxpbWcgYm9yZGVyPSIwIiBhbHQ9IiIgd2lkdGg9IjI2MCIgaGVpZ2h0PSI2MSIgc3JjPSIvVXNlci9kZWZhdWx0L1VwbG9hZC9mY2svaW1hZ2UvdGRzY3dfbG9nZS5wbmciIC8+PC9hPiZuYnNwOzxiciAvPg0KJm5ic3A7PHNwYW4gc3R5bGU9ImNvbG9yOiAjZmZmZmZmIj5Db3B5cmlnaHQgMjAwOC0yMDE0IERSQ25ldC4gQWxsIFJpZ2h0cyBSZXNlcnZlZCZuYnNwOyZuYnNwOyZuYnNwOyA8c2NyaXB0IHR5cGU9InRleHQvamF2YXNjcmlwdCI+DQp2YXIgX2JkaG1Qcm90b2NvbCA9ICgoImh0dHBzOiIgPT0gZG9jdW1lbnQubG9jYXRpb24ucHJvdG9jb2wpID8gIiBodHRwczovLyIgOiAiIGh0dHA6Ly8iKTsNCmRvY3VtZW50LndyaXRlKHVuZXNjYXBlKCIlM0NzY3JpcHQgc3JjPSciICsgX2JkaG1Qcm90b2NvbCArICJobS5iYWlkdS5jb20vaC5qcyUzRjgzODUzODU5YzcyNDdjNWIwM2I1Mjc4OTQ2MjJkM2ZhJyB0eXBlPSd0ZXh0L2phdmFzY3JpcHQnJTNFJTNDL3NjcmlwdCUzRSIpKTsNCjwvc2NyaXB0PiZuYnNwOzxiciAvPg0K54mI5p2D5omA5pyJJm5ic3A7IOS4reWbveWcn+WcsOW4guWcuue9kSZuYnNwOyZuYnNwO+aKgOacr+aUr+aMgTrmtZnmsZ/oh7vlloTnp5HmioDogqHku73mnInpmZDlhazlj7gmbmJzcDvkupHlnLDnvZE8YnIgLz4NCuWkh+ahiOWPtzog5LqsSUNQ5aSHMDkwNzQ5OTLlj7cg5Lqs5YWs572R5a6J5aSHMTEwMTAyMDAwNjY2KDIpJm5ic3A7PGJyIC8+DQo8L3NwYW4+Jm5ic3A7Jm5ic3A7Jm5ic3A7PGJyIC8+DQombmJzcDs8L3NwYW4+PC9wPh8BBWRCQUNLR1JPVU5ELUlNQUdFOnVybChodHRwOi8vd3d3LmxhbmRjaGluYS5jb20vVXNlci9kZWZhdWx0L1VwbG9hZC9zeXNGcmFtZUltZy94X3Rkc2N3MjAxM195d18xLmpwZyk7ZGR8R2Hf96YNnf6j1YMeSz+J5BPeYgyae/XkhbQJa7VIXQ==',
				'__EVENTVALIDATION':'/wEWAgLV6oKLBALN3cj/BO464ABoybQPHOdzQf2ngEaxl8Vo30d+g02QfNizQ7Ge',
				'hidComName':'default',
				'mainModuleContainer_492_1114_495_TabMenu1_selected_index':'1',
				'top1_QuerySubmitConditionData':'',
				'top1_QuerySubmitOrderData':'',
				'top1_RowButtonActionControl':'',
				'top1_QuerySubmitPagerData':'1',
				'top1_QuerySubmitSortData':'',
				'top2_QueryConditionItem': '8ede234a-9e5a-4bef-8d51-8157dceb471c',
				'top2_QuerySubmitConditionData':sum_query,
				'top2_QuerySubmitOrderData':'',
				'top2_RowButtonActionControl':'',
				'top2_QuerySubmitPagerData':str(page),
				'top2_QuerySubmitSortData':'',
				'top3_QuerySubmitConditionData':'',
				'top3_QuerySubmitOrderData':'',
				'top3_RowButtonActionControl':'',
				'top3_QuerySubmitPagerData':'1',
				'top3_QuerySubmitSortData':''}
			yield scrapy.FormRequest(url,formdata=param,cookies=cookies_query,callback=self.parse_info,meta={'data':sum_query,'page':str(page),'cookie':cookies_query,'district_1':fast_dict.get('district_1')})

		
	def parse_detail_Info(self,response):
		item=response.meta['item']
		item['detail_flag']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f11_r8_c2_ctrl')]/text()").extract()		
		item['detail_num']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f11_r8_c4_ctrl')]/text()").extract()
		item['detail_location']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f11_r3_c2_ctrl')]/text()").extract()
		item['detail_usenumber']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f11_r4_c2_ctrl')]/text()").extract()
		item['detail_area']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f11_r4_c6_ctrl')]/text()").extract()
		item['detail_use']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f11_r1_c2_ctrl')]/text()").extract()
		item['detail_level']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f11_r1_c6_ctrl')]/text()").extract()
		item['detail_status']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f11_r5_c2_ctrl')]/text()").extract()
		item['detail_years']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f11_r5_c6_ctrl')]/text()").extract()
		item['detail_date']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f11_r6_c2_ctrl')]/text()").extract()
		item['detail_date2']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f11_r6_c6_ctrl')]/text()").extract()
		item['detail_price']=response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f11_r7_c2_ctrl')]/text()").extract()
		yield item


		
			
			
			  
		
			

			
