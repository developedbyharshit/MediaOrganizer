Here's a GitHub-ready description for your script:

---

# Photo and Video Organizer 🖼️🎥

This script helps you organize your photo and video files into a neatly structured folder hierarchy based on their creation dates. It processes both images (using EXIF metadata) and videos (using file modification dates) and moves them into year/month-based folders, simplifying your media management.

## Features 🚀
- **EXIF Metadata Support**: Extracts the `DateTimeOriginal` from image EXIF data for precise organization.
- **Fallback to File Modification Dates**: For files without EXIF metadata, the script uses the file modification timestamp.
- **Automatic Folder Creation**: Creates folders for each year and month dynamically.
- **Handles Undated Files**: Moves files with no date information to a dedicated "No Date" folder.
- **Conflict Resolution**: Ensures no duplicate files overwrite existing ones.
- **Supports Various Formats**: Works with common image formats (`.jpg`, `.jpeg`, `.png`) and video formats (`.mp4`, `.mov`, `.avi`).

## Supported File Formats 🛠️
- **Images**: `.jpg`, `.jpeg`, `.png`
- **Videos**: `.mp4`, `.mov`, `.avi`

## Usage 💡
1. Clone the repository and install the required dependencies:
   ```bash
   pip install pillow
   ```
2. Run the script:
   ```bash
   python organize_photos_and_videos.py
   ```
3. Provide the source folder (where your files are located) and the destination folder (where you want the organized files to go).

## Example
Organize media files from a folder `C:/Users/Photos` into a destination folder `D:/OrganizedMedia`:
```bash
Enter the path of the folder to organize: C:/Users/Photos
Enter the destination folder path: D:/OrganizedMedia
```

## Improvements in Progress ✨
- Adding support for additional file formats (`.tiff`, `.webp`, `.heic`, etc.).
- Introducing a dry-run mode for previewing changes before organizing files.
- Enhanced logging for error tracking and debugging.

## Contributions 🤝
Contributions are welcome! If you have ideas to improve this script, feel free to submit a pull request or open an issue.

---

Let me know if you'd like to tweak anything!
