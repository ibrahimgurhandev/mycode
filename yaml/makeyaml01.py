#!/usr/bin/python3
import yaml


def main():
    ## create a blob of data to work with
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},
                   {"name": "Arthur Dent", "species": "Human"}]

    ## display our Python data (a list containing two dictionaries)
    print(hitchhikers)

    ## open a new file in write mode
    with open("galaxyguide.yaml", "w") as zfile:
        yaml.dump(hitchhikers, zfile)


if __name__ == "__main__":
    main()