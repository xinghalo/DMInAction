from src import tensorflow as tf

a = tf.constant(1.0,name="a")

sess = tf.Session()
print(sess.run(a))
sess.close()

with tf.Session() as sess:
	print(sess.run(a))

