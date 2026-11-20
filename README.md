# samuelballu.github.io

My personal site: who I am, my experience, my projects and my CV. It is one
Streamlit page written in Python, served by GitHub Pages and run in the
visitor's browser by [stlite](https://github.com/whitphx/stlite).

## Files

- `streamlit_app.py`: the page.
- `content.py`: the facts: text, numbers, jobs, degrees, projects and links.
  Section headings and button labels sit with the layout in `streamlit_app.py`.
- `.streamlit/config.toml`: colours and typefaces.
- `assets/`: the portrait, the project pictures and the CV.
- `build.py`: writes `index.html`, the file GitHub Pages serves.
- `Projet/`: reports of my earlier projects, linked from the page.

## Run it locally

```bash
python -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/streamlit run streamlit_app.py
```

## Publish a change

Edit the Python files or the pictures, then rebuild `index.html` and push:

```bash
.venv/bin/python build.py
```

`requirements.txt` pins the Streamlit version that stlite runs in the browser
(stlite 1.12.2 runs Streamlit 1.65.0). Change both together.
