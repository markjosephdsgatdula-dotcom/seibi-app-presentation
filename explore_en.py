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
            
            # Click Ma-Ku
            print("Logging in as 'Ma-Ku'...")
            await page.click("text=Ma-Ku")
            await page.wait_for_timeout(3000)
            
            # Click 'EN' language toggle
            print("Switching language to English...")
            # We see 'us EN' in the top right
            en_button = page.locator("text=us EN")
            await en_button.click()
            await page.wait_for_timeout(2000)
            
            # Save screenshot of English Dashboard
            screenshot_path = 'app_maku_dashboard_en.png'
            await page.screenshot(path=screenshot_path)
            print(f"Screenshot successfully saved to: {screenshot_path}")
            
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            await browser.close()

if __name__ == '__main__':
    asyncio.run(run())
