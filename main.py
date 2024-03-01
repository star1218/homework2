# list=[1,2,3,4,5] #1
# def list_numbers(lst):
#     result=1
#     for num in lst:
#         result *=num
#     return result
# print(list_numbers(list))

# list=[1,2,3,4,5,6,7,8,9]#2
# operation=("Минимум,Максимум")
# def list_numbers(lst):
#     max_value=max(lst)
#     print("Максимум",max_value)
#     min_value=min(lst)
#     print("Минимум",min_value)
#     return max_value,min_value
# print(list_numbers(list))

# my_list =[1,2,3,4,5,6,7,8,9]#3
#
# def list_numbers(lst):
#     even_numbers=[]
#     for num in lst:
#         if num%2==0:
#             even_numbers.append(num)
#     return even_numbers
# print(list_numbers(my_list))

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

# user={"Игорь","Алёна","Вова","Гриша","Варя"} #5
# user1={"Игорь","Варя","Алёна","Петя","Вася"}
#
# def people():
#     people_users=user.intersection(user1)
#     return people_users
# print(people())

# my_list = [1,2,3,4,5] #6
# power=2
#
# def power_list(lst,power):
#     power_list=[num**power for num in lst]
#     return power_list
# result=power_list(my_list,power)
# print(result)

