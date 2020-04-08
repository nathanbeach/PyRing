#Author: Rami Janini
#Version: 2.1: Fixing previous issues, adding coloring theme
import os
import sys
import time
import json
import getpass
import contextlib
from pathlib import Path
from pprint import pprint
from urllib.parse import urlencode
from urllib.request import urlopen
from ring_doorbell import Ring, Auth
from oauthlib.oauth2 import MissingTokenError


if sys.platform.lower() == "win32":
	os.system('color')

class style():
	BLACK = lambda x: '\033[30m' + str(x)
	RED = lambda x: '\033[31m' + str(x)
	GREEN = lambda x: '\033[32m' + str(x)
	YELLOW = lambda x: '\033[33m' + str(x)
	BLUE = lambda x: '\033[34m' + str(x)
	CYAN = lambda x: '\033[36m' + str(x)
	WHITE = lambda x: '\033[37m' + str(x)
	UNDERLINE = lambda x: '\033[4m' + str(x)
	RESET = lambda x: '\033[0m' + str(x)

cache_file = Path("private_token.cache")

def clear():
	print (u"{}[2J{}[;H".format(chr(27), chr(27)))

def banner():


	print(style.CYAN('''
	  ___       ___  _
	 / _ \__ __/ _ \(_)__  ___ _
	/ ___/ // / , _/ / _ \/ _ `/
	/_/   \_, /_/|_/_/_//_/\_, /
		/___/            /___/
			Author:Rami Janini
				v.2.1''')+ style.RESET(""))



def token_updated(token):
	cache_file.write_text(json.dumps(token))

def otp_callback():
	auth_code = input(style.GREEN("[+]2FA code: "))
	return auth_code

clear()
banner()
if cache_file.is_file():
	clear()
	banner()
	print(style.RED("\n[+]Getting username and password from cache file...") + style.RESET(""))
	auth = Auth("MyProject/1.0", json.loads(cache_file.read_text()), token_updated)
else:
	clear()
	banner()
	username = input(style.GREEN("[+]Username: "))
	password = getpass.getpass(style.GREEN("[+]Password: "))
	auth = Auth("MyProject/1.0", None, token_updated)
	try:
		auth.fetch_token(username, password)
	except MissingTokenError:
		auth.fetch_token(username, password, otp_callback())

ring = Ring(auth)
ring.update_data()
devices = ring.devices()

def CamerasStatus():
	for dev in list(devices['stickup_cams'] + devices['chimes'] + devices['doorbots']):
		dev.update_health_data()
		print(style.GREEN('\nName:    %s' % dev.name))
		print(style.RESET('nAddress:         %s' % dev.address))
		print('Device Type:       %s' % dev.family)
		print('Battery Life: %s' % dev.battery_life)
		print('ID:           %s' % dev.id)
		print('Timezone:     %s' % dev.timezone)
		print('Wifi Name:    %s' % dev.wifi_name)
		print('Wifi RSSI:    %s' % dev.wifi_signal_strength)
	back_but = print(input(style.YELLOW("\n[+]Press anything to go back to the home screen. ")))
	if back_but == "":
		print("")
	else:
		print("")

def listDevices():
	print(style.GREEN("\n1)Stickup Cameras:"))
	for stickup_cam in devices['stickup_cams']:
		if stickup_cam:
			print(style.RESET(str(stickup_cam).replace('<RingStickUpCam:', "").replace(">", "") + " Camera"))
		else:
			print("")

	print(style.GREEN("\n2)Doorbells: "))
	for doorbell in devices['doorbots']:
		if doorbell == "":
			print(style.RESET(doorbell))
		else:
			print("")

	print(style.GREEN("\n3)Chimes:"))
	for chime in devices['chimes']:
		if chime:
			print(style.RESET(chime))
		else:
			print("")
	back_but = print(input(style.YELLOW("\n[+]Press anything to go back to the home screen. ")))
	if back_but == "":
		print("")
	else:
		print("")

def lightson():
	clear()
	banner()
	for dev in list(devices['stickup_cams']):
		dev.update_health_data()
		if dev.family == 'stickup_cams' and dev.lights:
			dev.lights = 'on'
			print(style.GREEN("[+]Lights On"))
	back_but = print(input(style.YELLOW("\n[+]Press anything to go back to the home screen. ")))
	if back_but == "":
		print("")
	else:
		print("")

def lightsoff():
	clear()
	banner()
	for dev in list(devices['stickup_cams']):
		dev.update_health_data()
		if dev.family == 'stickup_cams' and dev.lights:
			dev.lights = 'off'
			print(style.RED("[+]Lights Off"))
	back_but = print(input(style.YELLOW("\n[+]Press anything to go back to the home screen. ")))
	if back_but == "":
		print("")
	else:
		print("")

def motionVidDownload_StickCam():
	if len(devices['stickup_cams']) == 0:
		print(style.RED("[+]You dont have any stick up cams."))
	else:
		stickup_cam_num = len(devices['stickup_cams'])

		for stickup_cam_motion in range(stickup_cam_num):
			try:
				stickup_cam = devices['stickup_cams'][stickup_cam_motion]
				print(style.RED("\n[+]Downloading motion from stickup camera number [{}]...".format(stickup_cam_motion)))
				mp4_download = stickup_cam.recording_download(
			stickup_cam.history(limit=100, kind='motion')[0]['id'],
							 filename='Camera_Num_{}.mp4'.format(stickup_cam_motion),
							 override=True)
				if mp4_download == True:
					print(style.GREEN('[+]Motion video downloaded successfully.'))

				recording_URL = stickup_cam.recording_url(stickup_cam.last_recording_id)
				if recording_URL == False:
					print()
				else:
					request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':recording_URL}))
					with contextlib.closing(urlopen(request_url)) as response:
						print(style.GREEN('[+]Recording Link: ') + style.RESET(response.read().decode('UTF-8')))
			except:
				print("error")
				pass



	back_but = print(input(style.YELLOW("\n[+]Press anything to go back to the home screen. ")))
	if back_but == "":
		print("")
	else:
		print("")

