# This is a module that provides a set of functions to interact with
# the demonstration book API hosted at PythonAnyhwere

import requests
import json
url = "http://andrewbeatty1.pythonanywhere.com/books"

def getallbooks():
    response = requests.get(url)
    return response.json()

def getBookById(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()

def createBook(book):
    book= {
        'Author':"test",
        'Title': "test title",
        "Price": 123
    }
    response = requests.post(url, json=book)
    # headers ={ "Content-type": "application/jason"}
    # response = requests.post(url, data=json.dumps(book), headers=headers)

    return response.json()

def updatebook(id, bookdiff):
    updateurl = url + "/" + str(id)
    response = requests.put(updateurl, json=bookdiff)
    return response.json()

def deleteBook(id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()

if __name__ == "__main__":
    book= {
        'Author':"test",
        'Title': "test title",
        "Price": 123
    }
    bookdiff= {
        "Price": 1000000
    }
    # print(getallbooks())
    # print(getBookById(198))
    # print(deleteBook(515))
    # print (createBook(book))
    print(updatebook(1, bookdiff))