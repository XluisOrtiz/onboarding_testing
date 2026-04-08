import sharepy
import pandas as pd
import os
from io import BytesIO

# --- CONFIGURACIÓN DE ENLACES ---
# La base de tu sitio personal en Intel
SITE_URL = "https://intel-my.sharepoint.com/personal/jose_a_navarro_garcia_intel_com"

# El link directo de descarga que armamos con tu ID de documento
SHAREPOINT_URL = f"{SITE_URL}/_layouts/15/download.aspx?sourcedoc=%7B13e1d868-5ec7-410a-a246-b693fc82cac8%7D"

def generate_onboarding_map():
    # 1. Obtener credenciales de los Secrets de GitHub
    username = os.getenv("SP_USERNAME")
    password = os.getenv("SP_PASSWORD")

    if not username or not password:
        print("❌ Error: No se encontraron las credenciales SP_USERNAME o SP_PASSWORD en GitHub Secrets.")
        return

    print("Conectando a SharePoint...")
    # 2. Autenticación automática (sin pedir input)
    s = sharepy.connect(SITE_URL, username=username, password=password)
    
    # 3. Descargar el archivo
    r = s.get(SHAREPOINT_URL)
    
    if r.status_code == 200:
        print("Archivo descargado con éxito. Procesando datos...")
        # Leer el Excel desde la memoria
        df = pd.read_excel(BytesIO(r.content))
        
        # 4. Crear el archivo Markdown con el mapa visual
        with open("PRODUCT_MAP.md", "w", encoding='utf-8') as f:
            f.write("# 🗺️ Visual Product Map\n\n")
            f.write("Este mapa se genera automáticamente desde el Excel en SharePoint. Haz clic en los productos para ir a su documentación.\n\n")
            f.write("```mermaid\n")
            f.write("graph LR\n") # LR es para vista horizontal
            
            # Estilos visuales
            f.write("    classDef category fill:#0071C5,stroke:#fff,stroke-width:2px,color:#fff,font-weight:bold;\n")
            f.write("    classDef product fill:#f4f4f4,stroke:#0071C5,stroke-width:1px,color:#333;\n")

            for _, row in df.iterrows():
                # IMPORTANTE: Aquí usamos iloc para agarrar las columnas por posición
                # iloc[0] es la primera columna (Categoría)
                # iloc[1] es la segunda columna (Producto)
                # iloc[2] es la tercera columna (Link)
                
                cat_raw = str(row.iloc[0])
                prod_raw = str(row.iloc[1])
                link = str(row.iloc[2])

                # Limpiar nombres para que Mermaid no se rompa (quitar espacios para IDs)
                cat_id = cat_raw.replace(" ", "_").replace("&", "And")
                prod_id = prod_raw.replace(" ", "_").replace("&", "And")
                
                # Crear la relación y aplicar estilos
                f.write(f"    {cat_id}([{cat_raw}]):::category --> {prod_id}[{prod_raw}]:::product\n")
                
                # Hacer el nodo interactivo
                if "http" in link:
                    f.write(f"    click {prod_id} \"{link}\" \"Ver documentación\"\n")
            
            f.write("```\n")
        print("✅ PRODUCT_MAP.md generado correctamente.")
    else:
        print(f"❌ Error al conectar a SharePoint. Status: {r.status_code}")
        print("Verifica que el link sea correcto y que las credenciales tengan acceso.")

if __name__ == "__main__":
    generate_onboarding_map()
