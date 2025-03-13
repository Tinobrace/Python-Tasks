def filter_logs(file, severity=None, date=None):
    with open(file, "r") as f:
        logs = f.readlines()

    filtered_logs = [line.strip() for line in logs if 
                     (not severity or severity.upper() in line) and 
                     (not date or line.startswith(date))]

    print("\n".join(filtered_logs) if filtered_logs else "\nNo logs found matching your criteria.")

date_filter = input("Enter date (YYYY-MM-DD) or press Enter: ").strip()
severity_filter = input("Enter severity (INFO, WARNING, ERROR) or press Enter: ").strip().upper()

filter_logs("sample.log", severity=severity_filter if severity_filter else None, date=date_filter if date_filter else None)

