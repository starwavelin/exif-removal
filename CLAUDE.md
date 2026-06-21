# Project: exif-removal

A single-file Python CLI tool that strips EXIF metadata from image/video files in a user-specified folder.

## File Structure

```
exif-removal/
├── remove_exif.py   # entire implementation lives here
├── README.md
├── .gitignore
└── CLAUDE.md
```

## How It Works

1. Checks that `exiftool` is installed on the system
2. Accepts a folder path via CLI arg or interactive prompt
3. Scans the **top-level folder only** (no recursion) for supported file types
4. Shows the user a file list and requires `y` confirmation before proceeding
5. Runs `exiftool -all= -overwrite_original` on all matched files in a single subprocess call
6. Reports success or failure

## Key Design Decisions

- **Single file**: All logic is in `remove_exif.py`. Do not split into modules unless the file grows substantially.
- **No Python dependencies**: Uses stdlib only (`sys`, `subprocess`, `pathlib`). Do not add `requirements.txt` or external packages unless absolutely necessary.
- **`-overwrite_original` flag**: This is intentional — it prevents `exiftool` from creating `filename_original` backup files. The operation is destructive by design.
- **No recursion**: Only top-level files in the specified folder are processed. This is a deliberate scope decision, not an oversight.
- **Confirmation required**: User must type `y` before any files are modified. Do not remove this step.

## Supported Extensions

Images: `.jpg`, `.jpeg`, `.png`, `.heic`, `.gif`, `.tiff`, `.tif`, `.webp`
Videos: `.mp4`, `.mov`, `.avi`, `.mkv`

Defined in `SUPPORTED_EXTENSIONS` set at the top of `remove_exif.py`.

## Running the Tool

```bash
# Requires exiftool: brew install exiftool
python3 remove_exif.py /path/to/folder
# or interactively:
python3 remove_exif.py
```

## Testing Changes

1. Create a test folder with image/video files that have EXIF data (e.g., phone photos)
2. Run the tool against that folder
3. Verify EXIF is cleared: `exiftool /path/to/folder/photo.jpg` should show minimal metadata
4. Confirm no `_original` backup files were created in the folder
