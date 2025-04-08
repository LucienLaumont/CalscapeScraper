---

# 🌿 Calscape Nursery Scraper

This Scrapy project crawls the [Calscape.org California Nurseries](https://calscape.org/california-nurseries) directory to extract useful data about native plant nurseries in California.

---

## 🚀 What It Does

For each nursery listed on the Calscape website, the scraper collects:

- ✅ **Name** of the nursery  
- ✅ **Address**  
- ✅ **Phone number**  
- ✅ **Email** (even if protected by Cloudflare)  
- ✅ **Website URL**  
- ✅ **List of available plants** (from the nursery's inventory page, without duplicates)

If the inventory page is empty or missing, the `inventory` field is set to `null`.

---

## ⚙️ Setup Instructions

1. **Create and activate a virtual environment** (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate     # On Windows
```

2. **Install dependencies** listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 🧪 How to Run the Scraper

Use the following command to run the scraper and export the results to a JSON file:

```bash
scrapy crawl calscape -o nurseries.json
```

This will create a file named `nurseries.json` containing one entry per nursery.

---

## ⚠️ Notes on Request Rate

By default, the scraper is configured to send **1 request per second** using:

```python
DOWNLOAD_DELAY = 1
```

You can **increase this delay** (e.g. to `2` or `3` seconds) if you notice the site becoming unresponsive or blocking requests.  
This helps reduce the load on the server and improves reliability over long runs.

To change it temporarily, you can also use:

```bash
scrapy crawl calscape -o nurseries.json -s DOWNLOAD_DELAY=2
```

---

## 📝 Sample Output

```json
{
  "name": "Bay Natives",
  "adress": "10 Cargo Way San Francisco, CA 94124",
  "phone": "(415) 287-6755",
  "mail": "info@baynatives.com",
  "website_url": "https://www.facebook.com/bay.natives/about",
  "inventory": [
    "Common Yarrow",
    "California Poppy",
    "Sticky Monkeyflower"
  ]
}
```

---

## ⚖️ Legal Disclaimer

This scraper accesses publicly available data and decodes obfuscated email addresses solely for educational or research purposes.  
Please ensure that your usage of the extracted data complies with all applicable laws and the [Calscape.org terms of service](https://calscape.org).

---
