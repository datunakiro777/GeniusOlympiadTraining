
solar_energy = str(input('enter solar energies: '))
solar_energy_list = solar_energy.split()
wind_source = str(input('enter wind sources: '))
wind_source_list = wind_source.split()
distance = []
wind_source_len = len(wind_source_list)
answer = 0
for i in solar_energy_list:
    for n in wind_source_list:
        d = int(i) - int(n)
        d = abs(d)
        distance.append(d)
        if n == wind_source_list[wind_source_len - 1]:
            best_distance = int(min(distance))
            answer += best_distance
print(answer)