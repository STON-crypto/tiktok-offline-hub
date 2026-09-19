import json
import os
import random
import time

LINKS_FILE = "links.json"
MAX_ALMACEN = 5000
VIDEOS_DIARIOS = 150

def cargar_datos():
    if os.path.exists(LINKS_FILE):
        with open(LINKS_FILE, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                return data
            except json.JSONDecodeError:
                return {"creadores": [], "almacen_enlaces": [], "historial_vistos": []}
    return {"creadores": [], "almacen_enlaces": [], "historial_vistos": []}

def guardar_datos(data):
    with open(LINKS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def simular_antibloqueo():
    time.sleep(random.uniform(2.0, 5.0))

def main():
    print("[*] Iniciando motor de recolección y rotación inteligente...")
    datos = cargar_datos()
    
    print(f"[*] Recolectando {VIDEOS_DIARIOS} enlaces diarios bajo protección...")
    nuevos_enlaces_simulados = [f"tiktok_video_fresco_{random.randint(10000, 99999)}" for _ in range(VIDEOS_DIARIOS)]
    
    if "almacen_enlaces" not in datos:
        datos["almacen_enlaces"] = []
        
    for enlace in nuevos_enlaces_simulados:
        simular_antibloqueo()
        datos["almacen_enlaces"].append(enlace)
        if len(datos["almacen_enlaces"]) > MAX_ALMACEN:
            datos["almacen_enlaces"].pop(0)
            
    guardar_datos(datos)
    print(f"[+] Almacén actualizado con éxito. Total en bodega: {len(datos['almacen_enlaces'])} enlaces rotando fresco.")

if __name__ == "__main__":
    main()
