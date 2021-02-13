import re
import sys
from lib.color import style
from urllib.parse import urlencode
from urllib.request import urlopen


def get_stickup_cam_motion(devices):
    while True:
        print (u"{}[2J{}[;H".format(chr(27), chr(27)))
        print('   --- Ring Stickup Cameras Motion Alerts ---   \n')

        count = 1

        if devices['stickup_cams']:
            for stickup_cam in devices['stickup_cams']:
                print(style.GREEN(f'[0{count}]') + style.RESET(f' {stickup_cam}.'))
                count += 1
            print(style.GREEN(f'[99]') + style.RESET(' Return to motion alerts menu.'))

            try:
                option_ = input(style.YELLOW('\n[+]') + style.RESET(' Choose your option [Eg: 01]: '))
            except KeyboardInterrupt:
                print (u"{}[2J{}[;H".format(chr(27), chr(27)))
                print(style.RED('\n[!]') + style.RESET(' Error: User exit.'))
                print(style.GREEN('[+]') + style.RESET(' Thank you for using PyRing.'))
                print(style.GREEN('[+]') + style.RESET(' Author: Pr0xy07'))
                print(style.GREEN('[+]') + style.RESET(' If you need any help, contact: pr0xy07@tutanota.com'))
                sys.exit(0)

            if option_ == "99":
                print (u"{}[2J{}[;H".format(chr(27), chr(27)))
                print(style.GREEN('\n[+]') + style.RESET(' Thank you for using PyRing.'))
                print(style.GREEN('[+]') + style.RESET(' Author: Pr0xy07'))
                print(style.GREEN('[+]') + style.RESET(' If you need any help, contact: pr0xy07@tutanota.com'))
                break
            else:
                option_ = int(option_) - 1
                current_cam = devices['stickup_cams'][option_]

            for event in current_cam.history(limit = 1):
                motion_time = str(event['created_at']).replace(':', '-')


            print(style.YELLOW('\n[*]') + style.RESET(f' Downloading {current_cam} motion video...'))
            recording_cam_name =  re.sub('[^a-zA-Z]+', '', str(current_cam))
            mp4_download = current_cam.recording_download(
                     current_cam.history(limit = 100, kind = 'motion')[0]['id'],
                     filename = f'Recordings/{recording_cam_name} - {motion_time}.mp4', override=True)
            if mp4_download:
                print(style.GREEN('[+]') + style.RESET(f' Downlaoded latest footage from {current_cam}'))
            else:
                None
            print(style.YELLOW('\n[*]') + style.RESET(f' Generating recording video URL...'))
            recording_url = current_cam.recording_url(current_cam.last_recording_id)
            if mp4_download:
                print(style.GREEN('[+]') + style.RESET(f' Recording full URL: {recording_url}'))
            else:
                None


            input(style.YELLOW('\n[*]') + style.RESET(' Press any key to return to devices list.'))
        else:
            print(style.RED('   [!]') + style.RESET(' Error: Cannot find any stickup cameras.'))
            input(style.YELLOW('\n[*]') + style.RESET(' Press any key to return to devices list.'))
            break


