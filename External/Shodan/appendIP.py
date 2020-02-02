
file = open('IPs.txt','a')

ip = '199.190.'

for i in range(16,32):
	for j in range(1,255):
		file.write(ip+str(i)+'.'+str(j)+'\n')

file.close()
