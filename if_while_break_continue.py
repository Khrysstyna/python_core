# всі парні менше 100 USING FOR
for val in range(1,101):
    if val%2==0:
      print(val)

#всі парні менше 100 USING WHILE
val=2
while val<101:
  print(val)
  val+=2

# непарні менше 100 USING CONTINUE
for val in range(1,101):
    if val%2==0:
      continue
    print(val)

#непарні менше 100 NOT USING CONTINUE
for val in range(1,101):
    if val%2==1:
      print(val)

#перевірка на парні числа
for y in [1,3,5,9,8]:
   if y%2==0:
    print("The list contains even number:",y)
    break
else:
  print("The list doesn't contain even number")

#факторіал числа
print("Enter number:")
val=int(input())
fac=1
for val in range(1,val+1):
  fac=val*fac
print("Factorial:",fac)
