vector1 = [2, 6, -7, 9]
vector2 = [7, 80, 32, -1]

mult() = zip(vector1,vector2)

res = 0

def mult(data):
  for i, j in mult(data):
    res += i * j
   return res
  print(res)