# Getting user access token.
import os
import sys
import json
import getpass
from lib.color import style
from pathlib import Path
from ring_doorbell import Ring, Auth
from oauthlib.oauth2 import MissingTokenError

token_file = Path('ring_access_token.json')


def update_token(token):
    token_file.write_text(json.dumps(token, indent = 4))

def two_factor_authentication(email):
    try:
	       auth_code = input(style.YELLOW('[+]') + style.RESET(f' Enter two factor authentication token sent to {email}: '))
	       return auth_code
    except KeyboardInterrupt:
        print (u"{}[2J{}[;H".format(chr(27), chr(27)))
        print(style.RED('\n[!]') + style.RESET(' Error: User exit.'))
        print(style.GREEN('[+]') + style.RESET(' Thank you for using PyRing.'))
        print(style.GREEN('[+]') + style.RESET(' Author: Pr0xy07'))
        print(style.GREEN('[+]') + style.RESET(' If you need any help, contact: pr0xy07@tutanota.com'))
        sys.exit(0)
    except:
        print (u"{}[2J{}[;H".format(chr(27), chr(27)))
        print(style.RED('\n[!]') + style.RESET(' Error: Connot verify the authentication token.'))
        print(style.GREEN('[+]') + style.RESET(' Thank you for using PyRing.'))
        print(style.GREEN('[+]') + style.RESET(' Author: Pr0xy07'))
        print(style.GREEN('[+]') + style.RESET(' If you need any help, contact: pr0xy07@tutanota.com'))
        sys.exit(0)

def get_access_token():
    auth = Auth("PyRing/1.0.0", None, update_token)

    if not os.path.exists(token_file):
        try:
            print('   --- Get Ring Access Token ---   \n')
            try:
                email = str(input(style.YELLOW('[+]') + style.RESET(f' Ring Email: ')))
            except KeyboardInterrupt:
                print (u"{}[2J{}[;H".format(chr(27), chr(27)))
                print(style.RED('\n[!]') + style.RESET(' Error: User exit.'))
                print(style.GREEN('[+]') + style.RESET(' Thank you for using PyRing.'))
                print(style.GREEN('[+]') + style.RESET(' Author: Pr0xy07'))
                print(style.GREEN('[+]') + style.RESET(' If you need any help, contact: pr0xy07@tutanota.com'))
                sys.exit(0)

            try:
                password = str(getpass.getpass(style.YELLOW('[+]') + style.RESET(f' Ring Password: ')))
            except KeyboardInterrupt:
                print (u"{}[2J{}[;H".format(chr(27), chr(27)))
                print(style.RED('\n[!]') + style.RESET(' Error: User exit.'))
                print(style.GREEN('[+]') + style.RESET(' Thank you for using PyRing.'))
                print(style.GREEN('[+]') + style.RESET(' Author: Pr0xy07'))
                print(style.GREEN('[+]') + style.RESET(' If you need any help, contact: pr0xy07@tutanota.com'))
                sys.exit(0)

            auth.fetch_token(email, password)
            get_access_token.auth = Auth("PyRing/1.0.0", json.loads(token_file.read_text()), update_token)

        except MissingTokenError:
            auth.fetch_token(email, password, two_factor_authentication(email))
            get_access_token.auth = Auth("PyRing/1.0.0", json.loads(token_file.read_text()), update_token)
        except:
            print (u"{}[2J{}[;H".format(chr(27), chr(27)))
            print(style.RED('\n[!]') + style.RESET(' Cannot log in with the provided credentials, exiting...'))
            print(style.GREEN('[+]') + style.RESET(' Thank you for using PyRing.'))
            print(style.GREEN('[+]') + style.RESET(' Author: Pr0xy07'))
            print(style.GREEN('[+]') + style.RESET(' If you need any help, contact: pr0xy07@tutanota.com'))
            sys.exit(0)
    else:
        get_access_token.auth = Auth("PyRing/1.0.0", json.loads(token_file.read_text()), update_token)
