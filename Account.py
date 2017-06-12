# encoding=utf-8

import requests
import re
import datetime
from datahandler import *
from info import *

class Account:

    def __init__(self):
        self.username = username
        self.pwd = pwd
        self.ck_pc = ''
        self.session = requests.session()

    def login_pc(self):

        t = requests.session()
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/54.0.2840.59 Safari/537.36 115Browser/8.0.0',
            'Accept': 'application / json'
        }

        html = t.get('http://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F',
                     headers=headers, verify=False).text

        pubkey = re.findall('id="pubKey" value="(.*?)"', html, re.S)[0]
        if 'JD_Verification' in html:
            url = 'http://' + re.findall('src2="//(.*?)"', html, re.S)[0].replace('amp;', '')
            ir = t.get(url, headers=headers)
            path_str = r'd:\Project\JDAssistant\authcode.jpg'
            save_img(path_str, ir)
            authcode = input("Enter the authcode to continue : ")
        else:
            authcode = ''
        data = {'uuid': re.findall('name="uuid" value="(.*?)"', html, re.S)[0],
                '_t': re.findall('id="token" value="(.*?)"', html, re.S)[0],
                'loginType': 'f',
                'loginname': self.username,
                'nloginpwd': self.pwd,
                'chkRememberMe': '',
                'authcode': authcode,
                'pubKey': pubkey,
                'sa_token': re.findall('name="sa_token" value="(.*?)"', html, re.S)[0],
                'seqSid': '9'
        }
        post_data = t.post(
            "http://passport.jd.com/uc/loginService",
            data=data, headers=headers, verify=False).text
        if 'success' in post_data:
            print(post_data)
        else:
            print(post_data)
            raise Exception('Login Failed！')
        cookiestr = ''
        for k, value in t.cookies.items():
            cookiestr = cookiestr + k + '=' + value + ';'
        self.ck_pc = cookiestr[:-1]
        return self.ck_pc

    def get_payment(self):
        payment_list = []
        headers = {'cookie': self.ck_pc}
        html = self.session.get('http://order.jd.com/center/list.action', headers=headers, verify=False).text
        print(html)

account = Account()
account.login_pc()
account.get_payment()
