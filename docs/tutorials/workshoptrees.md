---
layout: default
title: workshoptrees
parent: Tutorial
nav_order: 6
---
# Workshoptrees - Cockroach on trees
{: .no_toc }

<br />

Authors: [damien.gilliard@epfl.ch](damien.gilliard@epfl.ch), [joseph.tannous@epfl.ch](joseph.tannous@epfl.ch), [andrea.settimi@epfl.ch](andrea.settimi@epfl.ch)


This tutorial was made for a workshop held at IBois, EPFL for the sudio Weinand (directed by Prof. Yves Weinand, under supervision of dr. Agathe Mignon )


It uses open source 3D point clouds from [The Center of excellence in laser scanning research ](https://laserscanning.fi/). For more information: [International benchmarking of terrestrial laser scanning approaches for forest inventories (Liang et al 2018).](https://www.sciencedirect.com/science/article/pii/S0924271618301849?via%3Dihub)
**The cropped data converted to .e57 can be accessed through this [link](https://1drv.ms/f/s!Am3cYTZnGFlCg07Y7lWI361rvh4a?e=IF2Rms)**

 

<p align="center">
<img src="https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/Screenshotfrom2023-09-2517-41-31.png?raw=true" width="300" height="560"/>
</p> 

We propose to start from a pointcloud section of your choice from the highlighted link hereabove. 



First, import the pointcloud in Rhino. The simplest is to drag&drop in the Rhino workspace, or on the Rhino icon if Rhino is not open. 

<br/><br/>

## 0 Remove Ground 

We recommand to remove the ground manually (For this workshop, fiddling with ransac may not be the most suitable option).To remove some points from a pointcloud in Rhino, hold `ctrl + shift` and select with the mouse the region you want to select, then press `delete`.
<br/><br/>


## 1 Downsample
For further computation it might be better to downsample the pointcloud. For this, use the **[`Cockroach_Downsample(n_points)`](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/docs/cmd_description/Cockroach_Downsample.md#cockroach_downsample)** command. This command takes as argument the number of points you want in the result point cloud.


![img_2](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/WS_again_tutorial_1.png?raw=true)
<p style="text-align: center;"><font size="2"><i>Original point cloud with 10 000 000 points on the left, downsampled point cloud with 200 000 points on the right</i></font></p> 

We recommend using:

 `Cockroach_Downsample(200000)`

<br/><br/>

Once the point cloud is downsampled, we can start the processing:


## 2 Remove statistical outliers
The next step we propose is to remove the "statistical outilers", that is, points that probably are errors or unimportant points, because they are too isolated to be significant.

**[` Cockroach_RemoveStatisticalOutliers(Neighbours, ratio)`](https://ibois-epfl.github.io/Cockroach-documentation/docs/cmd_description/Cockroach_RemoveStatisticalOutliers/)**


 Of course, the limit between significant and unsignificant is quite vague, depends on the point cloud, and we encourage you to test some variation of the parameters we propose. Nevertheless, on our test pointcloud, those parameters yielded good results. 

Run the following commands:

```
Cockroach_RemoveStatisticalOutliers(1000 0.4)
Cockroach_RemoveStatisticalOutliers(1000 0.4)
Cockroach_RemoveStatisticalOutliers(800 0.5)
Cockroach_RemoveStatisticalOutliers(800 0.5)
Cockroach_RemoveStatisticalOutliers(800 0.5)
```


Those parameters (especially the 0.4 and 0.5) are quite agressive. It basically states that the points must be at least by group of 1000, and that we are quite strict when accepting a point as part of a group. 

![img_5](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/WS_again_tutorial_3.png?raw=true)
<p style="text-align: center;"><font size="2"><i>From left to right: original PC, then after 1,2,3,4,5 statistical removals</i></font></p> 


![img_6](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/WS_again_tutorial_3_bis.png?raw=true)


<p style="text-align: center;"><font size="2"><i>The result after the successive stastistical removals</i></font></p> 

The result should be different groups of points, some easily identifiable as trunks (and possibly entire small trees)
<br/><br/>


## 3 Euclidian clustering
The last step we propose is the Euclidian clustering, called with the command:

**[`Cockroach_ClusterEuclidianKSearch( Neighbours , DistanceThreshold , MinClusterSize, Color)`](https://ibois-epfl.github.io/Cockroach-documentation/docs/cmd_description/Cockroach_ClusterEuclideanKSearch/)**

Try:

 `Cockroach_ClusterEuclidianKSearch( 30 , 0.005 , 3000, True)`

Euclidian clustering means that we create groups of points purely based on distance. We set the minimum number of points in a group and the distance threshold. Based thereon, the pointcloud is subdivided into smaller pointclouds. By ungrouping, you can select them individually.

![img_7](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/WS_again_tutorial_4.png?raw=true)

<p style="text-align: center;"><font size="2"><i>Result of Cockroach_ClusterEuclidianKSearch( 30 , 0.005 , 3000, True)</i></font></p> 
<br/><br/>


## 4 Cleanup and sections

We then recommand to clean up the trunk, as it still inludes small branches.

![img_8](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/Capture_1.png?raw=true)
<p style="text-align: center;"><font size="2"><i>Hand selection of the points to delete</i></font></p> 

We then generate the point cloud cross section with the rhino command **[`PointCloudContour()`](https://docs.mcneel.com/rhino/7/help/en-us/commands/pointcloud.htm)**

You will need to generate closed sections:
<p align="center">
<img src="https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/PoinCloudContour_parameters.png?raw=true" width="350" height="560"/>
</p> 
<p style="text-align: center;"><font size="2"><i>The parameters for PointCloudContour()</i></font></p> 
![img_9](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/WS_again_tutorial_5.png?raw=true)
<p style="text-align: center;"><font size="2"><i>The result of the PointCloudContour()</i></font></p> 


<br/><br/>

## 5 Creating a closed Brep<a name="closedbrep"></a>

To create a closed brep, we propose to execute a short [python code donloadable here](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/assets/fjoint/brep_from_treePC.py). To do so, type `RunPythonScript` in the command line of Rhino. In the opened the window, select the .py code you just downloaded.

 You should be presented with this prompt: 

 `Admitted ratio for contour Bounding rectangle <1.6>:`

Press `Enter`, then select the curves.

 The result will be a closed Brep:
![img_10](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/WS_again_tutorial_6.png?raw=true)
<p style="text-align: center;"><font size="2"><i>The intended result of this tutorial: Closed breps approximating the segmented and cleaned point clouds</i></font></p> 
{: .fs-6 .fw-300 }

---

