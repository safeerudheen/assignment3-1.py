 user_input_list = []
number_of_elements = int(input("Enter number of elements:"))
count = 0
while count<number_of_elements:
    user_input = input("Enter the number:  ")
    count += 1
    num = int(user_input)
    user_input_list.append(num)  
print("List containing user input:", user_input_list)

def sum_of_numbers(user_input_list):
    result = 0
    for number in user_input_list:
            result += number
    return result

result = sum_of_numbers(user_input_list)
print(f"Sum of given {number_of_elements} numbers = ",result)  
