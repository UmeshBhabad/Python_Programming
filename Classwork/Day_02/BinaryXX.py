# Indexed
# Ordered
# Mutable

Data = bytearray([65, 97, 98])

print(Data)         # Aab
print(type(Data))   # bytes
print(Data[0])      # 65

Data[0] = 66

print(Data[0])      # 66