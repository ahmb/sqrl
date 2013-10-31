#!/usr/bin/env python

# TODO Catch connection errors
# TODO Catch sqrlurl format errors
# TODO Add logging option

"""
Usage: sqrl [-d] [-n] [--path=<Dir>] [<SQRLURL>]
       sqrl [-l] [-s <AccountID>] [--create]

Options:
  -d              Debugging output
  -l              List Accounts
  -n              Notify via libnotify (Gnome)
  -s              Set an account as Default
  --create        Create New Account
  --path=<Dir>    Path for config and key storage

Example:
    sqrl -l
    sqrl --id 2a9s8x
    sqrl --create
    sqrl -d "sqrl://example.com/login/sqrl?d=6&nut=a95fa8e88dc499758"
"""

import sys
from . import WORKING_DIR
from . import VERSION
from . import GNOME_ON
from .mkm import MKM
from client import Client
from docopt import docopt
from getpass import getpass
from sqrlgui import gui_get_pass


def main():
    arguments = docopt(__doc__, version=VERSION)

    # Collecting arguments
    url = arguments.get('<SQRLURL>')
    account_id = arguments.get('<AccountID>')
    create_acct = arguments.get('--create')
    bool_notify = arguments.get('-n')
    path = arguments.get('--path')
    debug = arguments.get('-d')
    list = arguments.get('-l')

    if not path:
        path = WORKING_DIR

    manager = MKM(path)

    if account_id:
        select_account(manager, account_id)

    if list:
        list_accounts(manager)

    if create_acct:
        create_account(manager)

    if not debug:
        debug = False

    run(url, manager, debug, bool_notify)


def list_accounts(manager):
    """
    List out ID and Name for each account
    or
    Create account is there are none
    """
    accounts = manager.list_accounts()
    output = []
    if accounts:
        for k in accounts.keys():
            line = accounts[k]['id'] + " [Name: " + accounts[k]['name'] + "]"
            if accounts[k]['active']:
                output.append("* " + line)
            else:
                output.append("  " + line)
        print "\n".join(output)
    else:
        create_account(manager)
    sys.exit()


def export_key(manager, id):
    pass


def delete_account(manager, id):
    pass


def select_account(manager, id):
    if manager.set_account(id):
        list_accounts(manager)
    else:
        print "Invalid Account ID"
    sys.exit()


def create_account(manager):
    try:
        name = raw_input("Please enter name of Account Owner: ")
        pswd = getpass("Please Enter Master Password: ")
        pswd_confirm = getpass("Please Confirm Master Password: ")
        if manager.create_account({'name': name}, pswd, pswd_confirm):
            print "Account Created"
    except:
        print "Account NOT Created"
    sys.exit()


def unlock_account(manager):

    if GNOME_ON:
        password = gui_get_pass()
    else:
        password = getpass("Please Enter Master Password: ")

    key = manager.get_key(password)
    if key:
        return key
    else:
        print "Invalid Password"
        notify("Invalid Password")
        return False


def run(url, manager, debug, bool_notify=False):
    accounts = manager.list_accounts()

    if not accounts:
        create_account(manager)

    masterkey = unlock_account(manager)

    if masterkey is not False:
        # Create sqrl client and submit request
        sqrlclient = Client(masterkey, url, bool_notify, debug)
        sqrlclient.submit()


if __name__ == "__main__":
    main()
