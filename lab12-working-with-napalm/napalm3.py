#!/usr/bin/env python3

import napalm
import sys
import os
import json

def main(config_file):

    if not (os.path.exists(config_file) and os.path.isfile(config_file)):
        msg = "Missing or invalid config file {0}".format(config_file)
        raise ValueError(msg)

    print("Loading config file {0}.".format(config_file))

    driver = napalm.get_network_driver("ios")

    # Connect:
    device = driver(
        hostname="192.168.0.51",
        username="admin",
        password="cisco"
    )

    print("Opening ...")
    device.open()

    print("Loading merging candidate ...")
    device.load_merge_candidate(filename=config_file)

    print("\nDiff:")
    print(device.compare_config())

    try:
        choice = input("\nWould you like to commit these changes? [y/n]: ")
    except NameError:
        choice = input("\nWould you like to commit these changes? [y/n]: ")
    if choice == "y":
        print("Committing ...")
        device.commit_config()
        print(json.dumps(device.get_interfaces_ip(), sort_keys=True, indent=2))
    else:
        print("Discarding ...")
        device.discard_config()

    device.close()
    print("Done.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Please supply the full path to "new_configuration.conf"')
        sys.exit(1)
    config_file = sys.argv[1]
    main(config_file)