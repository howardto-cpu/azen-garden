"""
Screenshot tool using Python playwright.
Usage: python screenshot.py <url> [label]
Saves to: ./temporary screenshots/screenshot-N[-label].png
"""
import sys, os, re
from pathlib import Path
from playwright.sync_api import sync_playwright

url   = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:3000"
label = sys.argv[2] if len(sys.argv) > 2 else ""

out_dir = Path(__file__).parent / "temporary screenshots"
out_dir.mkdir(exist_ok=True)

existing = [int(m.group(1)) for f in out_dir.iterdir()
            if (m := re.match(r"screenshot-(\d+)", f.name))]
n = max(existing) + 1 if existing else 1

filename = f"screenshot-{n}-{label}.png" if label else f"screenshot-{n}.png"
out_path = out_dir / filename

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.goto(url, wait_until="networkidle")
    page.screenshot(path=str(out_path), full_page=True)
    browser.close()

print(f"Screenshot saved: {out_path}")
