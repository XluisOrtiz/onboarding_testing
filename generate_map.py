import sharepy
import pandas as pd
from io import BytesIO

# 1. Your SharePoint Site (The base URL)
# Example: "https://intel.sharepoint.com/sites/YourTeamSite"
SITE_URL = "https://intel.sharepoint.com/sites/Navarro_Garcia_Jose_A" 

# 2. The Direct Path to the file
# This is the link you just copied, but only the part after the site name
FILE_PATH = "/Documents/YourFileName.xlsx" 

def generate_onboarding_map():
    # Authenticate (This will open a login window the first time)
    s = sharepy.connect(SITE_URL)
    
    # Download the file
    r = s.get(f"{SITE_URL}{FILE_PATH}?download=1")
    
    if r.status_code == 200:
        df = pd.read_excel(BytesIO(r.content))
        
        # Mapping your Excel Columns (Adjust names if they differ)
        # Based on your image, I see "Dynatrace", "IT Scan Team", etc.
        with open("PRODUCT_MAP.md", "w") as f:
            f.write("# 🗺️ Visual Product Map\n\n")
            f.write("```mermaid\n")
            f.write("graph LR\n")
            
            for _, row in df.iterrows():
                # Let's assume Column A is 'Category' and B is 'Product'
                cat = str(row.iloc[0]).replace(" ", "_")
                prod = str(row.iloc[1]).replace(" ", "_")
                link = str(row.iloc[2]) # Assuming Column C is the URL
                
                f.write(f"    {cat} --> {prod}\n")
                f.write(f"    click {prod} \"{link}\" \"Open Documentation\"\n")
            
            f.write("```\n")
        print("✅ PRODUCT_MAP.md has been generated!")
    else:
        print(f"❌ Failed to connect. Status: {r.status_code}")

if __name__ == "__main__":
    generate_onboarding_map()
