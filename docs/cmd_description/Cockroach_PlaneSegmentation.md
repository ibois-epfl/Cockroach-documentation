---
layout: default
title: Cockroach_PlaneSegmentation
parent: Cmd Description
---

# `Cockroach_PlaneSegmentation`
{: .no_toc }

![img_planesegmentation](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/cmds/cockroach_planesegmentation.jpg?raw=true)

It is often useful to segment a pointcloud into different planes. This command will segment a pointcloud into the biggest detected plane and the remaining pointcloud. The biggest plane is the plane that contains the most points with similar normals. Note that since this algorithm is based on the RANSAC algorithm, the result might not be the same every time you run the command. Also it requires the point cloud to have normals, if absent, it will compute them automatically.

**Command options:**
```
DistanceThreshold=0.01
```
{: .fs-6 .fw-300 }
This is the maximum distance between a point and a plane to be considered as part of the plane. The smaller the value, the more points will be considered as part of the plane.

```
RANSACValue=3
```
{: .fs-6 .fw-300 }
The plane detection algorithm is based on the RANSAC algorithm. This value is the number of points that will be used to compute the plane. The smaller the value, the faster the algorithm will be but the less accurate it will be.

```
Iterations=1000
```
{: .fs-6 .fw-300 }
This is the number of iterations that will be done by the RANSAC algorithm. The bigger the value, the more accurate the algorithm will be but the slower it will be.
