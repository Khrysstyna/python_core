#Count of positives / sum of negatives

def count_positives_sum_negatives(arr):
  if arr==[]:
    return []
  else:
    videmni=[i for i in arr if i<=0]
    dodatni=[i for i in arr if i>0]
    my_list=[len(dodatni), sum(videmni)]
    return(my_list)