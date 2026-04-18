#!/usr/bin/env python3
"""Pulido final Fase 4:
   1. Quita fondo gris de TextFormField (ID y password).
   2. Cambia texto informativo de la caja a mensaje claro para el usuario final.
   3. Agranda logo Univecs del panel izquierdo (maxHeight 60 -> 120)."""
from pathlib import Path

# ============================================================================
# 1. Quitar fondo gris de los TextFormField
# ============================================================================
HP = Path("flutter/lib/desktop/pages/desktop_home_page.dart")
hp = HP.read_text(encoding="utf-8")

old_deco_id = """                          decoration: InputDecoration(
                            border: InputBorder.none,
                            isDense: true,
                            contentPadding: EdgeInsets.zero,
                          ),"""

new_deco_id = """                          decoration: InputDecoration(
                            border: InputBorder.none,
                            enabledBorder: InputBorder.none,
                            focusedBorder: InputBorder.none,
                            disabledBorder: InputBorder.none,
                            filled: false,
                            isDense: true,
                            contentPadding: EdgeInsets.zero,
                          ),"""

if old_deco_id in hp:
    hp = hp.replace(old_deco_id, new_deco_id)
    print("OK: fondo gris quitado del ID")
else:
    print("AVISO: bloque decoration ID no encontrado")

old_deco_pwd = """                        decoration: InputDecoration(
                          border: InputBorder.none,
                          isDense: true,
                          contentPadding: EdgeInsets.zero,
                        ),"""

new_deco_pwd = """                        decoration: InputDecoration(
                          border: InputBorder.none,
                          enabledBorder: InputBorder.none,
                          focusedBorder: InputBorder.none,
                          disabledBorder: InputBorder.none,
                          filled: false,
                          isDense: true,
                          contentPadding: EdgeInsets.zero,
                        ),"""

if old_deco_pwd in hp:
    hp = hp.replace(old_deco_pwd, new_deco_pwd)
    print("OK: fondo gris quitado del Password")
else:
    print("AVISO: bloque decoration Password no encontrado")

# ============================================================================
# 2. Cambiar texto informativo
# ============================================================================
old_text = '"Puedes acceder a tu escritorio con esta ID y contrase\u00f1a.",'
new_text = '"Facilita esta ID y contrase\u00f1a al t\u00e9cnico para que pueda conectarse a tu ordenador.",'

if old_text in hp:
    hp = hp.replace(old_text, new_text)
    print("OK: texto informativo actualizado")
else:
    print("AVISO: texto informativo no encontrado")

HP.write_text(hp, encoding="utf-8", newline="\n")

# ============================================================================
# 3. Agrandar logo en common.dart
# ============================================================================
CM = Path("flutter/lib/common.dart")
cm = CM.read_text(encoding="utf-8")

old_logo = "constraints: BoxConstraints(maxWidth: 300, maxHeight: 60),"
new_logo = "constraints: BoxConstraints(maxWidth: 300, maxHeight: 120),"

if old_logo in cm:
    cm = cm.replace(old_logo, new_logo)
    print("OK: logo ampliado (60 -> 120)")
else:
    print("AVISO: constraints del logo no encontrado")

CM.write_text(cm, encoding="utf-8", newline="\n")

print("\nTodo aplicado. Revisa con git diff.")