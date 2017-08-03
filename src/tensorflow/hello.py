# import tensorflow as tf

# hello = tf.constant('Hello, TensorFlow!')
# sess = tf.Session()
# print(sess.run(hello))

import tensorflow as tf

a = tf.constant('hello')
with tf.Session() as sess:
    print(sess.run(a))