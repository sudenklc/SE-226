from data_package import remove_duplicates, strip_whitespaces
from data_package import calculate_mean, find_maximum, find_minimum


def main():
    user_input = input("Enter a comma-separated list of numbers (e.g., 12, 5, 12, 8 , 21): ")

    try:
        data_list = user_input.split(",")
        stripped_list = strip_whitespaces(data_list)

        number_list = []
        for item in stripped_list:
            number_list.append(float(item))

        cleaned_data = remove_duplicates(number_list)

        print("Cleaned and unique data:", cleaned_data)
        print("--------------------")
        print("Mean: {:.2f}".format(calculate_mean(cleaned_data)))
        print("Maximum:", find_maximum(cleaned_data))
        print("Minimum:", find_minimum(cleaned_data))

    except ValueError:
        print("Data Error: Please make sure you only enter numbers separated by commas.")
