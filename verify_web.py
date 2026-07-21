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
            
            # Slide 2
            await page.click('#next-btn')
            await page.wait_for_timeout(2000)
            await page.screenshot(path='web_slide_2.png')
            print("Captured Slide 2: web_slide_2.png")
            
            # Slide 3
            await page.click('#next-btn')
            await page.wait_for_timeout(2000)
            await page.screenshot(path='web_slide_3.png')
            print("Captured Slide 3: web_slide_3.png")
            
            # Slide 4 - State 1: Wire Map
            await page.click('#next-btn')
            await page.wait_for_timeout(2000)
            await page.screenshot(path='web_slide_4_wiremap.png')
            print("Captured Slide 4 (Wire Map active): web_slide_4_wiremap.png")
            
            # Slide 4 - State 2: Wait for wiremap.webm to finish and transition to history.webm
            # The wiremap video is about 4-5 seconds long. Let's wait 6 seconds.
            print("Waiting for Slide 4 video to automatically transition...")
            await page.wait_for_timeout(6000)
            await page.screenshot(path='web_slide_4_history.png')
            print("Captured Slide 4 (History Log active after transition): web_slide_4_history.png")
            
            # Slide 5
            await page.click('#next-btn')
            await page.wait_for_timeout(2000)
            await page.screenshot(path='web_slide_5.png')
            print("Captured Slide 5: web_slide_5.png")
            
            # Slide 6
            await page.click('#next-btn')
            await page.wait_for_timeout(2000)
            await page.screenshot(path='web_slide_6.png')
            print("Captured Slide 6: web_slide_6.png")
            
            # Slide 7
            await page.click('#next-btn')
            await page.wait_for_timeout(2000)
            await page.screenshot(path='web_slide_7.png')
            print("Captured Slide 7: web_slide_7.png")
            
        except Exception as e:
            print(f"An error occurred during verification: {e}")
        finally:
            await browser.close()

if __name__ == '__main__':
    asyncio.run(run())
