import tensorflow as tf
a = tf.constant([[1.0,2.0],[3.0,4.0]])
b = tf.constant([[5.0,6.0],[7.0,8.0]])

with tf.Session() as sess:
    print(tf.matmul(a,b).eval())
 