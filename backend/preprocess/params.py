import os

api_key = os.getenv("API_KEY")

# check https://docs.google.com/spreadsheets/d/15KFT2CPiXi74_9S1lg_uW75AcC2PkPM-mgVacItolO4/edit?gid=0#gid=0
values_keywords = {
  "quality_usability": [
    "quality", "reliability", "accessibility",  "easy",
    "functionality", "intuitive", "usability", "seamless",
    "affordable", "valuable", "flexibility", "smooth", "simple"
  ],
  "innovation_technology": [
    "innovation", "digital", "technology", "automation", "ai", "data",
    "realtime", "cloud", "learn", "smart"
  ],
  "trust_ethics": [
    "trust", "transparency", "accountability", "responsibility",
    "compliance", "security", "protection",  "secure",
    "protected", "sustainable", "safety", "impact"
  ],
  "empowerment_control": [
    "control", "freedom", "choice", "confidence", "insight",
    "choose", "personal", "empowerment", "goal"
  ],
  "user_centricity_support": [
    "support", "service", "experience", "care", "clarity", "enjoy",
    "people", "tailored"
  ],
  "community_belonging": [
    "community", "sharing", "global", "worldwide", "abroad", "social"
  ],
  "growth_ambition": [
    "growth", "ambition", "development", "expansion", "vision",
    "future", "progress", "opportunity", "earn", "free"
  ]
}
