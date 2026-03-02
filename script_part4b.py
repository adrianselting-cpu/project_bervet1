#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import route_nyc 

### Given contour plot ###
n_fine = 100
t_fine = np.linspace(0, 24, n_fine)
x_fine = np.linspace(0, 60, n_fine)
tt_fine, xx_fine = np.meshgrid(t_fine, x_fine)
zz_fine = route_nyc.route_nyc(tt_fine,xx_fine)
w, h = plt.figaspect(0.4)
fig = plt.figure(figsize=(w, h))
plt.axes().set_aspect(0.2, adjustable='box')
cs = plt.contourf(tt_fine, xx_fine, zz_fine, 50, cmap='jet')
plt.xlabel('Time [hour of day]',fontsize=18)
plt.ylabel('Distance [km]',fontsize=18)
plt.title('Speed [km/h]',fontsize=18)
fig.colorbar(cs)
plt.savefig("speed-data-nyc.eps", bbox_inches='tight')

# Definiera steglängd h för Euler-metoden
h_step = 0.01

# Beräkna och plotta färd med start kl 04.00
t0_early = 4.0
t_early, x_early, _ = route_nyc.nyc_route_traveler_euler(t0_early, h_step)
plt.plot(t_early, x_early, 'w-', linewidth=2, label='Start 04:00')

# Beräkna och plotta färd med start kl 09.30
t0_late = 9.5
t_late, x_late, _ = route_nyc.nyc_route_traveler_euler(t0_late, h_step)
plt.plot(t_late, x_late, 'm-', linewidth=2, label='Start 09:30')

plt.legend(loc='upper left')