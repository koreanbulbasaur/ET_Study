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
from tf_explain.core.grad_cam import GradCAM
from tf_explain.core.occlusion_sensitivity import OcclusionSensitivity

optimizers = tf.keras.optimizers
metrics = tf.keras.metrics
Input = tf.keras.Input
models = tf.keras.models
layers = tf.keras.layers

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
MaxPooling2D = tf.keras.layers.MaxPooling2D

# utils
to_categorical = tf.keras.utils.to_categorical

# preprocessing
sequence = tf.keras.preprocessing.sequence
Tokenizer = tf.keras.preprocessing.text.Tokenizer
text_to_word_sequence = tf.keras.preprocessing.text.text_to_word_sequence
pad_sequence = tf.keras.preprocessing.sequence.pad_sequences
ImageDataGenerator = tf.keras.preprocessing.image.ImageDataGenerator

# callbacks
EarlyStopping = tf.keras.callbacks.EarlyStopping

# 데이터
reuters = tf.keras.datasets.reuters
imdb = tf.keras.datasets.imdb
mnist = tf.keras.datasets.mnist

# applications
VGG16 = tf.keras.applications.VGG16

# 한글
plt.rcParams['font.family'] = 'Malgun Gothic'