import sys


couples: dict[str, str] = {}
try:
    with open(sys.argv[1], "r") as c:
        for line in c:
            clean_line = line.strip()
            if not clean_line:
                continue
            if clean_line.startswith('#'):
                continue
            if '=' in clean_line:
                key, value = clean_line.split('=')
                key = key.strip()
                value = value.strip()
                couples[key] = value

except Exception as e:
    print(f"Error: {e}")

mandatory_keys: list[str] = [
    "WIDTH",
    "HEIGHT",
    "ENTRY",
    "EXIT",
    "PERFECT",
    "OUTPUT_FILE",
]
for k in mandatory_keys:
    if k in couples:
        continue
    else:
        raise ValueError(f"Missing mandatory parameter: {k}")

try:
    couples["WIDTH"] = int(couples["WIDTH"])
    couples["HEIGHT"] = int(couples["HEIGHT"])

    if couples["PERFECT"].lower() in ("true", "false"):  
    	perfect = (perfect_str == "true")
    else:
    	raise ValueError("PERFECT must be True or False")

    if not output_file:
        raise ValueError("OUTPUT_FILE cannot be empty")

    parts = couples["ENTRY"].split(',')
    if len(parts) != 2:
        raise ValueError("ENTRY must be in format X,Y")
    couples["ENTRY"] = (int(parts[0].strip()), int(parts[1].strip()))

    parts = couples["EXIT"].split(',')
    if len(parts) != 2:
        raise ValueError("EXIT must be in format X,Y")
    couples["EXIT"] = (int(parts[0].strip()), int(parts[1].strip()))

except ValueError as e:
    print(f"Error: {e}")
    sys.exit(1)

print(couples)
