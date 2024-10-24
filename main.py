from pathlib import Path


# List of folders which should exist for data i/o
folders = [
    'source_files'  # For saved web content
    ,'outputs'      # Output location for scraped data files
]


# Verifying required folders exist and creating them if they are missing
for folder in folders:
    directory = Path(folder)
    # Check if the directory exists
    if not directory.exists():
        # Create the directory
        directory.mkdir(parents=True)
        print(f"Directory '{directory}' seems to be missing, creating it.")
    else:
        pass


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

