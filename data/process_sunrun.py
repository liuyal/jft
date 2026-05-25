
with open("sunrun_2026_raw.txt", 'r') as f:
    lines = f.readlines()

for line in lines:
    parts = line.strip().split()
    print(parts)