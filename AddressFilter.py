import csv

def count_by_state(filename, target_state):
    with open(filename) as lol:
        reader = csv.DictReader(lol, fieldnames=['first','last','address','city','state','zip'])
        count = 0
        for row in reader:
            if row['state'].strip() == target_state:
                count += 1
        return count

print(count_by_state('addresses.csv', 'NJ'))