def motionVidDownload_Doorbell():
	if len(devices['doorbots']) == 0:
		print(style.RED("[+]You dont have any doorbells."))
	else:
		stickup_doorbell_num = len(devices['doorbots'])

		for stickup_doorbell_motion in range(stickup_doorbell_num):
			try:
				doorbell = devices['doorbots'][stickup_doorbell_motion]
				print(style.RED("\n[+]Downloading motion from stickup doorbell camera number [{}]...".format(stickup_doorbell_motion)))
				mp4_download = doorbell.recording_download(
			doorbell.history(limit=100, kind='motion')[0]['id'],
							 filename='Camera_Num_{}.mp4'.format(stickup_doorbell_motion),
							 override=True)
				if mp4_download == True:
					print(style.GREEN('[+]Motion video downloaded successfully.'))

				recording_URL = doorbell.recording_url(doorbell.last_recording_id)
				if recording_URL == False:
					print()
				else:
					request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':recording_URL}))
					with contextlib.closing(urlopen(request_url)) as response:
						print(style.GREEN('[+]Recording Link: ') + style.RESET(response.read().decode('UTF-8')))
			except:
				print("error")
				pass

	back_but = print(input(style.YELLOW("\n[+]Press anything to go back to the home screen. ")))
	if back_but == "":
		print("")
	else:
		print("")

def get_alerts_StickCam():
	if len(devices['stickup_cams']) == 0:
		print(style.RED("[+]You dont have any stick up cams."))
	else:
		for stickup_cam in devices['stickup_cams']:
			print(style.GREEN("\n[+]" + str(stickup_cam.history).replace("<bound method RingDoorBell.history of <RingStickUpCam: ", "").replace(">>", "")) + style.RESET(""))


			for event in stickup_cam.history(limit=5):
				print(style.RESET('ID:       %s' % event['id']))
				print('Kind:     %s' % event['kind'])
				print('Answered: %s' % event['answered'])
				print('When:     %s' % event['created_at'])

			events = stickup_cam.history(kind='motion')

	back_but = print(input((style.YELLOW("\n[+]Press anything to go back to the home screen. "))))
	if back_but == "":
		print("")
	else:
		print("")

def get_alerts_doorbellCam():
	if len(devices['doorbots']) == 0:
		print(style.RED("[+]You dont have any doorbells."))
	else:
		for doorbell in devices['doorbots']:
			print(style.GREEN("\n[+]" + str(doorbell.history).replace("<bound method RingDoorBell.history of <Doorbots: ", "").replace(">>", "")) + style.RESET(""))


			for event in doorbell.history(limit=5):
				print(style.RESET('ID:       %s' % event['id']))
				print('Kind:     %s' % event['kind'])
				print('Answered: %s' % event['answered'])
				print('When:     %s' % event['created_at'])

		events = doorbell.history(kind='motion')
	back_but = print(input((style.YELLOW("\n[+]Press anything to go back to the home screen. "))))
	if back_but == "":
		print("")
	else:
		print("")


def main():
	while True:
		clear()
		banner()
		print(style.RESET("\n  1)Ring devices info.\n  2)Ring devices list.\n  3)Ring light control.\n  4)Download latest motion/ding video.\n  5)Get latest 5 motion alerts\n  6)Exit PyRing."))
		mode = input(style.CYAN("\n[+]PyRing: "))
		if mode == "1":
			clear()
			banner()
			print(style.RED("\n[+]Getting Ring device's info...\n"))
			CamerasStatus()
		elif mode == "2":
			clear()
			banner()
			print(style.RED("\n[+]Getting all your Ring devices...\n"))
			listDevices()
		elif mode == "3":
			clear()
			banner()
			print(style.RED("\n[+]Getting Ring light controls...\n"))
			print(style.RESET("\n  1)Ring lights on.\n  2)Ring lights off.\n"))
			status = input(style.CYAN("[+]PyRing: "))
			if status == "1":
				lightson()
			elif status == "2":
				lightsoff()
			else:
				continue
		elif mode == "4":
			clear()
			banner()
			print(style.RESET("\n  1)Stickup camera motion video.\n  2)Doorbell camera ding video.\n"))
			status = input(style.CYAN("[+]PyRing: "))
			if status == "1":
				motionVidDownload_StickCam()
			elif status == "2":
				motionVidDownload_Doorbell()
			else:
				continue
		elif mode == "5":
			clear()
			banner()
			print(style.RESET("\n  1)Stickup camera motion alerts.\n  2)Doorbell camera motion alerts.\n"))
			status = input(style.CYAN("[+]PyRing: "))
			if status == "1":
				get_alerts_StickCam()
			elif status == "2":
				get_alerts_doorbellCam()
			else:
				continue

		if mode == "6":
			clear()
			banner()
			print(style.RED("[+]Exiting PyRing...\n[+]Thank you for PyRing.\n[+]Author:janinirami@gmail.com"))
			break

if __name__ == "__main__":
	main()
