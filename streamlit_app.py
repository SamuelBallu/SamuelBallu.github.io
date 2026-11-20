"""Samuel Ballu's personal site, a plain Streamlit app.

Run it with `streamlit run streamlit_app.py`. The same file runs in the
browser on GitHub Pages through stlite (see build.py). The facts are in
content.py and the colours in .streamlit/config.toml.
"""

import datetime as dt
from pathlib import Path

import streamlit as st

import content as c

ASSETS = Path(__file__).parent / "assets"

st.set_page_config(page_title=c.PAGE_TITLE, page_icon=":material/person:")


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
    """The next step on top, then one bar per job and per degree with dates, newest first."""
    today = dt.date.today()
    rows = [
        {"where": item["timeline"], "kind": kind, "start": item["start"], "end": item["end"] or today.isoformat()}
        for kind, items in (("Study", c.EDUCATION), ("Work", c.JOBS))
        for item in items
        if "timeline" in item
    ]
    rows.sort(key=lambda row: row["start"], reverse=True)
    next_year = (today + dt.timedelta(days=365)).isoformat()
    return [{"where": c.NEXT_STEP, "kind": "Next", "start": today.isoformat(), "end": next_year}, *rows]


# Sidebar: who I am and how to reach me.
with st.sidebar:
    st.image(ASSETS / c.PORTRAIT, alt="Portrait of Samuel Ballu", width=120)
    st.header(c.NAME, anchor=False)
    st.caption(f"{c.ROLE} Toulouse, France.")
    st.link_button("Open my CV", c.CV_URL, type="primary", icon=":material/description:", width="stretch")
    st.link_button("Email me", f"mailto:{c.EMAIL}", icon=":material/mail:", width="stretch")
    st.link_button("LinkedIn", c.LINKEDIN, icon=":material/open_in_new:", width="stretch")
    st.link_button("GitHub", c.GITHUB, icon=":material/open_in_new:", width="stretch")

st.title(c.NAME)
st.markdown(f"**{c.ROLE}** {c.SEEKING}")

with st.container(horizontal=True):
    for label, value, detail in c.METRICS:
        st.metric(label, value, help=detail, border=True)

about, experience, projects, skills, resume = st.tabs(
    [
        ":material/person: About",
        ":material/work: Experience",
        ":material/folder: Projects",
        ":material/school: Skills and education",
        ":material/description: CV",
    ]
)

with about:
    for paragraph in c.ABOUT:
        st.markdown(paragraph)
    st.subheader("Languages")
    st.markdown(c.LANGUAGES)
    st.subheader("Outside work")
    st.markdown(c.INTERESTS)

with experience:
    st.vega_lite_chart(
        timeline_rows(),
        {
            "mark": "bar",
            "encoding": {
                "y": {"field": "where", "type": "nominal", "sort": None, "title": None},
                "x": {"field": "start", "type": "temporal", "title": None},
                "x2": {"field": "end"},
                "color": {"field": "kind", "type": "nominal", "title": None, "scale": {"domain": ["Work", "Study", "Next"]}},
            },
        },
        alt="Timeline of jobs and studies, newest first, from a V.I.E. as the next step down to 2020",
    )
    for job in c.JOBS:
        with st.container(border=True):
            st.subheader(job["company"], anchor=False)
            st.caption(f"{job['role']} · {period(job['start'], job['end'])} · {job['place']}")
            st.markdown("\n".join(f"- {point}" for point in job["points"]))

with projects:
    for project in c.PROJECTS:
        with st.container(border=True):
            st.image(ASSETS / project["cover"], alt=project["cover_alt"])
            st.subheader(project["name"], anchor=False)
            st.caption(f"{project['year']} · {project['fact']}")
            st.markdown(project["what"])
            st.link_button(project["link_label"], project["link"], icon=":material/open_in_new:")
    st.subheader("Earlier work", anchor=False)
    st.caption(c.EARLIER_NOTE)
    st.table(
        [
            {
                "Project": f"[{item['name']}]({c.REPORTS}{item['file']})",
                "Question": item["what"],
                "Method": item["method"],
                "Tool": item["tool"],
            }
            for item in c.EARLIER
        ],
        alt="Projects from my degrees, with their question, method and tool",
    )

with skills:
    st.subheader("Skills", anchor=False)
    for group, items in c.SKILLS:
        st.markdown(f"**{group}:** {items}")
    st.subheader("Education", anchor=False)
    for degree in c.EDUCATION:
        st.markdown(f"**{degree['degree']}**  \n{degree['school']}, {degree['year']}")

with resume:
    st.link_button("Open my CV (PDF)", c.CV_URL, type="primary", icon=":material/description:")
    st.image(ASSETS / c.CV_PREVIEW, alt="First page of Samuel Ballu’s CV", link=c.CV_URL)

st.caption(f"This site is a Streamlit app written in Python. [Read the source]({c.SOURCE}).")
