#-*- coding: UTF-8 -*-
#!/usr/bin/env python

import csv
import time
import requests
img_url = 0

def take_1000_posts():
    token = 'c3d08a34c3d08a34c3d08a34adc3a590eccc3d0c3d08a349c6c571a02e92dde004d5a46'
    version = 5.126
    domain = 'ecologynsk'
    count = 100 #количество записей
    #сдвиг на следующие 'count' постов
    all_posts = []
    for of in range(1000):
        response = requests.get('https://api.vk.com/method/wall.get',
                               params={
                                   'access_token': token,
                                   'v': version,
                                   'domain': domain,
                                   'count': count,
                                   'offset': of
                                }
                                )
        data = response.json()['response']['items']
        all_posts.extend(data)
        time.sleep(0.5)
    return all_posts

def file_writer(data):
    with open('ecologynsk.csv', 'w') as file:
        a_pen = csv.writer(file)   #переменная, записывающая данные в файл
        a_pen.writerow(('likes','body','url'))
        for post in data:
            try:
                if posts ['attachments'][0]['type']:
                    img_url = post['attachments'][0]['photo']['sizes'][-1]['url']
                else:
                    img_url = 'pass'
            except Exception as e:
                print(e)
            
        a_pen.writerow((post['likes']['count'], post['text'], img_url))

if  __name__ =='__main__':
    file_writer(take_1000_posts())

