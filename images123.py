#!/usr/bin/env python3
import re
from PIL import Image
import os,sys
log = sys.argv[1]
for files in os.listdir(log):
          root,ext = os.path.splitext(files)
          if root.startswith('ic'):
             imgjpg="/home/knambiar41/Documents/images/"+files
             img = Image.open(imgjpg).convert('RGB')
             out1 = img.resize((128,128))
             out2 = out1.rotate(90)
             out2.save("/home/knambiar41/Documents/icons/opt/"+files+".jpg")
       
       
             