import platform
import subprocess

def get_architecture():
    arch = platform.machine()
    return arch

def check_powerpc():
    arch = get_architecture()
    if "ppc" in arch.lower() or "power" in arch.lower():
        print(f"✅ Detected PowerPC architecture: {arch}")
    else:
        print(f"❌ Not a PowerPC system. Detected architecture: {arch}")

def run_sample_command():
    """ Runs a simple PowerPC-specific command if applicable """
    if "ppc" in get_architecture().lower():
        try:
            print("Running a PowerPC-specific command...")
            output = subprocess.check_output(["uname", "-m"], text=True)
            print(f"Command output: {output.strip()}")
        except Exception as e:
            print(f"Error running command: {e}")
    else:
        print("Skipping command since this is not a PowerPC system.")

if __name__ == "__main__":
    check_powerpc()
    run_sample_command()
