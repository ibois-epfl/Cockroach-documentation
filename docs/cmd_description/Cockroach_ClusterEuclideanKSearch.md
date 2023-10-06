---
layout: default
title: Cockroach_ClusterEuclideanKSearch
parent: Cmd Description
---

# `Cockroach_ClusterEuclideanKSearch`
{: .no_toc }

![cockroach_reg](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/cmds/cmd_clustereuclideanksearch.gif?raw=true)

This command allows to cluster/seperate a cloud based on its spatial proximity. It will create a series of clouds that are spatially close to each other. The command will output a group of clouds.

The main algorithm is based on the *Connected Component Extractor* with a distance proximity evaluator from the function in [cilantro::ConnectedComponentExtraction3f()](https://github.com/kzampog/cilantro/blob/57ad1a397b73b6f4bbf9604fd75f8fe4363206a7/include/cilantro/clustering/connected_component_extraction.hpp#L23).

**Command options:**
```
NeighboursToSearch=30
```
{: .fs-6 .fw-300 }
The search for establishing which parts of the cloud can be considered as spatially close is based on the [KNNsearch](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) algorithm. This value is the number of neighbours for each point to evaluate. The bigger the value, the more accurate the algorithm will be but the slower it will be.

```
DistanceThreshold=0.02
```
{: .fs-6 .fw-300 }
This is the maximum distance between two points to be considered as spatially close.

```
MinClusterSize=30
```
{: .fs-6 .fw-300 }
The minimum number of points that a cluster should have to be considered as a cluster. The smaller the value, the more clusters will be detected.

```
ColorPointCloud=True
```
{: .fs-6 .fw-300 }
Decide with `True/False` whether to color the output group of clusters with random colors of keep the original colors.