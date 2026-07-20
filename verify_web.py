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
            slide1_path = 'web_slide_1.png'
            await page.screenshot(path=slide1_path)
            print(f"Captured Slide 1: {slide1_path}")
            
            # Click next to advance to Slide 2 (The Challenge)
            print("Advancing to Slide 2...")
            await page.click('#next-btn')
            await page.wait_for_timeout(2000)
            
            # Capture Slide 2
            slide2_path = 'web_slide_2.png'
            await page.screenshot(path=slide2_path)
            print(f"Captured Slide 2: {slide2_path}")
            
            # Click next to check a slide with a screenshot embedded (Slide 3)
            print("Advancing to Slide 3...")
            await page.click('#next-btn')
            await page.wait_for_timeout(2000)
            
            # Capture Slide 3
            slide3_path = 'web_slide_3.png'
            await page.screenshot(path=slide3_path)
            print(f"Captured Slide 3: {slide3_path}")
            
        except Exception as e:
            print(f"An error occurred during verification: {e}")
        finally:
            await browser.close()

if __name__ == '__main__':
    asyncio.run(run())
