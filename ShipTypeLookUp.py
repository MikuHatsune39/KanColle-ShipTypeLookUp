#!/usr/bin/env python3
import os
if os.name == "nt":
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('Ship Type LookUp')

shipNames = {
    "DD": "Destroyer", 
    "DE": "Coastal Defense Ship",
    "CL": "Light Cruiser",
    "CT": "Training Cruiser",
    "CLT": "Torpedo Cruiser",
    "CA": "Heavy Cruiser",
    "CAV": "Aviation Cruiser",
    "BB": "Battleship",
    "BBV": "Aviation Battleship",
    "FBB": "Fast Battleship",
    "CVL": "Light Aircraft Carrier",
    "CV": "Regular Aircraft Carrier",
    "CVB": "Armored Aircraft Carrier",
    "SSV": "Submarine Aircraft Carrier",
    "SS": "Submarine",
    "AV": "Seaplane Tender",
    "AS": "Submarine Tender",
    "LHA": "Amphibious Assault Ship",
    "AO": "Fleet Oiler",
    "AR": "Repair Ship"
}

if __name__ == "__main__":
    keepGoing = True

    while keepGoing:
        inp = str(input("Enter the Short or Long Name for the ship type (enter Q to quit)> "))
        if inp.upper() == "Q":
            keepGoing = False
        else:
            try:
                if len(inp) > 3:
                    print("{}\n".format(
                        list(shipNames.keys())[list(shipNames.values()).index(inp.title())]
                    ))
                    pass
                else:
                    print("{}\n".format(shipNames[inp.upper()]))
            except Exception:
                print("Not Found\n")