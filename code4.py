import os
import json
from PIL import Image
import csv
import cv2

def extract_frames(video_path, output_folder, target_fps):
    # Open the video file with the specified fps
    cap = cv2.VideoCapture(video_path)
    cap.set(cv2.CAP_PROP_FPS, target_fps)

    # Get video information
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    frame_number = 0

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through each frame
    while True:
        # Read the next frame
        ret, frame = cap.read()

        # Break the loop if we have reached the end of the video
        if not ret:
            break

        # Save the frame as an image
        frame_name = f"{video_name}_frame_{frame_number}.jpg"
        frame_path = os.path.join(output_folder, frame_name)
        cv2.imwrite(frame_path, frame)

        frame_number += 1

    # Release the video capture object
    cap.release()

def load_json_data(json_data_path):
    # Load JSON data
    with open(json_data_path, "r") as json_file:
        data = json.load(json_file)
    return data

def extract_image_data(image_folder_path, events,target_fps):
    # Create a list to store image data
    image_data_list = []

    # Iterate through events and assign images
    for event in events:
        if event["_type"] == "event" and "x" in event and "y" in event and "sec" in event and "msec" in event:
            sec = event["sec"]
            msec = event["msec"]

            # Calculate timestamp and determine image filename
            timestamp = int((sec + msec / 1000) * target_fps)
            image_filename = f"1001_frame_{timestamp}.jpg"
            image_path = os.path.join(image_folder_path, image_filename)

            # Check if the image file exists
            if os.path.exists(image_path):
                # Append data to the list
                image_data_list.append({
                    "Image Name": image_filename,
                    "X": event["x"],
                    "Y": event["y"],
                    "Image X": None,  # Placeholder for image width (to be filled later)
                    "Image Y": None   # Placeholder for image height (to be filled later)
                })

    return image_data_list

def get_image_dimensions(image_data_list, image_folder_path):
    # Now, iterate through the list and get image dimensions
    for image_data in image_data_list:
        image_path = os.path.join(image_folder_path, image_data["Image Name"])
        
        try:
            with Image.open(image_path) as img:
                img_width, img_height = img.size
                image_data["Image X"] = img_width
                image_data["Image Y"] = img_height
        except FileNotFoundError:
            pass  # Handle missing images

    return image_data_list

def save_image_data_to_csv(image_data_list, csv_output_path):
    # Save image data to CSV
    fieldnames = ["Image Name", "X", "Y", "Image X", "Image Y"]

    with open(csv_output_path, mode="w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(image_data_list)

if __name__ == "__main__":
    # Specify the path to the video file
    video_path = "C:\\Users\\hp\\Desktop\\KoraState\\task2\\1001.mp4"

    # Specify the output folder for frames
    output_folder = "C:\\Users\\hp\\Desktop\\KoraState\\task2\\imgs"

    # Set the target frames per second (fps)
    target_fps = 25

    # Extract frames and save them in the output folder
    extract_frames(video_path, output_folder, target_fps)

    # Path to the folder containing images
    image_folder_path = "C:\\Users\\hp\\Desktop\\KoraState\\task2\\imgs"  # or output_folder

    # Path to the JSON data
    json_data_path = "C:\\Users\\hp\\Desktop\\KoraState\\task2\\13124.json"

    # Load JSON data
    data = load_json_data(json_data_path)

    # Extract events from JSON data
    try:
        events = data["data"]["match"]["events"]
    except KeyError:
        print("The 'events' key was not found in the JSON data.")
        events = []

    # Extract image data
    image_data_list = extract_image_data(image_folder_path, events, target_fps)

    # Get image dimensions
    image_data_list = get_image_dimensions(image_data_list, image_folder_path)

    # Save image data to CSV
    csv_output_path = "C:\\Users\\hp\\Desktop\\KoraState\\task2\\output.csv"
    save_image_data_to_csv(image_data_list, csv_output_path)
