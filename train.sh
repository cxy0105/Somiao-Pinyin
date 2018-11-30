#!/bin/bash
export LD_LIBRARY_PATH=/usr/local/cuda-9.1/lib64:$LD_LIBRARY_PATH
echo clean data start
/bigdata/ai_dev/congxy/venv36/bin/python clean_data.py
echo build corpus start
/bigdata/ai_dev/congxy/venv36/bin/python build_corpus.py
echo prepro start
/bigdata/ai_dev/congxy/venv36/bin/python prepro.py
echo train start
/bigdata/ai_dev/congxy/venv36/bin/python train.py
