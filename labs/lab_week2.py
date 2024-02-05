# This program requests information on all trains currently travelling around Ireland.
# The aim is learning the Request library functionalities and my point of reference is [Real Python](https://realpython.com/python-requests/).
# Program by Andrea Cignoni

import requests
import csv
from xml.dom.minidom import parseString

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc =parseString(page.content)
# check it works.
# print(doc.toprettyxml())

# Storing the xml in a file.

with open("trainxml.xml","w") as xmlfp:
    doc.writexml(xmlfp)

retrieveTags=['TrainStatus',
              'TrainLatitude',
              'TrainLongitude',
              'TrainCode',
              'TrainDate',
              'PublicMessage',
              'Direction'
              ]

# Declaring a new variable that contains all the nodes extracted from the document with the getElementsByTagName().
objTrainPositionsNodes = doc.getElementsByTagName('objTrainPositions')
# Iteration over each node.
for objTrainPositionsNode in objTrainPositionsNodes:
    traincode_node = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
    traincode = traincode_node.firstChild.nodeValue.strip()
    # print(traincode)
    TrainLatitude_Node = objTrainPositionsNode.getElementsByTagName("TrainLatitude").item(0)
    trainlatitude = TrainLatitude_Node.firstChild.nodeValue.strip()
    # print(trainlatitude)

# Storing train codes in CSV file.
with open('week03_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        traincode_node = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        traincode = traincode_node.firstChild.nodeValue.strip()
        
        dataList = []
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
            dataList.append(datanode.firstChild.nodeValue.strip())
        
        train_writer.writerow(dataList)


# Storing train codes startin with D in another CSV file.
with open('week03_traincodes_starting_for_D.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        traincode_node = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        traincode = traincode_node.firstChild.nodeValue.strip()
        
        if traincode.startswith('D'):
             dataList = []
             for retrieveTag in retrieveTags:
                datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
                dataList.append(datanode.firstChild.nodeValue.strip())
                train_writer.writerow(dataList)





