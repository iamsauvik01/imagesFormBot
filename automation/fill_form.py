from excel.readExcel import read_excel_rows

def fill_forms_from_excel(page):
    data_rows = read_excel_rows("data.xlsx")

    dropdown = page.locator("#select_data")

    for row in data_rows:
        qr_no = row["qr_no"]

        # 🔹 Select QRCode based on Excel
        dropdown.select_option(
            label=f"QRCode - {qr_no}"
        )

        page.wait_for_timeout(1500)  # allow form to load

        page.fill("#name", row["name"])
        page.fill("#designation", row["designation"])        
        page.fill("#company_name", row["company"])
        page.fill("#website", row["website"])
        page.fill("#address", row["address"])
        page.fill("#email", row["email"])
        page.fill("#office_contact", row["contact"])
        
        page.click("#submitBtn")
        
        try:
            next_button = page.locator("div#barcodeModal button", has_text="Next")
            next_button.wait_for(state="visible", timeout=3000)
            next_button.click()
        except:
             print(f"⚠️ Modal 'Next' button not found for QRCode - {qr_no}: {e}")
        

        print(f"✅ Filled form for QRCode - {qr_no}")


