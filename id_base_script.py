import json
import os
from tqdm import tqdm

DIV_FILE = "bgd_admin1.geojson"
DIS_FILE = "bgd_admin2.geojson"
UPA_FILE = "bgd_admin3.geojson"
UNI_FILE = "geoBoundaries-BGD-ADM4_simplified.geojson"

OUTPUT_DIR = "id_base"


def load_geojson(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)["features"]


# ---------- Create output folder ----------
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("Loading files...")
div_feat = load_geojson(DIV_FILE)
dis_feat = load_geojson(DIS_FILE)
upa_feat = load_geojson(UPA_FILE)
uni_feat = load_geojson(UNI_FILE)

# ---------------- DIVISION ----------------
print("Processing divisions...")
divisions = []
div_map = {}

for i, f in enumerate(tqdm(div_feat), start=1):
    name = f["properties"]["adm1_name"].strip()
    divisions.append({"id": i, "name": name})
    div_map[name.lower()] = i

# ---------------- DISTRICT ----------------
print("Processing districts...")
districts = []
dis_map = {}

for i, f in enumerate(tqdm(dis_feat), start=1):
    p = f["properties"]
    name = p["adm2_name"].strip()
    div_name = p["adm1_name"].strip().lower()

    div_id = div_map.get(div_name)
    if not div_id:
        continue

    districts.append({
        "id": i,
        "name": name,
        "division_id": div_id
    })
    dis_map[name.lower()] = i

# ---------------- UPAZILA ----------------
print("Processing upazilas...")
upazilas = []
upa_map = {}

for i, f in enumerate(tqdm(upa_feat), start=1):
    p = f["properties"]
    name = p["adm3_name"].strip()
    dis_name = p["adm2_name"].strip().lower()

    dis_id = dis_map.get(dis_name)
    if not dis_id:
        continue

    upazilas.append({
        "id": i,
        "name": name,
        "district_id": dis_id
    })
    upa_map[name.lower()] = i

# ---------------- UNION (SMART MATCH) ----------------
print("Processing unions with smart name matching...")
unions = []
missed = 0

for i, f in enumerate(tqdm(uni_feat), start=1):
    union_name = f["properties"]["shapeName"].strip()
    union_lower = union_name.lower()

    matched_upazila_id = None

    for upa_name, upa_id in upa_map.items():
        if upa_name in union_lower:
            matched_upazila_id = upa_id
            break

    if matched_upazila_id:
        unions.append({
            "id": i,
            "name": union_name,
            "upazila_id": matched_upazila_id
        })
    else:
        missed += 1

print(f"Unmatched unions: {missed}")

# ---------------- SAVE ----------------
def save(filename, data):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


print("Saving files into 'id_base' folder...")
save("division.json", divisions)
save("district.json", districts)
save("upazila.json", upazilas)
save("union.json", unions)

print("Done ✅ All files saved in 'id_base' folder.")