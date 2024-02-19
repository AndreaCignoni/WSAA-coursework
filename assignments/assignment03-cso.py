# "Exchequer account (historical series)" dataset reader

# This program retrieves the dataset for the "exchequer account (historical series)" from the CSO
# and stores it into a file called "cso.json".
# This operation is achieved by creating 2 functions: 
# 1. 'getAll' that retrieves the JSON data from a specified dataset.
# 2. 'getAllAsFile' that uses getAll to get the data and then writes it to a file.

import requests
import json


# Define the common parts of the URL
urlBeginning="https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd= "/JSON-stat/2.0/en"

# Function to retrieve data for a specific dataset
def getAll(dataset):
    url = urlBeginning + dataset + urlEnd
    # Make a GET request to the URL and parse the JSON response
    response = requests.get(url)
    return response.json()

# Create a jason file with content of the API for a specific dataset
def getAllAsFile(dataset):
    with open("cso.json", "wt") as fp:
        # Call the getAll function with a specific dataset ("FIQ02")
        print(json.dumps(getAll("FIQ02")), file=fp)


if __name__ == '__main__':
    # Call the getAllAsFile function with the dataset "FIQ02"
    getAllAsFile("FIQ02")