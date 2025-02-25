# https://www.youtube.com/@digitalrwanda


# Non-Linear Buit-in Data structures
# Dictionaly

person = {
    "name": "John Doe",
    "age": 33,
    "degree": "Phd"
}


h = 'good'

print(f"hello, that is {h}")

print("hello, welcome {}".format(h))


print(f"Person name is: {person['name']}, age: {person['age']}, degree is: {person['degree']}")

human = {
    "name": "Fils",
    "detail": {
        "age": 32,
        "degree": "Phd",
    }
}

human['name'] = "John Doe"
human.update({"hello" :  "Wold", "Data":"info", "Test": "Main"})

print(human)

print(f"\n Human name is: {human['name']} and age is: {human['detail']['age']}, degree: {human['detail']['degree']}")


Set

locations = {"kigali", "kigali", "Muhanga", "Nyanza"}

print(locations['kigali'])


peoples = {
    "John":{
        "sex": "Male",
        "age": 43,
        "degree": "phd"
    },
    "Fils": {
        "sex": "Male",
        "age": 50,
        "degree": "Professor"
    }
}

peoples.update(common = "relationship")

del peoples["common"]

peoples.update({
    "vegetables": {
        "green": "avocado",
        "red": "orange"
    }
})

peoples["vegetables"] = {
    "glass": "hopper",
    "data": "good"
}

veg = peoples.pop("vegetables")

print(veg , "\n")

print(peoples)

countries = {"Rwanda", "Kenya", "Congo", "Uganda"}

countries.add("Tanzania")

countries.remove("Kenya")

countries.update("Togo")

print(countries)


country = frozenset(("Rwanda", "Kenya", "Congo", "Uganda","Uganda"))

country.add("good")

print(country)