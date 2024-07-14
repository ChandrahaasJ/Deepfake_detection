import Server.instaloader as instaloader
import os

def download_instagram_video(url, download_path):
    try:
        # Create an instance of Instaloader
        L = instaloader.Instaloader()
       

        # Extract shortcode from the URL
        shortcode = url.split('/')[-2]

        # Fetch the post metadata using the shortcode
        post = instaloader.Post.from_shortcode(L.context, shortcode)

        # Create the download path if it doesn't exist
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        # Download the video
        L.download_post(post, target=download_path)
        print('Downloaded Successfully.')
    
    except instaloader.exceptions.InstaloaderException as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# URL of the Instagram video you want to download
video_url = 'https://www.instagram.com/p/C9VNUqthPGQ'  # Replace with the actual URL of the video

# Define the download path
download_path = 'D:/Projects/Deepfake_detection/dowload'  # Replace with your desired download path

download_instagram_video(video_url, download_path)