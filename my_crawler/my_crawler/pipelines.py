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
            'USER-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Cookie': 'b963ef2d97e050aaf90fd5fab8e78633',
            # 需要查看图片的cookie信息，否则下载的图片无法查看
        }

        folder_name = '{}'.format(item['title'])
        folder_name = folder_name.strip()
        folder_name = folder_name.strip(">>")
        folder_name = folder_name.rstrip("\\")

        for img_url, name in zip(item['src'], item['alt']):
            dir_path = '{}//{}'.format(IMAGES_STORE, folder_name)
            if not os.path.exists(dir_path) and len(item['src']) != 0:
                os.makedirs(dir_path)
            download_url = "{}/{}".format(self.base_site, img_url)

            with open('{}//{}.jpg'.format(dir_path, name), 'wb') as f:
                req = requests.get(download_url, headers=header)
                f.write(req.content)


        return item
