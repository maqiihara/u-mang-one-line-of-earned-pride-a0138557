import os

LINE = (
    "For nine months she soldered by torchlight after school, and tonight "
    "her father's dead radio crackles, finds the evening news, and she turns "
    "it up so the whole street hears it work."
)

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
