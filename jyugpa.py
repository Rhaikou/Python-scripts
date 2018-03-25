# Author: Riku Rundelin 21.2.2018
# Usage:
# 1. Go to https://korppi.jyu.fi
# 2. Go to Transcript of records page
# 3. Download the page as html
# 4. Run this script from command line: jyugpa.py <path-to-your-transcript>

import sys
from lxml import etree

try:
    path = sys.argv[1]
except:
    print( "Usage: jyugpa.py <file path>" )
    sys.exit(0)

myparser = etree.HTMLParser(encoding="utf-8")

doc = etree.parse(path, myparser)

root = doc.getroot()

courses = [ c for c in root.iterfind(".//tr") ]

gp = 0
total_credits = 0
gpa = 0

for c in courses:
    rows = [ r for r in c.iterfind(".//td") ]
    if len(rows) == 6:
        credit = rows[2].text[:4]
        grade = rows[3].text
        try:
            gp += float(grade) * float(credit)
            total_credits += float(credit)
        except:
            continue
       

if total_credits > 0:
    gpa = gp / total_credits

print(gpa)