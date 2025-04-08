import json
import csv

input_file = "nurseries.json"   
output_file = "nurseries.csv"

with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

if isinstance(data, dict):
    data = [data]

with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

print(f"Conversion done : {output_file}")
