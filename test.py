import os, subprocess

# Function to run a shell command and capture its output
TEST_DIR = "."         # Directory containing the C source code
CODE_FILE = "main.c"   # C source code file
COMPILER_TIMEOUT = 10  # seconds
RUN_TIMPOUT = 10       # seconds


code_path = os.path.join(TEST_DIR, CODE_FILE)
app_path = os.path.join(TEST_DIR, "app")

# Compile the C code
print(f"Compiling {code_path}...")
try:
    ret = subprocess.run(
        ["gcc", code_path, "-o", app_path],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        timeout=COMPILER_TIMEOUT
    )
    print("Compilation successful.")
except Exception as e:
    print(f"Compilation failed: {e}")
    exit(1)   

output = ret.stdout.decode('utf-8')
print(f"Compiler output: {output}") 
error = ret.stderr.decode('utf-8') 
print(f"Compiler error: {error}")  

if ret.returncode != 0:
    print(f"Compilation failed with return code {ret.returncode}")
    exit(1)

# Run the compiled application
print(f"Running {app_path}...")
try:
    ret = subprocess.run(
        [app_path],
        stdout = subprocess.PIPE,
        timeout=RUN_TIMPOUT
    )
except Exception as e:
    print(f"Execution failed: {e}")
    exit(1)

 # Capture and print the output
output = ret.stdout.decode('utf-8')
print(f"Application output: {output}")
if ret.returncode != 0:
    print(f"Application exited with return code {ret.returncode}")
    exit(1)      