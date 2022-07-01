import csv

# filename = input("Dosya ismini giriniz:...")
filename = "data_1.csv"
with open(filename, "r") as file:
    list_raw = csv.DictReader(file)
    list_raw = list(list_raw)

first = list_raw[0]
key1, key2 = list(first.keys())[0], list(first.keys())[1]

list_id = []
set_id = []
for line in list_raw:
    line["id"] = line[key1] + "-" + line[key2]
    list_id.append(line["id"])
set_temp = set(list_id)
for x in set_temp:
    set_id.append(x)
set_id.sort()

file_raw = {}
for x in set_id:
    count = list_id.count(x)
    file_raw[x] = count

file_final = []
for x, y in file_raw.items():
    temp = {"Ada-Parsel": x, "Adet": y}
    file_final.append(temp)

a = file_final[0]
k1, k2 = list(a.keys())[0], list(a.keys())[1]

with open("report_file.csv", "w", newline="") as file:
    titles = [k1, k2]
    writer = csv.DictWriter(file, fieldnames=titles)
    writer.writeheader()
    writer.writerows(file_final)
    print("Dosya <report_file.csv> ismiyle kaydedildi.")
