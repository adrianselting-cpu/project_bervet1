import roadster
import numpy as np
import matplotlib.pyplot as plt

files = ['speed_anna.npz', 'speed_elsa.npz']

for file in files: 
    distance_km, speed_kmph = roadster.load_route(file)
    s_fine = np.linspace(0, distance_km[-1], 500)
    v_fine = roadster.velocity(s_fine, file)

    plt.figure()
    plt.scatter(distance_km, speed_kmph)
    plt.plot(s_fine, v_fine)
    print(distance_km)
    plt.title(f'Rutt: {file}')
    plt.xlabel('s (km)')
    plt.ylabel('v (km/h)')
    plt.xlim(4, 10)
    plt.ylim(0,150)
    plt.legend()
    plt.show()