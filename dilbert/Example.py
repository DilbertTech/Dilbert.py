import requests
import Dilbert
import datetime
from PIL import Image
import io
import random

#Fetches and shows today's Dilbert
response = requests.get(Dilbert.dilbert_from_date(datetime.datetime.now()))
dilbertimg = Image.open(io.BytesIO(response.content))
dilbertimg.show()

#Fectches and shows Dilbert from 365 days ago
response = requests.get(Dilbert.dilbert_days_ago(365))
dilbertimg = Image.open(io.BytesIO(response.content))
dilbertimg.show()

#Fetches and shows a random Dilbert 
response = requests.get(Dilbert.dilbert_random())
dilbertimg = Image.open(io.BytesIO(response.content))
dilbertimg.show()