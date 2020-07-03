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








