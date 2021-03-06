
import re
import chardet
import urllib.request
import os
import requests
import random
import time
import tkinter.messagebox
#创建文件夹，作者电脑是’'C:/Users/99239/Desktop/pixivimg'‘，具体图片存放位置自己改下
if not os.path.exists('C:/Users/99239/Desktop/pixivimg'):
    os.mkdir('C:/Users/99239/Desktop/pixivimg')
headers = {
'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
'Referer' : 'https://www.pixiv.net/ranking.php'
}
def open_url(url):
    #读取找到图片的地址
    req = urllib.request.Request(url,headers=headers)
    next = urllib.request.urlopen(req).read()
    ecd = chardet.detect(next)
    #自动解析编码 auto mode --> html = next.decode(ecd['encoding'])
    html = next.decode('utf-8')
    find_img(html)

def find_img(html):
    #正则找到原图（大图）地址
    a = re.findall('"original":"(.+\.[pj][pn]g)"', html)
    i = '(' + a[0].split('"')[0].split('/')[-1].split('_')[0] + ')'
    _name = re.findall('"illustTitle":"(.+?)"',html)
    name =''
    for each in _name:
        name+=each
    img = a[0].split('"')[0]
    #储存图片
    filename = ''.join(['C:/Users/99239/Desktop/pixivimg/',i,name,img[-4:]])
    last = requests.get(img,headers=headers)
    with open(filename,'wb') as f:
        f.write(last.content)

def rank_page():
    url = 'https://www.pixiv.net/ranking.php' #pixiv 每日排行榜网址
    a = requests.get(url,headers=headers)
    get = re.findall('artworks/\d+', a.text)

    x = int(input('输入你想下载图片的数量'))
    while x > 0:
        num = random.randint(1, len(get))
        url = 'https://www.pixiv.net/artworks/'+get[num].split('/')[1]
        print(url)
        open_url(url)
        x -= 1

if __name__ == '__main__':
    print("此程序需要梯子使用！！！")
    rank_page()
