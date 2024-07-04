import csv


class Country:
    def __init__(self, name, city_id=None):
        global country_id_counter
        self.id = country_id_counter
        country_id_counter += 1
        self.name = name
        self.city_id = city_id

    def __str__(self):
        return f"Country(ID: {self.id}, Name: {self.name}, City ID: {self.city_id})"


class City:
    def __init__(self, name):
        global city_id_counter
        self.id = city_id_counter
        city_id_counter += 1
        self.name = name
        self.streets = []

    def __str__(self):
        return f"City(ID: {self.id}, Name: {self.name}, Streets: {[street.name for street in self.streets]})"


class Street:
    def __init__(self, name, city_id):
        global street_id_counter
        self.id = street_id_counter
        street_id_counter += 1
        self.name = name
        self.city_id = city_id

    def __str__(self):
        return f"Street(ID: {self.id}, Name: {self.name}, City ID: {self.city_id})"


# Глобальные счетчики ID
country_id_counter = 0
city_id_counter = 0
street_id_counter = 0


def add_country(countries):
    name = input("Enter country name: ")
    city_id = int(input("Enter city ID: ")) if input(
        "Does the country have a city ID? (y/n): ").lower() == 'y' else None
    countries.append(Country(name, city_id))


def add_city(cities):
    name = input("Enter city name: ")
    cities.append(City(name))


def add_street(streets):
    name = input("Enter street name: ")
    city_id = int(input("Enter city ID: "))
    streets.append(Street(name, city_id))


def remove_country(countries):
    country_id = int(input("Enter country ID to remove: "))
    for country in countries:
        if country.id == country_id:
            countries.remove(country)
            return
    print("Country not found!")


def remove_city(cities):
    city_id = int(input("Enter city ID to remove: "))
    for city in cities:
        if city.id == city_id:
            cities.remove(city)
            return
    print("City not found!")


def remove_street(streets):
    street_id = int(input("Enter street ID to remove: "))
    for street in streets:
        if street.id == street_id:
            streets.remove(street)
            return
    print("Street not found!")


def update_country(countries):
    country_id = int(input("Enter current country ID: "))
    for country in countries:
        if country.id == country_id:
            name = input("Enter new country name: ")
            country.name = name
            return
    print("Country not found!")


def update_city(cities):
    city_id = int(input("Enter current city ID: "))
    for city in cities:
        if city.id == city_id:
            name = input("Enter new city name: ")
            city.name = name
            return
    print("City not found!")


def update_street(streets):
    street_id = int(input("Enter current street ID: "))
    for street in streets:
        if street.id == street_id:
            name = input("Enter new street name: ")
            street.name = name
            return
    print("Street not found!")


def save_to_csv(countries, cities, streets, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Country ID', 'Country Name', 'City ID'])
        for country in countries:
            writer.writerow([country.id, country.name, country.city_id])

        writer.writerow(['City ID', 'City Name'])
        for city in cities:
            writer.writerow([city.id, city.name])

        writer.writerow(['Street ID', 'Street Name', 'City ID'])
        for street in streets:
            writer.writerow([street.id, street.name, street.city_id])


def load_from_csv(filename):
    global country_id_counter, city_id_counter, street_id_counter
    countries = []
    cities = []
    streets = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        section = None
        for row in reader:
            if not row:
                section = None
                continue

            if row[0] == 'Country ID':
                section = 'countries'
                continue
            elif row[0] == 'City ID':
                section = 'cities'
                continue
            elif row[0] == 'Street ID':
                section = 'streets'
                continue

            if section == 'countries':
                country_id, name, city_id = row
                countries.append(Country(name, int(city_id) if city_id else None))
                countries[-1].id = int(country_id)  # Обновляем ID вручную
                country_id_counter = max(country_id_counter, int(country_id) + 1)
            elif section == 'cities':
                city_id, name = row
                cities.append(City(name))
                cities[-1].id = int(city_id)  # Обновляем ID вручную
                city_id_counter = max(city_id_counter, int(city_id) + 1)
            elif section == 'streets':
                street_id, name, city_id = row
                streets.append(Street(name, int(city_id)))
                streets[-1].id = int(street_id)  # Обновляем ID вручную
                street_id_counter = max(street_id_counter, int(street_id) + 1)

    return countries, cities, streets


def print_countries(countries, cities):
    for country in countries:
        country_cities = [city.name for city in cities if city.id == country.city_id]
        print(f"Country: {country.name}, Cities: {country_cities}")


def print_streets_per_city(cities, streets):
    for city in cities:
        city_streets = [street.name for street in streets if street.city_id == city.id]
        print(f"City: {city.name}, Number of Streets: {len(city_streets)}")


def main():
    countries = []
    cities = []
    streets = []
    while True:
        print("\n1. Add Country")
        print("2. Add City")
        print("3. Add Street")
        print("4. Remove Country")
        print("5. Remove City")
        print("6. Remove Street")
        print("7. Update Country")
        print("8. Update City")
        print("9. Update Street")
        print("10. Save to CSV")
        print("11. Load from CSV")
        print("12. Print Countries and Cities")
        print("13. Print Streets per City")
        print("14. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_country(countries)
        elif choice == '2':
            add_city(cities)
        elif choice == '3':
            add_street(streets)
        elif choice == '4':
            remove_country(countries)
        elif choice == '5':
            remove_city(cities)
        elif choice == '6':
            remove_street(streets)
        elif choice == '7':
            update_country(countries)
        elif choice == '8':
            update_city(cities)
        elif choice == '9':
            update_street(streets)
        elif choice == '10':
            filename = input("Enter filename: ")
            save_to_csv(countries, cities, streets, filename)
        elif choice == '11':
            filename = input("Enter filename: ")
            countries, cities, streets = load_from_csv(filename)
        elif choice == '12':
            print_countries(countries, cities)
        elif choice == '13':
            print_streets_per_city(cities, streets)
        elif choice == '14':
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
