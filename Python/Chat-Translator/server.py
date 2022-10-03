import socket
from googletrans import Translator

# Create an object on the class
translator = Translator()
# Set default language on the server
server_land = 'en'

# Create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Link socket with a port
server.bind(('localhost', 1338))
# Start server
server.listen()
client, addr = server.accept()

# Process obtained messages and provide translated messages back
while True:
    # Read chunks 1,024 bytes
    message = client.recv(1024).decode()
    # Get inforamtion about user's language
    lang = message[1:message.index(']')]
    # Get user's intiial message
    translation = translator.translate(
        message[message.index(']')+1:],
        src=lang, dest=server_land
    )

    # Print translated message
    print(translation.text)
