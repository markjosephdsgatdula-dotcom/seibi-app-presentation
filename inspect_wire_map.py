import asyncio
import sys
from playwright.async_api import async_playwright

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(ignore_https_errors=True, viewport={'width': 1280, 'height': 800})
        page = await context.new_page()
        
        print("Navigating...")
        await page.goto("https://192.168.11.57:3001/", wait_until='load')
        await page.wait_for_timeout(2000)
        
        # Login
        print("Logging in...")
        await page.click("text=Ma-Ku")
        await page.wait_for_timeout(2000)
        
        # Click #tab-wiremap
        print("Clicking #tab-wiremap...")
        await page.click("#tab-wiremap")
        await page.wait_for_timeout(3000)
        
        # Click #wm-eq-pillar-a
        print("Clicking #wm-eq-pillar-a (Pillar A tile)...")
        await page.click("#wm-eq-pillar-a")
        await page.wait_for_timeout(3000)
        
        # Take screenshot
        await page.screenshot(path="debug_pillar_a.png")
        print("Captured debug_pillar_a.png")
        
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
