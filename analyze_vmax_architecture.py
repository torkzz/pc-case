import re

il_vmax = open("Vmax.il", "r", encoding="utf-8", errors="ignore").read()

def extract_pinvokes():
    pattern = r'\.method[^\n]+pinvokeimpl[^\n]+'
    matches = re.findall(pattern, il_vmax)
    print(f"Found {len(matches)} P/Invoke declarations in Vmax.il:")
    for m in matches:
        print("  ", m.strip())

def extract_class_references():
    pattern = r'\.class[^\n]+'
    classes = re.findall(pattern, il_vmax)
    print(f"\nFound {len(classes)} classes in Vmax.il:")
    for c in classes[:30]:
        print("  ", c.strip())

extract_pinvokes()
extract_class_references()

# Search for P/Invoke calls to Wrraper_MSDisplay
msdisplay_methods = re.findall(r'Wrraper_MSDisplay[A-Za-z0-9_]+', il_vmax)
print(f"\nFound {len(set(msdisplay_methods))} MSDisplay wrapper method calls in Vmax.il:")
for m in sorted(set(msdisplay_methods)):
    print("  ", m)

