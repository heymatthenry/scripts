#!/usr/local/bin/python

import sys
import parsedatetime as pdt

natLangDateStr = sys.argv[1]
dt = pdt.Calendar().parse(natLangDateStr)[0]

formattedDate = "{month}-{day}-{year}".format(month=dt.tm_mon,
        day=dt.tm_mday, year=dt.tm_year)

print formattedDate
