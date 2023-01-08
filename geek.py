# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os

url = "https://itawenya.cn"


# 获取网页资源
r = requests.get(url)


# 解析
soup = BeautifulSoup(r.text, 'html.parser')
texts = soup.get_text()

photo_urls = soup.find_all('img')


# 保存
# 文本
textf = open("geek.text", "w", encoding='utf8')
# for text in texts:
textf.write(texts)

textf.close()


# 图片
os.makedirs('./img/', exist_ok=True)
for photo_url in photo_urls:
    img = "https://itawenya.cn" + photo_url['src']
    q = requests.get(img, stream=True)
    image_name = img.split('/')[-1]
    with open('./img/%s' % image_name, 'wb') as f:
        f.write(q.content)
        f.flush()


# requests.adapters.DEFAULT_RETRIES = 5
# s = requests.session()
# s.keep_alive = False
# q = s.get(img)
# image_name = img.split('/')[-1]
# with open('./img/%s' % image_name, 'wb') as f:
#     f.write(q.content)


#photo = open("geek.photo", "wb")
# photo.write(photo_urls)

# photo.close()


# for photo_url in photo_urls:
#     img = photo_url['src']
#     q = requests.get(img, stream=True)
#     image_name = img.split('/')[-1]
#     with open('./img/%s' % image_name, 'wb') as f:
#         for chunk in q.iter_content(chunk_size=128):
#             f.write(chunk)
#             f.flush()
