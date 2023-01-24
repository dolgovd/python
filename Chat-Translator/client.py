import socket

# Ask a user about source language
land = input('Please enter  source language: ')

# Create a client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Make a connection with socket
client.connect(('localhost', 1338))

# Send message
while True:
    message = input('Please enter text for translation: ')
    # Drop connection with the server if user provided Q
    if message == 'Q':
        client.close()
        break
    # Send message for translation
    else:
        client.send(f'[{land}]{message}'.encode())