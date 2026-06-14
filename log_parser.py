from dataclasses import dataclass
import datetime

@dataclass
class LogEntry:
    timestamp: datetime
    level: str
    service: str
    message: str

@dataclass
class LogSummary:
    count_per_level: dict
    top_5_messages: list
    busiest_hour: int

def parse_log_line(log_line):
    log_items = log_line.split(' ', 3)
    if len(log_items)<4:
        raise ValueError('Incorret log format: atleast 4 log-items were expected')
    timestamp = None
    try: 
        timestamp = datetime.datetime.fromisoformat(log_items[0])
    except ValueError as err:
        raise ValueError('Incorrect timestamp format') from err
    level = log_items[1].strip('[]')
    service = None
    service_strs = log_items[2].split("=", 1)
    if len(service_strs)==2:
        service = service_strs[1]
    else:
        raise ValueError('Incorrect service format')
    message = log_items[3].strip('\n')

    return LogEntry(timestamp, level, service, message)

def summarize_logs(log_entries):
    if(len(log_entries)==0):
        raise ValueError('The list of input LogEntry objects is empty')
    count_per_level = {}
    count_per_msg = {}
    count_per_hour = {}

    for log_entry in log_entries:
        level = log_entry.level
        count_per_level[level] = count_per_level.get(level, 0)+1
        msg = log_entry.message
        count_per_msg[msg] = count_per_msg.get(msg, 0)+1
        hour_of_day = log_entry.timestamp.hour
        count_per_hour[hour_of_day] = count_per_hour.get(hour_of_day, 0)+1
    
    top_5_messages = list(dict(sorted(count_per_msg.items(), key=lambda item: (-item[1], item[0]))[:5]).keys())
    sorted_hours_by_business = list(dict(sorted(count_per_hour.items(), key=lambda item: (-item[1], item[0]))).keys())
    return LogSummary(count_per_level, top_5_messages, sorted_hours_by_business[0])

def main():
     with open('log.txt', 'r', encoding='utf-8') as file:
        log_entries = []
        for log_line in file:
            try:
                log_entries.append(parse_log_line(log_line))
            except ValueError:
                print("unparseable log line encountered")
        log_summary = summarize_logs(log_entries)
        print(log_summary)

if __name__ == '__main__':
    main()
 