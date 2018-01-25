# -*- coding: utf-8 -*-
import time
from scrapy import log
import requests
from scrapy.downloadermiddlewares.retry import RetryMiddleware
import pdb
class LocalRetryMiddleware(RetryMiddleware):

    def process_response(self, request, response, spider):
        retries = request.meta.get('retry_times', 0) + 1

        if request.meta.get('dont_retry', False):
            return response

        if response.status in [500]:
            log.msg("反爬机制可能更新了",level=log.INFO)
        if response.status in [200]:
            safe_dog = response.selector.xpath('//script').re(r'.*WebShield(.*)".*')
            log.msg(safe_dog, level=log.INFO)
            ret_code=0
            if len(safe_dog) > 0:
                click_url = request.url + '&WebShield' + safe_dog[0]
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
                try:
                    r = requests.get(click_url, cookies={'safedog-flow-item': ''},headers=headers,timeout=10)
                    time.sleep(5)
                except:
                    return self._retry(request,"safe_dog:retry", spider)
                return self._retry(request,"safe_dog:retry", spider) or response
            tag = response.selector.xpath("//a[contains(@herf,'http://www.safedog.cn/?from=sitedog')]/text()")
            if len(tag) != 0:
                log.msg("安全狗冻结中,稍等自动开始", level=log.INFO)
                time.sleep(360)
                return self._retry(request,"safe_dog:retry",spider) or response
            if (request.url.find("tabid=386")):
                tag1 = response.selector.xpath("//span[contains(@id,'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r1_c2_ctrl')]/text()").extract()
                if(len(tag1)==0):
                    return self._retry(request, "block_white:retry", spider) or response
            return response

        if retries > 3:
            log.msg("sleeping for network", level=log.INFO)
            time.sleep(3600)
            return self._retry(request, "safe_dog:retry", spider) or response