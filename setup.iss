[Setup]
AppName=SNATAS
AppVersion=1.0
DefaultDirName={autopf}\SNATAS
DefaultGroupName=SNATAS
UninstallDisplayIcon={app}\main.exe
Compression=lzma2
SolidCompression=yes
WizardStyle=modern

[Files]
Source: "dist/main"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\SNATAS"; Filename: "{app}\main.exe"
Name: "{commondesktop}\SNATAS"; Filename: "{app}\main.exe"
