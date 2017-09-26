from src import tensorflow as tf

node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0) # also tf.float32 implicitly
print(node1, node2) # Tensor("Const:0", shape=(), dtype=float32) Tensor("Const_1:0", shape=(), dtype=float32)

sess = tf.Session()
print(sess.run([node1,node2])) #[3.0, 4.0]

node3 = tf.add(node1,node2)
print(node3) # Tensor("Add:0", shape=(), dtype=float32)
print(sess.run(node3)) # 7.0

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a+b
print(sess.run(adder_node,{a:3,b:4})) #7.0
print(sess.run(adder_node,{a:[1,2],b:[3,4]})) #[ 4.  6.]

add_and_triple = a*3
print(sess.run(add_and_triple,{a:5})) #15.0
print(sess.run(add_and_triple,{a:[1,2]})) #[ 3.  6.]

W = tf.Variable([.3],dtype=tf.float32)
b = tf.Variable([-.3],dtype=tf.float32)		
x = tf.placeholder(tf.float32)
linear_model = W*x + b
init = tf.global_variables_initializer()
sess.run(init) # 这个时候变量才会被初始化
print(sess.run(linear_model, {x:[1,2,3,4]}))

y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)
print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))

fixW = tf.assign(W, [-1.])
fixb = tf.assign(b, [1.])
sess.run([fixW, fixb])
print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))