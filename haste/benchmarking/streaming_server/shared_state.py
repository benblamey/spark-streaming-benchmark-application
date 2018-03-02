import threading

# Default state shared between threads:
shared_state = {
    'params': {
        'cpu_pause_ms': 20,
        'message_bytes': 200,
        'period_sec': 1.0,
    }
}
shared_state_lock = threading.Lock()
