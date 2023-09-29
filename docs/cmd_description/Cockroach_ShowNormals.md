---
layout: default
title: Cockroach_ShowNormals
parent: Cmd Description
---

# `Cockroach_ShowNormals`
{: .no_toc }

![img_planesegmentation](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/cmds/cockroach_shownormals.jpg?raw=true)

This command will display the normals of the pointcloud as colored (based on direction) Rhino line objects. Note that it requires the point cloud to have normals (if it is not the case try to run the `Cockroach_ComputePointCloudNormals`). It is often useful to display the normals of a pointcloud to check if the normals are correctly placed in the right direction.

**Command options:**
```
ShowNormalsEveryN=3
```
{: .fs-6 .fw-300 }
Display the normal every e.g. 3 points. If you have a large pointcloud you probably do not need to show all the normals but just few.

```
LengthNormalFactor=0.2
```
{: .fs-6 .fw-300 }
This is the length of the lines signifying the normals. The bigger the value, the longer the lines will be.