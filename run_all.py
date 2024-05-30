import subprocess

## Fisierele normale
subprocess.run(["python3", "stats.py"], capture_output=True, text=True)
subprocess.run(["python3", "histograme.py"], capture_output=True, text=True)

## Fisierele cu cerinta{i}
filepaths = [f'cerinta{i}.py' for i in range(4, 11)]
for filepath in filepaths:
    subprocess.run(["python3", filepath], capture_output=True, text=True)
