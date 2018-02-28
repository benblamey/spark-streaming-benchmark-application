from .streaming_server import start_streaming_server


# State shared between threads
shared_state = {
    'params': {
        'cpu_pause_ms': 20,
        'message_bytes': 200,
        'message_count_per_second': 2,
    }
}


start_streaming_server(shared_state)
