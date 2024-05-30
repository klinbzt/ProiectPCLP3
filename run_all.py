import os
import subprocess

filepaths = [f'./cerinta{i}.py' for i in range(4, 9)]
subprocess.run(["python", str(filepaths[4:8])], capture_output=True, text=True)