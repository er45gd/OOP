file1=open("myText.txt", "a")

file1.writelines("Hello World ")
file1.writelines(input("Enter Your Name: "))
file1.close()

file2 = open("mytext.txt", "r")

for line in file2:
    print(line)

file2.close()