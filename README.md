# Fire TV Sreensaver Scraper
The Fire TV streaming device has a screensaver mode that showcases many beautiful images. Amazon has made these images available for download [here](https://amazonfiretv.blog/all-182-screensavers-on-your-amazon-fire-tv-and-their-locations-photos-71e9f756067f). Unfortunately, there is no mass download link, and it would be extremely cumbersome to download all 182 images individually. This repo contains a simple python script that will scrape the webpage and save all 182 images to your current working directory.

I use these images as backgrounds for my project [Flex Launcher](https://github.com/complexlogic/flex-launcher).

## Usage
The script depends on the modules Beautiful Soup and Requests. Make sure you have them installed.
```
pip3 install beautifulsoup4 requests
```

Then, simply run the script from the python interpreter:
```
python scraper.py
```

## Improving Contrast For Background Use
Many of the images in the set are quite bright, which results in poor contrast and readability when images and text are drawn over top. I use the excellent utility [ImageMagick](https://github.com/ImageMagick/ImageMagick) to improve the contast by darkening the images and applying a slight gaussian blur. The images can be mass converted using a Bash script, such as the following:

```
#!/bin/bash
OUTPUT_DIR=./backgrounds
OUTPUT_RESOLUTION=1920x1080
mkdir -p "$OUTPUT_DIR"
for file in *.jpg; do echo "Converting $file"; convert "$file" -fill black -colorize 60% -blur 0x1.5 -resize $OUTPUT_RESOLUTION  "$OUTPUT_DIR/$(basename $file)"; done
```