import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed

def check_site(url):
    if not url.startswith('http'):
        url = 'https://' + url

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return True, url
    except requests.exceptions.RequestException as e:
        return False, str(e)  # Hataları döndür

def find_platform(url):
    platforms = {  # you can customize these platforms according to your preferences
        "Shopify": "shopify",
        "WooCommerce": "woocommerce",
        "Ticimax": "ticimax",
        "Wix" : "wix",
        "OpenCart": "route=product",
        "Magento": "mage-",
        "PrestaShop": "prestashop",
        "BigCommerce": "bigcommerce"
    }

    if not url.startswith('http'):
        url = 'https://' + url

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        html_code = response.text.lower()

        for platform, keyword in platforms.items():
            if keyword.lower() in html_code:
                return platform, "OK"
        return "Unknown Platform", "OK"

    except requests.exceptions.RequestException as e:
        return None, str(e) 

df = pd.read_excel('/content/sampledata.xlsx') # data path

def process_site(row, processed_urls):
    e_ticaret_sitesi = row['E Ticaret Sitesi']
    if e_ticaret_sitesi in processed_urls:
        return None  

    is_valid, message = check_site(e_ticaret_sitesi)
    processed_urls.add(e_ticaret_sitesi) 

    if is_valid:
        platform, _ = find_platform(e_ticaret_sitesi)
        return [row['İşletme Unvanı'], e_ticaret_sitesi, platform]
    else:
        print(f"{e_ticaret_sitesi}: {message}") 
    return None

valid_sites = []
processed_urls = set() 

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(process_site, row, processed_urls): row for index, row in df.iterrows()}
    for future in as_completed(futures):
        result = future.result()
        if result:
            valid_sites.append(result)

platforms_df = pd.DataFrame(valid_sites, columns=['İşletme Unvanı', 'E Ticaret Sitesi', 'Platform'])

platforms_df.to_excel('platforms.xlsx', index=False)

print("Operation complete. Check platforms.xlsx for platforms.")
