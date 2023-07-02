
filename = "wimbledon.csv"
index_country = 1
index_champion = 2

def main():
   records = get_records(filename)
   count_number_of_champions, countries = process_records(records)
   display_results(count_number_of_champions, countries)

def process_records(records):
    count_number_of_champions = {}
    countries = set()
    for record in records:
        countries.add(record[index_country])
        try:
            count_number_of_champions[record[index_country]] += 1
        except KeyError:
            count_number_of_champions[record[index_champion]] = 1
    return count_number_of_champions, countries

def display_results(count_number_of_champions, countries):
    print("Wimbledon Champions: ")
    for name, count in count_number_of_champions.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))
def get_records(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records

main()