import os
import argparse # This is to allow us to use the CLI
import yaml # This is a markup language file to define the configurations
import logging

# We can have a function to read the config from params.yaml as

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

# We need to read the parameters from default_config_path which we can do as:

def main(config_path,datasource):
    config = read_params(config_path)
    print(config)


if __name__ == "__main__":
    args = argparse.ArgumentParser() # To enable CLI argument passing
    default_config_path = os.path.join("config","params.yaml")
    args.add_argument("--config",default=default_config_path) # This config will tell us all the configurations and default paths etc.
    args.add_argument("--datasource",default=None) # If we put datasource as None then it will take from config

    # Now let's parse the arguments for the CLI
    parsed_args = args.parse_args()
    #print(parsed_args)
    #print(parsed_args.config, parsed_args.datasource)
    main(config_path=parsed_args.config, datasource=parsed_args.datasource) # we can keep our default datasource here or we can have it from CLI