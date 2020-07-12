import sys
from lib.color import style

def get_alerts(devices):
    try:
        print (u"{}[2J{}[;H".format(chr(27), chr(27)))
        print('   --- All Ring Devices Motion Alerts ---   \n')

        try:
            motion_limit = int(input(style.GREEN('[+]') + style.RESET(' How many latest motion alerts you want to get [EG: 3]: ')))
        except KeyboardInterrupt:
            print (u"{}[2J{}[;H".format(chr(27), chr(27)))
            print(style.RED('\n[!]') + style.RESET(' Error: User exit.'))
            print(style.GREEN('[+]') + style.RESET(' Thank you for using PyRing.'))
            print(style.GREEN('[+]') + style.RESET(' Author: Pr0xy07'))
            print(style.GREEN('[+]') + style.RESET(' If you need any help, contact: pr0xy07@tutanota.com'))
            sys.exit(0)
        except :
            print (u"{}[2J{}[;H".format(chr(27), chr(27)))
            print(style.RED('\n[!]') + style.RESET(' Error: Wrong Input.'))
            print(style.GREEN('[+]') + style.RESET(' Thank you for using PyRing.'))
            print(style.GREEN('[+]') + style.RESET(' Author: Pr0xy07'))
            print(style.GREEN('[+]') + style.RESET(' If you need any help, contact: pr0xy07@tutanota.com'))
            sys.exit(0)

        print(style.GREEN('\n[+]') + style.RESET(' Ring Stickup Cameras:'))
        if  devices['stickup_cams']:
            for stickup_cam in devices['stickup_cams']:
                print(style.YELLOW('    \n[-]') + style.RESET(str(stickup_cam)))
                for event in stickup_cam.history(limit = motion_limit):
                    print(style.CYAN('         [*]') + style.RESET(f' Motion event ID: {event["id"]}'))
                    print(style.CYAN('         [*]') + style.RESET(f' Motion kind: {event["kind"]}'))
                    print(style.CYAN('         [*]') + style.RESET(f' Answered status: {event["answered"]}'))
                    print(style.CYAN('         [*]') + style.RESET(f' Motion time: {event["created_at"]}'))
                    print('-' * 50)
        else:
            print(style.RED('   [!]') + style.RESET(' Error: Cannot find any stickup cameras.'))

        print(style.GREEN('\n[+]') + style.RESET(' Ring Doorbell Cameras:'))
        if  devices['doorbots']:
            for doorbell in devices['doorbots']:
                print(style.YELLOW('    \n[-]') + style.RESET(str(doorbell)))
                for event in doorbell.history(limit = motion_limit):
                    print(style.CYAN('         [*]') + style.RESET(f' Motion event ID: {event["id"]}'))
                    print(style.CYAN('         [*]') + style.RESET(f' Motion kind: {event["kind"]}'))
                    print(style.CYAN('         [*]') + style.RESET(f' Answered status: {event["answered"]}'))
                    print(style.CYAN('         [*]') + style.RESET(f' Motion time: {event["created_at"]}'))
                    print('-' * 50)
        else:
            print(style.RED('   [!]') + style.RESET(' Error: Cannot find any doorbell cameras.'))

        input(style.YELLOW('\n[*]') + style.RESET(' Press any key to return to PyRing main menu.'))
    except KeyboardInterrupt:
        print (u"{}[2J{}[;H".format(chr(27), chr(27)))
        print(style.RED('\n[!]') + style.RESET(' Error: User exit.'))
        print(style.GREEN('[+]') + style.RESET(' Thank you for using PyRing.'))
        print(style.GREEN('[+]') + style.RESET(' Author: Pr0xy07'))
        print(style.GREEN('[+]') + style.RESET(' If you need any help, contact: pr0xy07@tutanota.com'))
        sys.exit(0)
