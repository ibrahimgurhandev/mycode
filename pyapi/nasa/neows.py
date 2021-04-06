#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    startdate = "start_date=2019-11-11"

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    # sum = 0
    # #how many hazardous asteroids
    # for date in neodata['near_earth_objects']:
    #     for haz in neodata['near_earth_objects'][date]:
    #         if haz['is_potentially_hazardous_asteroid'] == True:
    #             sum+=1
    # print(sum)
    #
    # name =''
    # size = 0
    # for date in neodata['near_earth_objects']:
    #     for x in neodata['near_earth_objects'][date]:
    #         if x["estimated_diameter"]["kilometers"]["estimated_diameter_max"] > size:
    #             name = x['name']
    #             size = x["estimated_diameter"]["kilometers"]["estimated_diameter_max"]
    # print("Largest asteroid is :", name, "Its size is: ", size, "Kilometers")
    #
    # name =''
    # distance = 10000000000
    # for date in neodata['near_earth_objects']:
    #     for x in neodata['near_earth_objects'][date]:
    #         if float(x["close_approach_data"][0]["miss_distance"]["kilometers"]) < distance:
    #             name = x['name']
    #             distance = float(x["close_approach_data"][0]["miss_distance"]["kilometers"])
    # print("Closest asteroid is :", name, "Its distance away from Earth is: ", distance, "Kilometers")



if __name__ == "__main__":
    main()