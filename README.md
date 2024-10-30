# E-commerce Platform Detection 

This Python script checks a list of e-commerce websites for their platform information and logs the results in an Excel file. It leverages multi-threading to handle multiple requests concurrently, improving efficiency when processing large datasets. The sample data taken from ETBİS. (https://www.eticaret.gov.tr/)

# Requirements
The script requires the following Python libraries:

- requests - for making HTTP requests to each URL.
- pandas - for handling and processing data in Excel format.
- concurrent.futures - for handling concurrent threads.

# Installation

Clone or download the repository.

Save your list of e-commerce sites in an Excel file named sampledata.xlsx with the columns:

- E Ticaret Sitesi - URL of the e-commerce website
- İşletme Unvanı - Business Name
- Place the Excel file in the same directory as the script.

A new file, platforms.xlsx, will be generated, listing:

- İşletme Unvanı: The business name.
- E Ticaret Sitesi: The URL of the e-commerce site.
- Platform: The detected e-commerce platform.

# Notes

- Platform List Customization: The list of platforms in the script is based on popular e-commerce platforms, but it can be modified as needed. New platforms can be added or existing ones updated in the platforms dictionary within the find_platform function.
- Keyword Matching: Each platform is identified based on specific keywords found in the website's HTML. For accurate detection, you may adjust the keywords for new or less common platforms.

