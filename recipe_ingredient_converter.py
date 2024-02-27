def convert_ingredient(quantity, from_unit, to_unit, conversion_table):
    if from_unit not in conversion_table or to_unit not in conversion_table[from_unit]:
        return "Conversion not possible or not available."

    conversion_factor = conversion_table[from_unit][to_unit]
    return quantity * conversion_factor

def main():
    conversion_table = {
        'cups': {'grams': 236.588, 'tablespoons': 16},
        'tablespoons': {'grams': 14.787, 'cups': 0.0625},
        'grams': {'cups': 0.00423, 'tablespoons': 0.06763},
        # Add more conversions as needed
    }

    quantity = float(input("Enter the ingredient quantity: "))
    from_unit = input("Enter the current unit (cups, tablespoons, grams): ")
    to_unit = input("Enter the unit to convert to (grams, tablespoons, cups): ")

    converted_quantity = convert_ingredient(quantity, from_unit, to_unit, conversion_table)
    print(f"{quantity} {from_unit} is {converted_quantity} {to_unit}")

if __name__ == "__main__":
    main()
