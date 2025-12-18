# simple_interest.py
from calfun import add,sub,mul,div
def calculate_simple_interest(principal, rate, time):
    return mul(principal, mul(rate, time)) / 100

def main():
    print("Simple Interest Calculator")
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter rate of interest (%): "))
    time = float(input("Enter time period (years): "))

    simple_interest = calculate_simple_interest(principal, rate, time)
    print(f"Simple Interest: {simple_interest:.2f}")
    total_amount = add(principal, simple_interest)
    print(f"Total Amount: {total_amount:.2f}")

if __name__ == "__main__":
    main()
