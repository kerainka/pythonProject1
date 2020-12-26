#!/usr/bin/env python
# -*- coding: utf-8 -*-


with open("scratch.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    list = ["ingredient_name", "quantity", "measure"]
    cook_book = {}
    index = 0
    while index < len(lines):
        name = lines[index].strip()
        cook_book[name] = []
        index += 1
        count = int(lines[index])
        for ingredient_index in range(1, count+1):
            ingredients = lines[index+ingredient_index].split("|")
            ingredient_name = ingredients[0].strip()
            quantity = int(ingredients[1].strip())
            measure = ingredients[2].strip()
            dictionary = dict(zip(list, [ingredient_name, quantity, measure]))
            cook_book[name].append(dictionary)
        index = index + count + 2
    print(cook_book)

    def get_shop_list_by_dishes(dishes, person_count):
        grocery_list = {}
        for dish in dishes:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                ingredient_name = ingredient["ingredient_name"]
                if ingredient_name not in grocery_list:
                    grocery_list[ingredient_name] = {"measure": ingredient["measure"], "quantity": ingredient["quantity"]*person_count}
                else:
                    grocery_list[ingredient_name]["quantity"] += ingredient["quantity"]*person_count
        print(grocery_list)

    get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)

