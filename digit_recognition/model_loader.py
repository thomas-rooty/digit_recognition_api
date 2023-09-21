import os
import tensorflow as tf


def load_digit_recognition_model():
  # Define the path to your .h5 file
  model_file_path = os.path.join('ai_model', 'modelH5.h5')

  if os.path.exists(model_file_path):
    model = tf.keras.models.load_model(model_file_path)
    return model
  else:
    raise FileNotFoundError("The model file 'modelH5.h5' was not found.")
