import os
import pandas as pd
from io import BytesIO
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext

# URL de tu OneDrive Intel
site_url = "https://intel-my.sharepoint.com/personal/jose_a_navarro_garcia_intel_com"
# Link de descarga directa
file_url = f"{site_url}/_layouts/15/download.aspx?sourcedoc=%7B13e1d868-5ec7-410a-a246-b693fc82cac8%7D"

def generate_onboarding_map():
    username = os.getenv("SP_USERNAME")
    password = os.getenv("SP_PASSWORD")

    if not username or not password:
        print("❌ ERROR: No se detectan los SECRETS en GitHub.")
        return

    print(f"Iniciando conexión para: {username}")
    user_credentials = UserCredential(username, password)
    ctx = ClientContext(site_url).with_credentials(user_credentials)

    try:
        # Intentamos obtener el archivo
        response = ctx.web.send_request(file_url)
        response.raise_for_status()
        
        # Cargar datos
        df = pd.read_excel(BytesIO(response.content))
        print(f"Éxito: Se encontraron {len(df)} filas en el Excel.")

        # Escribir el README
        with open("README.md", "w", encoding='utf-8') as f:
            f.write("# 🗺️ Visual Product Map (Intel Onboarding)\n\n")
            f.write("```mermaid\n")
            f.write("graph LR\n")
            f.write("    classDef category fill:#0071C5,stroke:#fff,stroke-width:2px,color:#fff,font-weight:bold;\n")
            f.write("    classDef product fill:#f4f4f4,stroke:#0071C5,stroke-width:1px,color:#333;\n")

            for index, row in df.iterrows():
                # Forzamos la lectura por posición para evitar errores de nombres
                cat_name = str(row.iloc[0]).strip()
                prod_name = str(row.iloc[1]).strip()
                link = str(row.iloc[2]).strip()

                if cat_name.lower() in ['nan', 'none', ''] or prod_name.lower() in ['nan', 'none', '']:
                    continue

                # IDs limpios para Mermaid
                cat_id = "".join(e for e in cat_name if e.isalnum())
                prod_id = "".join(e for e in prod_name if e.isalnum())[:30] + str(index)

                f.write(f"    {cat_id}([{cat_name}]):::category --> {prod_id}[\"{prod_name}\"]:::product\n")
                if "http" in link:
                    f.write(f"    click {prod_id} \"{link}\" \"Wiki\"\n")
            
            f.write("```\n")
        print("✅ README.md generado localmente en el runner.")

    except Exception as e:
        print(f"❌ FALLO TÉCNICO: {str(e)}")
        # Si esto falla aquí, es el MFA de Intel bloqueando al bot.

if __name__ == "__main__":
    generate_onboarding_map()
