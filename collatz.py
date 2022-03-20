# Weel 04 Task
# Author: Andras Csullog

# Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.

#  Have the program end if the current value is one.
# Please enter a positive integer: 10
# 10 5 16 8 4 2 1

posInteger = int(input ("Please enter a positive integer: "))
print(posInteger, end=" ")
while posInteger != 1 :
    
    if (posInteger % 2) == 0 :
       posInteger = int(posInteger/2)
    
    else :
        posInteger = int(posInteger*3+1)
    print (posInteger, end=" ")

# Used refenrences:
# https://www.datacamp.com/community/tutorials/loops-python-tutorial?utm_source=adwords_ppc&utm_medium=cpc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=332602034364&utm_targetid=dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9063089&gclid=CjwKCAiA9aKQBhBREiwAyGP5laWVd5eYdz5_VaUe6QEjpvMABW3Dn6WC1D6To2iRG-1yJic3vEMYWBoCWmEQAvD_BwE
# https://www.codegrepper.com/code-examples/python/how+to+print+vertical+line+in+python