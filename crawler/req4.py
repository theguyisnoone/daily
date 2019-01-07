import requests

response=requests.get('https://tieba.baidu.com/p/6000332972')

a=response.content.decode()

input=open('b.txt','w')

for i in a:
    input.write(i)

input.close()

print('over')


