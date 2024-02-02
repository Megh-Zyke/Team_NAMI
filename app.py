from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
import subprocess
import shutil 
from ImageProcessor import addImages
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded file from the form
        uploaded_file = request.files['image']

        if uploaded_file:
            # Create the directory if it doesn't exist
            save_directory = 'cloth_masking/input'
            os.makedirs(save_directory, exist_ok=True)

            # Save the uploaded file with the fixed name "shirt.jpg"
            filename = os.path.join(save_directory, 'shirt.jpg')
            uploaded_file.save(filename)

            # Run the process.py script with the uploaded image
            process_folder = 'cloth masking'  # Adjust to the actual folder name
            process_command = f"python cloth_masking/process.py --image cloth_masking/input/shirt.jpg"

            # Capture the output of the subprocess
            result = subprocess.run(process_command, shell=True, capture_output=True)

            # Check the exit code to determine success or failure
            if result.returncode == 0:
                # Successfully run
                output_image_path = 'output/alpha/1.png'
                destination_path = 'datasets/test/cloth-mask/shirt.jpg'
                shutil.copy(output_image_path, destination_path)

                addImages()

                test_command = "python test.py --name my_test_run"
                test_result = subprocess.run(test_command, shell=True, capture_output=True)

                generated_images_dir = 'results/my_test_run/'
                generated_images = [os.path.join(generated_images_dir, image) for image in os.listdir(generated_images_dir)]
                
                # Copy generated images to static/result
                destination_folder = 'static/result'
                os.makedirs(destination_folder, exist_ok=True)
                for generated_image in generated_images:
                    shutil.copy(generated_image, destination_folder)
                
                if test_result.returncode == 0:
                    # Successfully run
                    return redirect(url_for('success'))
            else:
                # Failed to run
                return jsonify({'imageSaved': False, 'errorMessage': result.stderr.decode('utf-8')})

    # Render the template with the list of images
    image_folder = 'static/images'
    image_list = os.listdir(image_folder)
    gen_images_dir = 'static/result'
    gen_images = os.listdir(gen_images_dir)
    
    return render_template('index.html', image_list=image_list ,generated_images=gen_images)


@app.route('/success', methods=['GET'])
def success():
    # Render the success template
    image_folder = 'static/images'
    image_list = os.listdir(image_folder)
    gen_images_dir = 'static/result'
    gen_images = os.listdir(gen_images_dir)
    return render_template('index.html',  image_list=image_list ,generated_images=gen_images)

if __name__ == '__main__':
    app.run(debug=True)
