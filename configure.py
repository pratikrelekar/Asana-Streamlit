import os

# Set the path for the .streamlit directory and the config.toml file
streamlit_dir = os.path.join(os.path.expanduser("~"), ".streamlit")
config_path = os.path.join(streamlit_dir, "config.toml")

# Ensure the .streamlit directory exists
if not os.path.exists(streamlit_dir):
    os.makedirs(streamlit_dir)

# Write the theme configuration to config.toml
with open(config_path, "w") as config_file:
    config_file.write("[theme]\n")
    config_file.write("base = \"light\"\n")

print(f"config.toml created at {config_path}")
