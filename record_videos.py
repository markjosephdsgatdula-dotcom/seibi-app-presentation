import os
import sys
import shutil
import asyncio
from playwright.async_api import async_playwright

# Reconfigure stdout for UTF-8 encoding on Windows to prevent console crashes
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

async def record_section(name, action_func):
    async with async_playwright() as p:
        print(f"\n--- Recording video for: {name} ---")
        browser = await p.chromium.launch(headless=True)
        
        # Create context with video recording enabled
        videos_temp_dir = 'videos_temp'
        context = await browser.new_context(
            ignore_https_errors=True,
            viewport={'width': 1280, 'height': 800},
            record_video_dir=videos_temp_dir,
            record_video_size={'width': 1280, 'height': 800}
        )
        
        page = await context.new_page()
        url = 'https://192.168.11.57:3001/'
        print(f"Navigating to {url}...")
        
        try:
            await page.goto(url, wait_until='load', timeout=15000)
            await page.wait_for_timeout(2000)
            
            # Execute the specific actions for this video
            await action_func(page)
            
            # Retrieve video path before closing context
            temp_video_path = await page.video.path()
            print(f"Temporary video saved at: {temp_video_path}")
            
            # Close browser context to flush the video file
            await context.close()
            await browser.close()
            
            # Create final videos directory if it doesn't exist
            os.makedirs('videos', exist_ok=True)
            final_path = os.path.join('videos', f'{name}.webm')
            
            # Move the video to the final location
            if os.path.exists(temp_video_path):
                # If target file exists, remove it first
                if os.path.exists(final_path):
                    os.remove(final_path)
                shutil.move(temp_video_path, final_path)
                print(f"Successfully saved final video to: {final_path}")
            else:
                print(f"Warning: Temporary video file not found at {temp_video_path}")
                
        except Exception as e:
            print(f"An error occurred while recording {name}: {e}")
            await context.close()
            await browser.close()
        
        # Clean up temporary videos directory if empty
        if os.path.exists(videos_temp_dir):
            try:
                shutil.rmtree(videos_temp_dir)
            except Exception:
                pass

# Actions for each slide video
async def do_dashboard(page):
    print("Logging in as 'Ma-Ku'...")
    await page.click("text=Ma-Ku")
    await page.wait_for_timeout(3000)
    
    print("Scrolling down the dashboard...")
    await page.evaluate("window.scrollBy({ top: 300, behavior: 'smooth' })")
    await page.wait_for_timeout(2500)
    await page.evaluate("window.scrollBy({ top: 300, behavior: 'smooth' })")
    await page.wait_for_timeout(2500)

async def do_wire_map(page):
    print("Logging in...")
    await page.click("text=Ma-Ku")
    await page.wait_for_timeout(2000)
    
    print("Going to Wire Map...")
    await page.click("#tab-wiremap")
    await page.wait_for_timeout(2500)
    
    print("Opening Pillar A tile (#wm-eq-pillar-a)...")
    await page.click("#wm-eq-pillar-a")
    await page.wait_for_timeout(4500)

async def do_history(page):
    print("Logging in...")
    await page.click("text=Ma-Ku")
    await page.wait_for_timeout(2000)
    
    print("Going to History...")
    await page.locator(".nav-label", has_text="履歴").click()
    await page.wait_for_timeout(3000)
    
    print("Filtering history...")
    await page.click("text=30日")
    await page.wait_for_timeout(2000)
    await page.click("text=異常あり")
    await page.wait_for_timeout(3000)

async def do_bulletin(page):
    print("Logging in...")
    await page.click("text=Ma-Ku")
    await page.wait_for_timeout(2000)
    
    print("Going to Bulletin Board...")
    await page.locator(".nav-label", has_text="掲示板").click()
    await page.wait_for_timeout(3000)
    
    print("Scrolling down feed...")
    await page.evaluate("window.scrollBy({ top: 200, behavior: 'smooth' })")
    await page.wait_for_timeout(2000)
    
    print("Typing a quick comment...")
    text_area = page.locator("#compose-message")
    await text_area.click()
    await text_area.fill("設備点検および配線の確認を開始します。")
    await page.wait_for_timeout(3000)

async def do_manuals(page):
    print("Logging in...")
    await page.click("text=Ma-Ku")
    await page.wait_for_timeout(2000)
    
    print("Going to Manuals...")
    await page.locator(".nav-label", has_text="マニュアル").click()
    await page.wait_for_timeout(3000)
    
    print("Searching for troubleshooting help...")
    search_input = page.locator("#ts-query-input")
    await search_input.click()
    await search_input.fill("ロボットアームが震えている")
    await page.wait_for_timeout(2000)
    
    print("Clicking AI Q&A...")
    await page.click("text=AIに質問する")
    await page.wait_for_timeout(4000)

async def main():
    await record_section("wire_map", do_wire_map)
    print("\nWire Map video recorded successfully!")

if __name__ == '__main__':
    asyncio.run(main())
