import time
from collections import deque

import numpy as np
import tensorflow as tf
from six import next
from tensorflow.core.framework import summary_pb2

import dataio
import ops

np.random.seed(13575)

# BATCH_SIZE = 1000
BATCH_SIZE = 1
USER_NUM = 6040
ITEM_NUM = 3952
DIM = 15
EPOCH_MAX = 100
DEVICE = "/cpu:0"


def clip(x):
    return np.clip(x, 1.0, 5.0)


def make_scalar_summary(name, val):
    return summary_pb2.Summary(value=[summary_pb2.Summary.Value(tag=name, simple_value=val)])


def get_data():
    df = dataio.read_process("/Users/xinghailong/Documents/workspace/my/DMInAction/src/tesnsorflow/recommend/ml-1m/test.dat", sep="::")
    rows = len(df)
    # 打乱顺序
    # np.permutation(rows) 随机生成rows内的一维数组：
    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.permutation.html
    # 并且重置索引
    df = df.iloc[np.random.permutation(rows)].reset_index(drop=True)
    # 切分数据集，90%用于训练集，10%用于测试集
    split_index = int(rows * 0.9)
    df_train = df[0:split_index]
    df_test = df[split_index:].reset_index(drop=True)
    return df_train, df_test


def svd(train, test):

    # 获取训练集的长度
    samples_per_batch = len(train) // BATCH_SIZE

    # 把列数据转变成行数据，然后随机打散
    iter_train = dataio.ShuffleIterator([train["user"],
                                         train["item"],
                                         train["rate"]],
                                        batch_size=BATCH_SIZE)
    print(iter_train)

    iter_test = dataio.OneEpochIterator([test["user"],
                                         test["item"],
                                         test["rate"]],
                                        batch_size=-1)
    print(iter_test)

    user_batch = tf.placeholder(tf.int32, shape=[None], name="id_user")
    item_batch = tf.placeholder(tf.int32, shape=[None], name="id_item")
    rate_batch = tf.placeholder(tf.float32, shape=[None])

    infer, regularizer = ops.inference_svd(user_batch, item_batch, user_num=USER_NUM, item_num=ITEM_NUM, dim=DIM,
                                           device=DEVICE)
    global_step = tf.contrib.framework.get_or_create_global_step()
    _, train_op = ops.optimization(infer, regularizer, rate_batch, learning_rate=0.001, reg=0.05, device=DEVICE)

    # 初始化变量
    init_op = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init_op)

        # 定义日志输入环境，需要跟ternsorboard的地址对应上
        summary_writer = tf.summary.FileWriter(logdir="/log", graph=sess.graph)

        print("{} {} {} {}".format("epoch", "train_error", "val_error", "elapsed_time"))
        
        errors = deque(maxlen=samples_per_batch)
        start = time.time()
        for i in range(EPOCH_MAX * samples_per_batch):
            
            users, items, rates = next(iter_train)
            _, pred_batch = sess.run([train_op, infer], feed_dict={user_batch: users,
                                                                   item_batch: items,
                                                                   rate_batch: rates})
            pred_batch = clip(pred_batch)
            # np.power指数，计算平方差
            errors.append(np.power(pred_batch - rates, 2))
            
            # 输出信息
            if i % samples_per_batch == 0:
                train_err = np.sqrt(np.mean(errors))
                test_err2 = np.array([])
                for users, items, rates in iter_test:
                    pred_batch = sess.run(infer, feed_dict={user_batch: users,
                                                            item_batch: items})
                    pred_batch = clip(pred_batch)
                    test_err2 = np.append(test_err2, np.power(pred_batch - rates, 2))
                end = time.time()
                test_err = np.sqrt(np.mean(test_err2))
                print("{:3d} {:f} {:f} {:f}(s)".format(i // samples_per_batch, train_err, test_err,
                                                       end - start))
                train_err_summary = make_scalar_summary("training_error", train_err)
                test_err_summary = make_scalar_summary("test_error", test_err)
                summary_writer.add_summary(train_err_summary, i)
                summary_writer.add_summary(test_err_summary, i)
                start = end


if __name__ == '__main__':
    df_train, df_test = get_data()
    svd(df_train, df_test)
    print("Done!")
