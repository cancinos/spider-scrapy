# -*- coding: utf-8 -*-
import scrapy


class WikipediaSpider(scrapy.Spider):
    name = 'wikipedia'
    start_urls = ['https://en.wikipedia.org/wiki/Wikipedia:Featured_articles']
      
    def parse(self, response):
        links = response.css('span.featured_article_metadata.has_been_on_main_page a::attr(href)').getall()
        yield from response.follow_all(links, self.parse_article)

    def parse_article(self, response):
        articles = response.css('#firstHeading::text').get(default='').strip()
        first_paragraph = response.xpath('//p').extract()[1]

        yield { 
            'link': response.request.url,
            'body': {
                'title': articles,
                'first_paragraph': first_paragraph
            }
        }



