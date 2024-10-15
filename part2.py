volume_of_discete = 1.44 #Мегабайты
pages_of_book = 100
strings_on_page = 50
chars_in_string = 25
volume_of_char = 4 #байты

volume_of_discete_bytes = volume_of_discete * 1024 ** 2 #В байтах
one_book = pages_of_book * strings_on_page * chars_in_string * volume_of_char
count_of_books = volume_of_discete_bytes // one_book

print("Количество книг, помещающихся на дискету:", int(count_of_books))