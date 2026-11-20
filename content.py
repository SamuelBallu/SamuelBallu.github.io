"""The facts the site shows.

Edit this file to update the site: the text, the numbers, the jobs, the
degrees, the projects and the links. Tab names and button labels sit with
the layout in streamlit_app.py.
"""

SITE_URL = "https://samuelballu.github.io/"

NAME = "Samuel Ballu"
PAGE_TITLE = f"{NAME}, AI specialist"
PORTRAIT = "portrait.jpg"
CV_PREVIEW = "cv_preview.jpg"
EMAIL = "ballu.samu@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/samuel-ballu-3833a3202"
GITHUB = "https://github.com/SamuelBallu"
SOURCE = "https://github.com/SamuelBallu/SamuelBallu.github.io"
CV_URL = SITE_URL + "assets/Samuel_Ballu_CV.pdf"

ROLE = "AI specialist at Akkodis, on assignment at Airbus in Toulouse."
SEEKING = (
    "I am looking for a V.I.E. in AI project or product management, "
    "pre-sales or data science. Available with three months’ notice."
)

# The key figures at the top of the page: label, value, detail shown on hover.
METRICS = [
    ("Airbus AI projects", "Top 5", "Airbus picked the LLM assistant I started alone as one of its top 5 AI projects to accelerate."),
    ("Team I coordinate", "5", "I run the sprints and stand-ups and write the client reports."),
    ("Managers on my app", "20+", "They use the assembly-line app I built alone, more than 10 of them every day."),
    ("Calls for tender", "4", "Answered with the sales team, with demos to clients."),
]

ABOUT = [
    "I trained as a statistician: a master’s degree in applied mathematics and "
    "statistics on the AI track, and a magistère in economic modeling, both in Rennes.",
    "I joined Airbus as a data science intern. Akkodis then placed me on the Final "
    "Assembly Line ground tests in Toulouse, where I started an LLM assistant on my "
    "own. Airbus picked it as one of its top 5 AI projects to accelerate.",
    "Today I coordinate its team of five and the link with the client: sprints, "
    "client reports, meetings in English with the assembly line in Germany, and "
    "demos during calls for tender. That is the work I want to do abroad.",
]
LANGUAGES = "French (native), English (B2/C1, used daily at work), Spanish (beginner)."
INTERESTS = (
    "Dance (rock and salsa), basketball (10 years at regional level, 4 titles, "
    "team captain), cinema (Villeneuve, Tarantino, Nolan)."
)

# Jobs, most recent first. "start" and "end" give the dates shown and place the
# bar on the timeline; an empty "end" means the job is still running.
JOBS = [
    {
        "company": "Akkodis",
        "role": "AI specialist, consultant at Airbus",
        "place": "Final Assembly Line ground tests, Toulouse",
        "timeline": "Akkodis at Airbus",
        "start": "2025-09-01",
        "end": "",
        "points": [
            "Started an LLM assistant for ground tests alone. Airbus selected it among its top 5 AI projects to accelerate.",
            "Coordinate its team of 5: run sprints and stand-ups, track progress and each member’s needs, write client reports.",
            "Lead client meetings in English with the assembly line in Germany, at least twice a week, and report to Airbus’s internal AI program.",
            "Built the assistant’s interface in Streamlit, then Dash, and contributed to its skills and single sign-on.",
            "Built alone a statistical app tracking aircraft through assembly stations, in production with 20+ managers (10+ daily).",
            "Analyzed click data from an internal Airbus app. The findings led to its redesign.",
            "Pre-sales: answered 4 calls for tender with the sales team, studying the required technologies, and demo the project during these bids, internally and directly to clients.",
        ],
    },
    {
        "company": "Airbus",
        "role": "Data scientist intern",
        "place": "Ground Test department, Toulouse",
        "timeline": "Airbus",
        "start": "2025-02-01",
        "end": "2025-08-31",
        "points": [
            "Classified free-text non-conformity reports with machine learning and deep learning models (82% accuracy), still in use.",
            "Built interactive Dash apps aggregating quality data across several business units.",
            "Met a German colleague for one hour every morning, in English, to work on hydraulic leaks.",
        ],
    },
    {
        "company": "Mecadaq Group",
        "role": "Data analyst intern",
        "place": "Finance and HR, Tarnos",
        "timeline": "Mecadaq",
        "start": "2024-05-01",
        "end": "2024-08-31",
        "points": [
            "Built an automated VBA dashboard on salary data for the CFO and the accounting and HR teams.",
            "Built visual indicators flagging anomalies in the US subsidiary’s data (SQL), working directly with the US team in English.",
        ],
    },
    {
        "company": "Thales",
        "role": "Business intelligence intern",
        "place": "Reliability department, Châtellerault",
        "timeline": "Thales",
        "start": "2022-04-01",
        "end": "2022-07-31",
        "points": [
            "Migrated Knime and VBA workflows to Power BI (DAX) to detect manufacturing defects.",
        ],
    },
]

