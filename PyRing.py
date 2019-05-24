#Author: Rami Janini
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
					 v.1.1

''')

ringEmail = input('Ring Email: ')
ringPassword = getpass('Ring Password: ')

ring = Ring(ringEmail,ringPassword )

RingCameras = ring.stickup_cams

def CameraCheck():
	for dev in list(RingCameras):

		dev.update()

		print('Your Account ID: %s' % dev.account_id)
		print('Your Camera ID: %s' % dev.id)
		print("Has Subscription: %s" % dev.has_subscription)
		print('Your Camera Adress: %s' % dev.address)
		print("Camera's Wifi ESSID: %s" % dev.wifi_name)
		print("Battery Life: %s" % dev.battery_life)
		print("Light Status: %s" % dev.lights)
		print("Siren Status: %s" % dev.siren)

def GetVideo():
	stickupCamera = RingCameras[0]
	stickupCamera.recording_download(
		stickupCamera.history(limit=100, kind='motion')[0],
								filename='last_motion.mp4', override=True)

	#prints out a url with your latest motion video
	#return stickupCamera.recording_url(stickupCamera.last_recording_id)

def GetMotionAlerts():
	for stickup_cams in RingCameras:
		#You can change the limit
		for event in stickup_cams.history(limit=10):
			print('Footage ID:     %s' % event['id'])
			print('Kind:     %s' % event['kind'])
			print('Answered:     %s' % event['answered'])
			print('Date/Time:     %s' % event['created_at'])
			print('--' * 50)


		#To show only motion events:	
		#event = stickup_cams.history(kind='motion')

def sirenController():
	for dev in list(RingCameras):
	 seconds = input('After how many seconds do you want the alarm to be turned off? ')
	 seconds=int(seconds)
	 print("Activating alarm for " + str(seconds) + " seconds...")
	 dev.siren = 60
	 time.sleep(seconds)
	 dev.siren = 0
	 
def startProgram():
	print('Logged in as: ', ringEmail)
	print("")
	print('Your Devices List:')
	print(RingCameras)
	print("")
	while True:
		answer = input('Select: 1--> Cameras Check  2--> Motion Footage  3--> Motion Alerts  4--> Alarm Controller  5--> Exit  :')

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
			print("Thanks For using PyRing!")
			break
		else:
			print("")
			print("Invaild input, please choose again!")
			print("")
			continue

startProgram()
