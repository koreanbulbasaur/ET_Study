'''
import os, sys
current_dir = os.path.dirname(os.path.abspath("../module.py"))
sys.path.append(current_dir)
from module import *
'''
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# models
Sequential = tf.keras.models.Sequential

# layers
Dense = tf.keras.layers.Dense
LSTM = tf.keras.layers.LSTM
Embedding = tf.keras.layers.Embedding
Dropout = tf.keras.layers.Dropout
Conv1D = tf.keras.layers.Conv1D
MaxPooling1D = tf.keras.layers.MaxPooling1D
Activation = tf.keras.layers.Activation

# utils
to_categorical = tf.keras.utils.to_categorical

# preprocessing
sequence = tf.keras.preprocessing.sequence

# callbacks
EarlyStopping = tf.keras.callbacks.EarlyStopping

# 데이터
reuters = tf.keras.datasets.reuters
imdb = tf.keras.datasets.imdb