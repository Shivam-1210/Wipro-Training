from basic_programs.basicshapes import area_of_square, perimeter_of_square, area_of_rectangle
from basic_programs.circle import area_of_circle, perimeter_of_circle

radius =  int(input('enter radius'))

print('Area: ',area_of_circle(rad = radius))

print('Perm:', perimeter_of_circle(rad = radius))

si =  int(input('enter side of sq'))

print('Area: ',area_of_square(side = si))

print('Perm:', perimeter_of_square(side = si))

l = int(input('enter length'))
b = int(input('enter breadth'))

print('Area', area_of_rectangle(l, b))