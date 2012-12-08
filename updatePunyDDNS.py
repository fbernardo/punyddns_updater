import requests
import sys
import re
import xml.etree.ElementTree as ET

domain = "<your Puny DDNS address>"
record_type = "A"
username = "<your SAPO login>"
password = "<your SAPO password>"

UpdateIPServiceURL = "https://services.sapo.pt/PunyUrl/DNS/UpdateDNs?domain={0}&ip={1}&record_type={2}&ESBUsername={3}&ESBPassword={4}"

def main(argv=None):
	# get ip address
	r = requests.get("http://myip.dnsdynamic.org")

	# error checking
	if r.status_code != 200:
		print "myip.dnsdynamic.org failed."
		return 0
	
	ip = r.text

	if not re.match('[0-9]+(?:\.[0-9]+){3}', ip):
		print "myip.dnsdynamic.org failed."
		return 0

	# construct the update url
	updateurl = UpdateIPServiceURL.format(domain, ip, record_type, username, password)

	# go for it
	r2 = requests.get(updateurl)	

	if r2.status_code != 200:
		print "UpdateDNs failed:"
		print r2.text
		return 0
	
	# error checking
	try:
		tree = ET.fromstring(r2.text)	
	except:
		print "UpdateDNs failed:"
		print r2.text
		return 0

	elements = tree.findall("result")

	if not elements:
		print "UpdateDNs failed:"
		print r2.text
		return 0

	if elements is None:
		print "UpdateDNs failed:"
		print r2.text
		return 0

	if len(elements) != 1:
		print "UpdateDNs failed:"
		print r2.text
		return 0

	if elements[0].text != "OK":
		print "UpdateDNs failed:"
		print r2.text
		return 0	

	# print success
	print "Successfully changed "+domain+" to "+ip

if __name__ == "__main__":
	sys.exit(main())