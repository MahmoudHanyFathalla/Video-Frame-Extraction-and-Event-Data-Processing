# Video Frame Extraction and Event Data Processing

This project is designed to extract frames from a video file and process event data from a JSON file to associate specific frames with event data. The extracted frames and processed data are then saved in a structured format for further analysis.

## Project Overview

The project consists of the following main components:

1. **Video Frame Extraction**: Extracts frames from a video file at a specified frame rate.
2. **Event Data Processing**: Processes event data from a JSON file to associate specific frames with event data.
3. **Image Data Extraction**: Extracts image data (dimensions) from the frames.
4. **CSV Output**: Saves the processed data (frame information and event data) into a CSV file.

## Requirements

To run this project, you need the following Python libraries:

- `os`
- `json`
- `PIL` (Pillow)
- `csv`
- `cv2` (OpenCV)

You can install the required libraries using pip:

```bash
pip install pillow opencv-python
```

## Project Structure

The project consists of the following files:

- `code4.py`: The main Python script that performs frame extraction, event data processing, and CSV output.
- `data.json`: A sample JSON file containing event data.

## Functions

### `extract_frames(video_path, output_folder, target_fps)`

- **Description**: Extracts frames from a video file at the specified frame rate and saves them in the output folder.
- **Parameters**:
  - `video_path`: Path to the video file.
  - `output_folder`: Path to the folder where extracted frames will be saved.
  - `target_fps`: Target frames per second (fps) for frame extraction.

### `load_json_data(json_data_path)`

- **Description**: Loads JSON data from a file.
- **Parameters**:
  - `json_data_path`: Path to the JSON file containing event data.
- **Returns**: The loaded JSON data.

### `extract_image_data(image_folder_path, events, target_fps)`

- **Description**: Extracts image data (frame information) based on event data.
- **Parameters**:
  - `image_folder_path`: Path to the folder containing extracted frames.
  - `events`: List of events from the JSON data.
  - `target_fps`: Target frames per second (fps) used for frame extraction.
- **Returns**: A list of dictionaries containing image data (frame name, event coordinates, etc.).

### `get_image_dimensions(image_data_list, image_folder_path)`

- **Description**: Extracts image dimensions (width and height) for each frame in the image data list.
- **Parameters**:
  - `image_data_list`: List of dictionaries containing image data.
  - `image_folder_path`: Path to the folder containing extracted frames.
- **Returns**: The updated image data list with image dimensions.

### `save_image_data_to_csv(image_data_list, csv_output_path)`

- **Description**: Saves the processed image data to a CSV file.
- **Parameters**:
  - `image_data_list`: List of dictionaries containing image data.
  - `csv_output_path`: Path to the output CSV file.

## Usage

1. **Set the Paths**: Modify the paths in the `__main__` block of `code4.py` to point to your video file, output folder, and JSON data file.

2. **Run the Script**: Execute the script to extract frames, process event data, and save the results to a CSV file.

```bash
python code4.py
```

## Example

Given a video file `1001.mp4` and a JSON file `13124.json`, the script will:

1. Extract frames from `1001.mp4` at 25 fps and save them in the `imgs` folder.
2. Process the event data from `13124.json` to associate specific frames with event data.
3. Extract image dimensions for each frame.
4. Save the processed data (frame information and event data) to `output.csv`.

## Output

The output CSV file (`output.csv`) will contain the following columns:

- `Image Name`: The name of the extracted frame.
- `X`: The X-coordinate of the event.
- `Y`: The Y-coordinate of the event.
- `Image X`: The width of the image.
- `Image Y`: The height of the image.

## Sample Output

```csv
Image Name,X,Y,Image X,Image Y
1001_frame_0.jpg,50,49,1920,1080
1001_frame_1.jpg,28,33,1920,1080
...
```

## Notes

- Ensure that the video file and JSON file paths are correctly specified in the script.
- The script assumes that the JSON file contains a list of events under the key `data.match.events`.
- The script handles missing images by skipping them during the dimension extraction process.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the developers of OpenCV and Pillow for providing powerful libraries for image and video processing.
- Special thanks to the KoraState team for providing the sample data.
