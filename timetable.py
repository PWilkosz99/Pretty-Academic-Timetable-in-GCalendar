import openpyxl

tt = 'timetable.xlsx'
data = openpyxl.load_workbook(tt)
sheet = data.active

GK = [1,2]

for row in sheet.rows:
    for cell in row:
        print(cell.value, end=" ")
