import random



def convert_to_bool(option):
     if option == 'True':
         return True
     elif option == 'False':
         return False


def expression_evaluation(random_example: str) -> bool:
     values = random_example.split(" ")
     value_a = convert_to_bool(values[0])
     value_op = values[1]
     value_b = convert_to_bool(values[2])
     value_cmp = values[3]
     value_c = convert_to_bool(values[4])

     if "or" in value_op:
         logic_operator = value_a or value_b
     elif "and" in value_op:
         logic_operator = value_a and value_b

     if "==" in value_cmp:
         compar_operator = logic_operator == value_c
         return compar_operator
     elif "!=" in value_cmp:
         compar_operator = logic_operator != value_c
         return compar_operator



def value_comparison(option: bool, random_example):
     if option == expression_evaluation(random_example):
         print("Správná odpověď")
     elif option != expression_evaluation(random_example):
         print("šPATNÁ ODPOVĚĎ")

def users_input():
     return

def main():
     number_of_repetitions = int(input("Zadejte počet úloh, které chcete řešit: "))

     number_of_row = 0
     while number_of_row < number_of_repetitions:
         number_of_row += 1
         random_example = (f"{random.choice([False, True])} {random.choice(['and', 'or'])} "
                             f"{random.choice([False, True])} {random.choice(['==', '!='])} {random.choice([False, True])}")
         option = input(f"{number_of_row}) Je daný příklad True nebo False: {random_example} ? ")
         value_comparison(convert_to_bool(option), random_example)
         print(expression_evaluation(random_example))


if __name__ == "__main__":
     main()

