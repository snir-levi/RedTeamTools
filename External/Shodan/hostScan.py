import shodan

SHODAN_API_KEY = ""

api = shodan.Shodan(SHODAN_API_KEY)

# Lookup the host

file = open('16-31.txt','r')

for ip in file:
	fileDeadIP = open('deadIPs.txt','w')
	try:
		host = api.host(ip)

		# Print general info
		print("""
			IP: {}
			Organization: {}
			Operating System: {}
		""".format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

		# Print all banners
		for item in host['data']:
			print("""
			        Port: {}
			        Banner: {}

			""".format(item['port'], item['data']))
	except:
		fileDeadIP.write("\n host "+ip + "failed")
		fileDeadIP.close()
