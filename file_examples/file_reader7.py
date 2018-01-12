with open('plan.txt', 'r') as file:
    planets = file.readlines()

print(planets)

for planet in reversed(planets):
    print(planet.strip())
