import os
import pandas as pd
from io import BytesIO
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext

# URL de tu sitio personal (OneDrive)
site_url = "https://intel-my.sharepoint.com/personal/jose_a_navarro_garcia_intel_com"
# El ID del documento que sacamos de tu link
file_url = f"{site_url}/_layouts/15/download.aspx?sourcedoc=%7B13e1d868-5ec7-410a-a246-b693fc82cac8%7D"

def generate_onboarding_map():
    username = os.getenv("SP_USERNAME")
    password = os.getenv("SP_PASSWORD")

    if not username or not password:
        print("❌ Credenciales no encontradas.")
        return

    # 1. Autenticación profesional
    user_credentials = UserCredential(username, password)
    ctx = ClientContext(site_url).with_credentials(user_credentials)

    print("Intentando descargar el archivo...")
    try:
        # 2. Descarga directa usando el contexto de Office365
        response = ctx.web.send_request(file_url)
        response.raise_for_status()
        
        # 3. Procesar con Pandas
        df = pd.read_excel(BytesIO(response.content))
        print("Archivo leído correctamente.")

        with open("PRODUCT_MAP.md", "w", encoding='utf-8') as f:
            f.write("# 🗺️ Visual Product Map\n\n")
            f.write("```mermaid\n")
            f.write("graph LR\n")
            f.write("    classDef category fill:#0071C5,stroke:#fff,stroke-width:2px,color:#fff,font-weight:bold;\n")
            f.write("    classDef product fill:#f4f4f4,stroke:#0071C5,stroke-width:1px,color:#333;\n")

            for _, row in df.iterrows():
                # Asumimos Columnas: 0=Cat, 1=Prod, 2=Link
                cat = str(row.iloc[0]).replace(" ", "_").replace("&", "And")
                prod = str(row.iloc[1]).replace(" ", "_").replace("&", "And")
                link = str(row.iloc[2])

                f.write(f"    {cat}([{row.iloc[0]}]):::category --> {prod}[{row.iloc[1]}]:::product\n")
                if "http" in link:
                    f.write(f"    click {prod} \"{link}\" \"Ver Wiki\"\n")
            
            f.write("```\n")
        print("✅ PRODUCT_MAP.md generado.")

    except Exception as e:
        print(f"❌ Error: {e}")
        print("Nota: Si el error persiste, es probable que el MFA (Duo) de Intel esté bloqueando el acceso automático.")

if __name__ == "__main__":
    generate_onboarding_map()
