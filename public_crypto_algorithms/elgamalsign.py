

p = 262643
g = 9563
d = 3632
y = (g**d)%p
k=601
m = 152015


bb = None

a=(g**k)%p

x = m + 3322*(p-1) - d*a
print(x/k)

for num in range(1, 5001):
    myFirstNum = m + num*(p-1) -d*a
    if myFirstNum > k:
        bb = myFirstNum/k
    if bb and bb.is_integer():
        print('num= ', num, ' b=', bb) 