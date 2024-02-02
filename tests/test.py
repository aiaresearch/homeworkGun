import cnocr
import os
from generate import generate_number_image

image_dir = r"E:\homeworkGun\tests\images"

# Initialize the OCR model
ocr = cnocr.CnOcr(rec_model_name='number-densenet_lite_136-fc', det_model_name='en_PP-OCRv3_det')

# Generate images for testing
generate_number_image()

# start recognition
for file in os.listdir(image_dir):
    if file.endswith(".jpg") or file.endswith(".png"):
        for line in ocr.ocr(os.path.join(image_dir, file), det=True):
            print('recognized text: ', line['text'], 'fact: ', os.path.splitext(file)[0])

def delete_files_in_directory(directory):
    # List all files in the directory
    files = os.listdir(directory)
    
    for file_name in files:
        # Construct the full path to the file
        file_path = os.path.join(directory, file_name)
        
        # Check if it's a file and not a directory
    if os.path.isfile(file_path):
        # Delete the file
        os.remove(file_path)
                
    print("All files deleted successfully.")
    
# Call the function to delete files
delete_files_in_directory(image_dir)