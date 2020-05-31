import requests
import Dilbert
import datetime
from PIL import Image
import io
response = requests.get(Dilbert.dilbert_from_date(datetime.datetime.now()))
dilbertimg = Image.open(io.BytesIO(response.content))
dilbertimg.show()