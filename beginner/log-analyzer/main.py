from datetime import datetime

# Parse, validate, and store log entries
def parse_logs(filepath):
    total_entries = 0
    valid_entries = 0
    invalid_entries = 0
    parsed_logs = []
    while True:
        try:
            with open(filepath, "r",encoding="utf-8") as logfile:
                for log in logfile:
                    total_entries += 1
                    parts = log.split()
                    try:
                        timestamp = " ".join(parts[:2])
                        log_level = parts[2]
                        message = " ".join(parts[3:])
                        log_datetime = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")

                        if log_level in ("INFO", "WARNING", "ERROR") and message != "":
                            valid_entries += 1
                            parsed_logs.append({
                                "timestamp": timestamp,
                                "log_level": log_level,
                                "message": message,
                                "datetime": log_datetime
                            })
                        else:
                            invalid_entries += 1
                            continue

                    except (IndexError, ValueError):
                        invalid_entries += 1
                        continue
            break

        except FileNotFoundError:
            print("File not found. Please try again.")
            filepath=input("Enter the correct file path: ")

    return total_entries,valid_entries,invalid_entries,parsed_logs

# Count log levels and rank the most common error messages
def analyze_logs(parsed_logs):
    info_count = 0
    warning_count = 0
    error_count = 0
    error_counts = {}
    for log in parsed_logs:
        if log["log_level"] == "INFO":
            info_count += 1

        elif log["log_level"] == "WARNING":
            warning_count += 1

        elif log["log_level"] == "ERROR":
            error_count += 1
            error_counts[log["message"]] = error_counts.get(log["message"],0) + 1

    sorted_errors = sorted(error_counts.items(), key=lambda item: item[1], reverse=True)
    return info_count, warning_count, error_count, sorted_errors


def filter_logs(parsed_logs):
    filtered_logs=[]
    while True:
        target_log_level=input("Enter a log level (INFO, WARNING, ERROR): ").strip().upper()
        if target_log_level not in ("INFO", "WARNING", "ERROR"):
            print("Invalid log level. Please try again.")
            continue
        else:
            for log in parsed_logs:
                if log["log_level"] == target_log_level:
                    filtered_logs.append(log)
            break
    return filtered_logs

def filter_by_time(parsed_logs):
    time_filtered_logs=[]
    while True:
        try:
            start_time = input("Enter start time (YYYY-MM-DD HH:MM:SS): ").strip()
            end_time = input("Enter end time (YYYY-MM-DD HH:MM:SS): ").strip()
            start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
            end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
            if end_time < start_time:
                print("End time must be greater than or equal to start time")
                continue

        except ValueError:
            print("Invalid date/time format. Please use YYYY-MM-DD HH:MM:SS.")
            continue

        for log in parsed_logs:
            if start_time <= log['datetime'] <= end_time:
                time_filtered_logs.append(log)
        break

    return time_filtered_logs

def save_report(total_entries,valid_entries,invalid_entries,info_count,warning_count,error_count,sorted_errors,filtered_logs,filtered_time_logs):
    with open("report.txt","w",encoding="utf-8") as reportfile:
        reportfile.write(f"""======================== LOG ANALYZER REPORT ======================== \n Total entries: {total_entries} | Valid entries: {valid_entries} | Invalid entries: {invalid_entries} \n Log Level ==> INFO:{info_count} | WARNING:{warning_count} | ERROR:{error_count} \n""")
        reportfile.write("Most Common errors : \n ")
        for index, error in enumerate(sorted_errors, start=1):
            reportfile.write(f"{index}. {error[0]}: {error[1]} \n")

        reportfile.write("Logs Filtered by Level:\n")
        for index, log in enumerate(filtered_logs, start=1):
            reportfile.write(f"{index}. {log['timestamp']}| {log['log_level']} | {log['message']} \n")

        reportfile.write("Logs Filtered by Level and Time Range:\n")
        for index, log in enumerate(filtered_time_logs, start=1):
            reportfile.write(f"{index}. {log['timestamp']}| {log['log_level']} | {log['message']} \n")

        print("Report saved successfully to report.txt.")

def display_reports(total_entries,valid_entries,invalid_entries,info_count,warning_count,error_count,sorted_errors,filtered_logs,filtered_time_logs):
    print("======================== LOG ANALYZER ========================")
    print(f"Total entries: {total_entries}")
    print(f"Valid entries: {valid_entries}")
    print(f"Invalid entries: {invalid_entries}")
    print()
    print("Log levels:")
    print(f"INFO:{info_count}")
    print(f"WARNING:{warning_count}")
    print(f"ERROR:{error_count}")
    print()
    print("Most common errors:")
    for index, error in enumerate(sorted_errors, start=1):
        print(f"{index}. {error[0]}: {error[1]}")
    print()
    print("Logs Filtered by Level: ")
    for index,log in enumerate(filtered_logs,start=1):
        print(f"{index}. {log['timestamp']}| {log['log_level']} | {log['message']}")
    print()
    print("Logs Filtered by Level and Time Range: ")
    for index, log in enumerate(filtered_time_logs, start=1):
        print(f"{index}. {log['timestamp']}| {log['log_level']} | {log['message']}")




total_entries,valid_entries,invalid_entries,parsed_logs=parse_logs("server.log")
info_count, warning_count, error_count, sorted_error_logs=analyze_logs(parsed_logs)
filtered_logs=filter_logs(parsed_logs)
filtered_time_logs=filter_by_time(filtered_logs)
display_reports(total_entries,valid_entries,invalid_entries,info_count,warning_count,error_count,sorted_error_logs,filtered_logs,filtered_time_logs)
save_report(total_entries,valid_entries,invalid_entries,info_count,warning_count,error_count,sorted_error_logs,filtered_logs,filtered_time_logs)

