def get_doorbell_cam_motion(devices):
    while True:
        print (u"{}[2J{}[;H".format(chr(27), chr(27)))
        print('   --- Ring Doorbell Cameras Motion Alerts ---   \n')

        count = 1

        if devices['doorbots']:
            for doorbell in devices['doorbots']:
                print(style.GREEN(f'[0{count}]') + style.RESET(f' {doorbell}.'))
                count += 1
            print(style.GREEN(f'[99]') + style.RESET(' Return to motion alerts menu.'))

            try:
                option_ = input(style.YELLOW('\n[+]') + style.RESET(' Choose your option [Eg: 01]: '))
            except KeyboardInterrupt:
                print (u"{}[2J{}[;H".format(chr(27), chr(27)))
                print(style.RED('\n[!]') + style.RESET(' Error: User exit.'))
                print(style.GREEN('[+]') + style.RESET(' Thank you for using PyRing.'))
                print(style.GREEN('[+]') + style.RESET(' Author: Pr0xy07'))
                print(style.GREEN('[+]') + style.RESET(' If you need any help, contact: pr0xy07@tutanota.com'))
                sys.exit(0)

            if option_ == "99":
                print (u"{}[2J{}[;H".format(chr(27), chr(27)))
                print(style.GREEN('\n[+]') + style.RESET(' Thank you for using PyRing.'))
                print(style.GREEN('[+]') + style.RESET(' Author: Pr0xy07'))
                print(style.GREEN('[+]') + style.RESET(' If you need any help, contact: pr0xy07@tutanota.com'))
                break
            else:
                option_ = int(option_) - 1
                current_cam = devices['doorbots'][option_]

            recording_cam_name =  re.sub('[^a-zA-Z]+', '', str(current_cam))
            print(current_cam)

            for event in current_cam.history(limit = 1000, enforce_limit=True, retry=10):
                print(event['created_at'])

                if event['created_at'].month == 11:
                    motion_time = str(event['created_at']).replace(':', '-')
                    id_to_get = event['id']

                    print(style.YELLOW('\n[*]') + style.RESET(f' Downloading {current_cam} motion video...'))
                    # mp4_download = current_cam.recording_download(
                    #          id_to_get,
                    #          filename = f'Recordings/{recording_cam_name} - {motion_time}.mp4', override=True)
                    # if mp4_download:
                    #     print(style.GREEN('[+]') + style.RESET(f' Downlaoded footage from {current_cam} at {motion_time}'))
                    # else:
                    #     None
                    # print(style.YELLOW('\n[*]') + style.RESET(f' Generating recording video URL...'))
                    # recording_url = current_cam.recording_url(current_cam.last_recording_id)
                    # if mp4_download:
                    #     print(style.GREEN('[+]') + style.RESET(f' Recording full URL: {recording_url}'))
                    # else:
                    #     None

            input(style.YELLOW('\n[*]') + style.RESET(' Press any key to return to devices list.'))

        else:
            print(style.RED('   [!]') + style.RESET(' Error: Cannot find any doorbell cameras.'))
            input(style.YELLOW('\n[*]') + style.RESET(' Press any key to return to devices list.'))
            break


def get_motions(devices):
    while True:
        print (u"{}[2J{}[;H".format(chr(27), chr(27)))
        print('   --- Ring Motion Alerts ---   \n')
        print(style.GREEN('[01]') + style.RESET(' Ring stickup camera motion video.'))
        print(style.GREEN('[02]') + style.RESET(' Ring doorbell camera motion video..'))
        print(style.GREEN('[99]') + style.RESET(' PyRing main menu.'))

        try:
            option = input(style.YELLOW('\n[+]') + style.RESET(' Choose your option [Eg: 01]: '))
        except KeyboardInterrupt:
            print (u"{}[2J{}[;H".format(chr(27), chr(27)))
            print(style.RED('\n[!]') + style.RESET(' Error: User exit.'))
            print(style.GREEN('[+]') + style.RESET(' Thank you for using PyRing.'))
            print(style.GREEN('[+]') + style.RESET(' Author: Pr0xy07'))
            print(style.GREEN('[+]') + style.RESET(' If you need any help, contact: pr0xy07@tutanota.com'))
            sys.exit(0)


        if option == "01":
            get_stickup_cam_motion(devices)
        elif option == "02":
            get_doorbell_cam_motion(devices)
        elif option == "99":
            print (u"{}[2J{}[;H".format(chr(27), chr(27)))
            print(style.GREEN('\n[+]') + style.RESET(' Thank you for using PyRing.'))
            print(style.GREEN('[+]') + style.RESET(' Author: Pr0xy07'))
            print(style.GREEN('[+]') + style.RESET(' If you need any help, contact: pr0xy07@tutanota.com'))
            break
