#def make_negative( number ):
 #   return -number if number > 0 else number

#print(make_negative(-15))
#print(make_negative(8))


#there was another method of doing the same thing:
def make_negative( number ):
    return -abs(number)

print(make_negative(-15))
print(make_negative(8))