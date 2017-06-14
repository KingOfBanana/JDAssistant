# encoding=utf-8

from os import popen
from os import system
import subprocess
from sys import getdefaultencoding
import re

cmd = 'd:\slimerjs-0.10.3\slimerjs-0.10.3\slimerjs.bat d:\Project\JDAssistant\JDtest_slimer.js'
# print(getdefaultencoding())
# output = subprocess.getoutput(cmd)

instance = subprocess.run(cmd, stdout=subprocess.PIPE)
output = instance.stdout

output = str(output, encoding = "utf-8")
# print(output)
match_rule = re.compile('https://a.jd.com/indexAjax/getCouponListByCatalogId.html.*\"body\":\"jQuery\d+.(.*)')
match_str = re.findall(match_rule, output)

match_str = re.sub(r'\\"','',match_str[0])

print(match_str)
# str = popen('cmd')
# print(str.read()[1])