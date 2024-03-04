# my_list=[1,2,3,4,5] #1
# def list_numbers(lst):
#     result=1
#     for num in lst:
#         result *=num
#     return result
# print(list_numbers(my_list))


# my_list=[1,2,3,4,5,6,7,8,9]#2
# operation=("Минимум,Максимум")
# def list_numbers(lst):
#     max_value=max(lst)
#     print("Максимум",max_value)
#     min_value=min(lst)
#     print("Минимум",min_value)
#     return max_value,min_value
# print(list_numbers(my_list))

# import random #3
#
# def is_prime(numbers:int)->bool:
#      is_prime_numbers=True
#
#      for num in range(2,numbers):
#          if numbers % num== 0:
#              is_prime_numbers= False
#              break
#      return is_prime_numbers
# numbers=[random.randint(1,20) for i in range(10)]
# print(numbers)




# my_list = [1, 2, 3, 4, 5]#4
# number_to_remove=5
#
# def list_remove_numbers(lst,num):
#     count_remove=0
#     while num in lst:
#         lst.remove(num)
#         count_remove+=1
#     return count_remove
# print(list_remove_numbers(my_list,number_to_remove))
# print(my_list)

user = ["Игорь", "Алёна", "Вова", "Гриша", "Варя"]
user1 = ["Игорь", "Варя", "Алёна", "Петя", "Вася"]

def merge_lists():
    merged_users = user + user1
    return merged_users

print(merge_lists())


# my_list = [1,2,3,4,5] #6
# power=2
#
# def power_list(lst,power):
#     power_list=[num**power for num in lst]
#     return power_list
# result=power_list(my_list,power)
# print(result)
