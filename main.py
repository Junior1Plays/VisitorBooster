import requests

print("VisitorBooster\n              made by JuniorSchueller\n\n")

profile = input("(required) Visitor counter URL/link: ")
visits = input("(optional) Number of current visits: ")
plus = False

if visits == "":
    visits = 0
    plus = True


def visitorsIncrease(profileUrl, actualVisits, addPlus):
    r = requests.get(profileUrl)
    if r.status_code == 200:
        actualVisits += 1
        if addPlus == True:
            print("+" + str(actualVisits) + " visits")
        else:
            print(str(actualVisits) + " visits (" + str(actualVisits + 1) + " if you access)")
    else:
        print("Failed to add visit")
    visitorsIncrease(profileUrl, actualVisits, addPlus)
visitorsIncrease(profile, int(visits), plus)
