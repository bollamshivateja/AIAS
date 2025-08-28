f = open("numbers.txt","r")
nums =f.readlines()
squares=[]
for n in nums:
    n=n.strip()
    if n.isdigit( ):
        squares.append(int(n)*int(n))
f.close()
f2=open("squares.txt","w")
for sq in squares:
    f2.write(str(sq)+ "\n")
    f2.close()
print("squares written")
