import urllib.request
import urllib.parse
import re

query = 'site:github.com "33c3" OR "f101" OR "HL-VMAX" OR "HL VMAX"'
url = "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(query)

req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0"})

try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        links = re.findall(r'href="([^"]*github\.com[^"]*)"', html)
        print(f"Discovered {len(links)} GitHub links on DuckDuckGo:")
        for l in set(links[:15]):
            print("  ", l)
except Exception as e:
    print("Search error:", e)

