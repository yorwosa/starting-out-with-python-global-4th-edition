def create_dictionaries():
    JupiterMoons = ('Io','Europa','Ganymede','Callisto')
    Radius = (1821.6,1560.8,2634.1,2410.3)
    Gravity = (1.796,1.314,1.438,1.235)
    Orbit = (1.769,3.551,7.154,16.689)
    MeanRadius = dict()
    SurfaceGravity = dict()
    OrbitalPeriod = dict()
    for index in range(len(JupiterMoons)):
        MeanRadius[JupiterMoons[index]] = Radius[index]
        SurfaceGravity[JupiterMoons[index]] = Gravity[index]
        OrbitalPeriod[JupiterMoons[index]] = Orbit[index]
    return JupiterMoons,MeanRadius, SurfaceGravity,OrbitalPeriod

def main():
    JupiterMoons, MeanRadius, SurfaceGravity, OrbitalPeriod = create_dictionaries()
    print("This program displays information about Jupiter's Moons")
    print()
    print('The Moons are: ',end ='')
    for moon in JupiterMoons:
        print(moon + ' ',end='')
    print()
    choice = input('For which moon, would you like to see more information? ')
    print()
    if choice in JupiterMoons:
        print('Mean Radius in KM: ', MeanRadius[choice])
        print('Surface Gravity in m/sec squared: ', SurfaceGravity[choice])
        print('Orbital period in days: ',OrbitalPeriod[choice])
    else:
        print('There is no moon by this name')

main()
