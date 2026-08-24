import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

search_queries = [
    "33c3",
    "f101",
    "HL-VMAX",
    "VMAX",
    "AHMI",
    "MSUSBDisplay",
    "345f"
]

print("=== SEARCHING GITHUB CODE REPOS ===")
for q in search_queries:
    url = f"https://api.github.com/search/code?q={q}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"})
    try:
        with urllib.request.urlopen(req, context=ctx) as response:
            res = json.loads(response.read().decode())
            total = res.get('total_count', 0)
            print(f"Query '{q}': {total} matches")
            for item in res.get('items', [])[:3]:
                print(f"  - Repo: {item['repository']['full_name']} | File: {item['path']} | URL: {item['html_url']}")
    except Exception as e:
        print(f"Query '{q}' error: {e}")

