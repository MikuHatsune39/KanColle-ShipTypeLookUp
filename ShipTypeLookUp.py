shortNames = ["DD", "DE", "CL", "CT", "CLT", "CA", "CAV", "BB", "BBV", "FBB", "CVL", "CV", "CVB", "SSV", "SS", "AV", "AS", "LHA", "AO", "AR"]
fullNames = ["Destroyer", "Coastal Defense Ship", "Light Cruiser", "Training Cruiser", "Torpedo Cruiser", "Heavy Cruiser", "Aviation Cruiser", "Battleship", "Aviation Battleship", "Fast Battleship", "Light Aircraft Carrier", "Regular Aircraft Carrier", "Armored Aircraft Carrier", "Submarine Aircraft Carrier", "Submarine", "Seaplane Tender", "Submarine Tender", "Amphibious Assault Ship", "Fleet Oiler", "Repair Ship"]
keepGoing = True

while keepGoing:
    inp = str(input("Enter the Short Name for the ship type (enter Q to quit)> "))
    if inp.upper() == "Q":
        keepGoing = False
    else:
        i = 0
        while i < len(shortNames):
            if inp.upper() == shortNames[i]:
                print(fullNames[i] + "\n")
                break
            i = i + 1
        if i >= len(shortNames):
            print("Not Found\n")