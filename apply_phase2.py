#!/usr/bin/env python3
"""Fase 2: separa ConnectionPage en modos (connectOnly, historyOnly, full)
   y reorganiza el layout: conectar a la izquierda, ID+historial a la derecha."""
from pathlib import Path

# ============================================================================
# PARTE 1: Modificar connection_page.dart
# ============================================================================
CP = Path("flutter/lib/desktop/pages/connection_page.dart")
cp_content = CP.read_text(encoding="utf-8")

# 1.a - Añadir enum al inicio del fichero (justo después de imports)
enum_def = "\nenum ConnectionPageMode { full, connectOnly, historyOnly }\n\n"

marker_after_imports = "class OnlineStatusWidget extends StatefulWidget {"
if enum_def not in cp_content:
    cp_content = cp_content.replace(marker_after_imports, enum_def + marker_after_imports)
    print("OK: enum ConnectionPageMode añadido")
else:
    print("INFO: enum ya existe, saltando")

# 1.b - Añadir parametro mode al constructor de ConnectionPage
old_ctor = "class ConnectionPage extends StatefulWidget {\n  const ConnectionPage({Key? key}) : super(key: key);"
new_ctor = """class ConnectionPage extends StatefulWidget {
  final ConnectionPageMode mode;
  const ConnectionPage({Key? key, this.mode = ConnectionPageMode.full}) : super(key: key);"""

if old_ctor in cp_content:
    cp_content = cp_content.replace(old_ctor, new_ctor)
    print("OK: constructor de ConnectionPage con parametro mode")
else:
    print("AVISO: constructor original no encontrado (quizás ya modificado)")

# 1.c - Modificar build() para respetar el modo
old_build = """  Widget build(BuildContext context) {
    final isOutgoingOnly = bind.isOutgoingOnly();
    return Column(
      children: [
        Expanded(
            child: Column(
          children: [
            Row(
              children: [
                Flexible(child: _buildRemoteIDTextField(context)),
              ],
            ).marginOnly(top: 22),
            SizedBox(height: 12),
            Divider().paddingOnly(right: 12),
            Expanded(child: PeerTabPage()),
          ],
        ).paddingOnly(left: 12.0)),
        if (!isOutgoingOnly) const Divider(height: 1),
        if (!isOutgoingOnly) OnlineStatusWidget()
      ],
    );
  }"""

new_build = """  Widget build(BuildContext context) {
    final isOutgoingOnly = bind.isOutgoingOnly();
    final mode = widget.mode;
    return Column(
      children: [
        Expanded(
            child: Column(
          children: [
            if (mode != ConnectionPageMode.historyOnly) ...[
              Row(
                children: [
                  Flexible(child: _buildRemoteIDTextField(context)),
                ],
              ).marginOnly(top: 22),
              SizedBox(height: 12),
            ],
            if (mode != ConnectionPageMode.connectOnly) ...[
              Divider().paddingOnly(right: 12),
              Expanded(child: PeerTabPage()),
            ],
          ],
        ).paddingOnly(left: 12.0)),
        if (!isOutgoingOnly && mode != ConnectionPageMode.connectOnly) const Divider(height: 1),
        if (!isOutgoingOnly && mode != ConnectionPageMode.connectOnly) OnlineStatusWidget()
      ],
    );
  }"""

if old_build in cp_content:
    cp_content = cp_content.replace(old_build, new_build)
    print("OK: build() de ConnectionPage con soporte de mode")
else:
    print("AVISO: build() original no encontrado")

CP.write_text(cp_content, encoding="utf-8", newline="\n")

# ============================================================================
# PARTE 2: Modificar desktop_home_page.dart
# ============================================================================
HP = Path("flutter/lib/desktop/pages/desktop_home_page.dart")
hp_content = HP.read_text(encoding="utf-8")

# 2.a - Quitar buildTip del panel izquierdo, añadir ConnectionPage(connectOnly)
old_left = """      buildTip(context),
      // Moved to right pane in buildRightPane: buildIDBoard, buildPasswordBoard"""

new_left = """      // buildTip moved: info now shown in buildLocalIdCard on right pane
      // buildIDBoard, buildPasswordBoard moved to right pane
      SizedBox(
        height: 220,
        child: ConnectionPage(mode: ConnectionPageMode.connectOnly),
      ),"""

if old_left in hp_content:
    hp_content = hp_content.replace(old_left, new_left)
    print("OK: panel izquierdo ahora incluye caja conectar (connectOnly)")
else:
    print("AVISO: bloque panel izquierdo no encontrado")

# 2.b - Cambiar buildRightPane para usar historyOnly
old_right = "Expanded(child: ConnectionPage()),"
new_right = "Expanded(child: ConnectionPage(mode: ConnectionPageMode.historyOnly)),"

if old_right in hp_content:
    hp_content = hp_content.replace(old_right, new_right)
    print("OK: panel derecho ahora muestra solo historial (historyOnly)")
else:
    print("AVISO: ConnectionPage() sin mode no encontrado en right pane")

# 2.c - Ensanchar panel izquierdo de 200px a 340px
old_width = "width: isIncomingOnly ? 280.0 : 200.0,"
new_width = "width: isIncomingOnly ? 280.0 : 340.0,"

if old_width in hp_content:
    hp_content = hp_content.replace(old_width, new_width)
    print("OK: panel izquierdo ancho aumentado de 200 a 340")
else:
    print("AVISO: width del panel izquierdo no encontrado")

HP.write_text(hp_content, encoding="utf-8", newline="\n")

print("\nTodo aplicado. Revisa con: git diff")