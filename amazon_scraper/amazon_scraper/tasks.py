from celery import Celery
import os

# Initialize Celery
app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def run_scraper():
    """Runs the Scrapy spider to scrape Amazon data."""
    os.system("scrapy crawl amazon")

from celery.schedules import crontab

app.conf.beat_schedule = {
    'scrape_amazon_every_4_hours': {
        'task': 'tasks.run_scraper',
        'schedule': crontab(minute=0, hour='*/4'),  # Runs every 4 hours
    },
}
