# Task 2: Write and Append Data to a File

filename = "output.txt"

# Step 1: Take user input and write to file
data = input("Enter something to write into the file: ")

with open(filename, "w") as file:
    file.write(data + "\n")

print("Data written to output.txt")

# Step 2: Append more text to the file
with open(filename, "a") as file:
    file.write("This is appended text.\n")

print("Additional data appended.")

# Step 3: Read and display final file content
print("\nFinal content of output.txt:")

with open(filename, "r") as file:
    print(file.read())
