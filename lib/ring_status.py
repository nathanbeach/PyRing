import sys
from lib.color import style


def get_status(devices):
    try:
        print('   --- All Ring Devices Status ---   ')
        print(style.GREEN('\n[+]') + style.RESET(' Ring Stickup Cameras:'))
        if  devices['stickup_cams']:
            for stickup_cam in devices['stickup_cams']:
                stickup_cam.update_health_data()
                print(style.YELLOW('    [-]') + style.RESET(str(stickup_cam)))
                print(style.CYAN('         [*]') + style.RESET(f' Device address: {stickup_cam.address}'))
                print(style.CYAN('         [*]') + style.RESET(f' Device ID: {stickup_cam.id}'))
                print(style.CYAN('         [*]') + style.RESET(f' Device type: {stickup_cam.family}'))
                print(style.CYAN('         [*]') + style.RESET(f' Device current battery life: {stickup_cam.battery_life}'))
                print(style.CYAN('         [*]') + style.RESET(f' Device timezone: {stickup_cam.timezone}'))
                print(style.CYAN('         [*]') + style.RESET(f' Device WiFi name: {stickup_cam.wifi_name}'))
                print(style.CYAN('         [*]') + style.RESET(f' Device WiFi strength: {stickup_cam.wifi_signal_strength}\n'))
        else:
            print(style.RED('   [!]') + style.RESET(' Error: Cannot find any stickup cameras.'))

        print(style.GREEN('\n[+]') + style.RESET(' Ring Doorbells:'))
        if  devices['doorbots']:
            for doorbell in devices['doorbots']:
                doorbell.update_health_data()
                print(style.YELLOW('    [-]') + style.RESET(str(doorbell)))
                print(style.CYAN('         [*]') + style.RESET(f' Device address: {doorbell.address}'))
                print(style.CYAN('         [*]') + style.RESET(f' Device ID: {doorbell.id}'))
                print(style.CYAN('         [*]') + style.RESET(f' Device type: {doorbell.family}'))
                print(style.CYAN('         [*]') + style.RESET(f' Device current battery life: {doorbell.battery_life}'))
                print(style.CYAN('         [*]') + style.RESET(f' Device timezone: {doorbell.timezone}'))
                print(style.CYAN('         [*]') + style.RESET(f' Device WiFi name: {doorbell.wifi_name}'))
                print(style.CYAN('         [*]') + style.RESET(f' Device WiFi strength: {doorbell.wifi_signal_strength}\n'))
        else:
            print(style.RED('   [!]') + style.RESET(' Error: Cannot find any doorbells.'))

        print(style.GREEN('\n[+]') + style.RESET(' Ring Chimes:'))
        if  devices['chimes']:
            for chime in devices['chimes']:
                chime.update_health_data()
                print(style.YELLOW('    [-]') + style.RESET(str(chime)))
                print(style.CYAN('         [*]') + style.RESET(f' Device address: {chime.address}'))
                print(style.CYAN('         [*]') + style.RESET(f' Device ID: {chime.id}'))
                print(style.CYAN('         [*]') + style.RESET(f' Device type: {chime.family}'))
                print(style.CYAN('         [*]') + style.RESET(f' Device current battery life: {chime.battery_life}'))
                print(style.CYAN('         [*]') + style.RESET(f' Device timezone: {chime.timezone}'))
                print(style.CYAN('         [*]') + style.RESET(f' Device WiFi name: {chime.wifi_name}'))
                print(style.CYAN('         [*]') + style.RESET(f' Device WiFi strength: {chime.wifi_signal_strength}\n'))
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
