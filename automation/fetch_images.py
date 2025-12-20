import os

IMAGES_DIR = "images"


def fetch_qr_images(page):
    os.makedirs(IMAGES_DIR, exist_ok=True)

    dropdown = page.locator("#select_data")
    options = dropdown.locator("option")
    count = options.count()

    for i in range(1145, count):
        value = options.nth(i).get_attribute("value")
        if not value:
            continue

        dropdown.select_option(value=value)
        page.wait_for_timeout(1500)

        img = page.locator("#blah")
        img_url = img.get_attribute("src")

        if img_url and img_url.startswith("http"):
            response = page.request.get(img_url)
            image_path = os.path.join(IMAGES_DIR, f"qr_{i}.jpg")

            with open(image_path, "wb") as f:
                f.write(response.body())

            print(f"✅ Downloaded {image_path}")
