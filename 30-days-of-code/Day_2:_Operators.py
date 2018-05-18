#!/usr/bin/python3

# Task
# Given the meal price (base cost of a meal), tip percent
# (the percentage of the meal price being added as tip), and tax percent (the
# percentage of the meal price being added as tax) for a meal, find and print
# the meal's total cost.

# Note: Be sure to use precise values for your calculations, or you may end up
# with an incorrectly rounded result!

# Input Format

# There are 3 lines of numeric input:
# The first line has a double, mealCost (the cost of the meal before
# tax and tip).
# The second line has an integer, tipPercent (the percentage of mealCost
# being added as tip).
# The third line has an integer, taxPercent (the percentage of mealCost being
# added as tax).

# Output Format

# Print The total meal cost is totalCost dollars., where totalCost is the
# rounded integer result of the entire bill (mealCost with
# added tax and tip).

import sys


if __name__ == "__main__":
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())
    tip = meal_cost * (tip_percent / 100)
    tax = meal_cost * (tax_percent / 100)

    # cast the result of the rounding operation to an int and
    # save it as total_cost
    total_cost = int(round(meal_cost + tip + tax))
    print("The total meal cost is {} dollars.".format(str(total_cost)))
