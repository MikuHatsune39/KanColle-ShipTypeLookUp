arr = ["DD", "Destroyer", "DE", "Coastal Defense Ship", "CL", "Light Cruiser", "CT", "Training Cruiser", "CLT", "Torpedo Cruiser", "CA", "Heavy Cruiser", "CAV", "Aviation Cruiser", "BB", "Battleship", "BBV", "Aviation Battleship", "CVL", "Light Aircraft Carrier", "CV", "Regular Aircraft Carrier", "CVB", "Armored Aircraft Carrier", "SSV", "Submarine Aircraft Carrier", "SS", "Submarine", "AV", "Seaplane Tender", "AS", "Submarine Tender", "LHA", "Amphibious Assault Ship", "AO", "Fleet Oiler", "AR", "Repair Ship"]
i = 0
for x in arr:
    #if i == 0 or (i % 2) == 0:
    if (i % 2) != 0:
        print(x)
        i = i + 1
    else:
        i = i + 1
