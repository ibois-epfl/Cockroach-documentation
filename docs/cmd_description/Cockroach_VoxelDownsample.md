---
layout: default
title: Cockroach_VoxelDownsample
parent: Cmd Description
---

# `Cockroach_VoxelDownsample`
{: .no_toc }

![img_downsample](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/cmds/cockroach_voxeldownsample.jpg?raw=true)

Downsaample a pointcloud based on a grid with a given distance (a voxel grid). If two or more points are in the same voxel, only one point will be kept. This is a very fast way to downsample a pointcloud. The command will output a pointcloud that is the result of the downsampling. The result will have a regular appearance.

The main algorithm is based on the the function in [open3d::geometry::VoxelDownSample()](http://www.open3d.org/docs/0.7.0/cpp_api/_down_sample_8cpp.html).

**Command options:**
```
VoxelSize=0.01
```
{: .fs-6 .fw-300 }
This is the size of the voxel. The smaller the value, the more points will be removed.
