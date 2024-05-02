from pytube import YouTube
import os

def download_video(url):
    try:
        yt = YouTube(url)

        format_choice = input("Enter 'mp3' to download as audio or 'mp4' to download as video: ").lower()
        if format_choice == 'mp3':
            download_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
            if not os.path.exists(download_dir):
                os.makedirs(download_dir)
            print("Downloading audio...")
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_file = audio_stream.download(download_dir)
            base, ext = os.path.splitext(audio_file)
            os.rename(audio_file, base + '.mp3')
            print("Download complete!")
        elif format_choice == 'mp4':
            print("Available video qualities:")
            streams = yt.streams.filter(progressive=True)
            for i, stream in enumerate(streams):
                print(f"{i+1}. {stream.resolution} - {stream.mime_type}")

            choice = int(input("Enter the number corresponding to the video quality you want to download: "))
            selected_stream = streams[choice - 1]

            download_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
            if not os.path.exists(download_dir):
                os.makedirs(download_dir)

            print(f"Downloading {selected_stream.resolution} video...")
            selected_stream.download(download_dir)
            print("Download complete!")
        else:
            print("Invalid format choice. Please enter 'mp3' or 'mp4'.")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    download_video(url)
