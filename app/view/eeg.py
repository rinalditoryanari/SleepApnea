from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model

model = load_model(
    "sources/model/2023-06-26_13-19-38_CNN_Raw")


@csrf_exempt
def predict_api(request):
    if request.method == 'POST':
        # Get the text data from the API request
        eeg_file = request.FILES['eeg_file']

        eeg_file = extract_file(eeg_file)

        # alternatively, you can reshape the array to match the desired axes
        eeg_file = eeg_file.reshape(1, eeg_file.shape[0], 1)

        predictions = model.predict(eeg_file)

        # percentage of certainty????
        percent = np.round((1 - predictions)*100)

        predictions = predictions.reshape(predictions.shape[1])
        predictions = np.round(predictions)

        response = {
            'predictions': str(predictions[0]),
            'percentage': str(percent[0][0]) + "%",
        }
        return JsonResponse(response)


def extract_file(eeg_file):
    # Read the file and extract signal values
    data = []
    is_first_line = True

    for line in eeg_file:
        if is_first_line:
            is_first_line = False
            continue

        values = line.decode().strip().split(";")
        if len(values) >= 5:
            data.append(float(values[4]))

    # Convert the list of values to a numpy array
    data = np.array(data)

    return data
