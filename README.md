# ecommerceplatformdetection
E-commerce Platform Detection
E-commerce Platform Detection Tool
This Python script checks a list of e-commerce websites for their platform information and logs the results in an Excel file. It leverages multi-threading to handle multiple requests concurrently, improving efficiency when processing large datasets.

Table of Contents
Requirements
Installation
Usage
Features
License
Requirements
The script requires the following Python libraries:

requests - for making HTTP requests to each URL.
pandas - for handling and processing data in Excel format.
concurrent.futures - for handling concurrent threads.
Install the necessary libraries using:

bash
Copy code
pip install requests pandas
Installation
Clone or download the repository.

Save your list of e-commerce sites in an Excel file named sampledata.xlsx with the columns:

E Ticaret Sitesi - URL of the e-commerce website
İşletme Unvanı - Business name
Place the Excel file in the same directory as the script.

Usage
Run the script with the following command:
bash
Copy code
python script_name.py
Upon execution, the script will:

Check each website URL to verify if it is accessible.
Attempt to detect the e-commerce platform based on specific keywords in the website's HTML content.
A new file, platforms_istanbul.xlsx, will be generated, listing:

İşletme Unvanı: The business name.
E Ticaret Sitesi: The URL of the e-commerce site.
Platform: The detected e-commerce platform.
Features
URL Validation: Each URL is checked for accessibility; if inaccessible, the error is logged in the console.
Platform Detection: The script identifies the e-commerce platform based on keywords specific to each platform.
Concurrent Processing: By using ThreadPoolExecutor, the script processes multiple websites simultaneously, enhancing performance with larger datasets.
License
This project is free to use and distribute.

