import subprocess
import sys


def run_step(file_name):
    print(f"\nRunning {file_name}...")
    result = subprocess.run([sys.executable, file_name])

    if result.returncode != 0:
        raise RuntimeError(f"{file_name} failed.")


def main():
    run_step("download.py")
    run_step("clean.py")
    run_step("reshape.py")
    run_step("merge_prices.py")

    print("\nStarting Streamlit app...")
    subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])


if __name__ == "__main__":
    main()