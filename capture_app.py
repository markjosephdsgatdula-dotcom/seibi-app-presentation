import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        print("Launching browser...")
        browser = await p.chromium.launch(headless=True)
        # Create a new browser context that ignores HTTPS certificate errors
        context = await browser.new_context(
            ignore_https_errors=True,
            viewport={'width': 1280, 'height': 800}
        )
        page = await context.new_page()
        
        url = 'https://192.168.11.57:3001/'
        print(f"Navigating to {url}...")
        try:
            # Navigate and wait for the page to load
            await page.goto(url, wait_until='load', timeout=15000)
            
            # Additional wait to let any client-side JS finish rendering
            await page.wait_for_timeout(3000)
            
            # Print page title
            title = await page.title()
            print(f"Page Title: {title}")
            
            # Save screenshot
            screenshot_path = 'app_landing.png'
            await page.screenshot(path=screenshot_path)
            print(f"Screenshot successfully saved to: {screenshot_path}")
            
            # Let's check some text content on the page
            body_text = await page.inner_text('body')
            print("\nPage body text snippet:")
            print(body_text[:1000])
            
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            await browser.close()

if __name__ == '__main__':
    asyncio.run(run())
