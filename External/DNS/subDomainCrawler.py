##Sub Domain Crawler by Snir Levi##
'''
Description: The script checks for any subdomains present in HTML file of given domain. For each subdomain the script crawls recursivly to find more subdomains.
Results output file: finaldomains.txt

Usage: python subDomainCrawler.py <domain>

Example: python subDomainCrawler.py www.google.com
'''

import urllib2
import sys,os
import ssl


def printUsage():
	print "Usage: python subDomainCrawler.py <domain>"

def checkHTTP():
	global domain
	global fullDomain
	if (domain[0:7]) == "http://":
		fullDomain = domain
		domain = domain[7:]
		return
	if (domain[0:8]) == "https://":
		fullDomain = domain
                domain = domain[8:]
		return
	fullDomain = setHTTP(domain)
def setHTTP(domain):
	return "http://"+domain

def getHtml(url):
	print "Scanning for Sub Domains: " + url
	ssl._create_default_https_context = ssl._create_unverified_context
	html = urllib2.urlopen(url).read()
	file = open('index.html','w')
	file.write(html)
	file.close()
	print "Done " + url

def getSubDomains(domain,subDomains):
	os.system("grep -o '[A-Za-z0-9_\.-]*\.*'"+ domain + " index.html | sort -u > domains.txt")
	subDomains = syncSubDomains(subDomains)
	return subDomains

def syncSubDomains(subDomains):
	global domain
	listFile = open('domains.txt','r')
        for dom in listFile:
		if dom.strip('\n') not in subDomains and dom.strip('\n') != domain:
			subDomains.append(dom.strip('\n'))
	return subDomains

def recursiveSubDomains(subDomains):
	newSubDomains = []
	for domain in subDomains:
		domain = setHTTP(domain)
		getHtml(domain)
		subDomains = getSubDomains(domain,subDomains)
	return subDomains

def writeSubDomainsToFile(subDomains):
	file = open('finaldomains.txt','w')
	for domain in subDomains:
		file.write(domain+'\n')
	file.close()

if len(sys.argv) < 2:
	printUsage()
	exit()

domain = sys.argv[1]
fullDomain = ''
subDomains = []
os.system('touch domains.txt')
checkHTTP()
getHtml(fullDomain)
subDomains = getSubDomains(domain,subDomains)
subDomains = recursiveSubDomains(subDomains)
print subDomains
writeSubDomainsToFile(subDomains)
