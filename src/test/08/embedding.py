import tensorflow as tf
import numpy as np

np.random.seed(1)

with tf.variable_scope("foo"):
    v = tf.get_variable("v", [1])  # v.name == "foo/v:0"
    w = tf.get_variable("w", [1])  # w.name == "foo/w:0"


with tf.variable_scope("foo", reuse=True):
    v1 = tf.get_variable("v")  # The same as v above.

with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
	print(sess.run(v))
	print(sess.run(w))
	print(sess.run(v1))
# 	print(sess.run(v))