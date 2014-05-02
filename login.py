import urllib2
import urllib
info = {'DDDDD':'2013213317',
'upass':'f25407541d57499a530e984c3f844a65123456781',
'R1':'0',
'R2':'1',
'para':'00',
'0MKKey':'123456'}
key = urllib.urlencode(info)
url = "http://gw.bupt.edu.cn"
door = urllib2.Request(url,key)
res = urllib2.urlopen(door)