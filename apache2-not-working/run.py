#running sh file for permissions
import os

os.popen('sh permi.sh')



#/opt/lampp/etc/httpd.conf

f1 = open("/opt/lampp/etc/httpd.conf", "rt")
data = f1.read()
data = data.replace('Listen 80', 'Listen 8000')
f1.close()

f1 = open("/opt/lampp/etc/httpd.conf", "wt")
f1.write(data)
f1.close()

#opt/lampp/etc/extra/httpd-ssl.conf

f2 = open("/opt/lampp/etc/extra/httpd-ssl.conf", "rt")
data2 = f2.read()
data2 = data2.replace('Listen 443', 'Listen 4431')
f2.close()

f2 = open("/opt/lampp/etc/extra/httpd-ssl.conf", "wt")
f2.write(data2)
f2.close()



#/opt/lampp/lampp

f3 = open("/opt/lampp/lampp", "rt")
data3 = f3.read()
data3 = data3.replace('testport 80', 'testport 8000')
f3.close()

f3 = open("/opt/lampp/lampp", "wt")
f3.write(data3)

