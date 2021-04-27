import csv

def open_and_read(csv_name="user_details.csv"):
    with open(csv_name) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        iterable_csv = iter(csvreader)
        next(iterable_csv)
        csvlst = list(iterable_csv)
    return csvlst

def transform_user_details(csv_name="user_details.csv"):
    csvlst = open_and_read(csv_name)
    emp_lst = []
    for row in csvlst:
        emp_lst.append(row[1])
        emp_lst.append(row[2])
        emp_lst.append(row[-1])
    return emp_lst


def create_csv_file(old_user_details="user_details.csv", new_file_name="new_details.csv"):
    new_user_details = transform_user_details(old_user_details)

    with open(new_file_name, "w") as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerow(new_user_details)

print(create_csv_file())