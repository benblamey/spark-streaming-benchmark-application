import random
import string

MAX_MESSAGE_BYTES = 100 * (1000 ^ 2)  # 100MB
RANDOM_1_MB = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
                      for _ in range(MAX_MESSAGE_BYTES))


def generate_message(shared_state_copy):
    return bytes("C%06d-%s\n" % (shared_state_copy['params']['cpu_pause_ms'],
                                 RANDOM_1_MB[
                                 :(shared_state_copy['params']['message_bytes'] - 9)]),
                 'UTF-8')


def parse_message(line):
    return {'cpu_pause_ms': int(line[1:7])}


if __name__ == '__main__':
    shared_state = {'params': {'cpu_pause_ms': 123, 'message_bytes': 2000}}
    line = generate_message(shared_state)

    if len(line) != 2000:
        print(len(line))
        raise Exception('generated message is wrong length')
    print('generated message is correct length')

    parsed = parse_message(line)
    if parsed['cpu_pause_ms'] != 123:
        raise Exception('CPU pause failed round trip conversion')
    print('CPU pause completed round trip conversion')
