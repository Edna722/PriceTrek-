from celery import Celery
import os

# Initialize Celery
app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def run_scraper():
    """Runs the Scrapy spider to scrape Amazon data."""
    os.system("scrapy crawl amazon")
