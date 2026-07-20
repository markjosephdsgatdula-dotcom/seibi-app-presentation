import sys
import asyncio
from playwright.async_api import async_playwright

# Reconfigure stdout for UTF-8 encoding on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

async def run():
    async with async_playwright() as p:
        print("Launching browser...")
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            ignore_https_errors=True,
            viewport={'width': 1280, 'height': 800}
        )
        page = await context.new_page()
        
        url = 'https://192.168.11.57:3001/'
        print(f"Navigating to {url}...")
        try:
            await page.goto(url, wait_until='load', timeout=15000)
            await page.wait_for_timeout(2000)
            
            # Log in as Ma-Ku
            print("Logging in as 'Ma-Ku'...")
            await page.click("text=Ma-Ku")
            await page.wait_for_timeout(3000)
            
            # 1. Capture Dashboard
            print("Saving Dashboard screenshot...")
            await page.screenshot(path='app_dashboard.png')
            
            # 2. Go to Wire Map
            print("Navigating to 'Wire Map'...")
            # We target the .nav-label containing the text to avoid matching titles
            await page.locator(".nav-label", has_text="Wire Map").click()
            await page.wait_for_timeout(2000)
            await page.screenshot(path='app_wire_map.png')
            
            # 3. Go to 履歴 (History)
            print("Navigating to '履歴' (History)...")
            await page.locator(".nav-label", has_text="履歴").click()
            await page.wait_for_timeout(2000)
            await page.screenshot(path='app_history.png')
            
            # 4. Go to 掲示板 (Bulletin Board)
            print("Navigating to '掲示板' (Bulletin Board)...")
            await page.locator(".nav-label", has_text="掲示板").click()
            await page.wait_for_timeout(2000)
            await page.screenshot(path='app_bulletin.png')
            
            # 5. Go to マニュアル (Manuals)
            print("Navigating to 'マニュアル' (Manuals)...")
            await page.locator(".nav-label", has_text="マニュアル").click()
            await page.wait_for_timeout(2000)
            await page.screenshot(path='app_manuals.png')
            
            print("All screenshots successfully captured!")
            
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            await browser.close()

if __name__ == '__main__':
    asyncio.run(run())
