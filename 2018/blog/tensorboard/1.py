import tensorflow as tf
import os

tb_dir = os.path.join(os.getcwd(), "tb_tutorial")
cur_dir = os.path.join(tb_dir, "ex")

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
writer = tf.summary.FileWriter(cur_dir, graph=sess.graph)
writer.close()