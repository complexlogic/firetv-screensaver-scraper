from bs4 import BeautifulSoup
import requests
import os

# Scrape image URLs from web page
urls= []
print("Connecting...")
response = requests.get("https://amazonfiretv.blog/all-182-screensavers-on-your-amazon-fire-tv-and-their-locations-photos-71e9f756067f")
print("Parsing web page...")
soup = BeautifulSoup(response.text, 'html.parser')
for link in soup.find_all('img'):
    image=link.get('src')
    if image is not None and image.startswith("https://miro.medium.com/max/") and "?" not in image and ".png" not in image:
        urls.append("https://miro.medium.com/max/2400/" + os.path.basename(image))

# Download files
i = 1
for url in urls:
    print(f"Downloading image {i}")
    fileout = str(i) + ".jpg"
    response = requests.get(url)
    if response.status_code == 200:
        open(fileout, "wb").write(response.content)
    i += 1
