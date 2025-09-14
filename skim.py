import re
from pathlib import Path
from shutil import copy


def find_link_file(link: Path, root: Path) -> Path:



def detect_links(file: Path) -> list[Path]:
    # ![[f]]
    pattern_wiki = r"\[\[([^|\]]+)(?:\|[^]]+)?\]\]"
    # ![name](assets/imgs/f.png)
    pattern_md = r"\[.*\]\((.+)\)"
    new_links = []
    if file.suffix != ".md":
        return new_links
    with file.open("r") as f:
        text = f.read()
        new_links.extend(
            [find_link_file(link) for link in re.findall(pattern_wiki, text)]
        )
        new_links.extend([Path(f) for f in re.findall(pattern_md, text)])
    return new_links


def main() -> None:
    links: list[Path] = []
    query: list[Path] = []
    root_note = Path("./MIPT-differential-equations-2025.md")
    query.append(root_note)
    links.append(root_note)
    src_vault = Path("~/my/mipt/mipt_notes")
    dst_vault = Path("~/my/mipt/MIPT-notes-5")
    while query:
        cur_note = query.pop()
        print(cur_note)
        new_links = detect_links(cur_note)
        links.extend(new_links)
        query.extend(new_links)

    for link in links:
        root_dir = Path("DE")
        target = root_dir / link
        (target.parent).mkdir(parents=True, exist_ok=True)
        copy(link, root_dir / link)


if __name__ == "__main__":
    main()
