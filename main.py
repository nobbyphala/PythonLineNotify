#I Gede Putu Nobby Aswi Phala
#5114100048

import requests
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","12345678","test" )

#Line notify token
token = "Bearer 4lV2tBj5bpYT65q0hpojlwn5A22JOSjJELIAQJYMn8X"
line_api_url = "https://notify-api.line.me/api/notify" #Line notify POST API URL
headers = {
    "Content-Type" : "application/x-www-form-urlencoded",
    "Authorization" : token
} #header comply to line notify documentation


def getAllData(table):
    #SQL
    sql = "SELECT * FROM {} ".format(table)

    #cursor for get data and execute sql statement
    cur = db.cursor()
    cur.execute(sql)

    #return the results
    return cur.fetchall()

def sendMessage(message):
    data = {
        "message":message
    }#POST param

    #Make request
    req = requests.post(line_api_url, headers=headers, data=data)

    return req.text #return respone

def main():

    tableData = getAllData("class")

    for row in tableData:
        message = "name: {} \n type: {} \n".format(row[1],row[2])
        ret = sendMessage(message)

        print(ret)

main()
