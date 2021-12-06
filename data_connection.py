import csv


def open_csv_file_into_dict(file_path):
    with open(file_path, mode='r') as file:
        return [dictionary for dictionary in csv.DictReader(file)]


def open_csv_file(file_path):
    with open(file_path, mode='r') as file:
        return [line.split(';') for line in file.read().splitlines()]


def create_profiles_dictionary(profiles_list):

    def get_categories(categories_list):
        category_list = []
        for category in categories_list:
            if 'ideal' in category:
                category = category.split(' ', maxsplit=1)
                category_list += category
            else:
                category_list.append(category)
        return category_list

    categories = get_categories(profiles_list[0])

    # categories = [category if 'ideal' not in category else category.split(' ', maxsplit=1) for category in profiles_list[0] ]
    return [{categories[number]: profile_list[number] for number, category in enumerate(categories)} for profile_list in profiles_list]


if __name__ == "__main__":
    data = open_csv_file(file_path='data/profiles.csv')
    profiles = create_profiles_dictionary(data)
    print(profiles)
