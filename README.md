# keras-dcgan-test-to-image

Reference: https://github.com/chen0040/keras-text-to-image

基于https://github.com/chen0040/keras-text-to-image实现自己数据集的生成


1.I use dcgan_v2.py.Some problems have been modified.mainly use demo and keras_text_to_image.we should know what are those in demo.

demo/data/outputs => generator image

demo/data/pokemon => dataset

demo/data/snapshots => train info 

demo/models => save train model

demo/very_large_data => glove zip 

2.
python dcgan_v2_train.py => 训练作者自带的训练集， epoch 1000

3.
python dcgan_v2_generate.py => 效果不太理想

![image](https://github.com/rookiexiao123/keras-dcgan-test-to-image/blob/master/demo/data/outputs/dc-gan-v2-generated-0-0.png)
 
