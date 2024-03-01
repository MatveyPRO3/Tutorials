import random
from faker import Faker
import os 

id = 0

fake = Faker()

def Get_sample():
    global id
    id = id +1
    sex = random.choice(["_male_","female"])
    if sex == "male_":
        name = fake.name_male().split()
    else:
        name = fake.name_female().split()
    return {
    "id": id,
    "first_name": name[0],
    "last_name": name[1],
    "date_of_birth": str(fake.date_between(start_date="-80y",end_date="-18y")),
    "country": str(random.choice(["France", "Germany", "United Kingdom", "Spain", "Italy", "Poland"])),
    "married": decision(),
    "job": get_job(),
    "income_in_year": str(income_in_year()) + "$",
    "total_property_cost": str(total_property_cost()) + "$",
    "sex":sex,
    }

def decision(percent=60):
    return random.randrange(100) < percent

def get_job(percent=98):
    if random.randrange(100) < percent:
        return fake.job()
    else:
        return "unemployed"

def income_in_year():
    mu = random.randint(80000,100000)
    sigma = random.randint(15000, 25000)
    return round(random.gauss(mu, sigma))

def total_property_cost():
    return income_in_year() * random.randint(5, 25)

file_ = "data_sets/ma2.txt"
try:
    os.remove(file_)
except:
    pass

for i in range (int(input())):
    with open(file_, "a") as file:
        file.write(str(Get_sample())+"\n")
        file.close()
        # print(Get_sample())

        