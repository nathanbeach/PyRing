#Author: Rami Janini
from ring_doorbell import Ring


myring = Ring('ring email', 'ring password')

def CameraCheck():
	for dev in list(myring.stickup_cams):

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
	stickupCamera = myring.stickup_cams[0]
	stickupCamera.recording_download(
		stickupCamera.history(limit=100, kind='motion')[0],
								filename='last_motion.mp4', override=True)

	#prints out a url with your latest motion video
	#return stickupCamera.recording_url(stickupCamera.last_recording_id)




def GetMotionAlerts():
	for stickup_cams in myring.stickup_cams:
		#You can change the limit
		for event in stickup_cams.history(limit=10):
			print('Footage ID:     %s' % event['id'])
			print('Kind:     %s' % event['kind'])
			print('Answered:     %s' % event['answered'])
			print('Date/Time:     %s' % event['created_at'])
			print('--' * 50)


		#To show only motion events:	
		#event = stickup_cams.history(kind='motion')

def startProgram():
	print('''

 	  ___       ___  _          
	  / _ \__ __/ _ \(_)__  ___ _
 	/ ___/ // / , _/ / _ \/ _ `/
	/_/   \_, /_/|_/_/_//_/\_, / 
 	    /___/            /___/  
     		Authur:Rami Janini
     		         v.1.0

	''')

	answer = input('Select: 1--> Camera Check  2--> For Motion Footage 3--> To Get Motion Alerts:')

	if answer == '1':
		print("")
		CameraCheck()
	elif answer == '2':
		print("")
		GetVideo()
	elif answer == '3':
		print("")
		GetMotionAlerts()
	else:
		print("")
		print('Invaild Input!!')		

startProgram()
myring.is_connected 
True
