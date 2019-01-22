# Neural Networks and Deep Learning with TensorFlow (1.12)

import tensorflow as tf
import numpy as np


if __name__ == "__main__":
    # Create TF session
    # sesh = tf.Session()
    # sesh.run(tf.constant(100))

    # Operations
    x = tf.constant(2)
    y = tf.constant(3)
    with tf.Session() as sesh:
        print("Operations with Constants")
        print("Addition:", sesh.run(x+y))
        print("Subtraction:", sesh.run(x-y))
        print("Multiplication:", sesh.run(x*y))
        print("Division:", sesh.run(x/y))
    
    # # Variable input
    # s, t = tf.placeholder(tf.int32), tf.placeholder(tf.int32)
    # add = tf.add(s, t)
    # sub = tf.add(s, t)
    # with tf.Session() as sesh:
    #     print("Operations with Placeholders")
    #     print("Addition", sesh.run(add, feed_dict={s:20, y:30}))
    #     print("Subtraction", sesh.run(sub, feed_dict={s:20, y:30}))

    a, b = np.array([[5.0, 5.0]]), np.array([[2.0], [2.0]])
    # Convert matricies to tf objects
    mat1, mat2 = tf.constant(a), tf.constant(b)
    mat_mul = tf.matmul(mat1, mat2)
    with tf.Session() as sesh:
        print("Matrix multiplication", sesh.run(mat_mul))
