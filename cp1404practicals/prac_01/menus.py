name = input("Enter name: ")
MENU = "(H)ello\n(G)oodbye\n(Q)uit"
print(MENU)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "H":
        print("Hello", name, sep=" ")
    elif choice == "G":
        print("Goodbye", name, sep=" ")
    else:
        print("Invalid choice")
        choice = input(">>> ")
        print(MENU)
    choice = input(">>> ").upper()
print("Finished")




