import requests
import dilbert
import datetime
response = requests.get(dilbert.dilbert_from_date(datetime.datetime.now()))
dilbertimg = Image.open(io.BytesIO(response.content))
dilbertimg.show()