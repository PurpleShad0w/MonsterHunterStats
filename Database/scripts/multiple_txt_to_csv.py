import csv

equipment_data = []

for equip_type in range(1, 20):
    with open(f'database/{equip_type}.txt') as file:
        lines = file.readlines()
        for idx, line in enumerate(lines):
            equipment_data.append([equip_type, idx, line.strip()])

with open('equipment.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Type', 'ID', 'Name'])
    csv_writer.writerows(equipment_data)