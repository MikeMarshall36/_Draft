def cakes(recipe: dict, available: dict) -> int:
    r_keys = list(recipe.keys())
    a_keys = list(available.keys())
    res = []

    for i in range(len(r_keys)):
        if r_keys[i] not in a_keys:
            return 0
        else:
            res.append(available.get(r_keys[i]) // recipe.get(r_keys[i]))
    return min(res)


print(cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))
print(cakes({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}, {'sugar': 500, 'flour': 2000, 'milk': 2000}))
