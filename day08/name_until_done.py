# Keep accepting names until user types 'done'; print all names
names = []
while True:
    name = input("Enter a name (or 'done' to stop): ").strip()
    if name.lower() == "done":
        break
    if name in names:
        print("Duplicate! Already entered.")
    else:
        names.append(name)

print(f"\nYou entered {len(names)} names:")
for n in names:
    print(n)