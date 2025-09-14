import re
from pathlib import Path
from shutil import copy


def find_link_file(link: Path, root: Path) -> Path:
    for f in root.rglob(link):
        return f


def detect_links(file: Path, root: Path) -> list[Path]:
    # ![[f]]
    pattern_wiki = r"\[\[([^|\]]+)(?:\|[^]]+)?\]\]"
    # ![name](assets/imgs/f.png)
    pattern_md = r"\[.*\]\((.+)\)"
    patterns = [
        pattern_wiki,
        pattern_md,
    ]
    new_links = []
    if file.suffix != ".md":
        return new_links
    with file.open("r") as f:
        text = f.read()
        for pattern in patterns:
            new_links.extend(
                [find_link_file(link, root) for link in re.findall(pattern, text)]
            )
    return new_links


def main() -> None:
    src_vault = Path("~/my/mipt/mipt_notes")
    dst_vault = Path("~/my/mipt/MIPT-notes-5")
    root_note = src_vault / "courses" / "5семестр-ТФКП-семинары-Пыркова-2025.md"
    links: list[Path] = []
    query: list[Path] = []
    query.append(root_note)
    links.append(root_note)
    while query:
        cur_note = query.pop()
        print(cur_note)
        new_links = detect_links(cur_note)
        links.extend(new_links)
        query.extend(new_links)

    for link in links:
        target = dst_vault / link
        (target.parent).mkdir(parents=True, exist_ok=True)
        copy(link, root_dir / link)


if __name__ == "__main__":
    main()
