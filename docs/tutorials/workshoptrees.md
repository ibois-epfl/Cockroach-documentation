---
layout: default
title: workshoptrees
parent: Tutorial
nav_order: 6
---

# workshoptrees - Overview of different typologies
{: .no_toc }


![img_1](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/Screenshotfrom2023-09-2517-41-31.png?raw=true)

The proposed workflow to segment a forest pointcloud using Cockroach is detailed here. 

We encourage you to play with the parameters, as you go. 


We propose you to start from a pointcloud section of your choice. For computation time limitation we recommend to work with small portions, containing 3-5 trees. More is possible but might strain the ressources of your laptop.\

As always, experimentation is king/queen .


First, import the pointcloud in Rhino. The most simple is to drag&drop on the Rhino workspace, or in the Rhino icon if Rhino is not open. 
# Remove Ground
We recommand to remove the ground manually (or you can play with ransac, with some forest samples it might work better than with others)
To remove some points from a pointcloud in Rhino, hold  
`ctrl + shift` and select with the mouse the region you want to select, then press `delete`.

# Downsample
For further computation it might be better to downsample the pointcloud. For this, the **[``` Cockroach_Downsample(n_points) ```](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/docs/cmd_description/Cockroach_Downsample.md#cockroach_downsample)** command exists. This command takes as argument the number of points you want in the result point cloud.

![img_2](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/WS_again_tutorial_1.png?raw=true)

<p style="text-align: center;">Original point cloud with 10 000 000 points on the left, downsampled point cloud with 200 000 points on the right</p> 

Once the point cloud is downsampled, we can start the processing:

# Compute normals
Once we have a reduced point cloud, we can compute the normals. Note that computing the normals earlier would have been possible, but we would have partly calculated normals on points that we will delete just after, thus wasting computation time. 

To compute the normals, we can use the command **[```Cockroach_ComputePointCloudNormals(n_points)```](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/docs/cmd_description/Cockroach_ComputePointCloudNormals.md#cockroach_computepointcloudnormals)**, where n_points is the number of neighbouring points to be included in the computation for one single normal. 

Once the normals are computed, we can display them with the command: **[``` Cockroach_ShowNormals() ```](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/docs/cmd_description/Cockroach_ShowNormals.md#cockroach_shownormals)** 

![img_3](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/WS_again_tutorial_2.png?raw=true)

<p style="text-align: center;">Normals computed on the pointcloud. The colors represent the direction of the normal</p> 

![img_4](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/WS_again_tutorial_2_bis.png?raw=true)

<p style="text-align: center;">Close-up on the normals on the tree trunks and some small branches</p> 

# Remove statistical outliers
The next step we propose is to remove the "statistical outilers", that is, points that probably are errors or unimportant points, because they are too isolated to be significant. Of course, the limit between significant and unsignificant is quite vague, and we encourage you to test some variation of the parameters we propose. Nevertheless, on our test pointcloud, those parameters yielded good results. 

Run the following commands:

```Cockroach_RemoveStatisticalOutliers(1000 0.4)```
```Cockroach_RemoveStatisticalOutliers(1000 0.4)```
```Cockroach_RemoveStatisticalOutliers(800 0.5)```
```Cockroach_RemoveStatisticalOutliers(800 0.5)```
```Cockroach_RemoveStatisticalOutliers(800 0.5)```


Those parameters (especially the 0.4 and 0.5) are quite agressive. It basically states that the points must be at least by group of 1000, and that we are quite strict when accepting a point as part of a group. 

![img_5](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/WS_again_tutorial_3.png?raw=true)

<p style="text-align: center;">From left to right: original PC, after 1,2,3,4,5 statistical removals</p> 

The parameters of `Cockroach_RemoveStatisticalOutliers` are not that sensitive and slightly different parameters could lead to a very similar result

![img_6](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/WS_again_tutorial_3_bis.png?raw=true)


<p style="text-align: center;">Downsampled Pointcloud on the left, original on the right</p> 

The result should be some groups of points, some easily identifiable as trunks (and probably entire small trees)
# Euclidian clustering
The last step we propose is the Euclidian clustering, called with the command:

**[```Cockroach_ClusterEuclidianKSearch( Neighbours , DistanceThreshold , MinClusterSize, Color)```](https://ibois-epfl.github.io/Cockroach-documentation/docs/cmd_description/Cockroach_ClusterEuclideanKSearch/)**

Euclidian clustering means that we create groups of points purely based on distance. We set the minimum number of points in a group and the distance threshold. Based thereon, the pointcloud is subdivided into smaller pointclouds. By ungrouping, you can select them individually

![img_7](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/WS_again_tutorial_4.png?raw=true)

Result of `Cockroach_ClusterEuclidianKSearch( 30 , 0.005 , 3000, True)`

# Cleanup and sections

We then recommand to clean up the trunk, as it still inludes small branches.

![img_8](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/Capture_1.png?raw=true)
We then generate the point cloud cross section with the rhino command     

**[```PointCloudContour()```](https://docs.mcneel.com/rhino/7/help/en-us/commands/pointcloud.htm)**

You will need to generate closed sections.

![img_9](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/WS_again_tutorial_5.png?raw=true)

{: .fs-6 .fw-300 }

---

