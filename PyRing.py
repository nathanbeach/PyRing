#Author: Rami Janini
#Version: 1.3: Fixing issues and adding light control.
import time
from getpass import getpass
from ring_doorbell import Ring


print('''
	  ___       ___  _
	 / _ \__ __/ _ \(_)__  ___ _
	/ ___/ // / , _/ / _ \/ _ `/
	/_/   \_, /_/|_/_/_//_/\_, /
		/___/            /___/
			Author:Rami Janini
					 v.1.3
''')

ringEmail = input('Ring Email: ')
ringPassword = getpass('Ring Password: ')

ring = Ring(ringEmail, ringPassword)

ringCameras = ring.stickup_cams
ringDoorbells = ring.doorbells


def CameraCheck():
	for dev in list(ringCameras + ringDoorbells):

		dev.update()

		print('Account ID: %s' % dev.account_id)
		print('Device Type: %s' % dev.family)
		print('Address:    %s' % dev.address)
		print('Family:     %s' % dev.family)
		print('ID:         %s' % dev.id)
		print('Name:       %s' % dev.name)
		print('Timezone:   %s' % dev.timezone)
		print('Wifi Name:  %s' % dev.wifi_name)
		print('Wifi RSSI:  %s' % dev.wifi_signal_strength)
		print('Battery Life: %s' % dev.battery_life)


def GetVideo():
	def stickCamVideo():
		stickupCamera = ringCameras[0]
		stickupCamera.recording_download(
			stickupCamera.history(limit=100, kind='motion')[0],
									filename='last_motion.mp4', override=True)

	def doorbellCamVideo():
		doorbell = ringCameras[0]
		doorbell.recording_download(
			doorbell.history(limit=100, kind='motion')[0],
									filename='last_motion.mp4', override=True)

	while True:
		camFootageDevice = input('Select: 1--> Security Camera Footage  2--> Doorbell Camera Footage  3--> Go Back : ')
		if camFootageDevice == '1':
			print("")
			stickCamVideo()
			print("")
		elif camFootageDevice == '2':
			print("")
			doorbellCamVideo()
			print("")
		elif camFootageDevice == '3':
			break
		else:
			continue

def GetMotionAlerts():

	def stickCamMotion():
		for stickup_cams in ringCameras:
			#You can change the limit
			for event in stickup_cams.history(limit=10):
				print('Footage ID:     %s' % event['id'])
				print('Kind:     %s' % event['kind'])
				print('Answered:     %s' % event['answered'])
				print('Date/Time:     %s' % event['created_at'])
				print('--' * 50)
			events = stickup_cams.history(kind ='motion')

	def doorbellCamMotion():
		for doorbell in ringDoorbells:
			#You can change the limit
			for event in doorbell.history(limit=10):
				print('Footage ID:     %s' % event['id'])
				print('Kind:     %s' % event['kind'])
				print('Answered:     %s' % event['answered'])
				print('Date/Time:     %s' % event['created_at'])
				print('--' * 50)
			events = doorbell.history(kind ='motion')
	while True:
		camMotionDevice = input('Select: 1--> Security Camera Motion Alerts  2--> Doorbell Camera Motion Alerts  3--> Go Back : ')
		if camMotionDevice == '1':
			print("")
			stickCamMotion()
			print("")
		elif camMotionDevice == '2':
			print("")
			doorbellCamMotion()
			print("")
		elif camMotionDevice == '3':
			break
		else:
			continue

def sirenController():
	def stickCamSiren():
		for dev in list(ringCameras):

			seconds = input('After how many seconds do you want the alarm to be turned off? ')
			seconds=int(seconds)
			print("Activating alarm for " + str(seconds) + " seconds...")
			dev.siren = 60
			time.sleep(seconds)
			dev.siren = 0

	def doorbellSiren():
		for dev in list(ringDoorbells):

			seconds = input('After how many seconds do you want the alarm to be turned off? ')
			seconds=int(seconds)
			print("Activating alarm for " + str(seconds) + " seconds...")
			dev.siren = 60
			time.sleep(seconds)
			dev.siren = 0

	while True:
		camSiren = input('Select: 1--> Turn Security Camera Siren On  2--> Turn Doorbell Siren On  3--> Go Back : ')
		if camSiren == '1':
			print("")
			stickCamSiren()
			print("")
		elif camSiren == '2':
			print("")
			doorbellSiren()
			print("")
		elif camSiren == '3':
			break
		else:
			continue

def lightControl():
	def lightOn():
		for dev in list(ringCameras + ringDoorbells):

			dev.update()

			if dev.family == 'stickup_cams' and dev.lights:
				dev.lights = 'on'

			print('Lights On!')

	def lightOff():
		for dev in list(ringCameras + ringDoorbells):

			if dev.family == 'stickup_cams' and dev.lights:
				dev.lights = 'off'
			print('Lights Off!')


	while True:
		lightControlAnswer = input('Select: 1--> Turn Lights On  2--> TurnLights Off  3--> Go Back : ')
		if lightControlAnswer == '1':
			print("")
			lightOn()
			print("")
		elif lightControlAnswer == '2':
			print("")
			lightOff()
			print("")
		elif lightControlAnswer == '3':
			break
		else:
			continue

def startProgram():
	print('Logged in as: ', ringEmail)
	print("")
	print('Your Devices List:')
	print(ringCameras)
	print("")
	while True:
		answer = input('Select: 1--> Cameras Check  2--> Motion Footage  3--> Motion Alerts  4--> Siren Controller  5--> Light Controller  6--> Exit  :')

		if answer == '1':
			print("")
			CameraCheck()
			print("")

		elif answer == '2':
			print("")
			GetVideo()
			print("")
		elif answer == '3':
			print("")
			GetMotionAlerts()
			print("")
		elif answer == '4':
			print("")
			sirenController()
			print("Alarm is off!")
			print("")
		elif answer == '5':
			print("")
			lightControl()
			print("")
		elif answer == '6':
			print("")
			print("Thanks For using PyRing!")
			break
		else:
			print("")
			print("Invaild input, please choose again!")
			print("")
			continue

startProgram()
