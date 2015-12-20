# -*- coding: utf-8 -*-
import scrapy
import datetime
from sb6141_timeout.items import SB6141TimeoutItem


class Sb6141Spider(scrapy.Spider):
    name = "sb6141"
    allowed_domains = ["192.168.100.1"]
    start_urls = (
        'http://192.168.100.1/cmLogsData.htm',
    )

    def parse(self, response):
        rows = response.selector.xpath('//html/body/center/table/tbody/tr')
        for row in rows[1:]:
            date = row.xpath('td[1]/text()').extract()[0]
            message = row.xpath('td[4]/text()').extract()[0]
            #if u'T4 time out' not in message:
            #    continue
            item = SB6141TimeoutItem()
            item['date'] = self.parse_date(date)
            item['message'] = message
            yield item

    def parse_date(self, datestring):
        #'Dec 14 2015 08:01:33'
        format = '%b %d %Y %H:%M:%S'
        d = datetime.datetime.strptime(datestring, format)
        return d
