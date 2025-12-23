from openpyxl import load_workbook

wb = load_workbook("data.xlsx")
ws = wb["dataSheet"]

count = 1
for row in ws.iter_rows(min_row=1,max_row=10,values_only=True):
    print(f"\n{count}:{row}")
    count += 1

