#! /usr/bin/env python
# -*- coding: utf-8 -*-

from os import listdir
from os.path import join
from re import match

if __name__ == "__main__":
    DATA_DIR = "imgs"
    HTML_TEMPLATE = "template.html"
    BOOK_NAME = "iLikeYou"
    BODY_TAG = "<!-- !!! BODYBODY !!! -->"
    BODY = ""

    for imgFilename in [f for f in sorted(listdir(DATA_DIR)) if f.endswith(".png")]:
      fullPath = join(DATA_DIR, imgFilename)

      matchDates = match(r"^[0-9]{2}_([0-9]{4})([0-9]{2})\-?([0-9]{4})?([0-9]{2})?.png", imgFilename)
      fromYear, fromMonth, toYear, toMonth = matchDates.groups()

      mDate = fromMonth + "/" + fromYear
      mDate += " - " + toMonth + "/" + toYear if toYear is not None else ""

      BODY += "    <div class='page'>\n"
      BODY += "      <div class='likes' style='background-image: url(\"%s\");'></div>\n"%fullPath
      BODY += "      <div class='dates'>%s</div>\n"%mDate
      BODY += "    </div>\n"


    # write output file
    with open(BOOK_NAME+".html", 'w') as out:
      with open(HTML_TEMPLATE) as temp:
        for line in temp.readlines():
          if BODY_TAG in line:
            line = BODY
          out.write(line)
