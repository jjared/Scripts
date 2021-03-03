#!/usr/bin/python3

import requests, os, sys, argparse

CHROME_COMMAND = "open -a 'Google Chrome' %s"
PORTSWIGGER_URL = "https://portswigger.net/web-security/cross-site-scripting/cheat-sheet"

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Test XSS filter")
	parser.add_argument("-u", "--url", help="URL of request")
	# parser.add_argument("-p", "--param", help="Parameter to test (default: all)")
	parser.add_argument("-t", "--tags", default="/Users/jjared/Tools/SecLists/Other/xss-tags.txt", type=open, help="List of HTML tags to test")
	parser.add_argument("-a", "--attrs", default="/Users/jjared/Tools/SecLists/Other/xss-attributes.txt", type=open, help="List of HTML tag attributes to test")
	parser.add_argument("-s", "--status", default=[200], nargs='+', type=int, help="Success status (default: 200)")
	args = parser.parse_args(sys.argv[1:])

	if "%s" not in args.url:
		print("No placeholder (%s) found in URL")
		exit()

	allowed_tags = []
	for tag in ["body"]:
		tag = tag.strip()
		# test if tag is valid
		resp = requests.get(args.url.replace("%s", f"<{tag}>"))
		if resp.status_code in args.status:
			print(f"<{tag}>: {resp.status_code}")
			for attr in args.attrs:
				attr = attr.strip()
				# test if attribute is valid
				resp = requests.get(args.url.replace("%s", f"<{tag}%20{attr}%3D1>"))
				if resp.status_code in args.status:
					print(f"<{tag} {attr}=1>: {resp.status_code}")