import tensorflow as tf


const1 = tf.constant(3.0, tf.float32, name='const1')
const2 = tf.constant(4.0, name='const2')
print(const1, const2)

add = tf.add(const1, const2)
print(add)

sess = tf.Session()
sess.run(add)
