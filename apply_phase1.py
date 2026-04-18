#!/usr/bin/env python3
"""Aplica Fase 1: mueve ID/Password del panel izquierdo al panel derecho con caja destacada."""
from pathlib import Path

FILE = Path("flutter/lib/desktop/pages/desktop_home_page.dart")

# Leer en UTF-8
content = FILE.read_text(encoding="utf-8")

# 1. Quitar buildIDBoard y buildPasswordBoard del panel izquierdo
old_block = """      buildTip(context),
      if (!isOutgoingOnly) buildIDBoard(context),
      if (!isOutgoingOnly) buildPasswordBoard(context),"""

new_block = """      buildTip(context),
      // Moved to right pane in buildRightPane: buildIDBoard, buildPasswordBoard"""

if old_block not in content:
    print("ERROR: No se encontro el bloque de buildIDBoard/buildPasswordBoard.")
    print("Posiblemente el fichero ya fue modificado.")
    raise SystemExit(1)

content = content.replace(old_block, new_block)
print("OK: quitado buildIDBoard/buildPasswordBoard del panel izquierdo")

# 2. Reemplazar buildRightPane con version que incluye buildLocalIdCard
old_right_pane = """  buildRightPane(BuildContext context) {
    return Container(
      color: Theme.of(context).scaffoldBackgroundColor,
      child: ConnectionPage(),
    );
  }"""

new_right_pane = """  buildRightPane(BuildContext context) {
    final isOutgoingOnly = bind.isOutgoingOnly();
    return Container(
      color: Theme.of(context).scaffoldBackgroundColor,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          if (!isOutgoingOnly) buildLocalIdCard(context),
          Expanded(child: ConnectionPage()),
        ],
      ),
    );
  }

  Widget buildLocalIdCard(BuildContext context) {
    final model = gFFI.serverModel;
    return Container(
      margin: const EdgeInsets.fromLTRB(20, 20, 20, 0),
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: Color(0xFFE6F7FC),
        border: Border.all(color: Color(0xFF00ADD8), width: 2),
        borderRadius: BorderRadius.circular(12),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            translate("Your Desktop"),
            style: TextStyle(
              fontSize: 14,
              fontWeight: FontWeight.bold,
              color: Color(0xFF00ADD8),
            ),
          ),
          SizedBox(height: 4),
          Text(
            "Puedes acceder a tu escritorio con esta ID y contrase\u00f1a.",
            style: TextStyle(fontSize: 12, color: Colors.black54),
          ),
          SizedBox(height: 12),
          Row(
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      translate("ID"),
                      style: TextStyle(fontSize: 13, color: Colors.black54),
                    ),
                    GestureDetector(
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
                    ),
                  ],
                ),
              ),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      translate("Password"),
                      style: TextStyle(fontSize: 13, color: Colors.black54),
                    ),
                    SizedBox(height: 4),
                    Text(
                      model.serverPasswd.text,
                      style: TextStyle(
                        fontSize: 20,
                        fontWeight: FontWeight.w600,
                        color: Colors.black87,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }"""

if old_right_pane not in content:
    print("ERROR: No se encontro el bloque buildRightPane original.")
    raise SystemExit(1)

content = content.replace(old_right_pane, new_right_pane)
print("OK: buildRightPane reemplazado con version que incluye buildLocalIdCard")

# Escribir en UTF-8 SIN BOM
FILE.write_text(content, encoding="utf-8", newline="\n")
print(f"OK: {FILE} guardado en UTF-8 sin BOM")