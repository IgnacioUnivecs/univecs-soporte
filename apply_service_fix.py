#!/usr/bin/env python3
"""Arregla el bug de espacios en sc create/delete/stop/start/query
   anadiendo comillas dobles al nombre del servicio."""
from pathlib import Path

FILE = Path("src/platform/windows.rs")
content = FILE.read_text(encoding="utf-8")

# Reemplazar todas las variantes de 'sc COMANDO {app_name}' por 'sc COMANDO "{app_name}"'
replacements = [
    ("sc stop {app_name}", 'sc stop \\"{app_name}\\"'),
    ("sc delete {app_name}", 'sc delete \\"{app_name}\\"'),
    ("sc create {app_name} binpath", 'sc create \\"{app_name}\\" binpath'),
    ("sc start {app_name}", 'sc start \\"{app_name}\\"'),
    ("sc query {app_name}", 'sc query \\"{app_name}\\"'),
]

changes = 0
for old, new in replacements:
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        changes += count
        print(f"OK: {count} reemplazos de '{old}'")

# Tambien hay que poner comillas en DisplayName
old_display = 'DisplayName= \\"{app_name} Service\\"'
# Ya esta con comillas, no hace falta

if changes == 0:
    print("ERROR: no se hizo ningun reemplazo")
    raise SystemExit(1)

FILE.write_text(content, encoding="utf-8")
print(f"\nTotal cambios: {changes}")
print("Guardado.")