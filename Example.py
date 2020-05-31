import requests
response = requests.get(dilbert(5))
dilbert = Image.open(io.BytesIO(response.content))
dilbert.show()