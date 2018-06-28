import urllib.request
import json
import csv
import os
from tkinter import Tk
from tkinter import messagebox
from tkinter import filedialog
from validate_email import validate_email

root = Tk()
root.withdraw()

def options():
    global apiKey
    try:
        apiKey = input("Please enter fullcontact api key...")
    except:
        print("An error occured during inputting file. Please try again")
        return

# select a .csv file containing emails using the file dialog box
def openFile():
    print("Please select a .csv file...")
    try:
        emailFile = filedialog.askopenfilename()
    except:
        print("Error loading File")
    if(emailFile.endswith('.csv')):
        fileOpen = open(emailFile)
        return fileOpen
    else:
        messagebox.showwarning("Warning", "Wrong file format. Please input a valid .csv file")


# Create a new .csv file in the same location of the program. 
def createOutputFile():
    with open("userDetails.csv", 'w+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Email', 'Full Name', 'Linkedin URL'])


# Append fullname and linkedin url for each email into the userDetails.csv file
def writeIntoFile(email, fullname, link):
    # print("File appended fullname = ", fullname, "\n Link : ", link)
    with open("userDetails.csv", 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([email, fullname, link])


# Extract the fullname and linkedin url from json returned by api
def fullcontact(apiKey, email):

    fullname = "Not Found"
    linkedinLink = "Not Found"

    # print("Inside fullcontact: apikey = ", apiKey, " email = ", email)
    try:
        response = urllib.request.urlopen('https://api.fullcontact.com/v2/person.json?apiKey='+ apiKey + '&email='+ email)
    except:
        print("Oops!! can't find any details for ", email)
        writeIntoFile(email, fullname, linkedinLink)
        return()

    jsonData = json.load(response)
    fullnameData = jsonData["contactInfo"]
    socialData = jsonData["socialProfiles"]

    try:
        fullname = fullnameData['fullName']
    except:
        fullname = "Not Found"

    try:
        for item in socialData:
            if (item["type"] == "linkedin"):
                linkedinLink = item['url']
    except:
        linkedinLink = "Not Found"
    
    writeIntoFile(email, fullname, linkedinLink)


def Main():
    options()
    file = openFile()
    # checking error in inputting file
    try:
        fileRead = csv.reader(file)
    except:
        print("No file inputs...Please try again.")
        return

    createOutputFile()

    # Loop through all the rows in the file
    for row in fileRead:
        print(row[0])
        if(validate_email(row[0])):
            fullcontact(apiKey, row[0])

    print("New file (userDetails.csv) created at: ", os.getcwd())


if __name__=='__main__':
    Main()
