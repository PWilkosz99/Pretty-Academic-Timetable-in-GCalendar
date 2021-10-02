import csv

with open('timetable.csv', mode='r', encoding="utf-8") as source:

    GW=[]
    GA=[]
    GP=[]
    GL=[]
    GSL=[]
    GWA=[]
    defs = [GW,GA,GP,GL,GSL]

    csv_reader = csv.reader(source, delimiter=';')
    for row in csv_reader:
        if(row[4]=="wykład"):
            GW.append(row)
        else: 
            if(row[4]=="ćwiczenia projektowe"):
                GP.append(row)
            else:
                if(row[4]=="ćwiczenia laboratoryjne"):
                    GL.append(row)
                else:
                    if(row[4]=="zajęcia warsztatowe"):
                        GWA.append(row)


def loc(rr):
    if(rr[10]=="online"):
        return "online"
    else:
        return rr[10]+"-"+rr[11]

GWF = open("GW.csv", "w", encoding="utf-8")

if GWF.writable():
    GWF.write("Subject,Start Date,Start Time,End Date,End Time,Description,Location,,,,\n")
    for r in GW:
        GWF.write(r[3] + "," + r[7] + "," + str(r[8]) + "," + r[7] + "," + str(r[9]) + "," + r[6] + "," + loc(r) +",,,,\n")

GWF.close()

GPF = open("GP.csv", "w", encoding="utf-8")

if GPF.writable():
    GPF.write("Subject,Start Date,Start Time,End Date,End Time,Description,Location,,,,\n")
    for r in GP:
        GPF.write(r[3] + "," + r[7] + "," + str(r[8]) + "," + r[7] + "," + str(r[9]) + "," + r[6] + "," + loc(r) +",,,,\n")

GPF.close()

GLF = open("GL.csv", "w", encoding="utf-8")

if GLF.writable():
    GLF.write("Subject,Start Date,Start Time,End Date,End Time,Description,Location,,,,\n")
    for r in GL:
        GLF.write(r[3] + "," + r[7] + "," + str(r[8]) + "," + r[7] + "," + str(r[9]) + "," + str(r[6]) + "," + loc(r) +",,,,\n")

GLF.close()

GZWF = open("GWA.csv", "w", encoding="utf-8")

if GZWF.writable():
    GZWF.write("Subject,Start Date,Start Time,End Date,End Time,Description,Location,,,,\n")
    for r in GWA:
        GZWF.write(r[3] + "," + r[7] + "," + str(r[8]) + "," + r[7] + "," + str(r[9]) + "," + r[6] + "," + loc(r) +",,,,\n")

GZWF.close()


#r[10] +"-"+ r[11]

