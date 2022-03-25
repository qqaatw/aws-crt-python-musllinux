import sys
import requests

template ="""<!DOCTYPE html>
<html>
  <body>
    {}
  <body>
</html>
"""

releases = requests.get(sys.argv[1]).json()
asset_list = []

for release in releases:
    for asset in release["assets"]:
        asset_list.append(f'<a href="{asset["browser_download_url"]}">{asset["name"]}</a>')

with open("index.html", "w", encoding="utf8") as f:
    f.write(template.format("<br>".join(asset_list)))