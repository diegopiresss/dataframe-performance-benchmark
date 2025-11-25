import psutil
import time
import sys
import os

# Argumentos: arquivo primeiro, intervalo depois
arquivo = sys.argv[1] if len(sys.argv) > 1 else "memoria_log.csv"
intervalo = float(sys.argv[2]) if len(sys.argv) > 2 else 0.1

os.makedirs(os.path.dirname(arquivo) if os.path.dirname(arquivo) else '.', exist_ok=True)

with open(arquivo, 'w') as f:
    f.write("tempo_s,memoria_gb\n")

with open("monitor_pid.txt", "w") as f:
    f.write(str(os.getpid()) + "\n")

tempo_inicial = time.time()
try:
    while True:
        mem_gb = psutil.virtual_memory().used / (1024**3)
        tempo = time.time() - tempo_inicial
        
        with open(arquivo, 'a') as f:
            f.write(f"{tempo:.2f},{mem_gb:.3f}\n")
        
        time.sleep(intervalo)
except:
    pass
finally:
    if os.path.exists("monitor_pid.txt"):
        os.remove("monitor_pid.txt")