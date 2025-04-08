import scrapy
import random
import time
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError, TimeoutError

from calscapescraper.items import CalscapescraperItem

class CalscapeSpider(scrapy.Spider):
    name = "calscape"
    allowed_domains = ["calscape.org"]
    start_urls = ["https://calscape.org/california-nurseries"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                headers={"User-Agent": self.get_random_user_agent()},
                dont_filter=True
            )


    def parse(self, response):
        nursery_cards = response.css('div.result-warp')
        for card in nursery_cards:
            item = CalscapescraperItem()

            item["name"] = card.css("h3 a::text").get(default="").strip()
            item["adress"] = card.css("div.address::text").get(default="").strip()
            item["phone"] = card.css("div.phone::text").get(default="").strip()
            item["mail"] = card.css("div.email::text").get(default="").strip()
            item["website_url"] = card.css("div.url a::attr(href)").get(default="").strip()

            inventory_link = card.css("div.reserve-btn a::attr(href)").get()
            if inventory_link:
                url = response.urljoin(inventory_link)
                yield scrapy.Request(
                    url=url,
                    callback=self.parse_inventory,
                    meta={"item": item},
                    headers={"User-Agent": self.get_random_user_agent()}
                )
            else:
                yield item


    def parse_inventory(self, response):
        item = response.meta["item"]
        flower_names = set()

        plant_items = response.css("div.plants-list__item")
        for plant in plant_items:
            name = plant.css(".plants-list__title div::text").get()
            if not name:
                name = plant.css(".plants-list__title span::text").get()
            if name:
                flower_names.add(name.strip())

        item["inventory"] = list(flower_names) if flower_names else None
        return item
    

    def get_random_user_agent(self):
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
            "(KHTML, like Gecko) Version/16.0 Safari/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0",
        ]
        return random.choice(user_agents)