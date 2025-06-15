import flet as ft
from record import start_recording
import asyncio

def main(page: ft.Page):
    page.title = "Playwright Recorder"
    uuid = ft.TextField(label="Profile UUID", width=400)
    api = ft.TextField(label="2Captcha API", width=400)
    port = ft.TextField(label="Debug port", value="9222", width=200)
    log = ft.Text(value="")

    async def on_start(e):
        log.value = "Connecting..."
        await page.update_async()
        try:
            await start_recording(uuid.value, api.value, int(port.value))
            log.value = "Recording finished"
        except Exception as exc:
            log.value = f"Error: {exc}"
        await page.update_async()

    page.add(uuid, api, port, ft.ElevatedButton("Start recording", on_click=on_start), log)

ft.app(target=main)
