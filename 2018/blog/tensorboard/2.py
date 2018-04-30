import tensorflow as tf
import os

TB_DIR = os.path.join(os.getcwd(), "tb_tutorial")

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
multiple = tf.multiply(a, b)
tf.summary.histogram('multiple', multiple)

merged = tf.summary.merge_all()
sess = tf.Session()
sess.run([multiple], feed_dict={a:[1, 2, 3], b:[2, 4, 6]})
print(sess.run([multiple], feed_dict={a:[1, 2, 3], b:[2, 4, 6]}))
writer = tf.summary.FileWriter(TB_DIR, graph=sess.graph)
writer.close()