# Degrees, most recent first. A degree with "timeline", "start" and "end" also
# gets a bar on the timeline (the master's bar covers the magistère too).
EDUCATION = [
    {
        "year": "2025",
        "degree": "MSc in Applied Mathematics and Statistics, Artificial Intelligence track",
        "school": "Université Rennes 2",
        "timeline": "Master, Rennes",
        "start": "2023-09-01",
        "end": "2025-08-31",
    },
    {
        "year": "2025",
        "degree": "Magistère in Economic Modeling and Statistics",
        "school": "Université de Rennes 1, selective dual degree, with honors",
    },
    {
        "year": "2023",
        "degree": "BSc in Statistics",
        "school": "Université Bretagne Sud, ranked 2nd of 56",
        "timeline": "Bachelor, Vannes",
        "start": "2022-09-01",
        "end": "2023-06-30",
    },
    {
        "year": "2022",
        "degree": "DUT in Statistics and Business Intelligence",
        "school": "Université de Pau et des Pays de l’Adour",
        "timeline": "DUT, Pau",
        "start": "2020-09-01",
        "end": "2022-06-30",
    },
]

# The top bar of the timeline: what comes next.
NEXT_STEP = "Next: a V.I.E."

REPORTS = SITE_URL + "Projet/"

PROJECTS = [
    {
        "name": "Momo’s",
        "year": "2026",
        "fact": "FastAPI, React, PostgreSQL",
        "what": (
            "Full-stack app for a golf club: rounds, handicap index, rankings and "
            "membership fees. About 20 players use it every day, in French, English "
            "and Spanish. The repository is private, with a demo on request."
        ),
        "link": "https://momos-nu.vercel.app",
        "link_label": "Open the app",
        "cover": "project_momos.png",
        "cover_alt": "Sign-in screen of the Momo’s golf app",
    },
    {
        "name": "Star Wars NLP",
        "year": "2026",
        "fact": "Python, NLP, statistics",
        "what": (
            "Did Anakin Skywalker’s language actually change? I measure his turn to "
            "the dark side from screenplay dialogue alone, with emotion models, text "
            "classifiers and rotation tests. A rebuild of a master’s project, "
            "including where my first result did not hold up."
        ),
        "link": "https://github.com/SamuelBallu/anakin-nlp",
        "link_label": "Read it on GitHub",
        "cover": "project_anakin.png",
        "cover_alt": "Chart of Anakin’s dark-side score rising across the three prequel films",
    },
    {
        "name": "Craft beer cellar around Rennes",
        "year": "2024",
        "fact": "R, spatial statistics",
        "what": (
            "Where should a craft beer cellar open around Rennes? From the French "
            "business register (SIRENE) and census data by district (IRIS), I mapped "
            "the density of beer shops, modeled it against income, drew travel-time "
            "zones to measure competition and tested spatial autocorrelation. A "
            "master’s project."
        ),
        "link": REPORTS + "Projet_cave_final.html",
        "link_label": "Read the report (in French)",
        "cover": "project_cave.png",
        "cover_alt": "Two maps of Rennes from the report: density of beer shops and the graph of neighbouring districts",
    },
]

EARLIER_NOTE = "Projects from my degrees. Each name opens its report, written in French, some of them in pairs."
EARLIER = [
    {
        "name": "Survival of lung cancer patients",
        "what": "Classic survival models against support vector machines",
        "method": "Survival analysis",
        "tool": "R",
        "file": "Projet_veteran.html",
    },
    {
        "name": "Daily maximum temperature in London",
        "what": "Forty years of temperatures smoothed to compare two periods",
        "method": "Spline smoothing",
        "tool": "R",
        "file": "Projet_signal.html",
    },
    {
        "name": "Weather forecast for London",
        "what": "Trend, seasonality and forecasts of average temperatures",
        "method": "Time series, ARIMA",
        "tool": "R",
        "file": "ProjetMeteo.pdf",
    },
    {
        "name": "Road accidents in Rennes",
        "what": "Ten years of accidents by place, vehicle, hour and day",
        "method": "Data visualization",
        "tool": "Python",
        "file": "Projet_Visualisation_Accidents_Rennes.html",
    },
    {
        "name": "NBA salaries",
        "what": "How far performance explains players’ pay, 1996 to 2017",
        "method": "Econometrics",
        "tool": "R",
        "file": "Projet_NBA.pdf",
    },
    {
        "name": "Decryption",
        "what": "Breaking a substitution cipher with a Metropolis algorithm",
        "method": "Markov chain Monte Carlo",
        "tool": "R",
        "file": "MCMC_Decryptage_sortie.html",
    },
    {
        "name": "Athletics clubs in Brittany",
        "what": "An app that scores club performances for the inter-club ranking",
        "method": "Interactive app",
        "tool": "R Shiny",
        "file": "ProjetAthletisme.pdf",
    },
]

SKILLS = [
    (
        "AI and data",
        "Generative AI, large language models (LLM), retrieval-augmented generation (RAG), "
        "LangChain, Langfuse, machine learning, deep learning, natural language processing "
        "(NLP), statistics.",
    ),
    (
        "Programming and tools",
        "Python, pandas, NumPy, scikit-learn, PyTorch, spaCy, SQL, R, VBA, Dash, Streamlit, "
        "FastAPI, React, PostgreSQL, OpenShift, Git, Power BI, DAX.",
    ),
    (
        "Project and client",
        "AI project management, Agile sprints, client reporting, pre-sales, answers to "
        "calls for tender (RFP).",
    ),
]

CONTACT_PROMPT = "About a V.I.E., an AI project, or a demo of what I have built."
