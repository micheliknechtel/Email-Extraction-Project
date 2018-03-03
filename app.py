from flask import Flask, jsonify
from SerialiseData import SerialiseData
from Repository import Repository

app = Flask(__name__)

data = []

@app.route('/emails', methods=['GET'])
def get_tasks():

    pathOutput = "/Users/micheliknechtel/Documents/xCode/ivizone/json/"
    r = Repository()
    r.checkRepositoryExist(pathOutput)
    jsonFiles = r.getListOfFiles(pathOutput)
    listEmails = []
  
    for i in range (len(jsonFiles)):
        d = {}
        s = SerialiseData(d)
        data = s.readFromFile(pathOutput+jsonFiles[i])
        print(jsonFiles[i])
        emails = data['data']['email']
        
        for e in range(len(emails)):
            listEmails.append(emails[e])
    
    return jsonify({'emails': listEmails})



if __name__ == '__main__':
    app.run(debug=True, port=0)
