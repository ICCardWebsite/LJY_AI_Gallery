# coding:utf-8
from PIL import Image
import sys
import os
import json

imgs = []
res = {
    "photos":{
        "photo":[]
    }
}

imgnames = os.listdir("images")
for imgname in imgnames:
    if os.path.isfile("images/"+imgname):
        img = Image.open("images/"+imgname)
        imgSize = img.size  #大小/尺寸
        w = img.width       #图片的宽
        h = img.height      #图片的高
        f = img.format      #图像格式
        item = (imgname,w,h)
        imgs.append(item)


for info in imgs:
    item = {
        "title":info[0],
        "url_sq":"./images/thumbnails/%s"%info[0],
        "width_sq":100,
        "height_sq":100,
        "url_l":"./images/%s"%info[0],
        "width_l":info[1],
        "height_l":info[2]
    }
    res["photos"]["photo"].append(item)

fp = open("img_list.json","w")
json.dump(res,fp)
fp.close()