# 🏛️ Heritage Treasures: An In-Depth Analysis of UNESCO World Heritage Sites in Tableau

<div align="center">

**A comprehensive Tableau data analytics project exploring 1,121 UNESCO World Heritage Sites**  
**across 167 countries and 5 global regions**

[📊 View Dashboard](#-dashboards) • [🗺️ Visualizations](#-visualizations) • [🌐 Web App](#-web-integration) • [📁 Dataset](#-dataset)

</div>

---

## 📋 Table of Contents

- [🎯 Project Overview](#-project-overview)
- [📊 Key Statistics](#-key-statistics)
- [🛠️ Tech Stack](#️-tech-stack)
- [📁 Project Structure](#-project-structure)
- [🚀 Getting Started](#-getting-started)
- [📂 Dataset](#-dataset)
- [🔧 Data Preparation](#-data-preparation)
- [📈 Visualizations](#-visualizations)
- [📊 Dashboards](#-dashboards)
- [📖 Tableau Story](#-tableau-story)
- [🌐 Web Integration](#-web-integration)
- [🔍 Key Findings](#-key-findings)
- [👨‍💻 Author](#-author)
- [📄 License](#-license)

---

## 🎯 Project Overview

**Heritage Treasures** is a complete end-to-end data analytics project that analyzes UNESCO World Heritage Sites data using Tableau. The project covers the full data analytics lifecycle:

```
📥 Data Collection  →  🧹 Data Preparation  →  📊 Visualization
        →  🗂️ Dashboard  →  📖 Story  →  🌐 Web App
```

This project was developed as part of the **SkillWallet Data Analytics with Tableau** module at **Poornima University, Jaipur**.

### 🎯 Objectives
- Analyze the global distribution of UNESCO World Heritage Sites by region, country, and category
- Identify the top 10 countries by total heritage site area
- Map and analyze all sites currently listed as **"In Danger"** (endangered heritage)
- Forecast future heritage inscription trends using Tableau's built-in forecasting engine
- Present findings through a **professional Flask web application**

---

## 📊 Key Statistics

| Metric | Value |
|--------|-------|
| 🏛️ Total Heritage Sites | **1,121 sites** |
| 🌍 Countries Represented | **167 countries** |
| 🗺️ World Regions | **5 regions** |
| 📅 Year Range | **1972 – 2019** |
| ⚠️ Endangered Sites | **53 sites** |
| 🏛️ Cultural Sites | **869 (77.5%)** |
| 🌿 Natural Sites | **213 (19.0%)** |
| 🔀 Mixed Sites | **39 (3.5%)** |

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Data Source** | Kaggle (CSV) | UNESCO World Heritage Sites 2019 dataset |
| **Data Preparation** | Python 3.x, Pandas, OpenPyXL, RegEx | Data cleaning and transformation |
| **Visualization** | Tableau Desktop 2024 | 8 interactive charts |
| **Dashboard** | Tableau Desktop | 2 combined dashboards |
| **Story** | Tableau Desktop | 10-scene narrative story |
| **Map Tiles** | Mapbox / OpenStreetMap | Geographic visualizations |
| **Forecasting** | Tableau Built-in | Exponential smoothing forecast |
| **Web Framework** | Flask (Python), Jinja2 | 4-page web application |
| **Frontend** | HTML5, CSS3, Google Fonts | Responsive UI design |
| **Publishing** | Tableau Public | Cloud sharing |

---

## 📁 Project Structure

```
Heritage_Treasures_UNESCO/
│
├── 📊 Tableau/
│   └── Heritage_Treasures_Dashboard.twb       # Main Tableau workbook
│
├── 📂 data/
│   ├── whc-sites-2019.csv                     # Raw dataset from Kaggle
│   └── UNESCO_Heritage_Sites_Prepared.xlsx    # Cleaned dataset (18 fields)
│
├── 🐍 scripts/
│   └── data_preparation.py                    # Python cleaning script
│
├── 🌐 flask_app/
│   ├── app.py                                 # Main Flask application
│   └── templates/
│       ├── base.html                          # Base template with navbar
│       ├── index.html                         # Home page
│       ├── about.html                         # About page
│       ├── dashboard.html                     # Dashboard page
│       └── storyboard.html                    # Storyboard page
│
├── 📸 screenshots/
│   ├── dashboard1.png                         # UNESCO Overview Dashboard
│   ├── dashboard2.png                         # Danger Sites Dashboard
│   └── flask_app.png                          # Flask web app
│
├── 📄 docs/
│   ├── Brainstorm_Idea_Prioritization.docx
│   ├── Define_Problem_Statements.docx
│   ├── Empathy_Map_Canvas.docx
│   ├── Customer_Journey_Map.docx
│   ├── Solution_Requirements.docx
│   ├── Data_Flow_Diagram_User_Stories.docx
│   ├── Technology_Stack.docx
│   └── Project_Planning.docx
│
└── 📖 README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed
- Tableau Desktop (or Tableau Public)
- pip package manager

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/aditya-kumar-singh/Heritage_Treasures_UNESCO.git
cd Heritage_Treasures_UNESCO
```

**2. Install Python dependencies**
```bash
pip install pandas openpyxl flask
```

**3. Run data preparation script**
```bash
cd scripts
python data_preparation.py
```
This generates `UNESCO_Heritage_Sites_Prepared.xlsx` in the `data/` folder.

**4. Open Tableau workbook**
- Open `Heritage_Treasures_Dashboard.twb` in Tableau Desktop
- Connect to `data/UNESCO_Heritage_Sites_Prepared.xlsx`
- All 8 charts, 2 dashboards, and 1 story will load automatically

**5. Run the Flask web app**
```bash
cd flask_app
python app.py
```
Open your browser and go to → **http://localhost:1212**

---

## 📂 Dataset

| Attribute | Details |
|-----------|---------|
| **Dataset Name** | UNESCO World Heritage Sites 2019 |
| **Source** | [Kaggle - Ujwal Kandi](https://www.kaggle.com/datasets/ujwalkandi/unesco-world-heritage-sites) |
| **Raw File** | `whc-sites-2019.csv` (22 fields, 1121 rows) |
| **Cleaned File** | `UNESCO_Heritage_Sites_Prepared.xlsx` (18 fields, 1121 rows) |

### 📋 Cleaned Dataset Fields (18 Fields)

| # | Field Name | Type | Description |
|---|-----------|------|-------------|
| 1 | Site Name | Text | Name of the heritage site |
| 2 | Category | Text | Cultural / Natural / Mixed |
| 3 | Category Code | Text | C / N / M |
| 4 | Country | Geographic | Country where site is located |
| 5 | ISO Code | Text | 2-letter country code |
| 6 | Region | Text | UNESCO world region |
| 7 | Year Inscribed | Number | Year site was inscribed |
| 8 | **Decade Inscribed** | Text | **Calculated: 1970s, 1980s, etc.** |
| 9 | Longitude | Geographic | Longitude coordinate |
| 10 | Latitude | Geographic | Latitude coordinate |
| 11 | Area (Hectares) | Number | Site area in hectares |
| 12 | Danger | Number | 0 = Safe, 1 = In Danger |
| 13 | **Danger Status** | Text | **Calculated: 'In Danger' / 'Safe'** |
| 14 | Transboundary | Number | 0/1 spans multiple countries |
| 15 | **Transboundary Label** | Text | **Calculated: 'Transboundary' / 'Single Country'** |
| 16 | Criteria | Text | UNESCO inscription criteria |
| 17 | Description | Text | Short description (HTML cleaned) |
| 18 | Justification | Text | Justification for inscription |

> ⭐ Bold fields are **calculated columns** added during data preparation

---

## 🔧 Data Preparation

The Python script performs the following operations:

```python
import pandas as pd
import re
from openpyxl import Workbook

# Load raw data
df = pd.read_csv('data/whc-sites-2019.csv')

# 1. Remove unnecessary columns
drop_cols = ['rev_bis', 'secondary_dates', 'date_end', 'danger_list',
             'id_no', 'unique_number', 'udnp_code']
df.drop(columns=drop_cols, inplace=True)

# 2. Rename columns to readable names
df.rename(columns={
    'states_name_en': 'Country',
    'region_en': 'Region',
    'name_en': 'Site Name',
    'date_inscribed': 'Year Inscribed',
    'area_hectares': 'Area (Hectares)',
    ...
}, inplace=True)

# 3. Clean HTML tags from text columns
def clean_html(text):
    if pd.isna(text): return ''
    return re.sub(r'<[^>]+>', '', str(text)).strip()

df['Description'] = df['Description'].apply(clean_html)
df['Justification'] = df['Justification'].apply(clean_html)

# 4. Handle null values
df['Area (Hectares)'] = df['Area (Hectares)'].fillna(0)
df['ISO Code'] = df['ISO Code'].fillna('Unknown')

# 5. Add calculated columns
df['Danger Status'] = df['Danger'].apply(lambda x: 'In Danger' if x == 1 else 'Safe')
df['Transboundary Label'] = df['Transboundary'].apply(lambda x: 'Transboundary' if x == 1 else 'Single Country')
df['Decade Inscribed'] = (df['Year Inscribed'] // 10 * 10).astype(str) + 's'

# 6. Export clean file
df.to_excel('data/UNESCO_Heritage_Sites_Prepared.xlsx', index=False)
```

---

## 📈 Visualizations

The project contains **8 interactive Tableau charts**:

| # | Chart Name | Type | Key Insight |
|---|-----------|------|-------------|
| 1 | Countries per Region | 🫧 Packed Bubble | Europe & N. America leads with 73 countries |
| 2 | Top 10 Map | 🗺️ Filled World Map | France tops with 69.4M hectares |
| 3 | Heritage Ended | 🌍 Filtered World Map | 30 countries have endangered sites |
| 4 | Top 10 Danger Sites | 🟥 Treemap | Niger's Air & Ténéré: 7.7M ha — largest endangered |
| 5 | Year Forecasting | 📈 Line + Forecast | Peak 2000; stabilizing to 2028 |
| 6 | Categories by Sites Count | 📊 Bar Chart | Cultural 869 \| Natural 213 \| Mixed 39 |
| 7 | Site Count per Region | 🥧 Pie Chart | Europe & N. America: 531 sites (47%) |
| 8 | Danger Sites Analysis | 📉 Dual Axis | Danger spikes match global conflict years |

---

## 📊 Dashboards

### Dashboard 1 — UNESCO World Heritage Sites Overview
Contains 5 charts: Countries per Region, Site Count per Region, Top 10 Map, Year Forecasting, Categories

> 💡 Click any region bubble to **filter all other charts** interactively

### Dashboard 2 — UNESCO Danger Sites Overview
Contains 3 charts: Heritage Ended Map, Top 10 Danger Sites Treemap, Danger Sites Analysis Dual-Axis

> 💡 Focused exclusively on the **53 UNESCO endangered sites**

---

## 📖 Tableau Story

The project includes a **10-scene Tableau Story** presenting findings as a narrative:

| Scene | Title | Content |
|-------|-------|---------|
| 1 | UNESCO World Heritage Sites Overview | Dashboard 1 |
| 2 | UNESCO Danger Sites Overview | Dashboard 2 |
| 3 | Countries Represented per Region | Bubble Chart |
| 4 | Top 10 Countries by Heritage Area | World Map |
| 5 | Countries with Endangered Sites | Filtered Map |
| 6 | Top 10 Most Endangered Sites | Treemap |
| 7 | Heritage Inscriptions Over Time | Line + Forecast |
| 8 | Heritage Sites by Category | Bar Chart |
| 9 | Site Count Distribution by Region | Pie Chart |
| 10 | Danger Sites & Area Analysis | Dual Axis |

---

## 🌐 Web Integration

The Flask web application provides 4 pages:

```
http://localhost:1212/            →  🏠 Home Page
http://localhost:1212/about       →  ℹ️  About Page
http://localhost:1212/dashboard   →  📊 Dashboard Page
http://localhost:1212/storyboard  →  📖 Storyboard Page
```

### Flask App Structure

```python
# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/storyboard")
def storyboard():
    return render_template("storyboard.html")

if __name__ == "__main__":
    app.run(debug=True, port=1212)
```

---

## 🔍 Key Findings

> **Finding 1 — Regional Dominance**  
> 🌍 Europe & North America holds **531 sites (47.3%)** across 73 countries — nearly half of all UNESCO sites globally

> **Finding 2 — Category Imbalance**  
> 🏛️ Cultural sites dominate at **869 (77.5%)** vs Natural **(213, 19%)** and Mixed **(39, 3.5%)**

> **Finding 3 — Area Leaders**  
> 🗺️ **France (69.4M ha)** leads total heritage area, followed by Australia (45.8M), Kiribati (40.8M), USA (38.9M), Russia (24.6M)

> **Finding 4 — Endangered Crisis**  
> ⚠️ **53 sites** in 30 countries are endangered — Africa contributes 6 of the Top 10 by area. Niger's Air & Ténéré **(7.7M ha)** is the largest endangered site

> **Finding 5 — Inscription Trends**  
> 📈 Inscriptions peaked in **2000 (60 new sites)**; declining since, stabilizing at 15–25/year. Forecast stable through 2028

---

## 🗂️ Project Phases

```
Phase 1  →  📋 Ideation (Problem Statement, Empathy Map, Brainstorming)
Phase 2  →  📝 Requirement Analysis (Journey Map, DFD, Tech Stack)
Phase 3  →  🏗️  Design (Architecture, Solution Design)
Phase 4  →  📅 Planning (3 Sprints, 20 User Stories, 55 Story Points)
Phase 5  →  💻 Development (Data Collection → Preparation → Visualization → Dashboard → Story → Flask)
Phase 6  →  🧪 Testing (Data loaded, Filters used, Visualizations count)
Phase 7  →  📄 Documentation (All SkillWallet documents)
```

---

## 📅 Sprint Planning

| Sprint | Duration | Epic(s) | User Stories | Story Points |
|--------|----------|---------|--------------|-------------|
| Sprint 1 | 01–07 Jun 2025 | Data Collection + Data Preparation | USN-1 to USN-8 | 16 pts |
| Sprint 2 | 08–14 Jun 2025 | Data Visualization (8 Charts) | USN-9 to USN-16 | 19 pts |
| Sprint 3 | 15–21 Jun 2025 | Dashboard + Story + Flask App | USN-17 to USN-20 | 20 pts |
| **Total** | **21 Days** | **6 Epics** | **20 Stories** | **55 pts** |

**Team Velocity = 55 ÷ 3 = 18 Story Points per Sprint**

---

## 👨‍💻 Author

**Aditya Kumar Singh**

- 🎓 BCA (AI & Data Science) — 2nd Year
- 🏫 Poornima University, Jaipur, Rajasthan
- 📧 Platform: SkillWallet — SmartBridge

---

## 📄 License

This project is created for **educational purposes** as part of the SkillWallet Data Analytics with Tableau module.

Dataset: [UNESCO World Heritage Sites 2019](https://www.kaggle.com/datasets/ujwalkandi/unesco-world-heritage-sites) 
Youtube Video link: [https://youtu.be/A2uFsZtX2mQ]
---

<div align="center">

**⭐ If you found this project helpful, please give it a star! ⭐**

Made with ❤️ by Aditya Kumar Singh | SkillWallet — SmartBridge | July 2026

</div>
