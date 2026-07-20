import asyncio
from playwright.async_api import async_playwright

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
            
            print("Clicking on 'Ma-Ku'...")
            # We look for 'Ma-Ku' text. Playwright's click will find the element containing it.
            # We will use locator('text=Ma-Ku') or get_by_text('Ma-Ku')
            ma_ku_button = page.locator("text=Ma-Ku")
            await ma_ku_button.click()
            
            # Wait for transition/navigation
            print("Waiting for page update...")
            await page.wait_for_timeout(4000)
            
            # Take screenshot of the new state
            screenshot_path = 'app_maku_dashboard.png'
            await page.screenshot(path=screenshot_path)
            print(f"Screenshot successfully saved to: {screenshot_path}")
            
            title = await page.title()
            print(f"New Page Title: {title}")
            
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            await browser.close()

if __name__ == '__main__':
    asyncio.run(run())
