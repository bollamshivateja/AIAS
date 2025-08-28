data = open("input.txt","r").readlines()
output = open("output.txt","w")
for line in data:
    output.write(line.upper())
    output.close()
print("processing done")