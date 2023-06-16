'''
import os, sys
current_dir = os.path.dirname(os.path.abspath("../module.py"))
sys.path.append(current_dir)
from module import *
'''
import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from attention import Attention

# models
Sequential = tf.keras.models.Sequential
Model = tf.keras.models.Model

# layers
Dense = tf.keras.layers.Dense
LSTM = tf.keras.layers.LSTM
Embedding = tf.keras.layers.Embedding
Dropout = tf.keras.layers.Dropout
Conv1D = tf.keras.layers.Conv1D
MaxPooling1D = tf.keras.layers.MaxPooling1D
Activation = tf.keras.layers.Activation
Input = tf.keras.layers.Input
Reshape = tf.keras.layers.Reshape
BatchNormalization = tf.keras.layers.BatchNormalization
LeakyReLU = tf.keras.layers.LeakyReLU
UpSampling2D = tf.keras.layers.UpSampling2D
Conv2D = tf.keras.layers.Conv2D
Flatten = tf.keras.layers.Flatten


# utils
to_categorical = tf.keras.utils.to_categorical

# preprocessing
sequence = tf.keras.preprocessing.sequence
Tokenizer = tf.keras.preprocessing.text.Tokenizer
text_to_word_sequence = tf.keras.preprocessing.text.text_to_word_sequence
pad_sequence = tf.keras.preprocessing.sequence.pad_sequences

# callbacks
EarlyStopping = tf.keras.callbacks.EarlyStopping

# 데이터
reuters = tf.keras.datasets.reuters
imdb = tf.keras.datasets.imdb
mnist = tf.keras.datasets.mnist