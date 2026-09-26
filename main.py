import csv

with open("files/data.csv", newline= "") as file:
    rows = list(csv.DictReader(file))

col_names = rows[0]
col_list = list(rows[0])

framecolname = 'frame'
ecucolname = 'ecu'
frame_list = []

for r in rows:
    frame_list.append(r[framecolname])

frame_list = list(set(frame_list))
selectedFrame = frame_list[0]

ecu_list = list([r[ecucolname] for r in rows if r[framecolname] == selectedFrame])
ecu_list = list(set(ecu_list))
