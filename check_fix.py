from pathlib import Path

dll = Path('target/release/librustdesk.dll')
data = dll.read_bytes()

patterns = [
    b'sc create \\"',      # con escape \"
    b'sc create "',        # con comilla directa
    b'sc create {app_name}',  # sin arreglar
]

print(f"DLL: {dll}")
print(f"Tamanio: {len(data)} bytes")
print(f"LastWriteTime: {dll.stat().st_mtime}")
print()

for p in patterns:
    count = data.count(p)
    display = p.decode('ascii', errors='replace')
    if count > 0:
        print(f"  ENCONTRADO ({count}x): {display!r}")
    else:
        print(f"  no encontrado: {display!r}")

# Verdadero check
if b'sc create \\"' in data or b'sc create "' in data:
    print("\nRESULTADO: FIX OK - el parche de comillas esta aplicado")
else:
    print("\nRESULTADO: FIX NO APLICADO - hay que rebuild")