def isAnagram():
    print("This program checks whether input given by user is anagram or not.")
    a = input("Enter the first string: ")
    b = input("Enter the second string: ")
    if len(a) != len(b):
        print("False")
    elif sorted(a) == sorted(b):
        print("True")
    else:
        print("False")

isAnagram()