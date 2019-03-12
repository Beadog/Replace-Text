'''
Corrie Stewart
Program finds and replaces text in a file
Date: 10/28/18
'''

def main():
    filename = input("Enter a filename: ").strip()
    infile = open(filename, "r") # Open the file
    data = infile.read() #  Read all lines from the file

    old = input("Enter the old string to be replaced: ")

    while old not in data:
        print("Your input was not found in the file. Please try again.")
        old = input("Enter the old string to be replaced: ")

    new = input("Enter the new string to replace the old string: ")

    dataToWrite = data.replace(old, new)

    infile = open(filename, "w")
    infile.write(dataToWrite)

    print("Replacment complete.")

    infile.close()

main()
