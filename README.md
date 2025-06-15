# Playwright Recorder with Flet

This repository provides a simple tool for recording browser actions using Playwright and a Flet-based GUI.

## Features

- Connects to an existing Chromium profile via CDP using its debug port and UUID.
- Opens Playwright Inspector to record actions.
- Automatically accepts browser dialogs (useful for dApps confirmation).
- Attempts to solve non-hCaptcha challenges via the 2Captcha service (API key required).
- Injects a human-like cursor script into the page during recording.

## Usage

1. Install dependencies:

```bash
pip install -r requirements.txt
playwright install
```

2. Run the Flet application:

```bash
python app.py
```

3. Enter the browser profile UUID, optional 2Captcha API key, and the debug port of the running browser.

4. Click **Start recording** to open the Playwright Inspector and interact with the browser. The resulting script can later be reused with any profile that has the same extensions installed.

This is a minimal example intended as a starting point for further automation tasks.
