#!/usr/bin/env python3

"""Program to calculate the price of a fruit gift basket."""

__author__ = "Lydia Frame"
__date__ = "03/10/2025"

import pathlib
import csv


def read_prices(file_name):
    """Read prices from a text file and return them as a list of floats."""
    prices = []
    if pathlib.Path(file_name).exists():
        with open(file_name, 'r') as file:
            for line in file:
                prices.append(float(line.strip()))
    else:
        print("Error: Price file does not exist.")
    return prices


def calculate_basket_cost(price_file, order_file):
    """Calculate the total cost of the basket using price and order files."""
    prices = read_prices(price_file)
    total_cost = 0

    if pathlib.Path(order_file).exists():
        with open(order_file, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                item_num, quantity = int(row[0]), int(row[1])
                if 0 <= item_num < len(prices):
                    total_cost += prices[item_num] * quantity
    else:
        print("Error: Order file does not exist.")
    return total_cost


def main():
    """Main function to execute the program."""
    price_file = input("Price file? ")
    print()
    order_file = input("Basket file? ")
    print()
    total_cost = calculate_basket_cost(price_file, order_file)
    print(f"Basket will cost ${total_cost:.2f}")


if __name__ == "__main__":
    main()
