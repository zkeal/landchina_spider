import scrapy
class landchina(scrapy.Spider):
	name="landchina"
	allowed_domains = ["landchina.com"]
	start_urls = ["http://www.landchina.com/default.aspx?tabid=263"]
	
	def parse(self,response):
		filename = response.url.split("/")
		with open(filename,'wb') as f:
			f.write(reponse.body)
