"""
    Generic training script that trains a model using a given dataset.

    This code modifies the "TensorFlow-Slim image classification model library",
    Please visit https://github.com/tensorflow/models/tree/master/research/slim
    for more detailed usage.

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

import my_env
import train_models
import train_models_garbage
from datasets.utils import *

slim = tf.contrib.slim

def del_all_flags(FLAGS):
    flags_dict = FLAGS._flags()
    keys_list = [keys for keys in flags_dict]
    for keys in keys_list:
        if keys=='log_dir':
            FLAGS.__delattr__(keys)

FLAGS = tf.app.flags.FLAGS
del_all_flags(FLAGS)

#########################
# Training Directories #
#########################

tf.app.flags.DEFINE_string('dataset_name', 'garbage',
                           'The name of the dataset to load.')

tf.app.flags.DEFINE_string('split_name', 'train',
                           'The name of the data split.')

tf.app.flags.DEFINE_string('dataset_dir', f'{my_env.path}/datasets/results/garbage/tfrecords',
                           'The directory where the dataset files are stored.')

tf.app.flags.DEFINE_string('checkpoint_dir', 'garbage_dml_normal_06/checkpoint',
                           'Directory name to save the checkpoints [checkpoint]')

tf.app.flags.DEFINE_string('log_dir', 'garbage_dml_normal_06/logs',
                           'Directory name to save the logs')


#########################
#     Model Settings    #
#########################

tf.app.flags.DEFINE_string('model_name', 'normal_v1,normal_v1',
                           'The name of the architecture to train.')

tf.app.flags.DEFINE_string('preprocessing_name', 'reid',
                           'The name of the preprocessing to use. If left as `None`, '
                           'then the model_name flag is used.')

tf.app.flags.DEFINE_float('weight_decay', 0.004,
                          'The weight decay on the model weights.')

tf.app.flags.DEFINE_float('label_smoothing', 0.1,
                          'The amount of label smoothing.')

tf.app.flags.DEFINE_integer('batch_size', 16,
                            'The number of samples in each batch.')

tf.app.flags.DEFINE_integer('max_number_of_steps', 3000,
                            'The maximum number of training steps.')

tf.app.flags.DEFINE_integer('ckpt_steps', 25,
                            'How many steps to save checkpoints.')

tf.app.flags.DEFINE_integer('num_classes', 6,
                            'The number of classes.')

tf.app.flags.DEFINE_integer('num_networks', 2,
                            'The number of networks in DML.')

tf.app.flags.DEFINE_integer('num_gpus', 1,
                            'The number of GPUs.')

#########################
# Optimization Settings #
#########################

tf.app.flags.DEFINE_string('optimizer', 'sgd',
                           'The name of the optimizer, one of "adadelta", "adagrad", "adam",'
                           '"ftrl", "momentum", "sgd" or "rmsprop".')

tf.app.flags.DEFINE_float('learning_rate', 0.02,
                          'Initial learning rate.')

tf.app.flags.DEFINE_float('adam_beta1', 0.5,
                          'The exponential decay rate for the 1st moment estimates.')

tf.app.flags.DEFINE_float('adam_beta2', 0.999,
                          'The exponential decay rate for the 2nd moment estimates.')

tf.app.flags.DEFINE_float('opt_epsilon', 1e-8,
                          'Epsilon term for the optimizer.')


#########################
#   Default Settings    #
#########################
tf.app.flags.DEFINE_integer('num_clones', 1,
                            'Number of model clones to deploy.')

tf.app.flags.DEFINE_boolean('clone_on_cpu', False,
                            'Use CPUs to deploy clones.')

tf.app.flags.DEFINE_integer('worker_replicas', 1,
                            'Number of worker replicas.')

tf.app.flags.DEFINE_integer('num_ps_tasks', 0,
                            'The number of parameter servers. If the value is 0, then the parameters '
                            'are handled locally by the worker.')

tf.app.flags.DEFINE_integer('task', 0,
                            'Task id of the replica running the training.')

tf.app.flags.DEFINE_float('moving_average_decay', 0.9999,
                          'The decay to use for the moving average.'
                          'If left as None, then moving averages are not used.')

tf.app.flags.DEFINE_integer('input_queue_memory_factor', 16,
                            """Size of the queue of preprocessed images. """)

tf.app.flags.DEFINE_integer('num_readers', 4,
                            'The number of parallel readers that read data from the dataset.')

tf.app.flags.DEFINE_integer('num_preprocessing_threads', 4,
                            'The number of threads used to create the batches.')

tf.app.flags.DEFINE_boolean('log_device_placement', False,
                            """Whether to log device placement.""")


FLAGS = tf.app.flags.FLAGS


def main(_):
    # create folders
    mkdir_if_missing(FLAGS.checkpoint_dir)
    mkdir_if_missing(FLAGS.log_dir)
    # training
    train_models_garbage.train()


if __name__ == '__main__':
    tf.app.run()
