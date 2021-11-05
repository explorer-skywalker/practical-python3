
file_one = open("cosmos.txt")
contents = file_one.read()
file_one.close()    # It's important to close the file...

# print(2*contents)



# Better way to work with a file...

with open("cosmos.txt") as myfile:
    data = myfile.read()

print(data)
