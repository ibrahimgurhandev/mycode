#!/usr/bin/env python3
import operator

def calculator():
    print("Calculator App")

    def get_operand():
        while True:
            op = input("what will you like to do,\n "
                       "'+' to add, '/' to divide, '-' to subtract, '*' to multiply ").lower()
            if op in ["+", "/", "-", "*"]:
                return op

    def get_nums(count):
        while True:
            try:
                num = float(input(f"Enter {count} number -  it can be a float or integer: "))
                break
            except ValueError:
                print("That's not an a number!")
        return num

    def calculate():
        op = get_operand()
        operators = {'+': operator.add,
                     '-': operator.sub,
                     '*': operator.mul,
                     '/': operator.truediv}
        try:
            print(operators[op](get_nums("first"), get_nums("second")))
        except ZeroDivisionError:
            print("HEYYY! you can't divide by ZERO. DON'T YOU DARE DO THAT AGAIN")
            calculate()

    calculate()

def main():
    calculator()

if __name__ == "__main__":
    main()
