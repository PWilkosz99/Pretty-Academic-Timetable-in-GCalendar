import openpyxl

tt = 'timetable.xlsx'
data = openpyxl.load_workbook(tt)
sheet = data.active

groups = ["GW01", "GA02", "GĆP02","GĆL03"]


GW=[]
GA=[]
GP=[]
GL=[]
defs = [GW,GA,GP,GL]

for i in range(4):
    for row in sheet.rows:
        if(row[9].value==groups[i]):
            defs[i].append(row)


for row in GP:
    #row[2].value=row[2].value[:10]
    print(row[0].value + "," + row[2].value[:10] + "," + str(row[3].value) + "," + row[2].value[:10] + "," + str(row[4].value) + "," + row[1].value + "," + row[5].value + ",,,,")


