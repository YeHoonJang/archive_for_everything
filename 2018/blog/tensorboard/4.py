import tensorflow as tf
import numpy as np

x_data = [12.0, 28.0, 36.5, 42.0, 29.8]
y_data = [53.6, 82.4, 97.7, 107.6, 85.64]

def norm(data):
    data = np.array(data)
    x_norm = np.zeros([len(data)])
    for i in range(len(data)):
        x_norm[i] = data[i] / 100

    return np.reshape(x_norm, [-1, 1])

x_data = norm(x_data)
y_data = np.reshape(y_data, [-1, 1])


x = tf.placeholder(tf.float32, shape=[None,1])
y = tf.placeholder(tf.float32, shape=[None,1])

W = tf.Variable(tf.random_normal([1,1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = tf.add(tf.matmul(x, W), b)

cost = tf.reduce_mean(tf.square(y - hypothesis))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

# merged = tf.summary.merge_all()

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(30001):
    _cost, _W, _b, _ = sess.run([cost, W, b, train], feed_dict={x:x_data, y:y_data})
    if step % 1000 == 0:
        print("Step:", step, "\tCost:", _cost, "\tW:", _W[0], "\tb:", _b)

writer = tf.summary.FileWriter('./tb_tutorial/fahrenheit_converter', graph=sess.graph)
writer.close()
print("X: 20, Y:", sess.run(hypothesis[0], feed_dict={x:norm([20])}))
print("X: 30, Y:", sess.run(hypothesis[0], feed_dict={x:norm([30])}))
print("X: 40, Y:", sess.run(hypothesis[0], feed_dict={x:norm([40])}))
print("X: 50, Y:", sess.run(hypothesis[0], feed_dict={x:norm([50])}))
print("X: 60, Y:", sess.run(hypothesis[0], feed_dict={x:norm([60])}))