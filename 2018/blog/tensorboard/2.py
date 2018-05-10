import tensorflow as tf
import os

tb_dir = os.path.join(os.getcwd(), "tb_tutorial")
cur_dir = os.path.join(tb_dir, "ex")

const1 = tf.constant(3.0, name='const1')
tf.summary.scalar('const1', const1)

const2 = tf.constant(4.0, name='const2')
tf.summary.scalar('const2', const2)

add = tf.add(const1, const2)
tf.summary.histogram('add', add)

merged = tf.summary.merge_all()

sess = tf.Session()
sess.run(add)

writer = tf.summary.FileWriter(cur_dir, graph=sess.graph)
writer.close()
