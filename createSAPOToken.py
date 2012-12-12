import urllib
import requests
import sys
import getpass

# More info here: http://softwarelivre.sapo.pt/projects/developers/wiki/Services/STS/Operations/GetToken_PT

GetTokenURL = "https://services.sapo.pt/STS/GetToken?ESBUsername={0}&ESBPassword={1}&json=true"

def main(argv=None):
	# construct the token url
    if len(argv) != 2:
        print "usage: createSAPOToken.py <your SAPO username>"
        return 0

    # get the password
    username = argv[1]
    password = getpass.getpass("Password: ")

    # construct the url
    getTokenURL = GetTokenURL.format(urllib.quote(username), urllib.quote(password))

    # go for it
    r = requests.get(getTokenURL)

    # error checking
    if r.status_code != 200:
        print "GetToken failed:"
        print r.text
        return 0

    # error checking
    dict = r.json

    if not dict:
        print "GetToken failed:"
        print r.text
        return 0

    if dict is None:
        print "GetToken failed:"
        print r.text
        return 0

    token = dict["ESBToken"]["value"]

    if len(token) == 0:
        print "GetToken failed:"
        print r.text
        return 0

    print "Success. Your token is:\n"+token

if __name__ == "__main__":
	sys.exit(main(sys.argv))