#!/usr/bin/python3

import yaml

def main():
    ## Open a blob of YAML data
    with open("myYAML.yml", "r") as yf:
        ## convert YAML into Python data structures (lists and dictionaries)

        pyyammy = yaml.load(yf,  Loader=yaml.SafeLoader)
    # display our new Python data
    print(pyyammy)

if __name__ == "__main__":
    main()
