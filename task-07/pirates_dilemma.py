import os
import click
import requests
from bs4 import BeautifulSoup

@click.command()
@click.argument('video_file')
@click.option('-l', '--language', default='eng', help='Filter subtitles by language.')
@click.option('-o', '--output', default='./subtitles', help='Specify the output folder for subtitles.')
@click.option('-s', '--file-size', type=int, help='Filter subtitles by movie file size.')
@click.option('-h', '--match-by-hash', is_flag=True, help='Match subtitles by movie hash.')
@click.option('-b', '--batch-download', type=str, help='Enable batch mode and specify a directory.')
def download_subtitles(video_file, language, output, file_size, match_by_hash, batch_download):
    # Handle batch mode
    if batch_download:
        process_batch_directory(batch_download, language, output, file_size, match_by_hash)
        return

    print(f"Searching subtitles for {video_file}...")

    # Get IMDb ID and file size
    imdb_id = "0052077"  # Example IMDb ID for the video file
    file_size = os.path.getsize(video_file) if file_size is None else file_size

    # Construct the search URL
    search_url = f"https://www.opensubtitles.org/en/search/sublanguageid-{language}/imdbid-{imdb_id}/filesize-{file_size}"
    if match_by_hash:
        movie_hash = "6ec637c6887599299e999c431a5d2e71"  # Example hash
        search_url += f"/hash-{movie_hash}"
    
    print(f"Scraping URL: {search_url}")

    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and display subtitles
    subtitles = soup.find_all('a', href=True, class_='bnone')
    if not subtitles:
        print("No subtitles found.")
        return

    print(f"Found {len(subtitles)} subtitles:")
    for i, subtitle in enumerate(subtitles, start=1):
        print(f"{i}: {subtitle.get_text()} - https://www.opensubtitles.org{subtitle['href']}")

    choice = int(input("Enter the number of the subtitle to download: "))
    selected_subtitle = subtitles[choice - 1]

    # Download the selected subtitle
    download_url = f"https://www.opensubtitles.org{selected_subtitle['href']}"
    subtitle_response = requests.get(download_url)
    
    # Ensure output directory exists
    os.makedirs(output, exist_ok=True)
    
    # Save the subtitle file
    subtitle_path = os.path.join(output, f"{selected_subtitle.get_text()}.srt")
    with open(subtitle_path, 'wb') as file:
        file.write(subtitle_response.content)
    
    print(f"Subtitle downloaded to {subtitle_path}")

def process_batch_directory(directory, language, output, file_size, match_by_hash):
    for filename in os.listdir(directory):
        if filename.endswith(".mp4"):
            video_file = os.path.join(directory, filename)
            print(f"Processing {video_file}...")
            download_subtitles(video_file, language, output, file_size, match_by_hash, batch_download=None)

if __name__ == '__main__':
    download_subtitles()
