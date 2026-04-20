import json
import os
from tqdm import tqdm

BASE_PATH = r"C:\Users\shaki\Desktop\bgd_admin_boundaries.geojson"

ADM1_FILE = f"{BASE_PATH}\\bgd_admin1.geojson"
ADM2_FILE = f"{BASE_PATH}\\bgd_admin2.geojson"
ADM3_FILE = f"{BASE_PATH}\\bgd_admin3.geojson"
ADM4_FILE = f"{BASE_PATH}\\geoBoundaries-BGD-ADM4_simplified.geojson"

# ---------------- OUTPUT FOLDER ----------------
OUTPUT_FOLDER = "name_base"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ---------------- LOAD FILES ----------------
print("Loading files...")

adm1 = json.load(open(ADM1_FILE, encoding="utf-8"))["features"]
adm2 = json.load(open(ADM2_FILE, encoding="utf-8"))["features"]
adm3 = json.load(open(ADM3_FILE, encoding="utf-8"))["features"]
adm4 = json.load(open(ADM4_FILE, encoding="utf-8"))["features"]

# ---------------- OUTPUT LISTS ----------------
divisions = []
districts = []
upazilas = []
unions = []

# ---------------- DIVISION ----------------
print("\nProcessing Division...")
pk = 1
for f in tqdm(adm1):
    name = f["properties"].get("adm1_name")
    if name:
        divisions.append({
            "model": "org.division",
            "pk": pk,
            "fields": {"name": name}
        })
        pk += 1

# ---------------- DISTRICT ----------------
print("\nProcessing District...")
pk = 1
for f in tqdm(adm2):
    p = f["properties"]
    districts.append({
        "model": "org.district",
        "pk": pk,
        "fields": {
            "name": p.get("adm2_name"),
            "division": p.get("adm1_name")
        }
    })
    pk += 1

# ---------------- UPAZILA ----------------
print("\nProcessing Upazila...")
pk = 1
for f in tqdm(adm3):
    p = f["properties"]
    upazilas.append({
        "model": "upazila",
        "pk": pk,
        "fields": {
            "name": p.get("adm3_name"),
            "district": p.get("adm2_name")
        }
    })
    pk += 1

# ---------------- UNION ----------------
print("\nProcessing Union (ADM4)...")
pk = 1
for f in tqdm(adm4):
    p = f["properties"]
    name = p.get("shapeName")

    if name:
        unions.append({
            "model": "union",
            "pk": pk,
            "fields": {
                "name": name
            }
        })
        pk += 1

# ---------------- SAVE FILES ----------------
print("\nSaving files...")

def save(name, data):
    path = os.path.join(OUTPUT_FOLDER, name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

save("division.json", divisions)
save("district.json", districts)
save("upazila.json", upazilas)
save("union.json", unions)

print(f"\n✅ DONE! Files created inside '{OUTPUT_FOLDER}' folder:")
print("division.json")
print("district.json")
print("upazila.json")
print("union.json")