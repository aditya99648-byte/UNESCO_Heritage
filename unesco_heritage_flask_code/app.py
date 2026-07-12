from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# UNESCO Heritage Project Data
PROJECT = {
    "title": "UNESCO World Heritage Sites",
    "subtitle": "An In-Depth Analysis in Tableau",
    "tagline": "Preserving Our Shared Heritage for Future Generations",
    "description": """The UNESCO World Heritage Sites project is dedicated to identifying, protecting, and 
    preserving cultural and natural heritage around the world. Established in 1972, the World Heritage 
    Convention aims to promote international collaboration and provide support for the conservation of 
    sites of outstanding universal value.

    This analysis explores the distribution of 1,121 UNESCO World Heritage Sites across 168 countries 
    and 5 regions, examining patterns in cultural, natural, and mixed heritage designations. Through 
    interactive Tableau visualizations, we uncover insights about regional representation, endangered 
    sites, and future trends in heritage preservation.""",
    "stats": {
        "total_sites": 1121,
        "countries": 168,
        "regions": 5,
        "cultural": 869,
        "natural": 213,
        "mixed": 39,
        "endangered": 52
    }
}

# Dashboard items
DASHBOARDS = [
    {
        "id": "unesco-overview",
        "title": "UNESCO World Heritage Sites Overview",
        "image": "unesco_overview.png",
        "category": "Overview",
        "description": "Comprehensive dashboard combining regional distribution, site counts, geographic mapping, forecasting, and category analysis into a unified view.",
        "insights": ["Europe & North America dominate with 531 sites", "Cultural sites represent 77% of all listings", "Site inscriptions peaked around year 2000"]
    },
    {
        "id": "danger-overview",
        "title": "UNESCO Danger Sites Overview",
        "image": "danger_sites_overview.png",
        "category": "Endangered Heritage",
        "description": "Integrated analysis of endangered heritage sites combining geographic distribution, temporal trends, and risk assessment metrics.",
        "insights": ["52 sites currently listed as endangered", "Africa has the highest number of danger sites", "Conflict and development are primary threats"]
    },
    {
        "id": "countries-region",
        "title": "Countries per Region",
        "image": "countries_per_region.png",
        "category": "Regional Analysis",
        "description": "Bubble chart visualization showing the distribution of countries across UNESCO regions, with Europe and North America leading at 73 countries.",
        "insights": ["Europe & North America: 73 countries", "Asia and the Pacific: 38 countries", "Africa: 37 countries", "Latin America & Caribbean: 31", "Arab States: 19"]
    },
    {
        "id": "site-count",
        "title": "Site Count per Region",
        "image": "site_count_per_region.png",
        "category": "Regional Analysis",
        "description": "Pie chart displaying the proportional distribution of UNESCO World Heritage Sites across five global regions.",
        "insights": ["Europe & North America: 531 sites (47%)", "Asia and the Pacific: 266 sites (24%)", "Latin America & Caribbean: 142 sites", "Africa: 96 sites", "Arab States: 86 sites"]
    },
    {
        "id": "top-map",
        "title": "Top 10 Countries by Sites",
        "image": "top_10_map.png",
        "category": "Geographic Analysis",
        "description": "Geographic map highlighting the top 10 countries with the most UNESCO World Heritage Sites, including Russia, Canada, USA, France, and Australia.",
        "insights": ["Russian Federation leads in geographic coverage", "Canada and USA are major contributors", "France has significant cultural heritage density"]
    },
    {
        "id": "heritage-ended",
        "title": "Heritage Sites at Risk",
        "image": "heritage_ended.png",
        "category": "Endangered Heritage",
        "description": "Map visualization identifying countries with heritage sites that have lost UNESCO status or are currently classified as endangered.",
        "insights": ["Sites in Yemen, Syria, and Iraq face severe threats", "United States has sites under review", "Madagascar and Indonesia show emerging risks"]
    },
    {
        "id": "danger-sites",
        "title": "Top 10 Endangered Sites",
        "image": "top_10_danger_sites.png",
        "category": "Endangered Heritage",
        "description": "Treemap visualization ranking the most endangered UNESCO sites by protected area, with Air and Ténéré Natural Reserves in Niger being the largest at 7,736,000 hectares.",
        "insights": ["Air and Ténéré Reserves: 7,736,000 ha", "Selous Game Reserve: 5,120,000 ha", "Most danger sites are located in Africa"]
    },
    {
        "id": "forecasting",
        "title": "Year Forecasting",
        "image": "year_forecasting.png",
        "category": "Trend Analysis",
        "description": "Time series analysis with predictive forecasting showing the count of sites inscribed per year from 1974 to 2028, revealing cyclical patterns and projected trends.",
        "insights": ["Peak inscription years: 1978, 1987, 2000", "Forecast shows declining trend post-2020", "Cyclical patterns every 8-10 years"]
    },
    {
        "id": "categories",
        "title": "Heritage Categories",
        "image": "categories.png",
        "category": "Classification",
        "description": "Bar chart showing the distribution of UNESCO sites by heritage type: Cultural (869), Natural (213), and Mixed (39).",
        "insights": ["Cultural sites: 869 (77.5%)", "Natural sites: 213 (19%)", "Mixed sites: 39 (3.5%)", "Cultural heritage dominates global listings"]
    },
    {
        "id": "danger-analysis",
        "title": "Danger Sites Temporal Analysis",
        "image": "danger_sites_analysis.png",
        "category": "Trend Analysis",
        "description": "Dual-axis analysis combining bar chart of danger site counts and line chart of danger metrics over time from 1976 to 2020.",
        "insights": ["Danger listings peaked in 1980s and 2010s", "Correlation with political instability periods", "Conservation funding gaps evident in data"]
    }
]

