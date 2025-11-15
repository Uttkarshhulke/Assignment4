Assignment : 4		

try:
    file = open("sample.txt", "r")   # Try opening the file
    print("File found! Printing content:\n")

    for line in file:
        print(line.strip())          # Print each line without extra newline

    file.close()

except FileNotFoundError:
    print("Error: sample.txt does not exist!")
    print("Please make sure the file is present in the same folder.")
