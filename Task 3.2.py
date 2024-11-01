participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants()

#Использование метода intersection для пересечения множества и списка
#def find_common_participants(first_group, second_group, comma=","):
#    result = set(first_group.split("|")).intersection(second_group.split("|"))
#    result = list(result)
#    result.sort()
#    return result

#Перебор пар всех элементов: совпадение запоминается
#def find_common_participants(first_group, second_group, comma=","):
#    first_list = first_group.split("|")
#    second_list = second_group.split("|")
#    inter_list = list("")
#    for first_group_man in first_list:
#        for second_group_man in second_list:
#            if(first_group_man == second_group_man):
#                inter_list.append(first_group_man)
#    inter_list.sort()
#    return inter_list