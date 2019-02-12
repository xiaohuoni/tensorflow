import tensorflow as tf

a = tf.constant([1.0,2.0,3.0])

with tf.Session() as sess:
    print(tf.log(a).eval())