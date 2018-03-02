import threading
from ..messaging import generate_message

# Default state shared between threads:
shared_state = {
    'params': {
        'cpu_pause_ms': 20,
        'message_bytes': 200,
        'period_sec': 1.0,
    }
}

message = generate_message(shared_state)

def regenerate_data():
    message = generate_message(shared_state)

shared_state_lock = threading.Lock()
