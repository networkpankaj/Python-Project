# <-------------------------------------------------------Chapter One ------------------------------------------------>

# def adjust_recipe(recipe, servings):
    
#     new_recipe = [servings]  // here i create a list of servings

#     old_servings = recipe[0]
#     factor = servings / old_servings
#     recipe.pop(0)
    
#     while recipe:
#         ingredient, amount, unit = recipe.pop(0)
        
#         new_recipe.append((ingredient, amount * factor, unit))
        
#     return new_recipe



# from fractions import Fraction

    

# def adjust_recipe(recipe, servings):
    
#     """
#         Take a meal recipe and change the number of servings
#          :param recipe: a `Recipe` indicating what needs to be adusted
#         :param servings: the number of servings
#         :return Recipe: a recipe with serving size and ingredients adjusted
#         for the new servings
#     """
    
#     # create a copy of the ingredients
    
#     new_ingredients = list(recipe.get_ingredients())
#     recipe.get_ingredients()
    
    
#     for ingredient in new_ingredients:
#         ingredient.adjust_proportion(Fraction(servings, recipe.servings))   
        
#     return Recipe(servings, new_ingredients) 


    
    
#     old_servings = recipe.pop(0)
    
#     factor = servings / old_servings
    
#     new_recipe = {ingredient: (amount*factor, unit) for ingredient, amount, unit in recipe}
    
#     new_recipe["servings"] = servings
#     return new_recipe


# adjust_recipe()
# print(adjust_recipe)

# ------------------------------------------------- COLLECTIONS --------------------------------------------------

# Choosing a collection tells readers about your specific intentions....

# from typing import Counter

# # here i create a list cookbooks

# def create_author_count_mapping(cookbooks: list[Cookbook]):
#     #  count is a dictionary
#     count = {}
    
#     for cookbook in cookbooks:
        
#         if cookbook.author not in count:
#             count[cookbook.author] = 0
            
#         count[cookbook.author] += 1
#     return count



# defaultdict - A dictionary that provides a default value if the key is missing.

# from collections import defaultdict

# def create_author_count_mapping(cookbooks: list[Cookbook]):
    
#     counter = defaultdict(lambda: 0)
    
#     for cookbook in cookbooks:
#         counter[cookbook.author] +=1
    
#     return counter



# Counter - A special type of dictionary used for counting how many times an element appears.

# from collections import Counter

# def create_author_count_mapping(cookbooks: list[Cookbook]):
    
#     return Counter(book.author for book in cookbooks)


# ----------------------------------------------- Iteration ------------------------------------------

#  teration is another example where the abstraction you choose dictates the intent you convey.


# text = "There is Something I Don't No"
# index = 0

# while index < len(text):
#     print(text[index])
#     index += 1


# for character in text:
#     print(character)
    


#  Recursion

# def list_ingredients(item):
#     if isinstance(item, PreparedIngredient):
#         list_ingredients(item)
#     else:
#         print(ingredient)
        
    
#  Mechanical Representation

# from ctypes import string_at
# from sys import getsizeof
# from binascii import hexlify

# a = 0b010100000_01000001_01010100
# print(a)

# print(hexlify(string_at(id(a), getsizeof(a))))

# text = "PAT"
# print(hexlify(string_at(id(text), getsizeof(text))))


# Semantice Representation

# import datetime
# print(datetime.datetime.now())



# from contextlib import closing


# def close_kitchen_if_past_cutoff_time(point_in_time):
    
#     if point_in_time >= closing_time(): 
#         close_kitchen()
#         log_time_closed(point_in_time)
        
        
  
# import datetime 
      
# def close_kitchen_if_past_cutoff_time(point_in_time: datetime.datetime):
#     if point_in_time >= closing_time():
#         close_kitchen()
#         log_time_closed(point_in_time)

# close_kitchen_if_past_cutoff_time(CustomDateTime("now"))



# a : int = 5
# a = "strings"
# print(a)  

# a = tuple()
# print(a)


# from typing import Iterable

