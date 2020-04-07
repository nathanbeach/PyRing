#Author: Rami Janini
#Version: 2.0: Fixing issues and adding light control.
import time
import json
import getpass
from pathlib import Path
from pprint import pprint
from ring_doorbell import Ring, Auth
from oauthlib.oauth2 import MissingTokenError

cache_file = Path("test_token.cache")

def clear():
	print (u"{}[2J{}[;H".format(chr(27), chr(27)))

def banner():

	print('''
	  ___       ___  _
	 / _ \__ __/ _ \(_)__  ___ _
	/ ___/ // / , _/ / _ \/ _ `/
	/_/   \_, /_/|_/_/_//_/\_, /
		/___/            /___/
			Author:Rami Janini
					 v.2.0''')


def token_updated(token):
	cache_file.write_text(json.dumps(token))

def otp_callback():
	auth_code = input("2FA code: ")
	return auth_code

clear()
banner()
if cache_file.is_file():
	auth = Auth("MyProject/1.0", json.loads(cache_file.read_text()), token_updated)
else:
	username = input("Username: ")
	password = getpass.getpass("Password: ")
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
		print('\nAddress:    %s' % dev.address)
		print('Name:         %s' % dev.name)
		print('Device Type:       %s' % dev.family)
		print('Battery Life: %s' % dev.battery_life)
		print('ID:           %s' % dev.id)
		print('Timezone:     %s' % dev.timezone)
		print('Wifi Name:    %s' % dev.wifi_name)
		print('Wifi RSSI:    %s' % dev.wifi_signal_strength)
	back_but = input("\n[+]Press anything to go back to the home screen.\n[+]PyRing: ")
	if back_but == "":
		print("")
	else:
		print("")

def listDevices():
	print("\n1)Stickup Cameras:")
	for stickup_cam in devices['stickup_cams']:
		if stickup_cam:
			print(str(stickup_cam).replace('<RingStickUpCam:', "").replace(">", "") + " Camera")
		else:
			print("")

	print("\n2)Doorbells: ")
	for doorbell in devices['doorbots']:
		if doorbell == "":
			print(doorbell)
		else:
			print("")

	print("\n3)Chimes:")
	for chime in devices['chimes']:
		if chime:
			print(chime)
		else:
			print("")
	back_but = input("\n[+]Press anything to go back to the home screen.\n[+]PyRing: ")
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
			print("[+]Lights On")
	back_but = input("\n[+]Press anything to go back to the home screen.\n[+]PyRing: ")
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
			print("[+]Lights Off")
	back_but = input("\n[+]Press anything to go back to the home screen.\n[+]PyRing: ")
	if back_but == "":
		print("")
	else:
		print("")

def motionVidDownload_StickCam():

	stickup_cam_num = len(devices['stickup_cams'])

	for stickup_cam_motion in range(stickup_cam_num):
		try:
			stickup_cam = devices['stickup_cams'][stickup_cam_motion]
			print("\n[+]Downloading motion from stickup camera number [{}]...".format(name))
			stickup_cam.recording_download(
		stickup_cam.history(limit=100, kind='motion')[0]['id'],
						 filename='Camera_Num_{}.mp4'.format(stickup_cam_motion),
						 override=True)
			print("[+]Recording Link:" + stickup_cam.recording_url(stickup_cam.last_recording_id))
		except:
			pass
	back_but = input("\n[+]Press anything to go back to the home screen.\n[+]PyRing: ")
	if back_but == "":
		print("")
	else:
		print("")

def motionVidDownload_Doorbell():

	doorbell_cam_num = len(devices['doorbots'])
	for doorbell_cam_motion in range(doorbell_cam_num):
		try:
			doorbell = devices['doorbots'][doorbell_cam_motion]
			print("\n[+]Downloading ding from doorbell camera number [{}]...".format(stickup_cam_motion))
			doorbell.recording_download(
			  doorbell.history(limit=100, kind='ding')[0]['id'],
								filename='Doorbell_Camera_Num_{}.mp4'.format(stickup_cam_motion),
								override=True)

			print( + doorbell.recording_url(doorbell.last_recording_id))
		except:
			pass

	back_but = input("\n[+]Press anything to go back to the home screen.\n[+]PyRing: ")
	if back_but == "":
		print("")
	else:
		print("")

def get_alerts_StickCam():
	for stickup_cam in devices['stickup_cams']:

	    for event in stickup_cam.history(limit=5):
	        print('ID:       %s' % event['id'])
	        print('Kind:     %s' % event['kind'])
	        print('Answered: %s' % event['answered'])
	        print('When:     %s' % event['created_at'])
	        print('--' * 50)

	    events = stickup_cam.history(kind='motion')
	back_but = input("\n[+]Press anything to go back to the home screen.\n[+]PyRing: ")
	if back_but == "":
		print("")
	else:
		print("")

def get_alerts_doorbellCam():
	for doorbell in devices['doorbots']:

	    for event in doorbell.history(limit=5):
	        print('ID:       %s' % event['id'])
	        print('Kind:     %s' % event['kind'])
	        print('Answered: %s' % event['answered'])
	        print('When:     %s' % event['created_at'])
	        print('--' * 50)

	    events = doorbell.history(kind='motion')
	back_but = input("\n[+]Press anything to go back to the home screen.\n[+]PyRing: ")
	if back_but == "":
		print("")
	else:
		print("")


while True:
	clear()
	banner()
	print("\n  1)Ring devices info.\n  2)Ring devices list.\n  3)Ring light control.\n  4)Download latest motion/ding video.\n  5)Get latest 5 motion alerts\n  6)Exit PyRing.")
	mode = input("\n[+]PyRing: ")
	if mode == "1":
		clear()
		banner()
		print("\n[+]Getting Ring device's info...\n")
		CamerasStatus()
	elif mode == "2":
		clear()
		banner()
		print("\n[+]Getting all your Ring devices...\n")
		listDevices()
	elif mode == "3":
		clear()
		banner()
		print("\n[+]Getting Ring light controls...\n")
		print("\n  1)Ring lights on.\n  2)Ring lights off.\n")
		status = input("[+]PyRing: ")
		if status == "1":
			lightson()
		elif status == "2":
			lightsoff()
		else:
			continue
	elif mode == "4":
		clear()
		banner()
		print("\n  1)Stickup camera motion video.\n  2)Doorbell camera ding video.\n")
		status = input("[+]PyRing: ")
		if status == "1":
			motionVidDownload_StickCam()
		elif status == "2":
			motionVidDownload_Doorbell()
		else:
			continue
	elif mode == "5":
		clear()
		banner()
		print("\n  1)Stickup camera motion alerts.\n  2)Doorbell camera motion alerts.\n")
		status = input("[+]PyRing: ")
		if status == "1":
			get_alerts_StickCam()
		elif status == "2":
			get_alerts_doorbellCam()
		else:
			continue

	if mode == "6":
		clear()
		banner()
		print("[+]Exiting PyRing...\n[+]Thank you for PyRing.\n[+]Author:janinirami@gmail.com")
		break
