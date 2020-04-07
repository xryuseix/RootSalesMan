import getDistance as dist
import getPosition as pos

destinations = pos.readCSV()

for li in destinations:
    if li[1]=='-1' or li[2]=='-1':
        li[1], li[2] = pos.getPosition(li[0])
pos.writeCSV(destinations)