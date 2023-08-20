import datetime

def calculate_tax_and_netpay(total_hours, hourly_rate, tax_rate):
    tax = total_hours * hourly_rate * (tax_rate / 100)
    net_pay = total_hours * hourly_rate - tax
    return tax, net_pay

def get_from_and_to_date():
    from_date = input("Enter from date in mm/dd/yyyy format: ")
    to_date = input("Enter to date in mm/dd/yyyy format: ")
    from_date = datetime.datetime.strptime(from_date, "%m/%d/%Y").date()
    to_date = datetime.datetime.strptime(to_date, "%m/%d/%Y").date()
    return from_date, to_date

def main():
    employees = []

    while True:
        from_date, to_date = get_from_and_to_date()
        name = input("Enter employee name: ")
        if name.lower() == "end":
            break

        total_hours = float(input("Enter total hours: "))
        hourly_rate = float(input("Enter hourly rate: "))
        tax_rate = float(input("Enter tax rate (in %): "))
        
        employees.append({
            "from_date": from_date,
            "to_date": to_date,
            "name": name,
            "total_hours": total_hours,
            "hourly_rate": hourly_rate,
            "tax_rate": tax_rate
        })

    total_info = {
        "total_employees": 0,
        "total_hours": 0,
        "total_tax": 0,
        "total_net_pay": 0
    }

    print("\nEmployee Information:")
    for employee in employees:
        from_date = employee["from_date"]
        to_date = employee["to_date"]
        name = employee["name"]
        total_hours = employee["total_hours"]
        hourly_rate = employee["hourly_rate"]
        tax_rate = employee["tax_rate"]

        gross_pay = total_hours * hourly_rate
        tax, net_pay = calculate_tax_and_netpay(total_hours, hourly_rate, tax_rate)

        total_info["total_employees"] += 1
        total_info["total_hours"] += total_hours
        total_info["total_tax"] += tax
        total_info["total_net_pay"] += net_pay

        print("\n----------------------------------------------------")
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

    print("\nTotal Information:")
    print("----------------------------------------------------")
    print("Total number of employees:", total_info['total_employees'])
    print("Total hours:", total_info['total_hours'])
    print("Total tax:", total_info['total_tax'])
    print("Total net pay:", total_info['total_net_pay'])
    print("----------------------------------------------------")

if __name__ == "__main__":
    main()
