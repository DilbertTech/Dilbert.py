import requests
import time
from bs4 import BeautifulSoup
import io
import datetime
import urllib
from PIL import Image
from randomtimestamp import randomtimestamp

def dilbert_from_date(dateToFetch):
    formatted_date = '{0}-{1}-{2}'.format(dateToFetch.year, dateToFetch.month, dateToFetch.day)
    todays_page = 'http://dilbert.com/strip/{0}/'.format(formatted_date)
    response = requests.get(todays_page)
    dilbert_page_source = BeautifulSoup(response.text, 'html.parser')
    link = dilbert_page_source.find("img", class_='img-comic')['src']
    return "https:" + str(link)

def dilbert_days_ago(fromDaysAgo):
	return dilbert_from_date(datetime.datetime.now() - datetime.timedelta(days=fromDaysAgo))

def dilbert_random():
	return dilbert_from_date(randomtimestamp(1990, False))