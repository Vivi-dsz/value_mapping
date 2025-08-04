import os

api_key = os.getenv("OopenAI_API_KEY")

# check https://docs.google.com/spreadsheets/d/15KFT2CPiXi74_9S1lg_uW75AcC2PkPM-mgVacItolO4/edit?gid=0#gid=0
values_keywords = {"quality": ["product quality", "speed", "accessibility", "reliability", "aesthetics", "helpful",
                        "efficiency", "convenience", "flexibility", "stability", "functional", "affordable", "valuable"],
           "innovation": ["digital", "innovation", "technology", "automation", "disruption",
                          "modernity", "scalability", "data-driven", "cutting-edge", "ai", "inventive"],
           "user_centricity": ["customer orientation", "customer service", "user experience", "satisfaction",
                               "customization", "proactivity", "supportiveness", "personalization", "engagement", "support", "safety", "secure", "protection", "tailored"],
           "empowerment": ["self-determination", "financial independence", "control", "education",
                           "freedom", "choice", "autonomy", "empowerment", "international"
                           "wealth", "independence", "planning", "smart", "bravery"],
           "community": ["inclusion", "diversity", "global access", "local relevance",
                         "community", "cooperation", "collaboration", "social"],
           "ethos": ["fairness", "transparency", "trust", "sustainability", "responsibility", "impact",
                     "integrity", "accountability", "honesty", "parity", "sincerity", "ethics", "credibility"],
           "simplicity": ["simplicity", "simple", "ease", "clarity", "intuitive", "user-friendly", "clean", "smooth"],
           "growth": ["ambition", "growth", "expansion", "goal", "vision", "future", "development"]}
