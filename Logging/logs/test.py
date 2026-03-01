from logger import logging

def addition(a,b):
  logging.debug("The addition operation is taking place")
  return a+b

logging.debug("The adddition operation has took place")
print(addition(34,56))
