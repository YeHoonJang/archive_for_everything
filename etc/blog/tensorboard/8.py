import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import os

tb_dir = os.path.join(os.getcwd(), "tb_tutorial")
cur_dir = os.path.join(tb_dir, "mnist_cnn")

tf.set_random_seed(777)

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

learning_rate = 0.001
training_epochs = 15
batch_size = 100

x = tf.placeholder(tf.float32, [None, 784])
x_img = tf.reshape(x, [-1, 28, 28, 1])
y = tf.placeholder(tf.float32, [None, 10])

with tf.name_scope('conv1') as scope:
    W1 = tf.Variable(tf.random_normal([3, 3, 1, 32], stddev=0.01))

    L1 = tf.nn.conv2d(x_img, W1, strides=[1, 1, 1, 1], padding='SAME')
    L1 = tf.nn.relu(L1)
    L1 = tf.nn.max_pool(L1, ksize=[1, 2, 2, 1],
                        strides=[1, 2, 2, 1], padding='SAME')

with tf.name_scope('conv2') as scope:
    W2 = tf.Variable(tf.random_normal([3, 3, 32, 64], stddev=0.01))

    L2 = tf.nn.conv2d(L1, W2, strides=[1, 1, 1, 1], padding='SAME')
    L2 = tf.nn.relu(L2)
    L2 = tf.nn.max_pool(L2, ksize=[1, 2, 2, 1],
                        strides=[1, 2, 2, 1], padding='SAME')
    L2_flat = tf.reshape(L2, [-1, 7*7*64])

with tf.name_scope('fc') as scope:
    W3 = tf.get_variable("W3", shape=[7*7*64, 10],
                         initializer=tf.contrib.layers.xavier_initializer())
    tf.summary.histogram("weight", W3)

    b = tf.Variable(tf.random_normal([10]))
    tf.summary.histogram("bias", b)

    logits = tf.matmul(L2_flat, W3) + b
    tf.summary.histogram('logits', logits)

with tf.name_scope('train') as scope:
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=y))
    tf.summary.histogram('cost', cost)

    optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)
    train = optimizer.minimize(cost)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    writer = tf.summary.FileWriter(cur_dir, graph=sess.graph)
    merged = tf.summary.merge_all()

    for epoch in range(training_epochs):
        avg_cost = 0
        total_batch = int(mnist.train.num_examples / batch_size)

        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            feed_dict = {x:batch_xs, y:batch_ys}
            _merged, _cost, _ = sess.run([merged, cost, train], feed_dict=feed_dict)
            writer.add_summary(_merged, global_step=epoch*i)
            avg_cost += _cost / total_batch
        print('Epoch:', '%04d' % (epoch + 1), 'cost =', '{:.9f}'.format(avg_cost))
