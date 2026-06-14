from datetime import datetime, timedelta, timezone
import random

def generate_log_lines(num_lines=10):
    log_lines = []
    logs = [
        {'level': 'INFO', 'service': 'user-service', 'message': 'User logged in'},
        {'level': 'INFO', 'service': 'user-service', 'message': 'User logged out'},
        {'level': 'WARNING', 'service': 'user-service', 'message': 'Wrong credentials'},
        {'level': 'ERROR', 'service': 'user-service', 'message': 'User not found'},
        {'level': 'INFO', 'service': 'order-service', 'message': 'Order placed successfully'},
        {'level': 'WARNING', 'service': 'order-service', 'message': 'Order delayed'},
        {'level': 'ERROR', 'service': 'order-service', 'message': 'Order failed'},
        {'level': 'INFO', 'service': 'payment-service', 'message': 'Payment processed'},
        {'level': 'WARNING', 'service': 'payment-service', 'message': 'Payment pending'},
        {'level': 'ERROR', 'service': 'payment-service', 'message': 'Payment declined'}
    ]
    log_weights = [20, 12.5, 5, 2.5, 20, 7.5, 2.5, 20, 2.5, 7.5]
    timestamp = datetime.now(timezone.utc)
    for i in range(num_lines):
        # log_line = "this is a garbled log line\n"
        
        log = random.choices(population=logs, weights=log_weights, k=1)[0]

        time_diff = timedelta(microseconds=random.randint(1, 99999))
        timestamp = timestamp + time_diff
        
        log_line = f"{timestamp.isoformat()} [{log['level']}] service={log['service']} {log['message']}\n"

        log_lines.append(random.choices(population=[log_line, "this is a garbled log line\n"], weights = [9,1], k=1)[0])
    return log_lines

def main():
    with open("log.txt", "w") as f:
        log_lines = generate_log_lines(100)
        f.writelines(log_lines)

if __name__ == "__main__":
    main()