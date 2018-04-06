# -*- coding: utf-8 -*-
# @Author: Eric Huang
# @Date:   2018-04-05 20:30:34
# @Last Modified by:   Eric Huang
# @Last Modified time: 2018-04-05 23:01:59

import urllib
import urllib2
import re
import thread
import time
import Image
import sys
import cStringIO
import os

def homePage(url_Pass):
  page       = 1
  url        = url_Pass + str(page)
  user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
  headers    = {'User-Agent' : user_agent}

  try:
    request  = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    content  = response.read()
    pattern  = re.compile('<li>.*?href="(.*?)"><img.*?src="(.*?)".*?title.*?caption">(.*?)</span>',re.S)

    items = re.findall(pattern,content)



    for index,item in enumerate(items):
      print "Content address:", items[index][0]
      print "Image address:", items[index][1]
      print "Title: ", items[index][2]
      #raw_input("Press Enter to continue...")
      cwd = os.getcwd() + '/Recipes/' + str(items[index][2]).replace(' ','_')
      os.makedirs(cwd)
      urllib.urlretrieve(items[index][1], cwd + "/icon.jpg")
  except urllib2.URLError, e:
      if hasattr(e,"code"):
          print e.code
      if hasattr(e,"reason"):
          print e.reason

  return items[index][0]
def read_content(url_Pass):


if __name__ == "__main__":
    url = 'https://www.cookingclassy.com/category/appetizer/page/'
    content_link = homePage(url)
