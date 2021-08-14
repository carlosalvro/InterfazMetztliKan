import json_v3
import numpy as np
import serial

al = np.random.randint(0,401)
la = np.random.randint(0,401)
lo = np.random.randint(0,401)
te = np.random.randint(0,41)
pr = np.random.randint(0,3)
hu = np.random.randint(0,3)
ax = np.random.randint(-400,401)
ay = np.random.randint(-400,401)
az = np.random.randint(-400,401)
gx = np.random.randint(-400,401)
gy = np.random.randint(-400,401)
gz = np.random.randint(-400,401)

dic = {"Al": al, "La":la, "Lo":lo, "Te": te, "Pr": pr, "Hu": hu,"Ax": ax,"Ay": ay,"Az": az,"Gx": gx,"Gy": gy,"Gz": gz}
datos_recibidos = str(dic)

print(datos_recibidos)


ser = serial.Serial('/dev/pts/5')
ser.readline()

al, la, lo, te, pr, hu, ax, ay, az, gx, gy, gz
