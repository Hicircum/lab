import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as imgplt
from sklearn.cluster import KMeans
from sklearn.metrics import normalized_mutual_info_score,adjusted_rand_score
import clustering_performance


def getinfo():
    global total_photo
    print(os.getcwd())
    file = os.listdir(r"D:\\workspace\\sklearn\\Ch3_data\\face_images")
    i = 0
    for subfile in file:
        if subfile == "__pycache__":
            continue
        photo = os.listdir(r"D:\\workspace\\sklearn\\Ch3_data\\face_images\\" + subfile)
        for name in photo:
            photo_name.append(r"D:\\workspace\\sklearn\\Ch3_data\\face_images\\"+ subfile+'\\'+name)
            target.append(i)
        i += 1
    for path in photo_name:
        photo = imgplt.imread(path)
        photo = photo.reshape(1, -1)
        photo = pd.DataFrame(photo)
        total_photo = total_photo._append(photo, ignore_index=True)
    total_photo = total_photo.values


def kmeans():
    clf = KMeans(n_clusters=10)
    clf.fit(total_photo)
    y_predict = clf.predict(total_photo)
    centers = clf.cluster_centers_
    result = centers[y_predict]
    result = result.astype("int64")
    result = result.reshape(200, 200, 180, 3)
    return result,y_predict


def draw():
    fig,ax  = plt.subplots(nrows=10,ncols=20,sharex = True,sharey = True,figsize = [15,8],dpi = 80)
    plt.subplots_adjust(wspace = 0,hspace = 0)
    count = 0
    for i in range(10):
        for j in range(20):
            ax[i,j].imshow(result[count])
            count += 1
    plt.xticks([])
    plt.yticks([])
    plt.show()


def score():
    ACC = clustering_performance.cluster_acc(target, y_predict)
    NMI = normalized_mutual_info_score(target, y_predict)
    ARI = adjusted_rand_score(target, y_predict)
    print(" ACC = ", ACC)
    print(" NMI = ", NMI)
    print(" ARI = ", ARI)


photo_name = []
target = []
total_photo = pd.DataFrame()
getinfo()
result,y_predict = kmeans()
score()
draw()