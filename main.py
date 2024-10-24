# Importing code libraries so we can use them
from pathlib import Path


# List of folders which should exist for data i/o
folders = [
    'source_files'  # For saved web content
    ,'outputs'      # Output location for scraped data files
]


# This code block will verify required folders exist and create them if they are missing
for folder in folders: # Run this code for each folder in our "folders" list we defined above
    directory = Path(folder) # Create "directory" variable and use our folder string to create a "Path" object
    if not directory.exists(): # If the directory exists, run the below indented code
        directory.mkdir(parents=True) # Create the directory (folder) and make sure it has the correct path (that way it is located in the same folder as this python script
        print(f"Directory '{directory}' seems to be missing, creating it.") # Printing words to the console so we know whats up
    else: # In the case our "if" clause was not True, run this code
        pass # Do nothing, since our direcotry already exists


# ChatGPT ish below

# from bs4 import BeautifulSoup
#
# # Load the HTML file
# with open('page.html', 'r', encoding='utf-8') as file:
#     html_content = file.read()
#
# # Parse the HTML with Beautiful Soup
# soup = BeautifulSoup(html_content, 'html.parser')
#
# # Now you can find elements, e.g., all links
# links = soup.find_all('a')
# for link in links:
#     print(link.get('href'))

