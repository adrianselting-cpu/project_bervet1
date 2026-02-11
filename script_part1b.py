import roadster
import numpy as np
import matplotlib.pyplot as plt


distance_km, speed_kmph = roadster.load_route('speed_anna.npz')
distance_km, speed_kmph = roadster.load_route('speed_elsa.npz')

v1 = roadster.velocity(distance_km, 'speed_anna.npz')
v2 = roadster.velocity(distance_km, 'speed_elsa.npz')
v = (v1,v2)

for i in v: 
    plt.scatter(distance_km, speed_kmph)
    plt.plot(distance_km, i)
    print(distance_km)
    plt.xlabel('s (km)')
    plt.ylabel('v (km/h)')
    plt.xlim(-5, 70)
    plt.ylim(0,150)
    plt.show()