#Remove the time

def shorten_to_date(long_date):
  y=long_date.find(',')
  return long_date[0:y]