import paramiko
import time

def load_config_to_switch(switch_ip, username, password, config_file):
    # Create an SSH client
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the switch
        ssh_client.connect(hostname=switch_ip, username=username, password=password)

        # Open a shell session
        remote_connection = ssh_client.invoke_shell()

        # Read the configuration file
        with open(config_file, 'r') as config:
            commands = config.readlines()

        # Send each command to the switch
        for command in commands:
            remote_connection.send(command + '\n')
            time.sleep(1)  # Adding delay to allow command processing

        # Optionally, save the running config to startup config
        remote_connection.send('copy running-config startup-config\n')
        remote_connection.send('\n')  # Confirm the command if needed
        time.sleep(2)

        print(f"Configuration loaded successfully to {switch_ip}")

    except Exception as e:
        print(f"Failed to connect to {switch_ip}: {e}")

    finally:
        ssh_client.close()

if __name__ == "__main__":
    # Define the switch credentials 
    # Replace with your switch IP address
    username = 'admin'         # Replace with your switch username
    password = 'password'      # Replace with your switch password

    switches = {
        '192.169.1.1': 'NY switch.txt',  # Replace with the path to your configuration file
        '192.169.1.2': 'DA switch.txt',  # Replace with the path to your configuration file
        '192.169.1.3': 'SAN FRAN switch.txt',  # Replace with the path to your configuration file
        '192.169.1.4': 'CHICAGO switch.txt',  # Replace with the path to your configuration file
    }
    # Load the configuration to the switch
    for switch_ip, config_file in switches.items():
        load_config_to_switch(switch_ip, username, password, config_file)