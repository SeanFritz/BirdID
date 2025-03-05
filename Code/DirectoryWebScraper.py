# Code to set up a directory for the purpose of training the AI model

# Importing the necessary libraries
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# !=!=!=!=! READ THIS IMMEDIATELY - IT'S VERY IMPORTANT !=!=!=!=!

# use the command 'pip install selenium beautifulsoup4' in the command prompt to install the necessary libraries
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
driver.get(birdSite)                                # Opens the bird list page
time.sleep(2)                                       # Waits for the page to load
htmlContent = driver.page_source                    # Gets the HTML content of the page

# Parsing the HTML content
birdSoup = BeautifulSoup(htmlContent, 'html.parser')
birdRows = birdSoup.select("table[border='1'] tr")       # Selects the rows of the table

# Extract bird names from the first <td> element of each row
birdNames = []
for row in birdRows[1:]:
    try:
        birdName = row.select_one("td").text.strip()  # Extracts the bird name
        birdNames.append(birdName)                    # Adds the bird name to the list
    except Exception as e:
        print(f"Error reading row: {e}")

# Print the extracted bird names
# print("Bird Names:")
for name in birdNames:
    print(name)

# Creating a directory for each bird
for name in birdNames:
    birdDirectory = os.path.join(outputDirectory, name)
    if not os.path.exists(birdDirectory):
        os.makedirs(birdDirectory)
        print(f"Directory created for: {name}")
    else:
        print(f"Directory already exists for: {name}, skipping creation.")

    # # Download images for each bird
    # searchUrl = f"https://www.google.com/search?tbm=isch&q{name.replace(' ', '+')}"
    # headers= {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    # }
    # response = requests.get(searchUrl, headers=headers)
    # soup = BeautifulSoup(response.text, 'html.parser')
    # imageTags = soup.find_all("img")

    # for i, imgTag in enumerate(imageTags[:5]):  # Limit to first 30 images
    #         try:
    #             imgUrl = imgTag.get('src') or imgTag.get('data-src')
    #             if imgUrl and imgUrl.startswith('http'):
    #                 imgData = requests.get(imgUrl).content
    #                 imgFileName = os.path.join(birdDirectory, f"{name}_{i+1}.jpg")
    #                 with open(imgFileName, 'wb') as imgFile:
    #                     imgFile.write(imgData)
    #                 print(f"Downloaded {imgFileName}")
    #             else:
    #                 print(f"Invalid URL for image {i+1} for {name}")
    #         except Exception as e:
    #             print(f"Error downloading image {i+1} for {name}: {e}")

    # Download images for each bird
    
    

# Close the web driver after all images are downloaded
driver.quit()