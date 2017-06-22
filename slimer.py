# encoding=utf-8

from os import popen
from os import system
import subprocess
from sys import getdefaultencoding
import re
import json
import pymysql
from info import *

cmd = 'd:\slimerjs-0.10.3\slimerjs-0.10.3\slimerjs.bat d:\Project\JDAssistant\JDtest_slimer.js'
# print(getdefaultencoding())
# output = subprocess.getoutput(cmd)

instance = subprocess.run(cmd, stdout=subprocess.PIPE)
output = instance.stdout

output = str(output, encoding = "utf-8")
# print(output)
try:
	match_rule = re.compile('https://a.jd.com/indexAjax/getCouponListByCatalogId.html.*\"body\":\"jQuery\d+.(.*).","httpVersion')
	match_str = re.findall(match_rule, output)

	match_str = re.sub(r'\\','',match_str[0])

	json_dict = json.loads(match_str)
	coupon_list = json_dict['couponList']
	# conn = pymysql.connect(user = mysql_user, password = mysql_password, host = mysql_localhost, db = mysql_JDA_db, charset = mysql_charset)
	# insert_cursor = conn.cursor()

	# sqli="insert into student values(%s,%s,%s,%s)"
	# cur.executemany(sqli,[
	#     ('3','Tom','1 year 1 class','6'),
	#     ('3','Jack','2 year 1 class','7'),
	#     ('3','Yaheng','2 year 2 class','7'),
	#     ])


	# insert_cursor.execute('insert into jd_coupon(id) values (%s)' , json_dict["resultCode"])
	# conn.commit()
	# insert_cursor.close()
	field_list = []
	value_list = []
	flag = 0;
	for coupon in coupon_list:
		coupon_value_list = []
		for k, v in coupon.items():
			if flag == 0:
				field_list.append(k)
			value_list = 
		if flag == 0:
			flag = 1
		fields_tuple = tuple(field_list)
	print(str(fields_tuple))


except:
	print(e)
print(coupon_list[0])
# str = popen('cmd')
# print(str.read()[1])