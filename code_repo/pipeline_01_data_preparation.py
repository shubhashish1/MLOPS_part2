import os
import argparse # This is to allow us to use the CLI
import yaml # This is a markup language file to define the configurations
import logging


if __name__ == "__main__":
    args = argparse.ArgumentParser() # To enable CLI argument passing
    args.add_argument("--config",default="default") # This config will tell us all the configurations and default paths etc.
    args.add_argument("--datasource",default=None) # If we put datasource as None then it will take from config

    # Now let's parse the arguments for the CLI
    parsed_args = args.parse_args()
    #print(parsed_args)
    print(parsed_args.config, parsed_args.datasource)