"""Samuel Ballu's personal site, one Streamlit page.

Run it with `streamlit run streamlit_app.py`. The same file runs in the
browser on GitHub Pages through stlite (see build.py). The facts are in
content.py and the look is in .streamlit/config.toml.
"""

import datetime as dt
from pathlib import Path

import streamlit as st

import content as c

ASSETS = Path(__file__).parent / "assets"
SECTION_GAP = "xlarge"
NAV = {"Experience": "experience", "Projects": "projects", "Contact": "contact"}

st.set_page_config(page_title=c.PAGE_TITLE, page_icon=":material/flight_takeoff:", layout="wide")


def period(start: str, end: str) -> str:
    """'Sep 2025 to now', 'Feb to Aug 2025' or 'Sep 2023 to Aug 2025'."""
    first = dt.date.fromisoformat(start)
    if not end:
        return f"{first:%b %Y} to now"
    last = dt.date.fromisoformat(end)
    if first.year == last.year:
        return f"{first:%b} to {last:%b %Y}"
    return f"{first:%b %Y} to {last:%b %Y}"


def timeline_rows() -> list[dict]:
    """One bar per degree with dates and per job, oldest first, then the next step."""
    today = dt.date.today()

    def bar(item: dict, kind: str, what: str) -> dict:
        return {
            "timeline": item["timeline"],
            "kind": kind,
            "start": item["start"],
            "end": item["end"] or today.isoformat(),
            "what": what,
            "when": period(item["start"], item["end"]),
        }

    rows = [bar(degree, "Study", degree["degree"]) for degree in c.EDUCATION if "timeline" in degree]
    rows += [bar(job, "Work", job["role"]) for job in c.JOBS]
    rows.sort(key=lambda row: row["start"])
    next_year = (today + dt.timedelta(days=365)).isoformat()
    rows.append({**c.NEXT_STEP, "kind": "Next", "start": today.isoformat(), "end": next_year})
    return rows


def timeline_spec(rows: list[dict]) -> dict:
    """Vega-Lite chart: one row per station, a dashed bar for what comes next."""
    work_color, study_color = st.get_option("theme.chartCategoricalColors")[:2]
    bar = {"type": "bar", "height": 18}
    label = {"labelFontSize": 14, "labelColor": st.get_option("theme.textColor")}
    axis = {"title": None, "domain": False, "ticks": False, "grid": False, **label}
    return {
        "height": {"step": 34},
        "encoding": {
            "y": {
                "field": "timeline",
                "type": "nominal",
                "sort": [row["timeline"] for row in rows],
                "axis": {**axis, "labelPadding": 12, "labelLimit": 200},
            },
            "x": {
                "field": "start",
                "type": "temporal",
                "axis": {**axis, "format": "%Y", "tickCount": "year", "labelPadding": 10},
            },
            "x2": {"field": "end"},
            "tooltip": [
                {"field": "timeline", "title": "Where"},
                {"field": "what", "title": "What"},
                {"field": "when", "title": "When"},
            ],
        },
        "layer": [
            {
                "transform": [{"filter": "datum.kind != 'Next'"}],
                "mark": bar,
                "encoding": {
                    "color": {
                        "field": "kind",
                        "type": "nominal",
                        "scale": {"domain": ["Work", "Study"], "range": [work_color, study_color]},
                        "legend": {"title": None, "orient": "bottom", "symbolType": "square", **label},
                    }
                },
            },
            {
                "transform": [{"filter": "datum.kind == 'Next'"}],
                "mark": {**bar, "fillOpacity": 0, "stroke": work_color, "strokeWidth": 2, "strokeDash": [6, 4]},
            },
        ],
        "config": {"view": {"stroke": None}},
    }


def section(title: str, anchor: str) -> None:
    """The gap before a section and its heading, in capitals."""
    st.space(SECTION_GAP)
    st.header(title.upper(), anchor=anchor)


def label_row(label: str, text: str) -> None:
    """A bold label beside its text, stacked on a phone."""
    left, right = st.columns([2, 7], gap="xsmall")
    left.markdown(f"**{label}**")
    right.markdown(text)


# The pinned bar: the two actions never leave the screen.
with st.bottom:
    with st.container(horizontal=True, horizontal_alignment="right"):
        st.link_button("Email me", f"mailto:{c.EMAIL}", icon=":material/mail:")
        st.link_button("Open my CV", c.CV_URL, type="primary", icon=":material/description:")

