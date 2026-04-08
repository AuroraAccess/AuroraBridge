import os
import sys

# Пути к файлам (относительно расположения скрипта)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BRIDGE_SRC = os.path.normpath(os.path.join(SCRIPT_DIR, "../src"))
OUTPUT_HEADER = "src/bridge_data.h"

# Если передан аргумент — используем его
if len(sys.argv) > 1:
    OUTPUT_HEADER = sys.argv[1]

def generate_header():
    modules = []
    print(f"Scanning for Bridge modules in: {BRIDGE_SRC}")
    if not os.path.exists(BRIDGE_SRC):
        print(f"ERROR: Bridge source directory not found!")
        return

    for f in os.listdir(BRIDGE_SRC):
        if f.endswith(".acode"):
            name = f.replace(".acode", "").upper()
            print(f"Found Bridge module: {f} -> AURORA_{name}_SOURCE")
            with open(os.path.join(BRIDGE_SRC, f), "r") as src:
                content = src.read().replace('"', '\\"').replace('\n', '\\n')
                modules.append(f'#define AURORA_{name}_SOURCE "{content}"')
    
    with open(OUTPUT_HEADER, "w") as out:
        out.write("/* AUTO-GENERATED BRIDGE DATA */\n")
        out.write("#ifndef BRIDGE_DATA_H\n")
        out.write("#define BRIDGE_DATA_H\n\n")
        out.write("\n".join(modules))
        out.write("\n\n#endif\n")
    
    print(f"Bridge Header generated: {OUTPUT_HEADER}")

if __name__ == "__main__":
    generate_header()
