import threading
import sys

from PIL import Image, ImageDraw, ImageFont

image_size = 300

def start():
    t = threading.Thread(target=create_image,args=(image_size,))
    t.start()

def create_image(size):
    pri_image = Image.open("./ori-pic.jpg")
    pri_image.resize((size,size)).save('./dist/create-%d.jpg' % size)
    
    font = ImageFont.truetype('./SourceHanSansCN-Medium.otf', 50)
    drawImage = ImageDraw.Draw(pri_image)
    drawImage.text((10,10),"hello,一二三四五六七八九十",font=font)
    pri_image.save('./dist/add-font.jpg')
    
if __name__ == "__main__":
    start()

