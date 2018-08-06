import threading
import json, os
from PIL import Image

def readConfig():
    with open('config.json') as config_object:
        contents = config_object.read()
        return json.loads(contents)

def start():
    config = readConfig()
    t1 = threading.Thread(target=create_image,args=(config['imageSize'],))
    t1.start()
    t1.join()
    # t2 = threading.Thread(target=create_multi_image,args=(range(1,100),))
    # t2.start()
    # t2.join()

def create_image(size):
  im = Image.new('RGB', (size,size), '#000000')
  im.save('./dist/image-%d*%d.tiff' %(size,size))

def create_multi_image(sizeArr):
  for size in sizeArr:
    im = Image.new('RGB', (size,size), '#000000')
    im.save('./dist/image-%d*%d.tiff' %(size,size))
    
if __name__ == "__main__":
    start()

