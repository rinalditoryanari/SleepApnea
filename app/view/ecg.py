from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import tensorflow as tf
import pickle
import wfdb
import pandas as pd
from tensorflow.keras.models import load_model
import zipfile
import os
import shutil

from django.core.files.storage import FileSystemStorage
# with open('sources/model/modelApneaECG.pkl', 'rb') as file:
#         model = pickle.load(file)
model = load_model("sources/model/ModelApneaECG/ModelApnea")

@csrf_exempt
def predict(request):
     if request.method == 'POST':
          ecg_file = request.FILES['ecg_file']
          filepath = "sources/filecsv/"
          csv = []
          predik = []
          with zipfile.ZipFile(ecg_file) as scream_zip:
               scream_zip.extractall(filepath)

          namafile = os.listdir(filepath)
          nama = os.path.splitext(namafile[0])[0]
          record = wfdb.rdrecord(os.path.join(filepath, nama))
          file_size = 90000
          data = record.p_signal
          num_files = (len(data) + file_size - 1) // file_size
          for i in range(num_files):
                        # namecsv = f"{ecg_file} data{i}.csv"
               start = i * file_size
               end = min((i + 1) * file_size, len(data))
               DF = pd.DataFrame(data[start:end])
               csv.append(DF)
                        # DF.to_csv("sources/filecsv/" + namecsv, header = False, index = False)
                        # csv.append(namecsv)
          csv = csv[:-1]
          for data in csv:
               new_data = np.array(data)
               new_data = np.transpose(new_data)
                        # print(new_data.shape)
               predictions = model.predict(new_data)
                        # print(predictions)
               predik.append(predictions)
               calc = np.mean(predik)
                        # print(calc)
                        # 4. Tampilkan hasil prediksi
               if calc <= 0.5:
                    predictions = "Normal"
               elif calc >= 0.5:
                    predictions = "Apnea"
                        # print(predictions)
          response = {
               'calculate': str(calc),
               'predictions': predictions,
               }
          try:
            shutil.rmtree(filepath)  # Remove the directory and its contents
          except Exception as e:
            print(f"An error occurred while deleting files: {str(e)}")
     return JsonResponse(response)


