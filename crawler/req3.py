import requests
from io import BytesIO,StringIO
from PIL import Image
image_url='http://imglf1.ph.126.net/pWRxzh6FRrG2qVL3JBvrDg==/6630172763234505196.png'
response=requests.get(image_url)
f=BytesIO(response.content)
img=Image.open(f)
print(img.size)
