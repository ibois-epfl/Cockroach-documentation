---
layout: default
title: Cockroach_Downsample
parent: Cmd Description
---

# `Cockroach_Downsample`
{: .no_toc }

![img_downsample](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/cmds/cockroach_downsample.jpg?raw=true)

When you process pointclouds this is one of the very first type of operations you will do. The goal is to reduce the number of points in a pointcloud while keeping the overall shape of the pointcloud. This is done by removing points that are too close to each other.

**Command options:**
```
Downsample=5000
```
{: .fs-6 .fw-300 }
Set the target pointcloud size to 5000 points by default. The smaller the value, the more points will be removed.
