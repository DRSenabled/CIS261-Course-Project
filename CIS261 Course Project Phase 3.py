import datetime

def calculate_tax_and_netpay(total_hours, hourly_rate, tax_rate):
    tax = float(total_hours) * float(hourly_rate) * (float(tax_rate) / 100)
    net_pay = float(total_hours) * float(hourly_rate) - tax
    return tax, net_pay

def get_name():
    name = input("Enter employee name: ")
    return name

def get_total_hours():
    total_hours = float(input("Enter total hours: "))
    return total_hours

def get_hourly_rate():
    hourly_rate = float(input("Enter hourly rate: "))
    return hourly_rate

def get_tax_rate():
    tax_rate = float(input("Enter tax rate (in %): "))
    return tax_rate

def get_gross_pay(total_hours, hourly_rate):
    gross_pay = float(total_hours) * float(hourly_rate)
    return gross_pay

def display_employee_info(from_date, to_date, name, total_hours, hourly_rate, tax_rate, tax, gross_pay, net_pay):
    print("----------------------------------------------------")
    print("From date:", from_date.strftime('%m/%d/%Y'))
    print("To date:", to_date.strftime('%m/%d/%Y'))
    print("Employee name:", name)
    print("Total hours:", total_hours)
    print("Hourly rate:", hourly_rate)
    print("Gross pay:", gross_pay)
    print("Tax rate:", tax_rate)
    print("Income tax:", tax)
    print("Net pay:", net_pay)
    print("----------------------------------------------------")

def display_total_info(total_dict):
    print("----------------------------------------------------")
    print("Total number of employees:", total_dict['total_employees'])
    print("Total hours:", total_dict['total_hours'])
    print("Total tax:", total_dict['total_tax'])
    print("Total gross pay:", total_dict['total_gross_pay'])
    print("Total net pay:", total_dict['total_net_pay'])
    print("----------------------------------------------------")

def get_from_date():
    while True:
        from_date = input("Enter from date in mm/dd/yyyy format (or 'All' for all records): ")
        if from_date.lower() == "all" or is_valid_date(from_date):
            return from_date
        else:
            print("Invalid date format. Please use mm/dd/yyyy or 'All'.")

def is_valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%m/%d/%Y")
        return True
    except ValueError:
        return False

def process_records(file_path, from_date):
    with open(file_path, "r") as file:
        lines = file.readlines()

    total_dict = {"total_employees": 0, "total_hours": 0, "total_tax": 0, "total_gross_pay": 0, "total_net_pay": 0}

    for line in lines:
        record = line.strip().split("|")
        record_from_date = datetime.datetime.strptime(record[0], "%m/%d/%Y").date()

        if from_date.lower() == "all" or from_date == record_from_date:
            from_date = record_from_date
            to_date = datetime.datetime.strptime(record[1], "%m/%d/%Y").date()
            name = record[2]
            hours = float(record[3])
            hourly_rate = float(record[4])
            tax_rate = float(record[5])

            gross_pay = get_gross_pay(hours, hourly_rate)
            tax, net_pay = calculate_tax_and_netpay(hours, hourly_rate, tax_rate)
            display_employee_info(from_date, to_date, name, hours, hourly_rate, tax_rate, tax, gross_pay, net_pay)

            total_dict['total_employees'] += 1
            total_dict['total_hours'] += hours
            total_dict['total_tax'] += tax
            total_dict['total_gross_pay'] += gross_pay
            total_dict['total_net_pay'] += net_pay

    display_total_info(total_dict)

def main():
    file_path = "employee_records.txt"

    while True:
        name = get_name()

        if name == "End":
            break

        from_date, to_date = get_from_and_to_date()

        hours = get_total_hours()
        hourly_rate = get_hourly_rate()
        tax_rate = get_tax_rate()

        with open(file_path, "a") as file:
            file.write(f"{from_date}|{to_date}|{name}|{hours}|{hourly_rate}|{tax_rate}\n")

        print()  # To start printing in a new line 

    from_date_to_report = get_from_date()
    process_records(file_path, from_date_to_report)

if __name__ == "__main__":
    main()
