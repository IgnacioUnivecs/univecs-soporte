#!/usr/bin/env python3
"""Arregla el bug del ID/Password 'Generando...' usando TextFormField reactivo.
   Tambien baja fontSize de 36 a 28 para que el ID quepa en la caja."""
from pathlib import Path

FILE = Path("flutter/lib/desktop/pages/desktop_home_page.dart")
content = FILE.read_text(encoding="utf-8")

# Bloque antiguo: Text plano (no reactivo)
old_block = """                    GestureDetector(
                      onDoubleTap: () {
                        Clipboard.setData(
                            ClipboardData(text: model.serverId.text));
                        showToast(translate("Copied"));
                      },
                      child: Text(
                        model.serverId.text,
                        style: TextStyle(
                          fontSize: 36,
                          fontWeight: FontWeight.bold,
                          color: Color(0xFF00ADD8),
                        ),
                      ),
                    ),"""

# Bloque nuevo: TextFormField reactivo con el controller del modelo
new_block = """                    SizedBox(
                      height: 44,
                      child: GestureDetector(
                        onDoubleTap: () {
                          Clipboard.setData(
                              ClipboardData(text: model.serverId.text));
                          showToast(translate("Copied"));
                        },
                        child: TextFormField(
                          controller: model.serverId,
                          readOnly: true,
                          decoration: InputDecoration(
                            border: InputBorder.none,
                            isDense: true,
                            contentPadding: EdgeInsets.zero,
                          ),
                          style: TextStyle(
                            fontSize: 28,
                            fontWeight: FontWeight.bold,
                            color: Color(0xFF00ADD8),
                          ),
                        ),
                      ),
                    ),"""

if old_block in content:
    content = content.replace(old_block, new_block)
    print("OK: ID ahora es reactivo con TextFormField + fontSize 28")
else:
    print("ERROR: bloque del ID no encontrado")
    raise SystemExit(1)

# Bloque antiguo del Password: Text plano
old_pwd = """                    SizedBox(height: 4),
                    Text(
                      model.serverPasswd.text,
                      style: TextStyle(
                        fontSize: 20,
                        fontWeight: FontWeight.w600,
                        color: Colors.black87,
                      ),
                    ),"""

# Nuevo: TextFormField reactivo
new_pwd = """                    SizedBox(
                      height: 32,
                      child: TextFormField(
                        controller: model.serverPasswd,
                        readOnly: true,
                        decoration: InputDecoration(
                          border: InputBorder.none,
                          isDense: true,
                          contentPadding: EdgeInsets.zero,
                        ),
                        style: TextStyle(
                          fontSize: 18,
                          fontWeight: FontWeight.w600,
                          color: Colors.black87,
                        ),
                      ),
                    ),"""

if old_pwd in content:
    content = content.replace(old_pwd, new_pwd)
    print("OK: Password ahora es reactivo con TextFormField")
else:
    print("AVISO: bloque del Password no encontrado")

FILE.write_text(content, encoding="utf-8", newline="\n")
print("Guardado.")