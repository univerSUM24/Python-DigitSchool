def goods_finding(list_of_goods, good):
    index = 0
    goods = list_of_goods[0]
    for goods in list_of_goods:
        if(good == goods):
            break
        index = index + 1
    if(index >= len(list_of_goods)):
        index = None
    return index

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = goods_finding(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
