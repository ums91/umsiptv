import os

# Define base URL for the GitHub raw content
base_url = "https://raw.githubusercontent.com/ums91/umsiptv/master/streams/"
index_file_path = "streams/index.m3u"

# Get list of all .m3u files in streams directory
m3u_files = [f for f in os.listdir("streams") if f.endswith(".m3u")]

# Write to index.m3u file
with open(index_file_path, "w") as index_file:
    index_file.write("#EXTM3U\n")
    for m3u_file in m3u_files:
        # Write the title for the playlist
        index_file.write(f"#EXTINF:-1, {m3u_file.split('.')[0].capitalize()} Playlist\n")
        # Append the base URL
        index_file.write(f"{base_url}{m3u_file}\n")
        
        # Read the content of the current m3u file and append it
        with open(os.path.join("streams", m3u_file), "r") as f:
            content = f.read()
            index_file.write(content)  # Append the content of the m3u file
            index_file.write("\n")  # Add a newline for separation

print("index.m3u has been created with all .m3u file links and content.")
