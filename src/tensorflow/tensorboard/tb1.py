import tensorflow as tf

a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)
add = tf.add(a, b)
mul = tf.multiply(a, b)
with tf.Session() as sess:
    # Run every operation with variable input
    print("Addition with variables: %i" % sess.run(add, feed_dict={a: 2, b: 3}))
    # print("Multiplication with variables: %i" % sess.run(mul, feed_dict={a: 2, b: 3}))
# output:
# Addition with variables: 5
# Multiplication with variables: 6

with tf.Session() as sess:
    # Run every operation with variable input
    print("Addition with variables: %i" % sess.run(add, feed_dict={a: 5, b: 6}))
    # print("Multiplication with variables: %i" % sess.run(mul, feed_dict={a: 5, b: 6}))

writer = tf.summary.FileWriter("/log",tf.get_default_graph())
writer.close()  