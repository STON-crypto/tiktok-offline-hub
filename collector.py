import json
import os

LINKS_FILE = "links.json"
MAX_LINKS = 5000

def cargar_enlaces():
    if os.path.exists(LINKS_FILE):
        with open(LINKS_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def guardar_enlaces(enlaces):
    with open(LINKS_FILE, "w", encoding="utf-8") as f:
        json.dump(enlaces, f, ensure_ascii=False, indent=2)

def main():
    print("[*] Iniciando ciclo de recolección en la nube...")
    
    enlaces_actuales = cargar_enlaces()
    
    # Simulación de nuevos enlaces recolectados de forma segura en este ciclo
    # (Aquí es donde luego conectaremos la lógica de extracción o tus fuentes)
    nuevos_enlaces = [
        "https://www.tiktok.com/@ejemplo/video/nuevo_1",
        "https://www.tiktok.com/@ejemplo/video/nuevo_2"
    ]
    
    # Agregar los nuevos enlaces a la lista
    for link in nuevos_enlaces:
        if link not in enlaces_actuales:
            enlaces_actuales.append(link)
            
    # Aplicar la regla FIFO: Si pasamos el techo de 5000, eliminamos los más viejos (los primeros de la lista)
    if len(enlaces_actuales) > MAX_LINKS:
        exceso = len(enlaces_actuales) - MAX_LINKS
        enlaces_actuales = enlaces_actuales[exceso:]
        print(f"[*] Se eliminaron {exceso} enlaces antiguos para respetar el límite de {MAX_LINKS}.")
        
    guardar_enlaces(enlaces_actuales)
    print(f"[+] Total de enlaces en la bodega: {len(enlaces_actuales)}")

if __name__ == "__main__":
    main()
