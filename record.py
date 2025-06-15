from __future__ import annotations
import asyncio
import os
from pathlib import Path
from typing import Optional

from playwright.async_api import async_playwright, Page
from twocaptcha import TwoCaptcha

CURSOR_JS = Path(__file__).with_name("cursor.js")

async def _autoconfirm(page: Page):
    async def on_dialog(dialog):
        await dialog.accept()
    page.on("dialog", on_dialog)

async def _solve_captcha(page: Page, api_key: str):
    # Placeholder function for solving non-hCaptcha challenges using 2Captcha
    solver = TwoCaptcha(api_key)
    frames = page.frames
    for frame in frames:
        try:
            sitekey = await frame.get_attribute('div[g-recaptcha]', 'data-sitekey')
            if sitekey:
                url = page.url
                result = solver.recaptcha(sitekey=sitekey, url=url)
                code = result.get('code')
                if code:
                    await frame.evaluate(f'document.getElementById("g-recaptcha-response").innerHTML="{code}"')
                    await frame.evaluate('___grecaptcha_cfg.clients[0].R.R.callback()')
        except Exception:
            pass

async def start_recording(uuid: str, api_key: str, debug_port: int):
    ws_endpoint = f"ws://127.0.0.1:{debug_port}/devtools/browser/{uuid}"
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(ws_endpoint)
        context = browser.contexts[0] if browser.contexts else await browser.new_context()
        page = context.pages[0] if context.pages else await context.new_page()
        await page.add_init_script(path=CURSOR_JS)
        await _autoconfirm(page)
        if api_key:
            await _solve_captcha(page, api_key)
        # Start inspector
        await page.pause()
        await browser.close()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Record browser actions via Playwright")
    parser.add_argument("uuid", help="Browser profile UUID")
    parser.add_argument("api", nargs="?", default="", help="2Captcha API key")
    parser.add_argument("--port", type=int, default=9222, help="Debug port")
    args = parser.parse_args()

    asyncio.run(start_recording(args.uuid, args.api, args.port))
