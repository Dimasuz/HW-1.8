from pprint import pprint

with open('recipest.txt', encoding='utf-8') as file_cook:
  
  cook_book = {}
    
  for line in file_cook:       
    
    dish = line.strip()
    cook_book[dish] = []
    num = int(file_cook.readline())    
    
    for item in file_cook:
      if item == '\n':
        break    
      ing = item.strip().split(' | ')      
      ingredient = {}
      ingredient['ingredient_name'] = ing[0]
      ingredient['quantity'] = ing[1]
      ingredient['measure'] = ing[2]           
      cook_book[dish].append(ingredient)
   

pprint(cook_book)
    
