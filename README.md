# MRCNN_with_DFPN

Mask RCNN with double fpn and k-means anchors(not yolo version)

## 简介

这是一个带有双向特征金字塔的Mask-RCNN模型，目的是为了提高小目标检测的识别率与准确度，同时引入了聚类锚框重设方法，通过 k-means聚类算法对数据集中的边界框宽高比进行重设（非yolo版本，比较简单无脑，效果不好可以忽略）。

本项目作为我的本科毕业设计，也是踩了许多的坑，但最后的测试效果还是说得过去的，彻底感受了一把什么是真正的“炼丹师”。我的研究生方向可能不在此了（模式识别、目标检测类），故将踩过的坑开源，希望能给后面的学弟学妹们一点启发。

## 特点

- 将单向fpn扩展为双向
- 加入 Group Normalization （BN在小batchsize上效果不好）
- 增加imgaug数据增强方式
- 采用VEDAI小目标航拍数据集，完美转COCO格式，可以利用COCO评价指标评估小目标检测效果

## 食用方法

大致方法参考[matterport]([matterport/Mask_RCNN: Mask R-CNN for object detection and instance segmentation on Keras and TensorFlow (github.com)](https://github.com/matterport/Mask_RCNN)) 作者版本的Mask-RCNN源码，双向特征金字塔的改动主要集中在\MRCNN_with_DFPN\mrcnn\model.py文件中。[DFPNwA.ipynb](https://github.com/chikacya/MRCNN_with_DFPN/blob/master/DFPNwA.ipynb)文件可以用作Google Colab当中进行训练和测试。

[权重weight文件](https://drive.google.com/drive/folders/1YYBSTSKMyzsTaEyQ4JU85WhIbcwGYufv?usp=sharing)：mask_rcnn_coco_0200.h5代表原始Mask-RCNN训练VEDAI数据集后的权重

​								mask_rcnn_dfpn_coco.h5代表DFPN-Mask-RCNN训练VEDAI数据集后的权重

​								mask_rcnn_dfpn_ka_coco.h5代表经过k-means权重调整宽高比后DFPN-Mask-RCNN训练VEDAI数据集后的权重

**注意：使用mask_rcnn_dfpn_ka_coco.h5需要调整相应的setting**

## 测试结果

![alt 测试结果](https://i.bmp.ovh/imgs/2020/11/25edacbccacb1436.png)