# Storyboard chapters
STORYBOARD = [
    {
        "chapter": 1,
        "title": "The Global Heritage Landscape",
        "description": "Discover how UNESCO World Heritage Sites are distributed across our planet. From ancient monuments to pristine natural wonders, explore the geographic and categorical patterns that define our shared heritage.",
        "dashboards": ["unesco-overview", "countries-region", "site-count"]
    },
    {
        "chapter": 2,
        "title": "Mapping Our Treasures",
        "description": "Journey across continents through interactive geographic visualizations. See which nations steward the most sites and understand the spatial dynamics of cultural and natural preservation.",
        "dashboards": ["top-map", "categories"]
    },
    {
        "chapter": 3,
        "title": "Threats to Heritage",
        "description": "Examine the sobering reality of endangered sites. From conflict zones to climate change, understand the forces threatening our irreplaceable heritage and the urgent need for conservation action.",
        "dashboards": ["danger-overview", "heritage-ended", "danger-sites"]
    },
    {
        "chapter": 4,
        "title": "Looking Forward",
        "description": "Analyze historical trends and future projections. Understand how heritage preservation has evolved since 1972 and what the data tells us about the future of global conservation efforts.",
        "dashboards": ["forecasting", "danger-analysis"]
    }
]

@app.route("/")
def index():
    return render_template("index.html", project=PROJECT, dashboards=DASHBOARDS, storyboard=STORYBOARD)

@app.route("/about")
def about():
    return render_template("about.html", project=PROJECT)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", project=PROJECT, dashboards=DASHBOARDS)

@app.route("/dashboard/<dashboard_id>")
def dashboard_detail(dashboard_id):
    dashboard = next((d for d in DASHBOARDS if d["id"] == dashboard_id), None)
    if not dashboard:
        return "Dashboard not found", 404
    # Find related dashboards
    related = [d for d in DASHBOARDS if d["category"] == dashboard["category"] and d["id"] != dashboard_id][:3]
    return render_template("dashboard_detail.html", project=PROJECT, dashboard=dashboard, related=related, dashboards=DASHBOARDS)

@app.route("/storyboard")
def storyboard():
    return render_template("storyboard.html", project=PROJECT, storyboard=STORYBOARD, dashboards=DASHBOARDS)

@app.route("/storyboard/<int:chapter_id>")
def storyboard_chapter(chapter_id):
    chapter = next((s for s in STORYBOARD if s["chapter"] == chapter_id), None)
    if not chapter:
        return "Chapter not found", 404
    chapter_dashboards = [d for d in DASHBOARDS if d["id"] in chapter["dashboards"]]
    prev_chapter = next((s for s in STORYBOARD if s["chapter"] == chapter_id - 1), None)
    next_chapter = next((s for s in STORYBOARD if s["chapter"] == chapter_id + 1), None)
    return render_template("storyboard_chapter.html", project=PROJECT, chapter=chapter, 
                          dashboards=chapter_dashboards, prev_chapter=prev_chapter, next_chapter=next_chapter)

@app.route("/static/images/<path:filename>")
def serve_image(filename):
    return send_from_directory(os.path.join(app.root_path, "static", "images"), filename)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
