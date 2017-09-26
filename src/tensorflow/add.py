from src import tensorflow as tf

a = tf.constant('hello, TensorFlow!')

with tf.Session() as sess:
    print(sess.run(a))
    
writer = tf.summary.FileWriter("/log",tf.get_default_graph())
writer.close()