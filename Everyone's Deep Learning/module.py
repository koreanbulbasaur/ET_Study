'''
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname('"../module.py"'))))
from module import *
'''
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

Sequential = tf.keras.models.Sequential
Dense = tf.keras.layers.Dense
LSTM = tf.keras.layers.LSTM
to_categorical = tf.keras.utils.to_categorical
Embedding = tf.keras.layers.Embedding
sequence = tf.keras.preprocessing.sequence
EarlyStopping = tf.keras.callbacks.EarlyStopping

# 데이터
reuters = tf.keras.datasets.reuters
imdb = tf.keras.datasets.imdb