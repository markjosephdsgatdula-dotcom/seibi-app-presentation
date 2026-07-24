import os
import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        print("Launching browser for verification...")
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()
        
        # Resolve absolute path to index.html
        local_file = os.path.abspath('index.html')
        url = f"file:///{local_file}"
        print(f"Opening local web presentation at: {url}")
        
        try:
            await page.goto(url, wait_until='load')
            await page.wait_for_timeout(2000)
            
            # Capture Slide 1 (Title)
            await page.screenshot(path='web_slide_1.png')
            print("Captured Slide 1: web_slide_1.png")
            
            # Slide 2 to 12
            for slide_num in range(2, 13):
                await page.keyboard.press('ArrowRight')
                await page.wait_for_timeout(2500)  # Wait for animations and videos
                screenshot_name = f"web_slide_{slide_num}.png"
                await page.screenshot(path=screenshot_name)
                print(f"Captured Slide {slide_num}: {screenshot_name}")
                
        except Exception as e:
            print(f"An error occurred during verification: {e}")
        finally:
            await browser.close()

if __name__ == '__main__':
    asyncio.run(run())
