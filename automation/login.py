import os
from playwright.sync_api import sync_playwright
from automation.fetch_images import fetch_qr_images
from automation.fill_form import fill_forms_from_excel

LOGIN_URL = "https://dataincryptpro.online/login"

USERNAME = "sauvikdad64@gmail.com"
PASSWORD = "7005120476"


def automated_login_and_fetch():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.wait_for_load_state("domcontentloaded")
        # Step 1: Login
        page.goto(LOGIN_URL)
        page.fill('input[name="username"]', USERNAME)
        page.fill('input[name="password"]', PASSWORD)
        page.click('button[type="submit"]')

        # Step 2: Wait for dashboard
        page.wait_for_url("**/dashboard", timeout=15000)
        print("✅ Logged in, dashboard loaded")

        # Step 3: Navigate via menu to start-task
        page.click('a[href="https://dataincryptpro.online/start-task"]')

        # Step 4: Wait for QR page UI
        page.wait_for_selector("#select_data", timeout=15000)
        print("✅ QR generation page loaded")

        # Step 5: Fetch images
        # fetch_qr_images(page)
        
        fill_forms_from_excel(page)

        context.storage_state(path="auth.json")
        browser.close()


if __name__ == "__main__":
    automated_login_and_fetch()
