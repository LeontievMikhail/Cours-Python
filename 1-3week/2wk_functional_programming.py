square_list=[number**2 for number in range(10)]
print(square_list)

even_list=[num for num in range(10) if num % 2 == 0]
print(even_list)

square_map={number: number ** 2 for number in range(5)}
print(square_map)

reminders_set = {num % 10 for num in range(100)}
print(reminders_set)

num_list = range(7)
squared_list = [x**2 for x in num_list]
print(list(zip(num_list, squared_list)))
