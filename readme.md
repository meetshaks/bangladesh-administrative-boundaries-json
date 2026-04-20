## Bangladesh Administrative Boundary Data

This repository contains processed administrative boundary data for Bangladesh, organized by Division, District, Upazila, and Union levels.

## Overview

The source boundary data was obtained from authoritative GeoJSON datasets and transformed into compact JSON outputs suitable for downstream use in applications and data analysis.

## Data Sources

1. Division, District, Upazila
   - Source: [Humanitarian Data Exchange (HDX)](https://data.humdata.org/dataset/cod-ab-bgd)
   - Original file: `bgd_admin_boundaries.geojson.zip`
   - Extracted GeoJSON files:
     - `bgd_admin1.geojson` — Division boundaries
     - `bgd_admin2.geojson` — District boundaries
     - `bgd_admin3.geojson` — Upazila boundaries

2. Union
   - Source: [geoBoundaries](https://data.humdata.org/dataset/geoboundaries-admin-boundaries-for-bangladesh)
   - Original file: `geoBoundaries-BGD-ADM4.geojson`

## Processing

Python scripts were used to:

- parse GeoJSON boundary files
- normalize administrative names and identifiers
- generate optimized JSON files for each administrative level

The processed outputs are stored in the following directories:

- `id_base_json/` — structured JSON keyed by administrative identifiers
- `name_base_json/` — structured JSON keyed by administrative names

## Technology Stack

- Python
- GeoJSON
- JSON

## Files Included

- `bgd_admin1.geojson`
- `bgd_admin2.geojson`
- `bgd_admin3.geojson`
- `geoBoundaries-BGD-ADM4_simplified.geojson`
- `id_base_script.py`
- `name_base_script.py`
- `readme.md`
- `id_base_json/`
- `name_base_json/`
