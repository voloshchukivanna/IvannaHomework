#Task2

#4слайд
f = open('lalala.txt')
x = f.read()
print(x)

'''или так'''

with open('lalala.txt') as f:
    f.read()

#8слайд
f = open('lalala.txt')
for line in f:
    print(line.rstrip()+"!")

#9слайд
with open('lalala.txt') as f, open("lalala3.txt", "a") as f1:
    for i, line in enumerate(f, start = 1):
'''как мне опустить это number к каждой строке, а не записывать в новой?'''
        f1.write('number: %d' % (i) + '\n')
        print(line.rstrip()+"!", file=f1)

#10слайд
'''что-то беда какая-то с этим решением'''

f = open('Task3.txt')
f1 = open("Task4.txt", "w")

try:
    for line in f:
        print(int(line), file=f1)
        raise TypeError()
else:
    print("I did it!")
finally:
    print("Closing files!")
    f.close()
    f1.close()


#Task3
f = open('Task3.txt', 'r')
text = re.sub('[^A-Za-z0-9 ]+','',f.read()).split()
f.close()
textset = sorted(list(set(text)))
f = open('Task6.txt','w')
for x in textset:
    f.write(x+' '+str(text.count(x))+'\n')
f.close()


#Task4
import smtplib, ssl
port = 465
smtp_server = "smtp.gmail.com"
sender_email = "voloshchuk.ivanna@gmail.com"
receiver_email = "el.piankova@gmail.com"
password = input("Password: ")
message = "I did it!"
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)


#Task1
#1
 import requests
 import _json

 url='http://pulse-rest-testing.herokuapp.com/'
 r = requests.get(url)
 print(r.status_code)

'''создали книгу'''
 book_dict = {
       'title': "test book 2",
       'author': "Ivanna Voloshchuk"
   }
 resp = requests.post(url+'books/', data=book_dict)
 print(resp.status_code)
 req_dict = resp.json()
 for book in req_dict:
     print(req_dict['id'], req_dict['title'])
 book_id=req_dict['id']

 print(req_dict)

'''редактируем книгу'''
 r = requests.get(url)
 print(r.status_code)
 book_dict = {

     'title': 'test book 2 change',
     'author': 'Ivanna Voloshchuk'
     }
 resp = requests.put(url+'books/'+ str(book_id), data=book_dict)
 print(resp.status_code)
 req_dict = resp.json()
 for book in req_dict:
     print(req_dict['id'], req_dict['title'])

 print(req_dict)

'''удаляем книгу'''
del_book = request.delete(url + 'books/' + str(book_id))






