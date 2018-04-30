import tensorflow as tf

node1 = tf.constant(3.0, tf.float32, name='node1')
tf.summary.scalar('node1', node1)

node2 = tf.constant(4.0, name='node2')
tf.summary.scalar('node2', node2)

add = tf.add(node1, node2)
tf.summary.histogram('add', add)

merged = tf.summary.merge_all()

# print(node1, node2)
# print(add)

sess = tf.Session()
sess.run([add, merged])
writer = tf.summary.FileWriter("./tensorboard/ex", graph=sess.graph)
writer.close()