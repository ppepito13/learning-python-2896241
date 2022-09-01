# 
# Example file for parsing and processing JSON
# LinkedIn Learning Python course by Joe Marini
#

import urllib.request
import json


def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)

    # now we can access the contents of the JSON like any other Python object
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])
    # output the number of events, plus the magnitude and each event name
    count_events = theJSON["metadata"]["count"]
    print("Events count:", count_events)
    for i in range(0, count_events):
        print("Event:", i, "with magnitude:", theJSON["features"][i]["properties"]["mag"])
    print("-------------")

    # for each event, print the place where it occurred
    for i in theJSON["features"]:
        # doesn't work... hmm?
        print("Event occured in:", i["properties"]["place"])
        # print(i["properties"]["place"])
    print("-------------")
    # print the events that only have a magnitude greater than 4
    for i in range(0, count_events):
        if theJSON["features"][i]["properties"]["mag"] > 4:
            print("Event:", i, "with magnitude:", theJSON["features"][i]["properties"]["mag"])
    print("-------------")
    # print only the events where at least 1 person reported feeling something
    for i in range(0, count_events):
        if theJSON["features"][i]["properties"]["felt"] is not None:
            print("Event:", i, "was felt by:", theJSON["features"][i]["properties"]["felt"])
    print("-------------")
    # other version of the above
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if feltReports is not None:
            print("Event was felt by:", feltReports)

def main():
    # define a variable to hold the source URL
    # In this case we'll use the free data feed from the USGS
    # This feed list all earthquakes for the last day larger than Mag 2.5
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    # Open the URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    # print("result code: " + str(webUrl.getcode()))
    print("result code:", webUrl.getcode())
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print("Received an error, cannot print results", webUrl.getcode())


if __name__ == "__main__":
    main()
