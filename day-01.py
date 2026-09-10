#there are 5280 feet in a mile , write the python statement that calculates and print the number of feet in 13 miles
mile = 13
feet_per_miles = 5280
total_feet = mile * feet_per_miles
print(total_feet)

#2. write a python that calculate and print number of seconds in 7 hours 21 minutes 37 seconds
hour = 7
minutes = 21
second = 37
total_second = hour*60*60 + minutes*60 + second
print(total_second)

#3. the perimetrt of a rctangle is 2w + 2h, where w and h are two side of rectanglewwrite the python statement that caluate and prints the length in incxhes of the perimeter ofr a rectanglke whose side length is 4 and 7 inches
length = 4
breath = 7
perimeter = 2*length + 2*breath
print(perimeter + "feet")

#4.the area of the reactangle is wh , where w and h are length of its side calculate and print area of the square in inches length id 4 and 7 
length_1 = 4
length_2 = 7
area = Length_1 * Length_2
print(area , "inches")

#5. the circumstances of a circle is 2*3.14*r where r = radiuys , calulate circumference where r = 8
radius = 8
circumference = 2 * 3.14 * radius
print(circumference)

#6. the area of a circle is 3.14 *r^2, where r is = 8
radius = 8
area = 3.14 *radius * radius
print(area)

#7. given p doller, the value of this money when compounded year at a rate of r percent interest for y year is p(1+0'01r)^y. write python statement that calculate and print the values of 1000 dollar compounding at a rate 7 perecnt interest in 10 year
p = 1000
r = 7
year = 10
total_value_interest = p*(1+0.01*r)**year
print(total_value_interest)

#8. write a python statemrnt that combines the three string "my name is " "joe" nad "worren"
print("my name is " + "joe" +" "+ "warren")

#9.write a python program to cobine 52 year old with previous question
print("my name is " + "joe"+ " " + "warren"+ "and i am " + str(52) + " "+ "years old")