with st.container(horizontal=True, horizontal_alignment="right"):
    for label, anchor in NAV.items():
        st.markdown(f"[{label}](#{anchor})", width="content")

# Hero: the name at poster size, the portrait in a teal window.
words, window = st.columns([7, 4], gap="large", vertical_alignment="bottom")
with words:
    st.title(c.NAME.upper(), anchor=False)
    st.markdown(f"**{c.ROLE}** {c.SEEKING}", width=620)
with window:
    st.image(ASSETS / c.PORTRAIT, alt="Portrait of Samuel Ballu", width="stretch")

st.space(SECTION_GAP)

# One figure owns the screen, the three others answer it on the far side.
figure, others = st.columns([6, 5], gap="large", vertical_alignment="bottom")
with figure:
    st.header(c.MAIN_FIGURE["claim"].upper(), anchor=False)
    st.subheader(c.MAIN_FIGURE["figure"].upper(), anchor=False)
    st.markdown(c.MAIN_FIGURE["caption"], width=460)
with others:
    for number, sentence in c.OTHER_FIGURES:
        cell_number, cell_sentence = st.columns([1, 4], vertical_alignment="center", wrap=False)
        cell_number.markdown(f"#### {number}")
        cell_sentence.markdown(sentence)

section("About me", "about")
story, facts = st.columns([6, 5], gap="large")
with story:
    for paragraph in c.ABOUT:
        st.markdown(paragraph)
with facts:
    st.markdown(f"**Languages**  \n{c.LANGUAGES}")
    st.markdown(f"**Outside work**  \n{c.INTERESTS}")

section("Experience", NAV["Experience"])
rows = timeline_rows()
st.vega_lite_chart(
    rows,
    timeline_spec(rows),
    alt="Timeline of studies and jobs from 2020 to today, ending with a V.I.E. as the next step",
)
for job in c.JOBS:
    station, work = st.columns([3, 7], gap="small")
    with station:
        st.markdown(f"#### {job['company'].upper()}")
        st.markdown(f"**{job['role']}**  \n{period(job['start'], job['end'])}  \n{job['place']}")
    work.markdown("\n".join(f"- {point}" for point in job["points"]))

# Each project is one full panel with the same three-part row under it.
section("Projects", NAV["Projects"])
for project in c.PROJECTS:
    st.image(ASSETS / project["cover"], alt=project["cover_alt"], width="stretch", link=project["link"])
    with st.container(horizontal=True, horizontal_alignment="distribute", vertical_alignment="center"):
        with st.container(horizontal=True, vertical_alignment="center", width="content"):
            st.markdown(project["year"], width="content")
            st.markdown(f"#### {project['name'].upper()}", width="content")
        st.markdown(project["fact"], width="content")
    st.markdown(f"{project['what']} [{project['link_label']}]({project['link']}).", width=720)
    st.space("medium")

section("Earlier work", "earlier-work")
st.markdown(c.EARLIER_NOTE)
st.table(
    [
        {
            "Project": f"**[{item['name']}]({c.REPORTS}{item['file']})**  \n{item['what']}",
            "Method": item["method"],
            "Tool": item["tool"],
        }
        for item in c.EARLIER
    ],
    border=False,
    hide_header=False,
    alt="Projects from my degrees, with their question, method and tool",
)

section("Skills", "skills")
for group, items in c.SKILLS:
    label_row(group, items)

section("Education", "education")
for degree in c.EDUCATION:
    label_row(degree["year"], f"**{degree['degree']}**  \n{degree['school']}")

# The close: how to reach me on one half, the CV as an object on the other.
section("Write to me", NAV["Contact"])
reach, resume = st.columns([7, 4], gap="large")
with reach:
    st.markdown(c.CONTACT_PROMPT)
    st.markdown(f"#### [{c.EMAIL}](mailto:{c.EMAIL})")
    st.markdown(f"[LinkedIn]({c.LINKEDIN}) and [GitHub]({c.GITHUB}). Toulouse, France.")
    st.space("medium")
    st.caption(f"This site is a Streamlit app written in Python. [Read the source]({c.SOURCE}).")
with resume:
    st.image(ASSETS / c.CV_PREVIEW, alt="First page of Samuel Ballu’s CV", width="stretch", link=c.CV_URL)
    st.markdown("My CV, on one page. Click it to open the PDF.")
