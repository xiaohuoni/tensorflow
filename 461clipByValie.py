import tensorflow as tf

a = tf.constant([[1.0,2.0,3.0,4.0],[5.0,6.0,7.0,8.0]])

# print(tf.clip_by_value(a,2.5,6.5).eval())

with tf.Session() as sess:
    print(tf.clip_by_value(a, 2.5, 4.5).eval())