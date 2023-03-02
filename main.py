import matplotlib.pyplot as plt
import os.path
from typing import Tuple



ProductionBonusTech = 0.3
bioTrophyJob = 15
bioTrophyProd = 0.01 # Multiply fabricatorOutput by this total per bioTrophy
fabricatorJob = 6 # Add 2 to total due to building
mineralUpkeep = 12*(1.3-0.2) # assumes foundry designation AND tier 3 production bonus

def genGraph(size):
    basePlanetSize = size
    planetSize = basePlanetSize + 4  # For orbital Ring
    x1: [int] = []
    y1: [float] = []
    u1: [Tuple] = []  # Upkeep per at every index, 0 being minerals, 1 being food, 2 being consumer goods
    fabricatorProd = 7  # (4 base + 2 from building + 1 from orbital ring)
    for i in range(planetSize + 1):
        x1.append(i)
        totalAlloyJobs = fabricatorJob * (planetSize - i)
        alloyOut = round((fabricatorProd * (totalAlloyJobs + 2)) * (
                    1.2 + ProductionBonusTech + (i * bioTrophyJob) * bioTrophyProd), 3)
        y1.append(alloyOut)
        u1.append([round(((totalAlloyJobs + 2) * mineralUpkeep), 2), (i * bioTrophyJob), (i * bioTrophyJob)])

    x2: [int] = x1
    y2: [float] = []
    u2: [Tuple] = []
    fabricatorProd = 7
    for i in range(planetSize + 1):
        totalAlloyJobs = fabricatorJob * (planetSize - i)
        alloyOut = round((fabricatorProd * (totalAlloyJobs + 2)) * (
                    1.15 + ProductionBonusTech + (i * bioTrophyJob) * bioTrophyProd), 3)
        y2.append(alloyOut)
        u2.append([round(((totalAlloyJobs + 2) * mineralUpkeep), 2), (i * bioTrophyJob), (i * bioTrophyJob)])

    x3: [int] = x1
    y3: [float] = []
    u3: [Tuple] = []
    fabricatorProd = 6  # (4 base + 2 from building)
    for i in range(planetSize + 1):
        if basePlanetSize - i <= 0:
            totalAlloyJobs = 0
        else:
            totalAlloyJobs = fabricatorJob * (basePlanetSize - i)
        alloyOut = round((fabricatorProd * (totalAlloyJobs + 2)) * (
                    1.2 + ProductionBonusTech + (i * bioTrophyJob) * bioTrophyProd), 3)
        y3.append(alloyOut)
        u3.append([round(((totalAlloyJobs + 2) * mineralUpkeep), 2), (i * bioTrophyJob), (i * bioTrophyJob)])

    x4: [int] = x1
    y4: [float] = []
    u4: [Tuple] = []
    fabricatorProd = 6
    for i in range(planetSize + 1):
        if basePlanetSize - i <= 0:
            totalAlloyJobs = 0
        else:
            totalAlloyJobs = fabricatorJob * (basePlanetSize - i)
        alloyOut = round((fabricatorProd * (totalAlloyJobs + 2)) * (
                    1.15 + ProductionBonusTech + (i * bioTrophyJob) * bioTrophyProd), 3)
        y4.append(alloyOut)
        u4.append([round(((totalAlloyJobs + 2) * mineralUpkeep), 2), (i * bioTrophyJob), (i * bioTrophyJob)])

    # get max indexes
    max1 = [index for index, item in enumerate(y1) if item == max(y1)]
    max2 = [index for index, item in enumerate(y2) if item == max(y2)]
    max3 = [index for index, item in enumerate(y3) if item == max(y3)]
    max4 = [index for index, item in enumerate(y4) if item == max(y4)]

    plt.figure(figsize=(12, 6))
    plt.rcParams.update({'font.size': 8})
    title = "Base Planet Size " + str(basePlanetSize)
    lab1 = "OR + EP: " + str(max(y1)) + " alloys at: " + str(max1) + " sanctuary districts"
    lab2 = "Orbital Ring: " + str(max(y2)) + " alloys at: " + str(max2) + " sanctuary districts"
    lab3 = "Efficient Processors: " + str(max(y3)) + " alloys at: " + str(max3) + " sanctuary districts"
    lab4 = "Base Production: " + str(max(y4)) + " alloys at: " + str(max4) + " sanctuary districts"
    plt.scatter(x1, y1, label=lab1, color="blue", marker="*", s=20)
    plt.scatter(x2, y2, label=lab2, color="purple", marker="*", s=20)
    plt.scatter(x3, y3, label=lab3, color="green", marker="*", s=20)
    plt.scatter(x4, y4, label=lab4, color="red", marker="*", s=20)

    fileName: str = "Size" + str(basePlanetSize) + ".txt"
    graphFileName: str = "Size" + str(basePlanetSize) + ".png"
    plt.xlabel('Sanctuary Arcologies')
    plt.ylabel('Alloy Output')
    plt.title(title)
    plt.legend()
    plt.savefig(os.path.join("dataCollected", graphFileName))
    try:
        with open(os.path.join("dataCollected", fileName), "x") as f:
            f.write("OR+EP:\n")
            for i in range(len(y1)):
                f.write(str(x1[i]) + " : " + str(y1[i]) + " : " + str(u1[i][0]) + " : " + str(u1[i][1]) + " : " + str(
                    u1[i][2]) + '\n')
            f.write("\nOrbital Ring:\n")
            for i in range(len(y2)):
                f.write(str(x2[i]) + " : " + str(y2[i]) + " : " + str(u1[i][0]) + " : " + str(u1[i][1]) + " : " + str(
                    u1[i][2]) + '\n')
            f.write("\nEfficient Processors:\n")
            for i in range(len(y3) - 4):
                f.write(str(x3[i]) + " : " + str(y3[i]) + " : " + str(u1[i][0]) + " : " + str(u1[i][1]) + " : " + str(
                    u1[i][2]) + '\n')
            f.write("\nBase Production:\n")
            for i in range(len(y4) - 4):
                f.write(str(x4[i]) + " : " + str(y4[i]) + " : " + str(u1[i][0]) + " : " + str(u1[i][1]) + " : " + str(
                    u1[i][2]) + '\n')
    except FileExistsError:
        with open(os.path.join("dataCollected", fileName), "w") as f:
            f.write("OR+EP:\n")
            for i in range(len(y1)):
                f.write(str(x1[i]) + " : " + str(y1[i]) + " : " + str(u1[i][0]) + " : " + str(u1[i][1]) + " : " + str(
                    u1[i][2]) + '\n')
            f.write("\nOrbital Ring:\n")
            for i in range(len(y2)):
                f.write(str(x2[i]) + " : " + str(y2[i]) + " : " + str(u1[i][0]) + " : " + str(u1[i][1]) + " : " + str(
                    u1[i][2]) + '\n')
            f.write("\nEfficient Processors:\n")
            for i in range(len(y3) - 4):
                f.write(str(x3[i]) + " : " + str(y3[i]) + " : " + str(u1[i][0]) + " : " + str(u1[i][1]) + " : " + str(
                    u1[i][2]) + '\n')
            f.write("\nBase Production:\n")
            for i in range(len(y4) - 4):
                f.write(str(x4[i]) + " : " + str(y4[i]) + " : " + str(u1[i][0]) + " : " + str(u1[i][1]) + " : " + str(
                    u1[i][2]) + '\n')
    plt.close()


for size in range(6,33):
    genGraph(size)
genGraph(39)
#plt.show()