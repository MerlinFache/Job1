L = ['5','6','7','8','9']
def replace():
    new_value = L[2] + L[4]
   # L[3] - L[2] + L[4]
    L[3] = new_value
    L.pop(3)
    L.insert(3,new_value)

    return L

print(replace())