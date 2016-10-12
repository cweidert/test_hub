#!/usr/bin/env python

import re
import sys

def parseZip(zipString):
	pattern = re.compile("(?P<standard>[0-9]{3,5})(-(?P<plusFour>[0-9]{4}))?")
	result = pattern.search(zipString)
	if result:
		standardZip = result.group("standard")
		standardZip = "%05d" % int(standardZip)
		extension = result.group("plusFour")
		return standardZip, extension
	else:
		return None, None


if __name__ == "__main__":
	zipStrings = [
		"601-1234",
		"90036",
		"10012",
		"90036-4321"
	]
	for zipString in zipStrings:
		z, e = parseZip(zipString)
		print(zipString, "-->", z, e)


	for arg in sys.argv[1:]:
		print(arg)
