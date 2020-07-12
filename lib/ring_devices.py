from lib.color import style

def get_devices(devices):
    try:
        print('   --- All Ring Devices ---   ')

        print(style.GREEN('\n[+]') + style.RESET(' Ring Stickup Cameras:'))
        if  devices['stickup_cams']:
            for stickup_cam in devices['stickup_cams']:
                print(style.YELLOW('    [-]') + style.RESET(str(stickup_cam)))
        else:
            print(style.RED('[!]') + style.RESET(' Error: Cannot find any stickup camera.'))

        print(style.GREEN('\n[+]') + style.RESET(' Ring Doorbells:'))
        if  devices['doorbots']:
            for doorbell in devices['doorbots']:
                print(style.YELLOW('    [-]') + style.RESET(str(doorbell)))
        else:
            print(style.RED('   [!]') + style.RESET(' Error: Cannot find any doorbells.'))


        print(style.GREEN('\n[+]') + style.RESET(' Ring Chimes:'))
        if  devices['chimes']:
            for chime in devices['chimes']:
                print(style.YELLOW('    [-]') + style.RESET(str(chime)))
        else:
            print(style.RED('   [!]') + style.RESET(' Error: Cannot find any chimes.'))

        input(style.YELLOW('\n[*]') + style.RESET(' Press any key to return to PyRing main menu.'))

    except KeyboardInterrupt:
        print (u"{}[2J{}[;H".format(chr(27), chr(27)))
        print(style.RED('\n[!]') + style.RESET(' Error: User exit.'))
        print(style.GREEN('[+]') + style.RESET(' Thank you for using PyRing.'))
        print(style.GREEN('[+]') + style.RESET(' Author: Pr0xy07'))
        print(style.GREEN('[+]') + style.RESET(' If you need any help, contact: pr0xy07@tutanota.com'))
        sys.exit(0)
