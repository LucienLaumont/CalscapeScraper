---

# 🌿 Calscape Nursery Scraper

This Scrapy project crawls the [Calscape.org California Nurseries](https://calscape.org/california-nurseries) directory to extract useful data about native plant nurseries in California.

---

## 🚀 What It Does

For each nursery listed on the Calscape website, the scraper collects:

- ✅ **Name** of the nursery  
- ✅ **Address**  
- ✅ **Phone number**  
- ✅ **Email** (including decoding from Cloudflare email protection)  
- ✅ **Website URL**  
- ✅ **List of available plants** from the nursery's inventory page (as a unique set of plant names)

---

## 🧠 How It Works

1. **Starts** from the main nursery listing page:  
   `https://calscape.org/california-nurseries`

2. For each nursery card found, the spider:
   - Extracts metadata (name, address, phone, email, website)
   - Follows the "View inventory" link

3. On the inventory page (if it exists), it:
   - Extracts the **names of all available plants**
   - Removes duplicates and stores them as a **unique list**

4. The email is extracted even when it's **protected by Cloudflare** (`data-cfemail`) thanks to a decoding function built into the spider.

---

## 📝 Output Example

Each item is exported as a JSON object with the following structure:

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

If no inventory is available, the `inventory` field is set to `null`.
