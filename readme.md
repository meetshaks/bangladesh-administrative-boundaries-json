# Bangladesh Geospatial Administrative Data

**Version:** 1.0.0  
**Status:** Stable  

---

## 📌 Introduction
This repository hosts a comprehensive collection of administrative boundary data for **Bangladesh**. It provides processed JSON outputs for four distinct administrative levels: **Division, District, Upazila, and Union**. The data is derived from authoritative humanitarian sources and optimized for software development and GIS analysis.

---

## 🏛️ Data Sources
We ensure data integrity by sourcing our raw files from recognized global repositories:

* **Levels 1-3 (Division, District, Upazila):**
    * **Provider:** [Humanitarian Data Exchange (HDX)](https://data.humdata.org/dataset/cod-ab-bgd)
    * **Reference:** COD-AB - Bangladesh
* **Level 4 (Union):**
    * **Provider:** [geoBoundaries](https://data.humdata.org/dataset/geoboundaries-admin-boundaries-for-bangladesh)
    * **Reference:** ADM4 Boundaries

---

## 📦 Data Formats
The repository offers two distinct data structures to cater to different use cases:

1.  **ID-Based (`id_base_json/`):** Structures data using unique administrative identifiers. Ideal for relational database mapping and backend logic.
2.  **Name-Based (`name_base_json/`):** Structures data using standard English names. Ideal for frontend search features and user-facing applications.

---

## 🔨 Processing Methodology
The transformation from raw GeoJSON to optimized JSON is handled via **Python automation**:

* **Parsing:** Systematic reading of GeoJSON coordinate arrays.
* **Normalization:** Standardization of administrative naming conventions (removing special characters, fixing casing).
* **Optimization:** Reduction of file size for improved API latency and browser performance.

---

## 📂 Project Inventory

| Category | Item | Description |
| :--- | :--- | :--- |
| **Source Data** | `bgd_admin1.geojson` | Division Level Geometry |
| | `bgd_admin2.geojson` | District Level Geometry |
| | `bgd_admin3.geojson` | Upazila Level Geometry |
| | `geoBoundaries-BGD-ADM4.geojson` | Union Level Geometry |
| **Scripts** | `id_base_script.py` | Generates ID-indexed JSON |
| | `name_base_script.py` | Generates Name-indexed JSON |
| **Output** | `id_base_json/` | Directory containing ID outputs |
| | `name_base_json/` | Directory containing Name outputs |

---

## 🛠️ Tech Stack
* **Core:** Python 
* **Data Interchange:** GeoJSON, JSON
* **Domain:** Geospatial Analysis (GIS)

---

## 📄 License
Please refer to the original licenses of [HDX](https://data.humdata.org/faqs/licenses) and [geoBoundaries](https://www.geoboundaries.org/index.html#usage) for usage restrictions.
