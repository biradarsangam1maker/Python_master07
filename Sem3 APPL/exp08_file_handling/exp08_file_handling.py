file_object = open('file.txt', 'r')

data = file_object.read()
print(data)
file_object.close() # must close!


with open("input.txt","r") as file:
    lines = file.readlines()

print("Total number of lines: ",len(lines))

first_two_lines = lines[:2]

print("First 2 lines: ")
for line in first_two_lines:
    print(line, end="")

with open("output.txt", "w") as file:
    file.writelines(first_two_lines)

print("First 2 lines are successfully written to output.txt")
