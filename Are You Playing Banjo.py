#Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump/mpg<=fuel_left:
        return True
    else:
        return False
================================
#Will there be enough space?

def enough(cap, on, wait):
    if cap-on<wait:
        return wait-(cap-on)
    else:
        return 0
============================
#Are You Playing Banjo?

def areYouPlayingBanjo(name):
    if name[0]=='R'or name[0]=='r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
==============================
#Convert boolean values to strings 'Yes' or 'No'.

def bool_to_word(boolean):
    if boolean==True:
        return 'Yes'
    if boolean==False:
        return 'No'
=============================
#Is this my tail?

def correct_tail(body, tail):
    tail=str(tail)
    sub = body[len(body)-1]
    sub=str(sub)
    if sub == tail:
        return True
    else:
        return False
=========================
Simple: Find The Distance Between Two Points

def distance(x1, y1, x2, y2):
    x=x1-x2
    y=y1-y2
    return round((x**2+y**2)**0.5, 2)
=======================================
Counting sheep...

def count_sheeps(sheep):
  return = sheep.count(True)
  
======================
No yelling!

def filter_words(st):
  return(st[0].upper()+st[1:len(st)+1].lower())
=====================================
Unfinished Loop - Bug Fixing #1

def create_array(n):
    res=[]
    i=1
    while i<=n: 
      res+=[i]
      i=i+1
    return res

========================
Reverse List Order
def reverse_list(l):
  return l.reverse()
===============================
Grasshopper - Summation

def summation(num):
    i=1
    sum=0
    while i<=num in range(num+1):
      sum+=i
      i=i+1
    return sum
==============================
Count of positives / sum of negatives

def count_positives_sum_negatives(arr):
  if arr==[]:
    return []
  else:
    videmni=[i for i in arr if i<=0]
    dodatni=[i for i in arr if i>0]
    my_list=[len(dodatni), sum(videmni)]
    return(my_list)
==============================
Double Char

def double_char(s):
  y=list(s)
  double=[x*2 for x in y]
  double=''.join(double)
  return double
  pass
========================
Remove the time

def shorten_to_date(long_date):
  y=long_date.find(',')
  return long_date[0:y]
=======================
Is the string uppercase?

def is_uppercase(inp):
  y=inp.lower()
  if inp[0]==y[0]:   
    return False  
  else:
    return True