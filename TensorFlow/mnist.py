# MNIST dataset work

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Data
    mnist = input_data.read_data_sets("TensorFlow/MNIST_data/", one_hot=True)

    # Visualize (reshaping array of pixels)
    plt.imshow(mnist.train.images[1].reshape(28,28))
    plt.show()

    # Create classification model
    x = tf.placeholder(tf.float32, shape=[None, 784])
    weight = tf.Variable(tf.zeros([784, 10]))
    bias = tf.Variable(tf.zeros([10]))
    
    y = tf.matmul(x, weight) + bias
    y_true = tf.placeholder(tf.float32, shape=[None, 10])
    cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y_true, logits=y))
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.5)
    train = optimizer.minimize(cross_entropy)

    # Run session
    print("Creating session...")
    init = tf.global_variables_initializer()
    with tf.Session() as sesh:
        sesh.run(init)
        for step in range(1000):
            batch_x, batch_y = mnist.train.next_batch(100)
            sesh.run(train, feed_dict={x:batch_x, y_true:batch_y})
        
        matches=tf.equal(tf.argmax(y, 1), tf.argmax(y_true, 1))
        acc = tf.reduce_mean(tf.cast(matches, tf.float32))
        print(sesh.run(acc, feed_dict={x:mnist.test.images, y_true:mnist.test.labels}))