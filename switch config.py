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
    # Define the switch credentials 
    username = 'admin'         # Replace with your switch username
    password = 'password'      # Replace with your switch password

    config_files = [
        'NY switch.txt',  # Replace with the path to your configuration file
        'DA switch.txt',  # Replace with the path to your configuration file
        'SAN FRAN switch.txt',  # Replace with the path to your configuration file
        'CHICAGO switch.txt',  # Replace with the path to your configuration file
    ]

    # Load the configuration to the switch
    for config_file in config_files:
        commands = read_config(config_file)
        if commands:
            print(f"\n--- Configuration for {config_file} ---\n")
            print(commands)
            print("\n--- End of Configuration ---\n")
            input("Press Enter to load the next configuration...")
