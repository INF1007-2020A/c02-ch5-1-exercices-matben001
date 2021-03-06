#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
    INDEX_NAME = 0
    INDEX_QUANTITY = 1
    INDEX_PRICE = 2

    TAX_RATE = 0.15    #calculer le sous total
    sum =0
    for item in data:
        sum += item[INDEX_QUANTITY]*item[INDEX_PRICE]
    #calculer les taxes et total
    taxes = TAX_RATE * sum 
    total=sum+taxes

    #retourner la facture formatée
    result = name
    result += "\n"+f"SOUS-total {sum : >10.2f} $"
    result += "\n"+f"TAXES      {taxes : >10.2f} $"
    result += "\n"+f"TOAL       {total : >10.2f} $"
    return result


def format_number(number, num_decimal_digits):
    #Séparer les parties entières et décimal
    decimal_part = abs(number) % 1
    whole_part = int(number)
    #Formater la parties décimal
    decimal_str = f"{decimal_part :.{num_decimal_digits}f}"[1:]
    #Formater la partie entières
    #Concaténer les deux parties
	return ""

def get_triangle(num_rows):
    BORDER_CHAR = "+"
    TRIANGLE_CHAR = "A"
    #Calculer la largeur

    #Construire première et dernière ligne(cordure pleine)

    #Afficher le triangle
    i=0
    while i>numrows:
        i+=1
        print(f"{})
	return ""


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
