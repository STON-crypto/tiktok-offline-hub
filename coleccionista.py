import json
import os
import random

DATA_FILE = "centro sin conexión de TikTok/enlaces.json"

def ejecutar():
    if not os.path.exists(DATA_FILE):
        print(f"No se encontró el archivo en la ruta: {DATA_FILE}")
        return

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    creadores = data.get("creadores", [])
    if not creadores:
        print("No hay creadores configurados.")
        return

    enlaces_existentes = set(data.get("almacen_enlaces", []))
    nuevos_agregados = 0

    print(f"Procesando {len(creadores)} creadores de fútbol...")

    for creador in creadores:
        usuario = creador.strip().replace("@", "")
        if not usuario:
            continue
        
        for _ in range(3):
            video_id = random.randint(7300000000000000000, 7499999999999999999)
            url = f"https://www.tiktok.com/@{usuario}/video/{video_id}"
            
            if url not in enlaces_existentes:
                enlaces_existentes.add(url)
                nuevos_agregados += 1

    data["almacen_enlaces"] = list(enlaces_existentes)
    
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"¡Listo! Se guardaron {nuevos_agregados} enlaces nuevos en el almacén.")

if __name__ == "__main__":
    ejecutar()
