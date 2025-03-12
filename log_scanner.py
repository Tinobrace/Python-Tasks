log_file = "sample.log"  # Name of the log file

def count_errors(file):
    with open(file, "r") as f:
        logs = f.readlines()  # Read all lines of the file

    error_count = sum(1 for line in logs if "ERROR" in line)  # Count lines with "ERROR"
    print(f"Found {error_count} occurrences of 'ERROR' in logs.")

count_errors(log_file)
