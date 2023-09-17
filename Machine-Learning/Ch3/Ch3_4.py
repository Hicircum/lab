from scipy.cluster.vq import *
from pylab import *
from PIL import Image
import clustering_performance


def clusterpixels(infile, k, steps):
    im = array(Image.open(infile))
    dx = im.shape[0] / steps
    dy = im.shape[1] / steps
    features = []

    for x in range(steps):
        for y in range(steps):
            R = mean(im[int(x * dx):int((x + 1) * dx), int(y * dy):int((y + 1) * dy), 0])
            G = mean(im[int(x * dx):int((x + 1) * dx), int(y * dy):int((y + 1) * dy), 1])
            B = mean(im[int(x * dx):int((x + 1) * dx), int(y * dy):int((y + 1) * dy), 2])
            features.append([R, G, B])
    features = array(features, 'f')
    centroids, _ = kmeans(features, k)
    code, _ = vq(features, centroids)
    codeim = code.reshape(steps, steps)
    codeim = np.array(Image.fromarray(codeim).resize((im.shape[1], im.shape[0])))
    return codeim, code


infile_Stones = 'stones.jpg'
im_Stones = array(Image.open(infile_Stones))
# image is divided in steps*steps region
steps = (50, 100)

# show original image
subplot(231)
title('original')
axis('off')
imshow(im_Stones)

trueLabel = []
predictiveLabel = []

for k in range(2, 7):
    codeim, code = clusterpixels(infile_Stones, k, steps[-1])
    subplot(2, 3, k)
    title('K=' + str(k))
    axis('off')
    imshow(codeim)

    trueLabel.extend(code.flatten())
    predictiveLabel.extend(code)

show()

# performance
'''
    抱错修改clustering_performance.cluster_acc
    y_true = np.array(y_true).astype(np.int64)
    y_pred = np.array(y_pred).astype(np.int64)
'''
ACC, NMI, ARI = clustering_performance.clusteringMetrics(trueLabel, predictiveLabel)
print("ACC:", ACC)
print("NMI:", NMI)
print("ARI:", ARI)