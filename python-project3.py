import requests
import datetime 
import re
from datetime import datetime


i = 0
by_month = {}

print "Downloading log file ..."

log_file = requsts.get('https://s3.amazonaws.com/tcmg412-fall2016/http_access_log')
with open('http_log.txt', "w") as local:
  local.write(response.read())

print "Log file was saved ..."

regex = re.compile(".*\[(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")

for line in open(http_log.txt



def main():
  
