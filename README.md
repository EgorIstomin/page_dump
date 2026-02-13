# page_dump

Internal CLI tool for fetching, formatting, and saving HTML page snapshots for diagnostics and analysis in corporate infrastructure.

## Purpose

page_dump provides engineers with a simple and consistent way to capture the actual HTML returned by web services.  
It is designed for troubleshooting, post-deployment validation, and infrastructure diagnostics.

Typical use cases:

- Verify what a site actually returns after deployment
- Diagnose issues with proxies, CDNs, or load balancers
- Capture page snapshots for before/after comparison
- Debug integrations and parsers
- Inspect HTTP responses during incidents

## How It Works

High-level steps:

1. Connect to the target URL
2. Retrieve the raw HTML response
3. Parse and format the document
4. Output to console or save to file
5. Close connection safely

## Requirements

- Python 3.10+
- Internet or internal network access to target resource

Dependencies:

pip install beautifulsoup4

(Standard libraries used: urllib, ssl)

## Quick Start

Run against a target page:

python page_dump.py https://example.com

Save formatted HTML to file:

python page_dump.py https://example.com --output snapshot.html

Disable SSL verification (for internal/self-signed services):

python page_dump.py https://internal.service.local --no-ssl-verify

## Features

- Fetch HTML from any reachable web resource
- Pretty-print formatted HTML
- Save snapshots to file
- Optional SSL verification bypass
- Useful for diagnostics in restricted environments

## Repository Structure

- page_dump.py  
  Main CLI script

- example.jpg  
  Workflow diagram (embedded in README)

- README.md  
  Documentation

## Security Notes

- Avoid using SSL bypass in production environments unless necessary
- Do not store sensitive URLs or credentials in repository history
- Prefer internal secret management for protected resources

## Status

Developed as an internal tool for a specific corporate project.  
Extended features may be added as operational needs evolve.