# def print_items(items: Iterable):
#     for item in items:
#         print(item)
        
    
# print_items([1, 2, 3])
# print_items({4,5,6})
# print_items({"A": 1,"B": 2, "C": 3})
 
# print_items(5) it gives an error that int object is not iterable


# def double_value(value):
#     return value + value

# print(double_value(5))

# print(double_value('abc'))

# print(double_value([1, 2, 3]))


# import datetime
# import random

# def schedule_restaurant_open(open_time: datetime.datetime, workers_needed: int):
#     workers = find_workers_available_for_time(open_time)
#     # use random.sample to pick X available workers
#     # where X  is the number of workers needed
#     for worker in random.sample(workers, workers_needed):
#         worker.schedule(open_time)
        
    
# def find_workers_available_for_time(open_time: datetime.datetime) -> list[str]:
#     workers = worker_database.get_all_workers()
#     available_workers = [worker for worker in workers if is_available(worker)]
    
#     if available_workers:
#         return available_workers
    
#     open_time.astimezone
    
#     emergency_workers = [worker for worker in get_emergency_workers()
#                          if is_available(worker)]
    
    
#     if emergency_workers:
#         return emergency_workers
    
#     return [OWNER]


# def worker_database(workers):
    
    

     
    

#    workers: list[str] = find_workers_available_for_time(open_time)
#    numbers: list[str] = []
#    ratio: float = get_ratio(5,3)


# Optional Types: -----------------------------------------------

# def create_hot_dog():
#     bun = dispense_bun()
#     if bun is None:
#         print error_code("Bun is unavailable. check for bun")
#         return
    
#     frank = dispense_frank()
#     if frank is None:
#         print error_code("frank was not properly dispensed")
#         return

#     hot_dog = bun.add_frank(frank)
#     if hot_dog is None:
#         print error_code("Hot Dog unavailable. Check for Hot Dog")
#         return
    
#     ketchup = dispense_ketchup()
#     mustard = dispense_mustard()
    
#     if ketchup is None or mustard is None:
#         print error_code("Check for invalid catsup")
#         return
    
#     hot_dog.add_condiments(ketchup, mustard)
#     dispense_hot_dog_to_customer(hot_dog)
    


# def dispense_bun() -> Bun:
#     if not are_buns_available():
#         return None
#     return Bun('Wheat')


# # Union Types- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# def dispense_snack() -> HotDog:
    
#     if not are_ingredients_available():
#         raise RuntimeError("Not all ingredients available")
#     if order_interrupted():
#         raise RuntimeError("Order interrupted")
    
#     return create_hot_dog



# from typing import Union
# def dispense_snack(user_input: str) -> Union[HotDog, Pretzel]:
#     if user_input == "Hot Dog":
#         return dispense_hot_dog()
    
#     elif user_input == "Pretzel":
#         return dispense_pretzel()
    
#     raise RuntimeError("Should never reach this code," "as an invalid input has been entered")


# from typing import Optional, Union
# def place_order() -> Optional[HotDog]:
#     order = get_order()
#     result = dispense_snack(order.name)
    
#     if result is None:
#         print error_code("An error occurred" + result)
        
#         return None
#    Return  our HotDog
#     return result



# from dataclasses import dataclass
# from typing import Union
# @dataclass
# class Snack:
#     name: str
#     condiments: set[str]
#     error_code: int
#     disposed_of: bool
    
    
# @dataclass
# class Error:
#     error_code: int
#     disposed_of: bool 
    
# @dataclass
# class Snack:
#     name: str
#     condiments: set[str]
    
# snack: Union[Snack, Error] = Snack("Hotdog", {"Mustard", "Ketchup"})

# snack = Error(5, True)





# Snack("Hotdog", {"Mustard", "Ketchup"}, 5, False)


#  Literal Types ------------------------------

# from dataclasses import dataclass
# from typing import Literal
# @dataclass

# class Error:
#     error_code: Literal[1,2,3,4,5]
#     disposed_of: bool
    
# @dataclass

