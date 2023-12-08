import csv

equipment_data = []

with open(f'items.txt') as file:
	lines = file.readlines()
	for idx, line in enumerate(lines):
		equipment_data.append([idx, line.strip()])

with open('items.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['ID', 'Name'])
    csv_writer.writerows(equipment_data)