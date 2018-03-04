from flask import Flask, jsonify
from SerialiseData import SerialiseData
from Repository import Repository
from os import path
import os
app = Flask(__name__)

listEmails = []
topList = {}
topEmails = []

def getTopTenList(number):
    global topEmails
    global topList
    topEmails = []
    e = topList
    sortedItems = sorted(topList, key=topList.get, reverse = True)
    c  = 0
    for i in sortedItems :
        topEmails.append(i)
        c = c + 1
        if  c == number:
            break


def getListEmails():
    global listEmails
    global topList
    pathOutput = os.getcwd() + "/json/"
    r = Repository()
    r.checkRepositoryExist(pathOutput)
    jsonFiles = r.getListOfFiles(pathOutput)
    
    for i in range (len(jsonFiles)):
        d = {}
        s = SerialiseData(d)
        data = s.readFromFile(pathOutput+jsonFiles[i])
        emails = data['data']['email']
        
        for e in range(len(emails)):
            listEmails.append(emails[e])
            if  topList.get(str(emails[e])):
                topList[str(emails[e])] = topList.get(str(emails[e])) + 1
            else:
                topList.update({str(emails[e]):1})


@app.route('/emails', methods=['GET'])
def get_tasks():
    global listEmails
    listEmails = []
    getListEmails()
    return jsonify({'emails': listEmails})

@app.route('/top/n/emails/', methods=['GET'])
def getTopEmails():
    global listEmails
    global topList
    listEmails = []
    topEmails = []
    getListEmails()
    getTopTenList(10)
    return jsonify({'emails': topEmails})

if __name__ == '__main__':
    app.run(debug=True, port=0)




