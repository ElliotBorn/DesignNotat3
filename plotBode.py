import pandas as pd
import matplotlib.pyplot as plt

# Filsti til CSV-filen
filnavn = "default.csv"  # <-- Endre til ditt faktiske filnavn

# Les data direkte (ingen rader å hoppe over)
df = pd.read_csv(filnavn)

# Rens kolonnenavn
df.columns = [col.strip() for col in df.columns]

# Hent frekvens og magnitude
frekvens = pd.to_numeric(df['Frequency (Hz)'], errors='coerce')
magnitude_db = pd.to_numeric(df['Channel 1 Magnitude (dB)'], errors='coerce')

# Fjern ugyldige verdier
mask = (frekvens > 0) & magnitude_db.notna()
frekvens = frekvens[mask]
magnitude_db = magnitude_db[mask]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(frekvens, magnitude_db, linewidth=2)
plt.xscale('log')
plt.xlabel('Frekvens [Hz]')
plt.ylabel('Gain [dB]')
plt.title('Bode Diagram – Magnitude')
plt.grid(True, which='both', ls=':')
plt.axvline(x=1918, color='r')
plt.tight_layout()
plt.show()
