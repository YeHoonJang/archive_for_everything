import tensorflow as tf
import os

tb_dir = os.path.join(os.getcwd(), "tb_tutorial")
cur_dir = os.path.join(tb_dir, "multiple")

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
multiple = tf.multiply(a, b)
tf.summary.histogram('multiple', multiple)

merged = tf.summary.merge_all()

sess = tf.Session()
sess.run([multiple], feed_dict={a:[1, 2, 3], b:[2, 4, 6]})
print(sess.run([multiple], feed_dict={a:[1, 2, 3], b:[2, 4, 6]}))
writer = tf.summary.FileWriter(cur_dir, graph=sess.graph)
writer.close()