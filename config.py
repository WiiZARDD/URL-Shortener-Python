# config.py

BITLY_ACCESS_TOKEN = "YOUR_BITLY_ACCESS_TOKEN"

BITLY_URL = "https://api-ssl.bitly.com/v4/shorten"
BITLY_HEADERS = {
    "Authorization": f"Bearer {BITLY_ACCESS_TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}
