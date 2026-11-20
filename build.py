"""Write index.html, the page GitHub Pages serves.

GitHub Pages cannot run a Python server, so the site runs in the visitor's
browser with stlite (Streamlit compiled to WebAssembly). index.html tells
stlite which files to load. Run this script after changing a Python file,
the theme or a picture, then commit index.html with the rest:

    python build.py
"""

import hashlib
import json
from pathlib import Path
from string import Template

import content as c

ROOT = Path(__file__).parent

# stlite 1.12.2 bundles Streamlit 1.65.0: keep requirements.txt on the same version.
STLITE = "https://cdn.jsdelivr.net/npm/@stlite/browser@1.12.2/build"
ENTRYPOINT = "streamlit_app.py"

PAGE = Template(
    """\
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
    <title>$title</title>
    <meta name="description" content="$description" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="$url" />
    <meta property="og:title" content="$title" />
    <meta property="og:description" content="$description" />
    <link rel="stylesheet" href="$stlite/stlite.css" />
  </head>
  <body>
    <div id="root"></div>
    <script type="module">
      import { mount } from "$stlite/stlite.js";
      mount($options, document.getElementById("root"));
    </script>
  </body>
</html>
"""
)


def versioned(path: Path) -> str:
    """URL of a file with a short hash, so browsers reload it only when it changes."""
    digest = hashlib.sha1(path.read_bytes()).hexdigest()[:8]
    return f"./{path.relative_to(ROOT).as_posix()}?v={digest}"


def mounted_files() -> dict:
    """The files stlite downloads into its in-browser file system: only what the page uses.

    .nojekyll makes GitHub Pages serve the .streamlit folder like any other.
    """
    pictures = [c.PORTRAIT, c.CV_PREVIEW, *(project["cover"] for project in c.PROJECTS)]
    paths = [
        ROOT / ENTRYPOINT,
        ROOT / "content.py",
        ROOT / ".streamlit" / "config.toml",
        *(ROOT / "assets" / name for name in pictures),
    ]
    return {p.relative_to(ROOT).as_posix(): {"url": versioned(p)} for p in paths}


def main() -> None:
    options = {"entrypoint": ENTRYPOINT, "files": mounted_files()}
    page = PAGE.substitute(
        title=c.PAGE_TITLE,
        description=f"{c.ROLE} {c.SEEKING}",
        url=c.SITE_URL,
        stlite=STLITE,
        options=json.dumps(options, indent=2).replace("\n", "\n      "),
    )
    (ROOT / "index.html").write_text(page, encoding="utf-8")
    print(f"index.html written, {len(options['files'])} files mounted")


if __name__ == "__main__":
    main()
