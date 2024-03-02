# --------------------- Q 1 -------------------------------

print('Q 1')

n = 10
for i in range(1,n+1):
    print(i)
    if i == 5:
        break

#------------------------ Q 2 -----------------------------
print('Q 2')

lis = [ 1,2,'re','ft','ph']
for i in lis:
    print(i)
    if i == 'ft':
        break

# ------------------------- Q 3 --------------------------

print('Q 3')

for i in range(n+1):

    if i % 2 == 0:
        continue
    print(i)

#--------------------------- Q 4 -------------------------
    
print(" Q 4 ")    
num = 9 
for i in range(0,num+1):
    print(i) 

# -------------------------- Q 5 -------------------------

print("Q 5")
num2 = 5   
for i in range(1,num2+1):
    for j in range(1, 3):
        r = i * j
        print(f"{i} * {j} = {r} ", end = " ")
        break
    print()
    

# -------------------------- Q 6 -------------------------
    
num = 10
i = 0
while i <= num:
    i = i + 1
    if i % 2 == 0:
        continue
    print(i)