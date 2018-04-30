import tensorflow as tf

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
c = tf.placeholder(tf.float32)

multiple = tf.multiply(a, b)
tf.summary.histogram('multiple', multiple)

power = tf.pow(multiple, c)
tf.summary.histogram('power', power)

merged = tf.summary.merge_all()
sess = tf.Session()
sess.run([power], feed_dict={a:[1, 2, 3], b:[2, 4, 6], c:2})
print(sess.run([power], feed_dict={a:[1, 2, 3], b:[2, 4, 6], c:2}))
writer = tf.summary.FileWriter("./tb_tutorial", graph=sess.graph)
writer.close()