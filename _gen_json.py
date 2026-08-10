import os
import json

BASE = "https://jsd.anxy.top/gh/shangskr/owo"
NL = "\r\n"

# folder -> Chinese category name
FOLDERS = [
    ("Arknights", "明日方舟"),
    ("GuduYaoGun", "孤独摇滚"),
    ("KaLaBiQiu", "卡拉彼丘"),
    ("QianLianWanHua", "千恋万花"),
    ("Taffy", "塔菲"),
]


def build_category(cat, folder):
    files = sorted(f for f in os.listdir(folder) if f.endswith(".png"))
    if not files:
        raise SystemExit(f"no png files in {folder}")

    container = '\t\t"container": [{'
    for i, fn in enumerate(files):
        stem = os.path.splitext(fn)[0]
        url = f"{BASE}/{folder}/{fn}"
        if i > 0:
            container += NL + "\t\t\t{"
        container += NL + f'\t\t\t\t"text": "{stem}",'
        container += NL + f'\t\t\t\t"icon": "<img src=\'{url}\'>"'
        container += NL + ("\t\t\t}," if i < len(files) - 1 else "\t\t\t}")
    container += NL + "\t\t]"

    block = f'\t"{cat}": {{{NL}\t\t"type": "image",{NL}{container}{NL}\t}}'
    return block


def main():
    blocks = [build_category(cat, folder) for folder, cat in FOLDERS]
    new_cats = ("," + NL).join(blocks)

    with open("owo.json", "rb") as f:
        raw = f.read()

    content = raw.decode("utf-8")
    if not content.endswith("\r\n"):
        raise SystemExit("file does not end with CRLF")

    # strip the trailing newline to work with the JSON text
    body = content[:-2]  # drop final \r\n
    tail = "\t\t]" + NL + "\t}" + NL + "}"  # last category close + root close
    if not body.endswith(tail):
        raise SystemExit("unexpected tail in owo.json")

    new_body = body[: -len(tail)] + "\t\t]" + NL + "\t}," + NL + new_cats + NL + "}"
    new_content = new_body + NL

    # validate
    json.loads(new_content)
    if "\r" not in new_content or "\n" not in new_content:
        raise SystemExit("line ending issue")

    with open("owo.json", "wb") as f:
        f.write(new_content.encode("utf-8"))

    print("OK — new categories appended")
    for folder, cat in FOLDERS:
        n = len([f for f in os.listdir(folder) if f.endswith(".png")])
        print(f"  {folder} ({cat}): {n} entries")


if __name__ == "__main__":
    main()