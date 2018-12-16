# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests
from my_crawler.settings import IMAGES_STORE


class MyCrawlerPipeline(object):
    # 主站连接 用来拼接url
    base_site = "http://www.ccguitar.cn/"

    def process_item(self, item, spider):
        header = {
            'USER-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/58.0.3029.110 Safari/537.36',
            'Cookie': 'b963ef2d97e050aaf90fd5fab8e78633',
            # 需要查看图片的cookie信息，否则下载的图片无法查看
        }

        folder_name = f"{item['title']}"
        folder_name = folder_name.strip().strip(">>").rstrip("\\")

        for img_url, name in zip(item['src'], item['alt']):
            dir_path = f"{IMAGES_STORE}//{folder_name}"
            if not os.path.exists(dir_path) and not item['src']:
                try:
                    os.makedirs(dir_path)
                except OSError:
                    print(f"{dir_path}already exists! make it fail!")

            download_url = f"{self.base_site}/{img_url}"
            with open(f"{dir_path}//{name}.jpg", 'wb') as f:
                try:
                    req = requests.get(download_url, headers=header)
                except:
                    print(f"requests.get {name} fail!!")
                f.write(req.content)

        return item
