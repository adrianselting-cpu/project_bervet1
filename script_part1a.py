#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import roadster

speed_kmph = np.linspace(1., 200., 1000)
consumption_Whpkm = roadster.consumption(speed_kmph)

plt.plot(speed_kmph, consumption_Whpkm)
plt.xlabel("Hastighet (km/h)")
plt.ylabel("Elkonsumtion (Wh/km)")
plt.title("Tesla Roadster: Elkonsumption vs Hastighet")
plt.show()