import tensorflow as tf

a = tf.constant(1.0,name="a")
b = tf.constant([1.0,2.0],name="b")
c = tf.constant([[1.0,2.0],[1.0,2.0]],name="c")

print(a)
print(b)
print(c)

sess = tf.Session()
print(sess.run(a))
print(sess.run(b))
print(sess.run(c))

writer = tf.summary.FileWriter("/log",tf.get_default_graph())
writer.close()