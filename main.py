# Compute time to die, once event horizon is crossed
# M is mass of Black Hole, solar masses
# T is time, seconds
import pandas as pd

data = []
# M_bh = 20
M_solar = 1

# t = (1.54E-5 * M_bh) / M_solar

import pandas as pd77
data = []
for M_BlackHole in range(20, 3000001, 50):
    t = (1.54E-5 * M_BlackHole) / M_solar
    data.append({'Black Hole Mass (Solar Masses)': M_BlackHole, 'Time remaining before Singularity reached (Seconds)': t})


df = pd.DataFrame(data)
print(df)