# class Snack: 
#     name: Literal["Pretzel", "Hot Dog", "Veggie Burger"] 
#     condiments: set[Literal['Mustard', "Ketchup"]]
    
    
# Error(0, False)
# Snack("Invalid", set())
# Snack("Pretzel", {"Mustard", "Relish"})


# New Type --------------------------------------------------------

# from typing import NewType

# class HotDog:
    
#     # ... snip hot dog class implementation
    
# ReadyToServeHotDog = NewType("ReadyToServeHotDog", HotDog)

# def dispense_to_customer(hot_dog: ReadyToServeHotDog):
  
# from typing import NewType
# ReadyToServeHotDog = NewType("ReadyToServeHotDog", HotDog)


# def prepare_for_serving(hot_dog: HotDog) -> ReadyToServeHotDog:
#     assert not hot_dog.is_plated(), "Hot dog should not already be plated"
#     hot_dog.put_on_plate()
#     hot_dog.add_napkins()
#     return ReadyToServeHotDog(hot_dog)

# collection Types------------------------------------>

# AuthorToCountMapping = dict[str, int]
# def create_author_count_mapping(cookbooks: list[Cookbook]) -> AuthorToCountMapping:
    
#     counter = defaultdict(lambda: 0)
#     for book in cookbooks:
#         counter[book.author] += 1
        
#     return counter

# Homogeneous Versus Heterogeneous Collections ------------------------>

#  every value of same type.




# from ctypes import Union
# # (none, quantity, units)
# Ingredient = tuple[str, int, str]
# Recipe = list[Union[int, Ingredient]]

# def adjust_recipe(recipe, servings):
    
#     new_recipe = [servings]
#     old_servings = recipe[0]
#     factor = servings / old_servings
#     recipe.pop(0)
#     while recipe:
#         ingredient, amount, unit = recipe.pop(0)
        
#         # please only use numbers that will be easily measurable///
#         new_recipe.append((ingredient, amount * factor, unit))
        
#     return new_recipe


# Cookbook = tuple[str,int]
# food_lab : Cookbook = ("The Food Lab", 958)
# old_bits : Cookbook = ("Old Bits", 248)

# print(food_lab[0])


# TypedDict ------------------------------------->

# from typing import TypedDict
# class Range(TypedDict):
#     min: float
#     max: float
# class NutritionInformation(TypedDict):
#     value: int
#     unit: str
#     confidenceRange95Percent: Range
#     standardDeviation: float
# class RecipeNutritionInformation(TypedDict):
#     recipes_used: int
#     calories: NutritionInformation
#     fat: NutritionInformation
#     protein: NutritionInformation
#     carbs: NutritionInformation
    
    
# # nutrition_information:RecipeNutritionInformation = get_nutrition_from_spoonacular(recipe_name)

# def reverse(coll: list) -> list:
#     return coll[::-1]

# print(reverse([2, 4,5]))



# from typing import TypeVar

# T = TypeVar('T')
# def reverse(coll: list[T]) -> list[T]:
#     return coll[:: -1]

# print(reverse([1,2,3,4,5,6,7]))



# from collections import defaultdict
# from typing import Generic, TypeVar

# Node = TypeVar("Node")
# Edge = TypeVar("Edge")

# class Graph(Generic[Node, Edge]):
#     def __init__(self):
#         self.edges: dict[Node, list[Edge]] = defaultdict(list)
        
#     def add_relation(self, node: Node, to: Edge):
#         self.edges[node].append(to)
        
#     def get_relation(self, node: Node) -> list[Edge]:
#         return self.edges[node]
    
    
# cookbooks: Graph[Cookbook, Cookbook] = Graph()
# recipes: Graph[Recipe, Recipe] = Graph()

# cookbook_recipes: Graph[Cookbook, Recipe] = Graph()

# recipes.add_relation(Recipe('Pasta Bolognese'),Recipe('Pasta with Sausage and Basil'))

# cookbook_recipes.add_relation(Cookbook('The Food Lab'),Recipe('Pasta Bolognese'))

# cookbooks.add_relation(Recipe('Cheeseburger'), Recipe('Hamburger'))



