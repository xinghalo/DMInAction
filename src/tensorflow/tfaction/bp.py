from src import tensorflow as tf

w1 = tf.Variable(tf.random_normal([2,3],stddev=1))
w2 = tf.Variable(tf.random_normal([3,1],stddev=1))

x = tf.placeholder(tf.float32,shape=[3,2],name="input")
a = tf.matmul(x,w1)
y = tf.matmul(a,w2)

with tf.Session() as sess:
	sess.run(tf.initialize_all_variables())
	print(sess.run(y,feed_dict={x:[[0.7,0.9],[0.1,0.4],[0.5,0.8]]}))

	cross_entropy = - tf.reduce_mean( y * tf.log(tf.clip_by_value(y,1e-10,1.0)))

	learning_rate = 0.001
	train_step = tf.train.AdamOptimizer(learning_rate).minimize(cross_entropy)

	print(sess.run(tf.trainable_variables()))