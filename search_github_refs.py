import urllib.request
import json

search_terms = ["33c3:f101", "HL-VMAX-USB-Device", "33c3", "f101", "345f:9132", "MSUSBDisplay"]

for term in search_terms:
    print(f"=== SEARCHING GITHUB FOR '{term}' ===")
    url = f"https://api.github.com/search/code?q={term}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            total = data.get("total_count", 0)
            print(f"  Total GitHub code matches for '{term}': {total}")
            for item in data.get("items", [])[:5]:
                print(f"    - {item.get('repository', {}).get('full_name')}: {item.get('path')} ({item.get('html_url')})")
    except Exception as e:
        print(f"  GitHub Search error: {e}")

