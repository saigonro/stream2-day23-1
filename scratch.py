# Read a file into a list
#===================================================
f = open("data.txt", "r")
lines = f.read().split('\n')
f.close()
print(type(lines))
print(lines)

            # New version
            #=======================================
with open('data.txt'):
    lines = f.read().split('\n')

# Write a list out of a file
#===================================================
l = ['hello', 'world', 'this is it']
f = open('output.txt', 'w')
lines = str.join('\n', l)
f.write(lines)
f.close()