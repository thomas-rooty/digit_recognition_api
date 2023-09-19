from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from PIL import Image, ImageOps
import numpy as np
from .model_loader import load_digit_recognition_model

# Load your digit recognition model
model = load_digit_recognition_model()
import pymongo

client = pymongo.MongoClient('mongodb+srv://projetUser:projetUser@clustercoursmern.fmzajui.mongodb.net/')
dbname = client['digit-recognition']
collection = dbname['stockage']


# Create your views here.
@csrf_exempt
def recognize_digit(request):
    if request.method == 'POST':
        image_data = request.FILES.get('image')

        if image_data is None:
            return JsonResponse({'error': 'No image file provided'})

        # Load your digit recognition model
        model = load_digit_recognition_model()

        try:
            # Read the image data into a PIL Image
            image = Image.open(image_data)

            # Convert to grayscale
            image = ImageOps.grayscale(image)

            # Resize image
            image = image.resize((28, 28))

            # Convert to numpy array
            image = np.array(image)

            # 3. Convert 3D array to 2D list of lists
            lst = []
            for row in image:
                tmp = []
                for col in row:
                    tmp.append(str(col))
                lst.append(tmp)

            # Invert image
            image = 255 - image

            # Normalize image
            image = image / 255

            # Reshape image
            image = image.reshape(1, 28, 28, 1)

            # Make predictions using the model
            predicted_digit = model.predict(image)

            # Convert the prediction to an integer
            recognized_digit = int(np.argmax(predicted_digit))

            document = {
                'digit': recognized_digit,
                'confidence': float(predicted_digit[0][recognized_digit]),
            }

            # Add each pixel to the document
            for i, row in enumerate(lst):
              print(i)
              print(row)

            return JsonResponse({'digit': recognized_digit, 'confidence': float(predicted_digit[0][recognized_digit])})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'POST method required'})
