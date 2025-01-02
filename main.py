import os
import shutil
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

# Function to extract date from EXIF data
def get_exif_date(file_path):
    try:
        image = Image.open(file_path)
        exif_data = image._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                if tag_name == "DateTimeOriginal":
                    return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
    except Exception as e:
        print(f"Error extracting EXIF date: {e}")
    return None

# Function to extract the file's modification date if EXIF data is not available
def get_file_date(file_path):
    try:
        timestamp = os.path.getmtime(file_path)
        return datetime.fromtimestamp(timestamp)
    except Exception as e:
        print(f"Error getting file date: {e}")
    return None

# Main function to organize files
def organize_photos_and_videos(source_folder, destination_folder):
    no_date_folder = os.path.join(destination_folder, "No Date")
    os.makedirs(no_date_folder, exist_ok=True)

    for root, _, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Skip if it's not a photo or video
            if not file.lower().endswith((".jpg", ".jpeg", ".png", ".mp4", ".mov", ".avi")):
                continue

            # Get the date from EXIF or file metadata
            date = get_exif_date(file_path) if file.lower().endswith((".jpg", ".jpeg", ".png")) else get_file_date(file_path)
            if not date:
                print(f"File with no date: {file}")
                destination_path = os.path.join(no_date_folder, file)
                if os.path.exists(destination_path):
                    print(f"File already exists in 'No Date' folder, deleting source file: {file_path}")
                    os.remove(file_path)
                else:
                    shutil.move(file_path, destination_path)
                continue

            # Create year and month folders
            year_folder = os.path.join(destination_folder, str(date.year))
            month_folder = os.path.join(year_folder, date.strftime("%B"))

            os.makedirs(month_folder, exist_ok=True)

            # Move file to the correct folder
            destination_path = os.path.join(month_folder, file)
            if os.path.exists(destination_path):
                print(f"File already exists, deleting source file: {file_path}")
                os.remove(file_path)
            else:
                shutil.move(file_path, destination_path)

if __name__ == "__main__":
    source_folder = input("Enter the path of the folder to organize: ").strip()
    destination_folder = input("Enter the destination folder path: ").strip()
    if os.path.exists(source_folder) and os.path.exists(destination_folder):
        organize_photos_and_videos(source_folder, destination_folder)
        print("Organization complete.")
    else:
        print("The provided folder paths do not exist.")
