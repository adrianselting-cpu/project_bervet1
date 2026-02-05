import roadster
import numpy as np
import matplotlib.pyplot as plt


distance_km, speed_kmph = roadster.load_route('speed_anna.npz')

v = roadster.velocity(distance_km, 'speed_anna.npz')

plt.scatter(distance_km, speed_kmph)
plt.plot(distance_km, v)
print(distance_km)
plt.xlabel('s (km)')
plt.ylabel('v (km/h)')
plt.xlim(-5, 5)
plt.ylim(0,60)
plt.show()