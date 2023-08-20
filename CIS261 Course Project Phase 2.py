import datetime

def calculate_tax_and_netpay(total_hours, hourly_rate, tax_rate):
    tax = total_hours * hourly_rate * (tax_rate / 100)
    net_pay = total_hours * hourly_rate - tax
    return tax, net_pay

def get_name():
    name = input("Enter employee name: ")
    return name

def get_from_and_to_date():
    from_date = input("Enter from date in mm/dd/yyyy format: ")
    to_date = input("Enter to date in mm/dd/yyyy format: ")
    from_date = datetime.datetime.strptime(from_date, "%m/%d/%Y").date()
    to_date = datetime.datetime.strptime(to_date, "%m/%d/%Y").date()
    return from_date, to_date

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
    gross_pay = total_hours * hourly_rate
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

def main():
    employee_list = []
    total_dict = {
        "total_employees": 0,
        "total_hours": 0,
        "total_tax": 0,
        "total_gross_pay": 0,
        "total_net_pay": 0
    }

    while True:
        from_date, to_date = get_from_and_to_date()
        name = get_name()
        if name.lower() == "end":
            break

        total_hours = get_total_hours()
        hourly_rate = get_hourly_rate()
        tax_rate = get_tax_rate()
        
        gross_pay = get_gross_pay(total_hours, hourly_rate)
        tax, net_pay = calculate_tax_and_netpay(total_hours, hourly_rate, tax_rate)

        employee_info = {
            "from_date": from_date,
            "to_date": to_date,
            "name": name,
            "total_hours": total_hours,
            "hourly_rate": hourly_rate,
            "tax_rate": tax_rate,
            "tax": tax,
            "gross_pay": gross_pay,
            "net_pay": net_pay
        }

        employee_list.append(employee_info)

        total_dict['total_employees'] += 1
        total_dict['total_hours'] += total_hours
        total_dict['total_tax'] += tax
        total_dict['total_gross_pay'] += gross_pay
        total_dict['total_net_pay'] += net_pay

    for employee_info in employee_list:
        display_employee_info(employee_info["from_date"], employee_info["to_date"], employee_info["name"],
                              employee_info["total_hours"], employee_info["hourly_rate"], employee_info["tax_rate"],
                              employee_info["tax"], employee_info["gross_pay"], employee_info["net_pay"])

    display_total_info(total_dict)

if __name__ == "__main__":
    main()
