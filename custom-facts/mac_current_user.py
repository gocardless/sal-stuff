#!/usr/bin/python2.7

import os
from os import stat
import plistlib
import datetime
import pwd

managedinstalldir = '/Library/Managed Installs/'
conditionalitemspath = os.path.join(managedinstalldir, 'ConditionalItems.plist')

def get_mac_current_user():
  try:
    return pwd.getpwuid(stat("/dev/console").st_uid).pw_name
  except:
    return ""

def main():

    # CRITICAL! Checks if the ConditionalItems.plist already exists or not
    new_dict = dict(mac_current_user = get_mac_current_user() ) 

    if os.path.exists(conditionalitemspath):
        # "ConditionalItems.plist" exists, so read it FIRST (existing_dict)
        existing_dict = plistlib.readPlist(conditionalitemspath)
        # Create output_dict which joins new data generated in this script with existing data
        output_dict = dict(existing_dict.items() + new_dict.items() ) 
    else:
        # "ConditionalItems.plist" does not exist,
        # output only consists of data generated in this script
        output_dict = new_dict

        # Write out data to "ConditionalItems.plist"
    plistlib.writePlist(output_dict, conditionalitemspath)


if __name__ == '__main__':
    main()
