import requests
import logging
from api.utils.terabox import TeraboxFile

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_download():
    # Test URL
    url = "https://1024terabox.com/s/1DvuBkkzIYGKoQUghERfM4A"
    
    # Use premium cookie
    cookie = "ndus=YzPHGBZGz8KqS-HqPcCsBHDJZPHzO1N-TewUSukc; browserid=_UxNjM2MzE5MjQ5NTUyNjE4MzM5XzE3MzcyMDI0ODRfMA==; lang=en; TSID=wNu2vA8OeQG1234567890abcdef"
    
    # Initialize TeraboxFile with cookie
    tf = TeraboxFile(cookie=cookie)
    tf.search(url)
    
    # Print results
    logger.info("Search Result: %s", tf.result)
    
    # Get first video file
    video_files = []
    for file in tf.result['list']:
        if file['type'] == 'video':
            video_files.append(file)
        for nested_file in file.get('list', []):
            if nested_file['type'] == 'video':
                video_files.append(nested_file)
    
    if video_files:
        logger.info("\nFound Video Files:")
        for video in video_files:
            logger.info("Name: %s", video['name'])
            logger.info("Size: %s", video['size'])
            logger.info("FS_ID: %s", video['fs_id'])
            
            # Try to get download link directly
            direct_link = tf.getDownloadLink(video['fs_id'])
            logger.info("Direct Link: %s", direct_link)
            
            if direct_link:
                video['link'] = direct_link
            logger.info("Final Link: %s", video.get('link', 'No direct link'))
    else:
        logger.info("No video files found")

if __name__ == "__main__":
    test_download() 