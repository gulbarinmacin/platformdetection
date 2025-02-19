# Platform Detection 

This Python script checks a list of websites for their platform provider information and logs the results in an Excel file. It leverages multi-threading to handle multiple requests concurrently, improving efficiency when processing large datasets. The sample data taken from ETBİS. (https://www.eticaret.gov.tr/)

# Requirements
The script requires the following Python libraries:

- requests - for making HTTP requests to each URL.
- pandas - for handling and processing data in Excel format.
- concurrent.futures - for handling concurrent threads.

# Notes

- Platform List Customization: The list of platforms in the script is based on popular e-commerce platforms, but it can be modified as needed. New platforms can be added or existing ones updated in the platforms dictionary within the find_platform function.
- Keyword Matching: Each platform is identified based on specific keywords found in the website's HTML. For accurate detection, you may adjust the keywords for new or less common platforms.

