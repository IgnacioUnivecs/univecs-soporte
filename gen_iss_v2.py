from pathlib import Path

ISS = Path("UnivecsSoporte.iss")

content = """; Inno Setup Script - Univecs Soporte Installer v2
; Forzado 64-bit para instalar en C:\\Program Files (no x86)

#define MyAppName "Univecs Soporte"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "Univecs SL"
#define MyAppURL "https://soporteunivecs.es"
#define MyAppExeName "UnivecsSoporte.exe"
#define MyAppSourceDir "dist\\\\UnivecsSoporte"

[Setup]
AppId={{B7F8E3A2-4C9D-4E8F-A1B3-5C7D9E2F8A3B}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}

; IMPORTANTE: forzar 64-bit
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible

; Directorio de staging temporal (RustDesk copia luego a Program Files)
DefaultDirName={tmp}\\{#MyAppName}-Setup
CreateAppDir=yes
DisableDirPage=yes
DisableProgramGroupPage=yes
UsePreviousAppDir=no

PrivilegesRequired=admin

OutputDir=dist\\Installer
OutputBaseFilename=UnivecsSoporte-Setup-{#MyAppVersion}
SetupIconFile=logos-brand\\univecs_icon.ico

Compression=lzma2/ultra
SolidCompression=yes

WizardStyle=modern
DisableWelcomePage=no
DisableReadyPage=yes

UninstallDisplayIcon={commonpf64}\\{#MyAppName}\\{#MyAppExeName}
UninstallDisplayName={#MyAppName}

VersionInfoVersion={#MyAppVersion}
VersionInfoCompany={#MyAppPublisher}
VersionInfoDescription={#MyAppName} - Instalador
VersionInfoProductName={#MyAppName}
VersionInfoCopyright=Copyright (C) 2026 {#MyAppPublisher}

[Languages]
Name: "spanish"; MessagesFile: "compiler:Languages\\Spanish.isl"

[Files]
; Extraer a temporal (luego RustDesk los copia a Program Files)
Source: "{#MyAppSourceDir}\\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs deleteafterinstall

[Run]
; Ejecutar silent-install de RustDesk
Filename: "{app}\\{#MyAppExeName}"; Parameters: "--silent-install"; StatusMsg: "Instalando servicio de {#MyAppName}..."; Flags: runhidden waituntilterminated

; Ejecutar la app al terminar (desde Program Files donde RustDesk la instalo)
Filename: "{commonpf64}\\{#MyAppName}\\{#MyAppExeName}"; Description: "Ejecutar {#MyAppName}"; Flags: postinstall skipifsilent nowait unchecked

[UninstallRun]
Filename: "{commonpf64}\\{#MyAppName}\\{#MyAppExeName}"; Parameters: "--uninstall"; Flags: runhidden; RunOnceId: "UninstallUnivecs"
"""

ISS.write_text(content, encoding="utf-8")
print(f"OK: UnivecsSoporte.iss regenerado con {len(content)} bytes")
print("Cambios: ArchitecturesAllowed=x64compatible, {commonpf64} en vez de {autopf}")