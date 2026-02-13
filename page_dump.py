#!/usr/bin/env python3
import argparse
import ssl
import time
import urllib.request
from bs4 import BeautifulSoup


def fetch(url: str, verify_ssl: bool):
    ctx = None
    if not verify_ssl:
        ctx = ssl._create_unverified_context()

    start = time.time()
    response = urllib.request.urlopen(url, context=ctx)
    duration = time.time() - start

    html = response.read().decode("utf-8", errors="ignore")

    return {
        "status": response.status,
        "headers": dict(response.headers),
        "time": duration,
        "html": html,
    }


def main():
    parser = argparse.ArgumentParser(description="Fetch and inspect web page HTML.")
    parser.add_argument("url", help="Target URL")
    parser.add_argument("--no-ssl-verify", action="store_true", help="Disable SSL verification")
    parser.add_argument("--output", help="Save HTML to file")

    args = parser.parse_args()

    data = fetch(args.url, verify_ssl=not args.no_ssl_verify)

    print(f"URL: {args.url}")
    print(f"Status: {data['status']}")
    print(f"Response time: {data['time']:.3f}s")

    soup = BeautifulSoup(data["html"], "html.parser")
    pretty_html = soup.prettify()

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(pretty_html)
        print(f"Saved to {args.output}")
    else:
        print(pretty_html)


if __name__ == "__main__":
    main()
