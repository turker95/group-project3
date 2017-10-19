import requests
import datetime 
import re
from datetime import datetime


LOG = requests.get('https://s3.amazonaws.com/tcmg412-fall2016/http_access_log')

def main():
  
