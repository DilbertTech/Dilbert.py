import requests
from dilbert import *
import datetime
response = requests.get(dilbert_from_date(datetime.datetime.now()))
dilbertimg = Image.open(io.BytesIO(response.content))
dilbertimg.show()