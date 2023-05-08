import requests

from argparse import ArgumentParser

GITHUB_UPSTREAM_RELEASE_ENDPOINT = "https://api.github.com/repos/awslabs/aws-crt-python/releases"
GITHUB_RELEASE_ENDPOINT = "https://api.github.com/repos/qqaatw/aws-crt-python-musllinux/releases"

def check():
    latest_upstream_release_tag = requests.get(GITHUB_UPSTREAM_RELEASE_ENDPOINT).json()[0]["tag_name"].replace("v","")
    latest_release_tag = requests.get(GITHUB_RELEASE_ENDPOINT).json()[0]["tag_name"]

    if latest_upstream_release_tag == latest_release_tag:
        print(f"LATEST=true\nUPSTREAM={latest_upstream_release_tag}\nMAIN={latest_release_tag}")
    else:
        print(f"LATEST=false\nUPSTREAM={latest_upstream_release_tag}\nMAIN={latest_release_tag}")

def update():
    template ="""<!DOCTYPE html><html><body>{}</body></html>"""

    releases = requests.get(GITHUB_RELEASE_ENDPOINT, params={"per_page": 100}).json()
    assets = (
        f'<a href="{asset["browser_download_url"]}">{asset["name"]}</a>' 
        for release in releases for asset in release["assets"]
    )

    with open("index.html", "w", encoding="utf8") as f:
        f.write(template.format("<br>".join(assets)))


if __name__ == "__main__":
    parser = ArgumentParser()
    
    parser.add_argument("--task", choices=["check", "update"], required=True)

    args = parser.parse_args()

    if args.task == "check":
        check()
    elif args.task == "update":
        update()