import datetime

class EmployeeRecord:
    def __init__(self, from_date, to_date, name, hours, hourly_rate, tax_rate):
        self.from_date = from_date
        self.to_date = to_date
        self.name = name
        self.hours = hours
        self.hourly_rate = hourly_rate
        self.tax_rate = tax_rate

def write_record_to_file(file_path, record):
    with open(file_path, "a") as file:
        file.write(f"{record.from_date}|{record.to_date}|{record.name}|{record.hours}|{record.hourly_rate}|{record.tax_rate}\n")

def read_records_from_file(file_path):
    records = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            record_data = line.strip().split("|")
            from_date = datetime.datetime.strptime(record_data[0], "%m/%d/%Y").date()
            to_date = datetime.datetime.strptime(record_data[1], "%m/%d/%Y").date()
            name = record_data[2]
            hours = float(record_data[3])
            hourly_rate = float(record_data[4])
            tax_rate = float(record_data[5])
            records.append(EmployeeRecord(from_date, to_date, name, hours, hourly_rate, tax_rate))
    return records

def calculate_tax_and_netpay(total_hours, hourly_rate, tax_rate):
    tax = total_hours * hourly_rate * (tax_rate / 100)
    net_pay = total_hours * hourly_rate - tax
    return tax, net_pay

def display_employee_info(record, tax, net_pay):
    print("----------------------------------------------------")
    print("From date:", record.from_date.strftime('%m/%d/%Y'))
    print("To date:", record.to_date.strftime('%m/%d/%Y'))
    print("Employee name:", record.name)
    print("Total hours:", record.hours)
    print("Hourly rate:", record.hourly_rate)
    print("Gross pay:", record.hours * record.hourly_rate)
    print("Tax rate:", record.tax_rate)
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

def process_records(records):
    total_dict = {"total_employees": 0, "total_hours": 0, "total_tax": 0, "total_gross_pay": 0, "total_net_pay": 0}
    
    from_date_to_report = get_from_date()
    
    for record in records:
        if from_date_to_report.lower() == "all" or from_date_to_report == record.from_date:
            tax, net_pay = calculate_tax_and_netpay(record.hours, record.hourly_rate, record.tax_rate)
            display_employee_info(record, tax, net_pay)
            
            total_dict['total_employees'] += 1
            total_dict['total_hours'] += record.hours
            total_dict['total_tax'] += tax
            total_dict['total_gross_pay'] += record.hours * record.hourly_rate
            total_dict['total_net_pay'] += net_pay
            
    display_total_info(total_dict)

def main():
    file_path = "employee_records.txt"
    records = read_records_from_file(file_path)

    while True:
        name = input("Enter employee name: ")

        if name == "End":
            break

        from_date = input("Enter from date in mm/dd/yyyy format: ")
        to_date = input("Enter to date in mm/dd/yyyy format: ")
        hours = float(input("Enter total hours: "))
        hourly_rate = float(input("Enter hourly rate: "))
        tax_rate = float(input("Enter tax rate (in %): "))

        record = EmployeeRecord(from_date, to_date, name, hours, hourly_rate, tax_rate)
        write_record_to_file(file_path, record)
        print()

    process_records(records)

if __name__ == "__main__":
    main()
