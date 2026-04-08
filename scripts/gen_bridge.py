import os
import sys

# Пути к файлам
BRIDGE_SRC = "src"
OUTPUT_HEADER = "../ARM64-core/src/bridge_data.h"

# Если передан аргумент — используем его
if len(sys.argv) > 1:
    OUTPUT_HEADER = sys.argv[1]

def generate_header():
    modules = []
    for f in os.listdir(BRIDGE_SRC):
        if f.endswith(".acode"):
            name = f.replace(".acode", "").upper()
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
