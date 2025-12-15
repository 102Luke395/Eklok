import yt_dlp as ydl
import tkinter as tk
from tkinter import messagebox
import os

def download_video():
    url = url_entry.get()  # Get URL from input field
    if not url:
        messagebox.showwarning("Input Error", "Please enter a valid YouTube URL.")
        return
    
    try:
        # Settings for yt-dlp to download a single MP4 file (no merging)
        ydl_opts = {
            'format': 'mp4',  # Force downloading MP4 files only
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  # Save in selected folder
            'noplaylist': True,  # Ignore playlists, only download the single video
        }
        
        with ydl.YoutubeDL(ydl_opts) as ydl_instance:
            status_label.config(text="Downloading...", fg="blue")
            ydl_instance.download([url])  # Download the provided URL (single video)
            status_label.config(text="Download Complete!", fg="green")
            messagebox.showinfo("Download Complete", "Your video has been downloaded successfully!")
    
    except Exception as e:
        status_label.config(text="Error occurred!", fg="red")
        messagebox.showerror("Download Error", f"An error occurred: {str(e)}")

# Create GUI window
root = tk.Tk()
root.title("YouTube Downloader")

# Set window size
root.geometry("400x250")

# Create widgets
url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack(pady=10)

status_label = tk.Label(root, text="", font=("Arial", 12))
status_label.pack(pady=10)

# Define the folder to save the video
download_folder = os.path.expanduser("~/Downloads")  # Downloads in the home directory, can be changed

# Start the GUI loop
root.mainloop()
