# Python Scripts
Scripts that run on command line of Windows and Terminal of Mac OS and Linux. Tested in Python 3.6.5.

# About
Provided a list of valid email of people. This application will create a csv file containing each of their fullname and linkedin url along with the email.

# Requirements
1. fullcontact api key: 
Visit https://www.fullcontact.com/pricing-plans/ and create an account. After registering and veriying account, generate a fullcontact API key. This key will be asked at the beginning of the program execution.
2. Input a csv file containing just one column named Email and rows containing the emails of people whom you want to get the details of.
Here the input file is named emails.csv.
3. Output file will be named userDetails.csv and will be stored at the same location of the program.
This file will contain three columns - Email, Full Name, Linkedin URL. If the API could not find any of these details then "Not Found" will be the value.

# Packages and imports
1. urllib   |   Install - pip install urllib   |   Import urllib.request
2. json     |   pip install json
3. csv      |   pip install csv
4. os       |   pip install os
5. tkinter  |   pip install tkinter    |  import Tk, messagebox, filedialog
6. validate_email   |   pip install validate_email
