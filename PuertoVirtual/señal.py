import numpy as np
import subprocess
import time

while True:
  try:
    al = str(np.random.randint(0,401))
    la = str(np.random.randint(0,401))
    lo = str(np.random.randint(0,401))
    te = str(np.random.randint(0,41))
    pr = str(np.random.randint(0,3))
    hu = str(np.random.randint(0,3))
    ax = str(np.random.randint(-400,401))
    ay = str(np.random.randint(-400,401))
    az = str(np.random.randint(-400,401))
    gx = str(np.random.randint(-400,401))
    gy = str(np.random.randint(-400,401))
    gz = str(np.random.randint(-400,401))

    datos = {"\"Al\"": f'\"{al}\"', "\"La\"": f'\"{la}\"', "\"Lo\"": f'\"{lo}\"', "\"Te\"": f'\"{te}\"', "\"Pr\"": f'\"{pr}\"', "\"Hu\"": f'\"{hu}\"', "\"Ax\"": f'\"{ax}\"', "\"Ay\"": f'\"{ay}\"', "\"Az\"": f'\"{az}\"', "\"Gx\"": f'\"{gx}\"', "\"Gy\"": f'\"{gy}\"', "\"Gz\"": f'\"{gz}\"'}
    datos = str(datos)
    time.sleep(0.5)
    subprocess.Popen([f'echo {datos} > /dev/pts/3'], stdout=subprocess.PIPE, shell=True)

  except KeyboardInterrupt:
    break