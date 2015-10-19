# Practical Programming Chapter 5 exercises

alkaline_earth_metals = [4, 12, 20, 38, 56, 88]
alkaline_earth_metals[5]
alkaline_earth_metals[-1]
len(alkaline_earth_metals)
max(alkaline_earth_metals)

print 'a'
print 'b'
print 'a', 
# Adding a comma after a print statement means the next print statement
# will be on the same line.
print 'b'

celegans_markers = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
for marker in celegans_markers:
    print marker

half_lives = [87.74, 24110.0, 6537.0, 14.4, 376000.0]
for number in half_lives:
    print number,

country_populations = [1295, 23, 7, 3, 47, 21]
total = 0
for population in country_populations:
    total += population
print "\nTotal population is %d" % total

temps = [25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]
temps.sort()
cool_temps = temps[:2]
warm_temps = temps[2:]

temps_in_celsius = cool_temps + warm_temps

temps_in_fahrenheit = []
for temp in temps_in_celsius:
    v = round((temp + 32.0) / 5.0 * 9.0, 2)
    temps_in_fahrenheit.append(v)

alkaline_earth_metals = [[4, 9.012], [12, 24.305], [20, 40.078], [38, 87.62],
                         [56, 137.327], [88, 226]]
for metal in alkaline_earth_metals:
    print "Atomic number:", metal[0]
    print "Atomic weight:", metal[1]
    
number_and_weight = []
for metal in alkaline_earth_metals:
    number_and_weight.append(metal[0])
    number_and_weight.append(metal[1])
    
metals = open("alkaline_metals.txt", "r")
metals_list = metals.readlines()
metals.close()
new_metals_list = []
for line in metals_list:
    v = line.split()
    new_metals_list.append(v)

