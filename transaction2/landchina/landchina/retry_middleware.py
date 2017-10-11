# -*- coding: utf-8 -*-
import time
from scrapy import log
import requests
from scrapy.downloadermiddlewares.retry import RetryMiddleware
import pdb
class LocalRetryMiddleware(RetryMiddleware):

    def process_response(self, request, response, spider):
        if request.meta.get('dont_retry', False):
            return response

        if response.status in [500]:
            log.msg("反爬机制可能更新了",level=log.INFO)
        if response.status in [200]:
            # reason = response_status_message(response.status)
            # return self._retry(request, reason, spider) or response
            safe_dog = response.selector.xpath('//script').re(r'.*WebShield(.*)".*')
            log.msg(safe_dog, level=log.INFO)
            if len(safe_dog) > 0:
                #pdb.set_trace()
                click_url = request.url + '&WebShield' + safe_dog[0]
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
                r = requests.get(click_url, cookies={'safedog-flow-item': ''},headers=headers)
                time.sleep(5)
                return self._retry(request, "safe_dog:retry", spider) or response
            tag = response.selector.xpath("//a[contains(@herf,'http://www.safedog.cn/?from=sitedog')]/text()")
            if len(tag) != 0:
                log.msg("安全狗冻结中,稍等自动开始", level=log.INFO)
                time.sleep(360)
                return self._retry(request, "safe_dog:retry", spider) or response
            return response