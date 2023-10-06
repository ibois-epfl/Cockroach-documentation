---
layout: default
title: Cockroach_ClusterConnectedComponentRadius
parent: Cmd Description
---

# `Cockroach_ClusterConnectedComponentRadius`
{: .no_toc }

![cockroach_connectedcomponent](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/cmds/cockroach_connectedcomponent.jpg?raw=true)

This command allows to segment your cloud based on its normals. It will segment the cloud into clusters of points that have similar normals. The command will output a cloud for each cluster. Note that the cloud needs to have normals prior to the command. If absent, they will be computed automatically. This can be particularly useful to segment a cloud into different planes. It is particularly efficient with clouds/shapes that have sharp corners that can be detected by the normals as a clear change in direction.

The main algorithm is based on the *Connected Component Extractor* with a normal proximity evaluator from the function in [cilantro::ConnectedComponentExtraction3f](https://github.com/kzampog/cilantro/blob/57ad1a397b73b6f4bbf9604fd75f8fe4363206a7/include/cilantro/clustering/connected_component_extraction.hpp#L23).

**Command options:**
```
VoxelSizeSearch=0.1
```
{: .fs-6 .fw-300 }
This is the size of the voxel grid that will be used to search for neighbors. The smaller the value, the more accurate the algorithm will be but the slower it will be.

```
NormalThresholdDegree=2
```
{: .fs-6 .fw-300 }
This is the maximum angle between two normals to be considered as similar. The smaller the value, the more accurate the algorithm will be but the slower it will be.

```
MinClusterSize=100
```
{: .fs-6 .fw-300 }
The minimum number of points that a cluster should have to be considered as a cluster. The smaller the value, the more clusters will be detected.

```
ColorPointCloud=True
```
{: .fs-6 .fw-300 }
Whether to color the output group of clusters with random colors of keep the original colors.