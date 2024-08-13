def read_config(config_file):
    try:
        # Read the configuration file
        with open(config_file, 'r') as config:
            commands = config.read()
        return commands
        
    except Exception as e:
        print(f"Failed to connect to {config_file}: {e}")
        return None
if __name__ == "__main__":
    # Dictionary mapping each switch to its configuration file and credentials
    switches = {
        'NY switch': {
            'config_file': 'NY switch.txt',  # Replace with the path to your configuration file
            'username': 'admin',             # Replace with the specific username for this switch
            'password': 'password'           # Replace with the specific password for this switch
        },
        'DA switch': {
            'config_file': 'DA switch.txt',  # Replace with the path to your configuration file
            'username': 'admin',             # Replace with the specific username for this switch
            'password': 'password'           # Replace with the specific password for this switch
        },
        'SAN FRAN switch': {
            'config_file': 'SAN FRAN switch.txt',  # Replace with the path to your configuration file
            'username': 'admin',                   # Replace with the specific username for this switch
            'password': 'password'                 # Replace with the specific password for this switch
        },
        'CHICAGO switch': {
            'config_file': 'CHICAGO switch.txt',  # Replace with the path to your configuration file
            'username': 'admin',                  # Replace with the specific username for this switch
            'password': 'password'                # Replace with the specific password for this switch
        }
    }
    # Load the configuration to the switch
    for switch_name, switch_info in switches.items():
        print(f"Connecting to {switch_name}...")
        print(f"Username: {switch_info['username']}")
        print(f"Password: {switch_info['password']}")

        # Read and print the configuration file
        commands = read_config(switch_info['config_file'])
        if commands:
            print(f"\n--- Configuration for {switch_name} ---\n")
            print(commands)
            print("\n--- End of Configuration ---\n")

        input("Press Enter to load the next configuration...")
