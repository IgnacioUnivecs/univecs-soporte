from pathlib import Path

ISS = Path("UnivecsSoporte.iss")

content = """; Inno Setup Script - Univecs Soporte Installer
; Usa el comando --silent-install de RustDesk para registrar servicio automaticamente

#define MyAppName "Univecs Soporte"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "Univecs SL"
#define MyAppURL "https://soporteunivecs.es"
#define MyAppExeName "UnivecsSoporte.exe"
#define MyAppSourceDir "dist\\UnivecsSoporte"

[Setup]
AppId={{B7F8E3A2-4C9D-4E8F-A1B3-5C7D9E2F8A3B}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}

; RustDesk maneja su propia instalacion, usamos un directorio temporal como staging
DefaultDirName={tmp}\\{#MyAppName}-Setup
CreateAppDir=yes
DisableDirPage=yes
DisableProgramGroupPage=yes
UsePreviousAppDir=no

; Admin obligatorio: RustDesk necesita privilegios para registrar servicio Windows
PrivilegesRequired=admin
PrivilegesRequiredOverridesAllowed=dialog

OutputDir=dist\\Installer
OutputBaseFilename=UnivecsSoporte-Setup-{#MyAppVersion}
SetupIconFile=logos-brand\\univecs_icon.ico

Compression=lzma2/ultra
SolidCompression=yes
LZMAUseSeparateProcess=yes

WizardStyle=modern
WizardResizable=no
DisableWelcomePage=no
DisableReadyPage=yes
DisableFinishedPage=no

UninstallDisplayIcon={app}\\{#MyAppExeName}
UninstallDisplayName={#MyAppName}

VersionInfoVersion={#MyAppVersion}
VersionInfoCompany={#MyAppPublisher}
VersionInfoDescription={#MyAppName} - Instalador
VersionInfoProductName={#MyAppName}
VersionInfoCopyright=Copyright (C) 2026 {#MyAppPublisher}

[Languages]
Name: "spanish"; MessagesFile: "compiler:Languages\\Spanish.isl"

[Files]
; Extraer todos los ficheros a una carpeta temporal (RustDesk los copiara a su destino real)
Source: "{#MyAppSourceDir}\\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs deleteafterinstall

[Run]
; Ejecutar el modo instalacion silenciosa de RustDesk - copia ficheros y registra servicio
Filename: "{app}\\{#MyAppExeName}"; Parameters: "--silent-install"; StatusMsg: "Instalando servicio de {#MyAppName}..."; Flags: runascurrentuser waituntilterminated

; Abrir la aplicacion al terminar (opcional)
Filename: "{autopf}\\{#MyAppName}\\{#MyAppExeName}"; Description: "Ejecutar {#MyAppName}"; Flags: postinstall skipifsilent nowait runasoriginaluser

[UninstallRun]
; Al desinstalar, ejecutar el comando de desinstalacion de RustDesk
Filename: "{autopf}\\{#MyAppName}\\{#MyAppExeName}"; Parameters: "--uninstall"; Flags: runascurrentuser; RunOnceId: "UninstallRustDesk"

[Code]
function NeedRestart(): Boolean;
begin
  Result := False;
end;
"""

ISS.write_text(content, encoding="utf-8")
print(f"OK: {ISS} regenerado con {len(content)} bytes para silent-install")