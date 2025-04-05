import socket


def start_server():
    try:
        # Create a socket object
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the server to localhost and a port (e.g., 12345)
        server_socket.bind(("localhost", 12345))
        server_socket.listen(1)  # Listen for incoming connections

        print("Server is listening on port 12345...")

        # Accept incoming client connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        # Send a message to the client
        client_socket.sendall(b"Hello from server")

        # Close the client socket
        client_socket.close()
    except socket.error as e:
        print(f"Socket error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the server socket is closed
        server_socket.close()
        print("Server has shut down.")


# Start the server
start_server()
