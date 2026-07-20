import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        print("Launching browser...")
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(ignore_https_errors=True)
        page = await context.new_page()
        
        url = 'https://192.168.11.57:3001/'
        try:
            await page.goto(url, wait_until='load', timeout=15000)
            await page.wait_for_timeout(2000)
            await page.click("text=Ma-Ku")
            await page.wait_for_timeout(3000)
            
            # Find elements containing our target texts
            for text in ["Wire Map", "履歴", "掲示板", "マニュアル"]:
                locator = page.locator(f"text='{text}'")
                count = await locator.count()
                print(f"\n--- Elements matching '{text}' ({count} found):")
                for idx in range(count):
                    el = locator.nth(idx)
                    html = await el.evaluate("el => el.outerHTML")
                    is_visible = await el.is_visible()
                    print(f"[{idx}] Visible: {is_visible} | HTML: {html[:300]}")
                    
        except Exception as e:
            print(f"Error: {e}")
        finally:
            await browser.close()

if __name__ == '__main__':
    asyncio.run(run())
