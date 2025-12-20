from openpyxl import Workbook,load_workbook

# wb = Workbook()
# ws = wb.active
# ws.title = "Form Data"

# ws.append(['Sauvik','Das',25,80000,'Software Engineer'])

# wb.save("output.xlsx")

wb = load_workbook("output.xlsx")

ws = wb["Form Data"]
ws.append(['Cristiano','Ronaldo',40,80000000,'Best Footballer'])

wb.save("output.xlsx")