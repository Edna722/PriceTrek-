import scrapy

class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.com"]
    start_urls =  ["https://www.amazon.com/s?k=home+decor"]

    def parse(self, response):
        for product in response.css('div.s-main-slot div .s-result-item'):
            item =  {
                'name': product.css('span.a-text-normal::text').get(),
                'price': product.css('span. a-price-whole::text').get(),
                'image_url': product.css('img.s-image::attr(src)').get(),
                'product-url': response.urljoin(product.css('a.a-link-normal::attr(href)').get()),
                'rating': product.css('span.a-icon-alt::text').get(),
                'reviews':product.css('span.s-review-count::text').get()

            }
            save_product(item)

import random
from sqlalchemy.orm import sessionmaker

PROXIES = [
    "http://username:password@proxy1.com:8000"
    "http://username:password@proxy2.com:8000"
]
def start_requests(self):
    for url in self.start_urls:
        yield scrapy.Request(url, headers={"User-Agent": USER_AGENT}, meta={"proxy": random.choice(PROXIES)})

from sqlalchemy import create_engine, Column, String, Float, Integer, Base
from sqlalchemy.orm import sessionmaker

# Connect to the DB
engine = create_engine("postgresql://scraper:password@localhost/amazon_prices")
Session = sessionmaker(bind = engine)
session = Session()

# Define the table
class Product(Base):
    __tablename__= 'products'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    price = Column(Float)
    image_url = Column(String)
    product_url = Column(String)
    rating = Column(String)
    reviews = Column(String)

Base.metadata.create_all(engine)

def save_product(data):
    product = Product(**data)
    session.add(product)
    session.commit()
