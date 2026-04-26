from oopconcepts.rectangle import Rectangle
from oopconcepts.square import Sqaure



sqobj  = Sqaure(10)

print(f'Area_of_sq: {sqobj.calculate_area()} \tPerimeter_of_sq: {sqobj.calculate_perimeter()}')

rectobj = Rectangle(10, 5)
print(f'Area_of_rect: {rectobj.calculate_area()} \tPerimeter_of_rect: {rectobj.calculate_perimeter()}')
