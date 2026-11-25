"""The Best Advice I Ever Got — make.fun entry.

Writes one sentence to $MAKEFUN_OUTPUT_DIR/entry.txt: the best advice
the writer ever received, in one sentence of at most 200 characters.
Stdlib only, no network, deterministic.
"""

import os

LINE = (
    "A nurse told me on the worst night of my life, "
    "'You don't have to be brave \u2014 just be here in the morning.'"
)

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "entry.txt")
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.replace(tmp, path)
    # Self-check: the file must be exactly the line and pass the gate.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt differs from LINE"
    assert 1 <= len(written) <= 200 and written.strip(), "gate failed"
    # The brief asks for one sentence: the line must end in a full stop and
    # carry no earlier sentence terminator outside its quoted advice.
    assert written.endswith(".'"), "line must end as one sentence"
    assert written.count(".") == 1, "line must be a single sentence"


if __name__ == "__main__":
    main()
