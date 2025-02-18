person= {
    "name":"Jayanti",
    "age":22,
    "city":"Kanpur",
    'pincode' : 389382,
    'country' : 'India'
}
# get()
name = person.get("name")
age = person.get("age")
city = person.get("city")
pincode = person.get("pincode")
country = person.get("country")
print(name)
print(age)
print(city)
print(pincode)
print(country)

# pop()
person.pop('city')
print(person)

# popitem()
person.popitem()
print(person)

# update()
person.update({"name" : 'Smirti' , 'age' : 25 , 'state' : 'UP'})
print(person)

# clear()
person.clear()
print(person)