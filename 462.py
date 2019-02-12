import tensorflow as tf

a = tf.constant([1.0,2.0,3.0,4.0])
b = tf.constant([6.0,5.0,4.0,3.0])

with tf.Session() as sess:
    print(tf.greater(a,b).eval())
    print(tf.where(tf.greater(a,b),a,b).eval())