# Author: Rami Janini
# Version: 1.0.0
# Ring-Doorbell Version : 0.6.0
import os
import sys
from lib.color import style
from ring_doorbell import Ring, Auth
from lib.ring_devices import get_devices
from lib.ring_status import get_status
from lib.ring_lights import light_control
from lib.ring_motions import get_motions
from lib.ring_alerts import get_alerts
from lib.authentication import get_access_token

def py_ring():
    get_access_token()
    ring = Ring(get_access_token.auth)
    ring.update_data()
    devices = ring.devices()
    get_doorbell_cam_motion2(devices)
    sys.exit(0)
    while True:
        if os.path.isdir('Recordings'):
            None
        else:
            os.mkdir('Recordings')
        print (u"{}[2J{}[;H".format(chr(27), chr(27)))

        get_access_token()
        print (u"{}[2J{}[;H".format(chr(27), chr(27)))
        print('   --- PyRing Main Menu ---   \n')
        print(style.GREEN('[01]') + style.RESET(' Ring devices.'))
        print(style.GREEN('[02]') + style.RESET(' Ring devices status.'))
        print(style.GREEN('[03]') + style.RESET(' Ring light control.'))
        print(style.GREEN('[04]') + style.RESET(' Ring motion alerts.'))
        print(style.GREEN('[05]') + style.RESET(' Download Ring latest motion video.'))
        print(style.GREEN('[06]') + style.RESET(' Download a month of video.'))
        print(style.GREEN('[99]') + style.RESET(' Exit PyRing.'))

        try:
            option = input(style.YELLOW('\n[+]') + style.RESET(' Choose your option [Eg: 01]: '))
        except KeyboardInterrupt:
            print (u"{}[2J{}[;H".format(chr(27), chr(27)))
            print(style.RED('\n[!]') + style.RESET(' Error: User exit.'))
            print(style.GREEN('[+]') + style.RESET(' Thank you for using PyRing.'))
            print(style.GREEN('[+]') + style.RESET(' Author: Pr0xy07'))
            print(style.GREEN('[+]') + style.RESET(' If you need any help, contact: pr0xy07@tutanota.com'))
            sys.exit(0)
        try:
            ring = Ring(get_access_token.auth)
            ring.update_data()
            devices = ring.devices()
        except:
            print (u"{}[2J{}[;H".format(chr(27), chr(27)))
            print(style.RED('\n[!]') + style.RESET(' Error: User exit.'))
            print(style.GREEN('[+]') + style.RESET(' Thank you for using PyRing.'))
            print(style.GREEN('[+]') + style.RESET(' Author: Pr0xy07'))
            print(style.GREEN('[+]') + style.RESET(' If you need any help, contact: pr0xy07@tutanota.com'))
            sys.exit(0)

        if option == "01":
            print (u"{}[2J{}[;H".format(chr(27), chr(27)))
            get_devices(devices)
        elif option == "02":
            print (u"{}[2J{}[;H".format(chr(27), chr(27)))
            get_status(devices)
        elif option == "03":
            light_control(devices)
        elif option == "04":
            get_alerts(devices)
        elif option == "05":
            get_motions(devices)
        elif option == "06":
            get_doorbell_cam_motion2(devices)
        elif option == "99":
            print (u"{}[2J{}[;H".format(chr(27), chr(27)))
            print(style.GREEN('\n[+]') + style.RESET(' Thank you for using PyRing.'))
            print(style.GREEN('[+]') + style.RESET(' Author: Pr0xy07'))
            print(style.GREEN('[+]') + style.RESET(' If you need any help, contact: pr0xy07@tutanota.com'))
            break

def get_events_recursive(current_cam, events):
    for event in events:
        motion_time = str(event['created_at']).replace(':', '-').replace(' ', '_').replace('+', '_')
        event_id = event['id']
        print(motion_time + ' - id: ' + str(event_id))
        try:
            mp4_download = current_cam.recording_download(
                     event['id'],
                     filename = f'Recordings/{motion_time}_{event_id}.mp4', override=True)
        except:
            print('event not found: ' + motion_time + ' - id: ' + str(event_id))
    if (len(events) < 100):
        None
    else:
        get_events_recursive(current_cam, current_cam.history(limit = 100, older_than=events[-1]['id']))

def get_doorbell_cam_motion2(devices):

    if devices['doorbots']:
        current_cam = devices['doorbots'][0]
        print(current_cam)

        events = current_cam.history(limit = 100) #, older_than=6906518921932661433
        get_events_recursive(current_cam, events)
        # print(len(events))
        # events2 = current_cam.history(limit = 100, older_than=events[-1]['id'])
        # print(len(events2))
        # events3 = current_cam.history(limit = 100, older_than=events2[-1]['id'])
        # print(len(events3))
        # events4 = current_cam.history(limit = 100, older_than=events3[-1]['id'])
        # print(len(events4))
        # for event in events:
        #     motion_time = str(event['created_at']).replace(':', '-')
        #     print(event['created_at'])
            # print(style.YELLOW('\n[*]') + style.RESET(f' Downloading {current_cam} motion video at {motion_time}...'))
            # mp4_download = current_cam.recording_download(
            #          event['id'],
            #          filename = f'Recordings/{motion_time}.mp4', override=False)
            # sys.exit(0)
        # for event in events2:
        #     print(event['created_at'])
        # for event in events3:
        #     print(event['created_at'])
        # for event in events4:
        #     print(event['created_at'])



if __name__ == "__main__":
    py_ring()
