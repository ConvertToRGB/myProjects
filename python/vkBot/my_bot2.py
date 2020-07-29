# coding: utf-8

import time
import vk_api
vk = vk_api.VkApi(login = '79680944597', password = 'jkhds548884hdhdshdsNn')
#vk_api.VkApi(token = 'a02d...e83fd') #Авторизоваться как сообщество
vk.auth()

user_id = 219604409
my_user_id = u'422193859'

values = {'out': 0,'count': 100,'time_offset': 60}

def write_msg(user_id, s):
    vk.method('messages.send', {'user_id':user_id,'message':s})

count = 101
while True:
    response = vk.method('messages.get', values)
    if response['items']:
        values['last_message_id'] = response['items'][0]['id']
    for item in response['items']:
            write_msg(item[u'user_id'],u'Print this [{0}]'.format(count))
            count += 1
    time.sleep(1)