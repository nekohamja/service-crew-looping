while True:
    scname = input("Service Crew Name: ")
    hours = float(input("No. of Hours Worked: "))
    ot = float(input("Extra Service Hours (OT): "))
    ut = float(input("No. of Hours Late (UT): "))
    rate = float(input("Rate per Hour: "))
    fdeduction = float(input("Food Deduction: "))
    tip = float(input("Extra Income (Tip): "))
    ot_rate = rate * 0.03
    ut_pay = ut * rate
    ot_pay = ot * ot_rate
    gross = (hours * rate) + ot_pay
    insurance = gross * 0.03
    sss = gross * 0.05
    tax = gross * 0.1
    deduction = ut_pay + insurance + tax + sss + fdeduction
    net_pay = gross - deduction + tip
    print("Service Crew Name: ", scname)
    print("Under Time Pay: ", ut_pay)
    print("Over Time Pay: ", ot_pay)
    print("Extra Income (Tip): ", tip)
    print("Net Pay: ", net_pay)
    repeat = input("Another transaction? (y/n)")
    if repeat.lower() == "n":
        break
    elif repeat.lower() == "y":
        continue