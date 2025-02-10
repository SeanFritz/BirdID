# Code to set up a directory for the purpose of training the AI model

# Importing the necessary libraries
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# !=!=!=!=! READ THIS IMMEDIATELY - IT'S GENUINELY SO IMPORTANT !=!=!=!=!

# use the command 'pip install selenium beautifulsoup4' in teh command prompt to install the libraries
# ...if you do not have a powershell terminal, install the "Terminal" VS Code extension by Jun Han. It's depreciated, but it works well
# ...you may also need install a web driver on your computer. This program uses the Chrome Webdriver.
# To run via the command prompt, use the command 'python ./Code/DirectoryWebScraper.py'

# Program initialization
# birdSite = 'https://www.allaboutbirds.org/guide/browse.aspx'
birdSite = 'https://www.nj.gov/dep/fgw/chkbirds.htm'   # List of birds in New Jersey - for DataSet directoy population
outputDirectory = 'BirdID/DataSet'                     # Directory to store the images
os.makedirs(outputDirectory, exist_ok=True)            # Create the directory if it does not exist

# Setting up the web driver
driver = webdriver.Chrome()                            # Creates a new instance of the Chrome web driver

# Getting the HTML content of the page
try:
    driver.get(birdSite)                                # Opens the bird list page
    time.sleep(2)                                       # Waits for the page to load
    htmlContent = driver.page_source                    # Gets the HTML content of the page
finally:
    driver.quit()                                       # Closes the web driver

# Parsing the HTML content
birdSoup = BeautifulSoup(htmlContent, 'html.parser')
birdRows = birdSoup.select("table[border'1'] tr")       # Selects the rows of the table

# Extract bird names from the first <td> element of each row
birdNames = []
for row in birdRows[1:]:
    try:
        birdName = row.select_one("td").text.strip()    # Extracts the bird name
        birdNames.append(birdName)                      # Adds the bird name to the list
    except Exception as e:
        print(f"Error reading row: {e}")

# Print the extracted bird names
print("Bird Names:")
for name in birdNames:
    print(name)

# Creating a directory for each bird