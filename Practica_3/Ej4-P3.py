import os
import csv
from collections import Counter

logs = 'BBB_nuevo.csv'
with open(os.path.join(logs)) as logs_moodle:
    data_logs = csv.reader(logs_moodle, delimiter=',')
    header , logs_recurso = next(data_logs), list(data_logs )

dias = {}

for lin in logs_recurso:
    reg = lin[0].split()
    if reg[0] in dias.keys():
        dias[reg[0]] += 1
    else:
        dias[reg[0]] = 1

dias_mas_reg = Counter(dias).most_common(7)
print("Dias con mas registros")
print(dict(dias_mas_reg))