import csv

timetable_file = "timetable3isi-1.csv"

def write_csv(filename, data):
    if(len(data) > 0):
        with open(filename, mode='w', encoding="utf-8", newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(["Subject", "Start Date", "Start Time", "End Date", "End Time", "Description", "Location"])
            for row in data:
                writer.writerow([row[3], row[7], str(row[8]), row[7], str(row[9]), row[6], loc(row)])

def loc(rr):
    if(rr[11] == "online" or rr[11] == "on-line"):
        return "online"
    else:
        return rr[10]+" - "+rr[11]

with open(timetable_file, mode='r', encoding="utf-8") as source:

    GW = []
    GA = []
    GP = []
    GL = []
    GSL = []
    GWA = []
    GK = []
    GLC = []
    GS = []

    csv_reader = csv.reader(source, delimiter=';')
    next(csv_reader, None)
    
    category_map = {
        "wykład": GW,
        "ćwiczenia projektowe": GP,
        "ćwiczenia audytoryjne": GA,
        "ćwiczenia laboratoryjne": GL,
        "zajęcia warsztatowe": GWA,
        "konwersatorium": GK,
        "lektorat": GLC,
        "zajęcia seminaryjne": GS,
    }

    for row in csv_reader:
        category = row[4]
        if category in category_map:
            category_map[category].append(row)
        else:
            print("unknown category: " + category)

write_csv("GW.csv", GW)
write_csv("GP.csv", GP)
write_csv("GL.csv", GL)
write_csv("GWA.csv", GWA)
write_csv("GA.csv", GA)
write_csv("GK.csv", GK)
write_csv("GLC.csv", GLC)
write_csv("GS.csv", GS)