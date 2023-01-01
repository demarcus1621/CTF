import json
from rc4 import RC4

def recv_message(rx):
    ciphertext = rx.encrypt('ack')
    return ciphertext

def send_idle(tx):
    ciphertext = tx.encrypt('idle')
    return ciphertext

def send_flag(tx):
    with open('flag', 'r') as flag_file:
        flag = flag_file.read()
        ciphertext = tx.encrypt(flag)

    return ciphertext

def main():
    with open('key', 'r') as key_file:
        key = key_file.read()
 
    # Create encrypted sessions
    tx = RC4(key)
    rx = RC4(key)

    # Start recording messages
    messages = []
    messages.append({
        "sent": send_flag(tx),
        "received": recv_message(rx)
    })

    # Idle service
    for i in range(50):
        messages.append({
            "sent": send_idle(tx),
            "received": recv_message(rx)
        })

    # Write messages to file
    with open('messages', 'w') as message_file:
        json.dump(messages, message_file)

if __name__ == '__main__':
    main()
