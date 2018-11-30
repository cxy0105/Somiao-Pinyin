from __future__ import print_function
import tensorflow as tf
import numpy as np
from prepro import *
from data_load import load_vocab, load_test_string
from train import Graph
import codecs
import distance
import os


def load_data():
    result = []
    with open('data/zh.tsv', 'r', encoding='utf-8') as infile:
        for line in infile:
            line = line.strip().split('\t')
            if len(line) != 3:
                continue
            line[2] = line[2].replace("_", "").strip()
            result.append(line)
    return result


def save_error(errors):
    out = open('data/error.tsv', 'w', encoding='utf-8')
    for li in errors:
        line = '\t'.join(li)+'\n'
        out.write(line)
    out.close()


def main():
    errors = []
    g = Graph(is_training=False)

    # Load vocab
    pnyn2idx, idx2pnyn, hanzi2idx, idx2hanzi = load_vocab()

    with g.graph.as_default():
        sv = tf.train.Supervisor()
        with sv.managed_session(config=tf.ConfigProto(allow_soft_placement=True)) as sess:
            # Restore parameters
            sv.saver.restore(sess, tf.train.latest_checkpoint(hp.logdir));
            print("Restored!")

            # Get model
            mname = open(hp.logdir + '/checkpoint', 'r').read().split('"')[1]  # model name
            tests = load_data()
            for li in tests:
                line = li[1]
                if len(line) > hp.maxlen:
                    print('最长拼音不能超过50')
                    continue
                x = load_test_string(pnyn2idx, line)
                # print(x)
                preds = sess.run(g.preds, {g.x: x})
                # got = "".join(idx2hanzi[str(idx)] for idx in preds[0])[:np.count_nonzero(x[0])].replace("_", "")
                got = "".join(idx2hanzi[idx] for idx in preds[0])[:np.count_nonzero(x[0])].replace("_", "").strip()
                if got != li[2]:
                    errors.append(li + [got])
    save_error(errors)


if __name__ == '__main__':
    main()
    print("Done")