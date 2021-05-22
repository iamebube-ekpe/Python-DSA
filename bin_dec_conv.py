def convertToBinary(num):
   if num > 1:
       convertToBinary(num//2)
   print(num % 2,end = '')

# decimal number
dec = 128

convertToBinary(dec)
print()