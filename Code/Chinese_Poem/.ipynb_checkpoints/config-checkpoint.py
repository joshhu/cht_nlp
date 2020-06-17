class Config(object):
    poetry_file = 'dataset/poetrycht.txt'
    weight_file = 'poetry_model.h5'
    # 根據前6個字預測第7個字
    max_len = 6
    batch_size = 512
    learning_rate = 0.001
