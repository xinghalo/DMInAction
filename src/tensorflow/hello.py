# import tensorflow as tf

# hello = tf.constant('Hello, TensorFlow!')
# sess = tf.Session()
# print(sess.run(hello))


from src import tensorflow as tf

# 引入TensorFlow模块，并且起一个别名

# 定义一个常量
a = tf.constant('hello, TensorFlow!') 
# 创建会话，并输出
with tf.Session() as sess:
    print(sess.run(a))
    
writer = tf.summary.FileWriter("/log",tf.get_default_graph())
writer.close()