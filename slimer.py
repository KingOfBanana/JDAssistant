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
	# print(camel_to_underline('favNum'))


	match_rule = re.compile('https://a.jd.com/indexAjax/getCouponListByCatalogId.html.*\"body\":\"jQuery\d+.(.*).","httpVersion')
	match_str = re.findall(match_rule, output)

	match_str = re.sub(r'\\','',match_str[0])

	json_dict = json.loads(match_str)
	coupon_list = json_dict['couponList']
	
	field_type = []
	field_key = []
	field_value = []
	flag = 0;
	count = 0;
	for coupon in coupon_list:
		coupon_value = []
		for k, v in coupon.items():
			if flag == 0:
				field_key.append(camel_to_underline(k))
				field_type.append('%%s')
			coupon_value.append(v)		
		coupon_value = tuple(coupon_value)
		if flag == 0:
			flag = 1
			field_key = tuple(field_key)
		# field_key.sort()
		field_value.append(coupon_value)

	field_key = re.sub(r'\'','',str(field_key))
	field_key = re.sub(' position,', ' coupon_position,',field_key)
	field_key = re.sub(' key,', ' coupon_key,',field_key)
	field_type = str(tuple(field_type))
	print(field_value)
	print(field_key)
	sql = 'insert into jd_coupon' + field_key + 'values' + "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
	conn = pymysql.connect(user = mysql_user, password = mysql_password, host = mysql_localhost, db = mysql_JDA_db, charset = mysql_charset)
	insert_cursor = conn.cursor()

	insert_cursor.executemany(sql, field_value)
	
	conn.commit()
	insert_cursor.close()

	print(field_key)

except:
	print(e)
