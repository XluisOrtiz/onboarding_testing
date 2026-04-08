import os
import pandas as pd
from io import BytesIO
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext

# URL de tu sitio personal (OneDrive Intel)
site_url = "https://intel-my.sharepoint.com/personal/jose_a_navarro_garcia_intel_com"
# ID del documento Excel
file_url = f"{site_url}/_layouts/15/download.aspx?sourcedoc=%7B13e1d868-5ec7-410a-a246-b693fc82cac8%7D"

def generate_onboarding_map():
    username = os.getenv("SP_USERNAME")
    password = os.getenv("SP_PASSWORD")

    if not username or not password:
        print("❌ Credenciales no encontradas en Secrets.")
        return

    print("Conectando con Office365...")
    user_credentials = UserCredential(username, password)
    ctx = ClientContext(site_url).with_credentials(user_credentials)

    try:
        response = ctx.web.send_request(file_url)
        response.raise_for_status()
        
        # Leemos el Excel
        df = pd.read_excel(BytesIO(response.content))
        print("Excel leído exitosamente.")

        # Escribimos el resultado directamente en el README.md
        with open("README.md", "w", encoding='utf-8') as f:
            f.write("# 🗺️ Visual Product Map (Intel Onboarding)\n\n")
            f.write("Este mapa se genera automáticamente desde el Excel de SharePoint. Haz clic en los roles para ver detalles.\n\n")
            f.write("```mermaid\n")
            f.write("graph LR\n")
            
            # Estilos Intel Tech
            f.write("    classDef category fill:#0071C5,stroke:#fff,stroke-width:2px,color:#fff,font-weight:bold;\n")
            f.write("    classDef product fill:#f4f4f4,stroke:#0071C5,stroke-width:1px,color:#333;\n")

            for _, row in df.iterrows():
                # Extraemos datos basados en tus columnas: AGS role, Description, Notes
                cat_name = str(row.iloc[0]) # AGS role
                prod_name = str(row.iloc[1]) # Description
                link = str(row.iloc[2])      # Notes

                # Saltamos filas vacías
                if cat_name.lower() == 'nan' or prod_name.lower() == 'nan':
                    continue

                # Limpieza de IDs para Mermaid
                cat_id = "".join(filter(str.isalnum, cat_name))
                prod_id = "".join(filter(str.isalnum, prod_name[:20])) # Limitamos largo

                # Dibujamos la relación: AGS Role -> Descripción
                f.write(f"    {cat_id}([{cat_name}]):::category --> {prod_id}[\"{prod_name}\"]:::product\n")
                
                # Si hay un link en la columna Notes, lo hacemos clickable
                if "http" in link:
                    f.write(f"    click {prod_id} \"{link}\" \"Abrir Link\"\n")
            
            f.write("```\n")
        print("✅ README.md actualizado con éxito.")

    except Exception as e:
        print(f"❌ Error durante el proceso: {e}")

if __name__ == "__main__":
    generate_onboarding_map()
