from src import tensorflow as tf

with tf.variable_scope("foo"):
	a = tf.get_variable("bar",[1])
	print(a.name)

with tf.variable_scope("bar"):
	b = tf.get_variable("bar",[1])
	print(b.name)

with tf.name_scope("a"):
	a = tf.Variable([1])
	print(a.name)

	a = tf.get_variable("b",[1])
	print(a.name)

with tf.name_scope("b"):
	tf.get_variable("b",[1])

writer = tf.summary.FileWriter("/log",tf.get_default_graph())
writer.close()  