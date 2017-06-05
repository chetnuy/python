import vk, time, os,sys
session = vk.AuthSession('6062005', '+79164622650', '', scope='messages, wall, friends')
vk_api = vk.API(session)
#print(vk_api.users.get(user_id=1))
#vk_api.wall.post(message="hello")
#vk.api.messages.send(user id=0, messages="hello")
#vk_api.messages.send(users_id="364230799", messages="hello")
#print(vk_api.messages.get())
vk_api.friends.add(user_id="429784217")
#print(vk_api.account.getProfileInfo())
#Отправить сообщение
#vk_api.messages.send(user_id='364230799', message="heee1")
#time.sleep(10)

#vk_api.wall.post(owner_id='-34985835', message='Друзья, добавляйтесь)')
akk = vk_api.newsfeed.get(filters='friend')
import pickle

output = open('output.txt', 'wb')


pickle.dump(akk, output)
output.close()