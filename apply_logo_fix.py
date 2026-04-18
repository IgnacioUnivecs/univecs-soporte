from pathlib import Path

CM = Path("flutter/lib/common.dart")
cm = CM.read_text(encoding="utf-8")

old = "constraints: BoxConstraints(maxWidth: 300, maxHeight: 120),"
new = "constraints: BoxConstraints(maxWidth: 300, maxHeight: 90),"

if old in cm:
    cm = cm.replace(old, new)
    print("OK: logo ajustado a maxHeight 90")
else:
    print("ERROR: constraint no encontrado")

CM.write_text(cm, encoding="utf-8", newline="\n")