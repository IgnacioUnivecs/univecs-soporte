from pathlib import Path

ISS = Path("UnivecsSoporte.iss")

content = """; Inno Setup Script - Univecs Soporte Installer v4 FINAL
; RustDesk instala en C:\\Program Files\\UnivecsSoporte (sin espacio)

#define MyAppName "Univecs Soporte"
#define MyAppRealFolder "UnivecsSoporte"
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

ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible

DefaultDirName={tmp}\\{#MyAppRealFolder}-Setup
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

UninstallDisplayIcon={commonpf64}\\{#MyAppRealFolder}\\{#MyAppExeName}
UninstallDisplayName={#MyAppName}

VersionInfoVersion={#MyAppVersion}
VersionInfoCompany={#MyAppPublisher}
VersionInfoDescription={#MyAppName} - Instalador
VersionInfoProductName={#MyAppName}
VersionInfoCopyright=Copyright (C) 2026 {#MyAppPublisher}

[Languages]
Name: "spanish"; MessagesFile: "compiler:Languages\\Spanish.isl"

[Files]
Source: "{#MyAppSourceDir}\\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs deleteafterinstall

[Run]
; --silent-install copia a C:\\Program Files\\UnivecsSoporte y registra servicio
Filename: "{app}\\{#MyAppExeName}"; Parameters: "--silent-install"; StatusMsg: "Instalando servicio de {#MyAppName}..."; Flags: runhidden waituntilterminated

; Abrir la app al terminar desde la ruta real donde RustDesk la puso
Filename: "{commonpf64}\\{#MyAppRealFolder}\\{#MyAppExeName}"; Description: "Ejecutar {#MyAppName}"; Flags: postinstall skipifsilent nowait

[UninstallRun]
Filename: "{commonpf64}\\{#MyAppRealFolder}\\{#MyAppExeName}"; Parameters: "--uninstall"; Flags: runhidden; RunOnceId: "UninstallUnivecs"
"""

ISS.write_text(content, encoding="utf-8")
print(f"OK: UnivecsSoporte.iss v4 FINAL generado ({len(content)} bytes)")
print("Rutas corregidas a 'UnivecsSoporte' (sin espacio) que es donde RustDesk instala")