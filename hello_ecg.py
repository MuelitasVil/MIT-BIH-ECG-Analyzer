from pathlib import Path

import matplotlib.pyplot as plt
import physionet
import wfdb


# Descarga los archivos del registro 100.
# La versión queda fijada para que el ejemplo sea reproducible.
header_path = physionet.fetch(
    "mitdb", "100.hea", version="1.0.0"
)

physionet.fetch(
    "mitdb", "100.dat", version="1.0.0"
)

# WFDB recibe el nombre del registro sin la extensión .hea.
record_path = Path(header_path).with_suffix("")

# Lee el ECG.
record = wfdb.rdrecord(str(record_path))

# Toma los primeros cinco segundos del primer canal.
seconds_to_show = 5
number_of_samples = seconds_to_show * record.fs
signal = record.p_signal[:number_of_samples, 0]
time = [i / record.fs for i in range(number_of_samples)]

print("Hello, ECG!")
print(f"Frecuencia de muestreo: {record.fs} muestras por segundo")
print(f"Canales disponibles: {record.sig_name}")
print(f"Mostrando el canal: {record.sig_name[0]}")

plt.plot(time, signal)
plt.title("Registro ECG 100 — primer canal")
plt.xlabel("Tiempo (segundos)")
plt.ylabel("Amplitud (mV)")
plt.grid(True)
plt.show()
