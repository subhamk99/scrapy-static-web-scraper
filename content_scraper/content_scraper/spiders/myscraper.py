import scrapy
from content_scraper.items import UserItem


class MyscraperPySpider(scrapy.Spider):
    name = 'myscraper.py'
    allowed_domains = ['medium.com']
    start_urls = ['https://medium.com/search/users?q=reactJS%2C%20Django/']

    def parse(self, response):
        user = UserItem()
        user['userId'] = response.xpath('//span/@data-user-id').getall()
        user['profileLink'] = response.xpath('//h3/a[@class="link link--primary u-accentColor--hoverTextNormal"]/@href').getall()
        user['userName'] = response.xpath('//h3/a[@class="link link--primary u-accentColor--hoverTextNormal"]/text()').getall()
        user['userSkills']= response.xpath('//p[@class="ui-body u-fontSize14 u-lineHeightBaseSans u-textColorDark u-marginBottom4"]/text()').getall()
        return user
