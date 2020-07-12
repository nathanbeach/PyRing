import sys
from lib.color import style


def lights_on(devices):
    print (u"{}[2J{}[;H".format(chr(27), chr(27)))
    available_cams = []
    count = 1
    for stickup_cam in list(devices['stickup_cams']):
        if stickup_cam.lights:
            available_cams.append(stickup_cam)
            for cam in available_cams:
                print(style.GREEN(f'[{count}]') + style.RESET(f' {cam}'))
                count += 1
            try:
                option = input(style.YELLOW('\n[+]') + style.RESET(' Choose your camera [Eg: 1]: '))
                option = int(option) - 1
                if option > len(available_cams):
                    print (u"{}[2J{}[;H".format(chr(27), chr(27)))
                    print(style.RED('\n[!]') + style.RESET(' Error: Wrong input.'))
                    print(style.GREEN('[+]') + style.RESET(' Thank you for using PyRing.'))
                    print(style.GREEN('[+]') + style.RESET(' Author: Pr0xy07'))
                    print(style.GREEN('[+]') + style.RESET(' If you need any help, contact: pr0xy07@tutanota.com'))
                    sys.exit(0)
                else:
                    available_cams[option].update_health_data()
                    available_cams[option].lights = 'on'
                    print(style.GREEN('[+]') + style.RESET(f' Turned on {available_cams[option]} lights successfully.'))
                    input(style.YELLOW('\n[*]') + style.RESET(' Press any key to return to PyRing light control menu.'))
            except KeyboardInterrupt:
                print (u"{}[2J{}[;H".format(chr(27), chr(27)))
                print(style.RED('\n[!]') + style.RESET(' Error: User exit.'))
                print(style.GREEN('[+]') + style.RESET(' Thank you for using PyRing.'))
                print(style.GREEN('[+]') + style.RESET(' Author: Pr0xy07'))
                print(style.GREEN('[+]') + style.RESET(' If you need any help, contact: pr0xy07@tutanota.com'))
                sys.exit(0)


def lights_off(devices):
    print (u"{}[2J{}[;H".format(chr(27), chr(27)))
    available_cams = []
    count = 1
    for stickup_cam in list(devices['stickup_cams']):
        if stickup_cam.lights:
            available_cams.append(stickup_cam)
            for cam in available_cams:
                print(style.GREEN(f'[{count}]') + style.RESET(f' {cam}'))
                count += 1
            try:
                option = input(style.YELLOW('\n[+]') + style.RESET(' Choose your camera [Eg: 1]: '))
                option = int(option) - 1
                if option > len(available_cams):
                    print (u"{}[2J{}[;H".format(chr(27), chr(27)))
                    print(style.RED('\n[!]') + style.RESET(' Error: Wrong input.'))
                    print(style.GREEN('[+]') + style.RESET(' Thank you for using PyRing.'))
                    print(style.GREEN('[+]') + style.RESET(' Author: Pr0xy07'))
                    print(style.GREEN('[+]') + style.RESET(' If you need any help, contact: pr0xy07@tutanota.com'))
                    sys.exit(0)
                else:
                    available_cams[option].update_health_data()
                    available_cams[option].lights = 'off'
                    print(style.GREEN('[+]') + style.RESET(f' Turned off {available_cams[option]} lights successfully.'))
                    input(style.YELLOW('\n[*]') + style.RESET(' Press any key to return to PyRing light control menu.'))
            except KeyboardInterrupt:
                print (u"{}[2J{}[;H".format(chr(27), chr(27)))
                print(style.RED('\n[!]') + style.RESET(' Error: User exit.'))
                print(style.GREEN('[+]') + style.RESET(' Thank you for using PyRing.'))
                print(style.GREEN('[+]') + style.RESET(' Author: Pr0xy07'))
                print(style.GREEN('[+]') + style.RESET(' If you need any help, contact: pr0xy07@tutanota.com'))
                sys.exit(0)

def light_control(devices):
    while True:
        print (u"{}[2J{}[;H".format(chr(27), chr(27)))
        print('   --- All Ring Devices Status ---   ')
        print(style.YELLOW('\n[*]') + style.RESET(' This will only work with stickup cameras supporting light control.\n'))
        print(style.GREEN('[01]') + style.RESET(' Ring stickup camera lights on.'))
        print(style.GREEN('[02]') + style.RESET(' Ring stickup camera lights off.'))
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
            lights_on(devices)
        elif option == "02":
            lights_off(devices)
        elif option == "03":
             break
        elif option == "99":
            print (u"{}[2J{}[;H".format(chr(27), chr(27)))
            print(style.GREEN('\n[+]') + style.RESET(' Thank you for using PyRing.'))
            print(style.GREEN('[+]') + style.RESET(' Author: Pr0xy07'))
            print(style.GREEN('[+]') + style.RESET(' If you need any help, contact: pr0xy07@tutanota.com'))
            break
        else:
            print (u"{}[2J{}[;H".format(chr(27), chr(27)))
            print(style.RED('\n[!]') + style.RESET(' Error: Wrong input.'))
            print(style.GREEN('[+]') + style.RESET(' Thank you for using PyRing.'))
            print(style.GREEN('[+]') + style.RESET(' Author: Pr0xy07'))
            print(style.GREEN('[+]') + style.RESET(' If you need any help, contact: pr0xy07@tutanota.com'))
            sys.exit(0)
