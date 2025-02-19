import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm


def check_and_find_platform(row):
    platforms = {
        "WooCommerce": "woocommerce",
        "CS Cart": "cscart.com",
        "Summer Cart": ".summercart.",
        "Jumpseller": "jumpseller.com",
        "Hyva Themes": "hyva.setCookie",
        "X-Cart": "content=\"X-Cart\"",
        "Bilginet": "bilginet.com",
        "Yampi": "yampi.io",
        "Sellix": "sellix.io"
    }

    website = row['E-commerce Site']
    if not website.startswith('https'):
        website = 'https://' + e_ticaret_sitesi

    try:
        response = requests.get(website, timeout=15)
        response.raise_for_status()
        html_code = response.text.lower()

        for platform, keyword in platforms.items():
            if keyword.lower() in html_code:
                return [row['Company Name'], website, platform, "OK"]
        return [row['Company Name'], e_ticaret_sitesi, "Unknown Platform", "OK"]

    except requests.exceptions.RequestException as e:
        return [row['Company Name'], e_ticaret_sitesi, "Connection Error", str(e)]

df = pd.read_excel('you_data_path')

results = []
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(check_and_find_platform, row): row for index, row in df.iterrows()}
    for future in tqdm(as_completed(futures), total=len(df), desc="Processing"):
        result = future.result()
        results.append(result)

platforms_df = pd.DataFrame(results, columns=['Company Name', 'E-comerce Site', 'Platform', 'Status'])

platforms_df.to_excel('add_name_for_output', index=False)

print("Operation complete. Check document for platforms.")
