---
layout: default
title: Cockroach_ComputePointCloudNormals
parent: Cmd Description
---

# `Cockroach_ComputePointCloudNormals`
{: .no_toc }

![img_planesegmentation](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/cmds/cockroach_computepointcloudnormals.jpg?raw=true)

The command allors to compute the normals of any pointcloud. It is often useful to compute the normals of a pointcloud to be able to use other commands such as the `Cockroach_PlaneSegmentation`, other clustering techniques, or to **mesh** the pointcloud with `Cockroach_PoissonMesh`. Note that this command will not work if the pointcloud already has normals.

The command add normal to every point by calculating the axis of the best fit plane for the points around it. The normal is then the axis perpendicular to the plane. The algorithm used is rebased from [Open3D::EstimateNormals() function](http://www.open3d.org/docs/0.12.0/cpp_api/classopen3d_1_1geometry_1_1_point_cloud.html#a0eb1b6e14c8beb0073bded699b3c81a7). For more info on how the normals are estimated check out this [paper](https://www.cs.princeton.edu/~smr/papers/fasticp/fasticp.pdf) by Rusu et al. (2009).

**Command options:**
```
NormalsNeighbours=30
```
{: .fs-6 .fw-300 }
The value set the neighbours to test for the normal computation. The bigger the value, the more accurate the normal will be but the slower the algorithm will be. The default value 30 is a good compromise in most cases. If you have a very large pointcloud though you might want to decrease this value.

```