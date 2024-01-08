import re
from datetime import date
import time
import os.path
import sys


def read_file(name_file):
     file = open(name_file)
     next(file)
     return file.readlines()


def write_file(name_file, list_of_operator):
     file = open(name_file, "w")
     for user in list_of_operator:
         time.sleep(0.001)
         file.write(",".join(user) + "\n")
     file.close()
     return file


def write_greeting(name_file, salutation, name):
     file = open(os.path.join('blue_line_greetings', name_file), "w")
     greeting = f"Dear {salutation} {name}, we wish you a nice and successful day!"
     file.write(greeting)
     file.close()
     return file


def calculate_age(born):
     today = date.today()
     born = int(born)
     return today.year - born


def sort_numbers(user):
     return user[2]


def sorting_users():
     row = 0
     boys = 0
     girls = 0
     list_of_users = []
     green_line = []
     red_line = []
     blue_line_boys = []
     blue_line_girls = []
     users = read_file(sys.argv[1])

     for line in users:
         row += 1
         user = line.rstrip("\n").split(",")
         name_surname, year, number, sex, subscribed = user
         list_of_users.append(user)

         if "boy" in sex and re.search("^733", number):
             boys += 1
             green_line.append(user)
             green_line.sort(key=sort_numbers)

         if "girl" in sex and re.search("^921", number) and re.search("^False", subscribed):
             girls += 1
             red_line.append(user)
             red_line.sort(key=sort_numbers)

         if calculate_age(year) >= 18 and re.search("^645", number) and re.search("^True", subscribed):
             name_surname = name_surname.split(" ")
             name = name_surname[0]

             if "boy" in sex:
                 blue_line_boys.append((user, name))
                 "_".join(name_surname)

             if "girl" in sex:
                 blue_line_girls.append((user, name))
                 "_".join(name_surname)

     return green_line, red_line, blue_line_boys, blue_line_girls


def main():
     green_line, red_line, blue_line_boys, blue_line_girls = sorting_users()
     print(blue_line_boys)
     print(blue_line_girls)
     green_line = write_file("green_line.txt", green_line)
     red_line = write_file("red_line.txt", red_line)
     for user, name in blue_line_boys:
         write_greeting(f"greeting_{user[0]}.txt", "Mr.", name)
     for user, name in blue_line_girls:
         write_greeting(f"greeting_{user[0]}.txt", "Madam", name)
     return green_line, red_line, blue_line_boys, blue_line_girls


if __name__ == '__main__':
     main()
