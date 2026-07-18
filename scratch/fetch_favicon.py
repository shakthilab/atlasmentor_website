import urllib.request
import re

url = "https://atlasmentor.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        # Find all link tags
        links = re.findall(r'<link\s+[^>]*>', html)
        print("Found link tags:")
        for link in links:
            if 'icon' in link.lower() or 'shortcut' in link.lower():
                print(link)
except Exception as e:
    print(f"Error fetching url: {e}")
