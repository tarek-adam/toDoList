Liste_Aroundi = []
Liste_Actuel = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

for num in Liste_Actuel:
    i = round(num)
    Liste_Aroundi.append(i)

Result = Liste_Aroundi
print("Liste_Aroundi:", Result)

Liste_Ordered = []

# Sorting logic using comparison
for i in range(len(Liste_Aroundi)):
    for j in range(i + 1, len(Liste_Aroundi)):
        if Liste_Aroundi[i] > Liste_Aroundi[j]:
            Liste_Aroundi[i], Liste_Aroundi[j] = Liste_Aroundi[j], Liste_Aroundi[i]

# Print sorted list
print("Liste_Ordered:", Liste_Aroundi)

# The line of code Liste_Aroundi[i], Liste_Aroundi[j] = Liste_Aroundi[j], Liste_Aroundi[i] 
# is an example of Python's multiple assignment feature, commonly used for swapping values between variables without using a temporary variable. 
# This operation is specific to Python and is a part of Python's syntax. 

# This logic effectively exchanges the values of a and b. However, 
# there's a condition implied in your logic: it only performs the swap if a is greater than b. If a is not greater than b, 
# then no swap occurs, and the values remain unchanged.

# This logic is essentially a way to perform a swap operation with three variables. 
# It's commonly used in programming languages like C, 
# where direct swapping of variables isn't as straight forward as it is in some other
# languages.
