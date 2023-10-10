---
layout: default
title: Cockroach_RemoveStatisticalOutliers
parent: Cmd Description
---

# `Cockroach_RemoveStatisticalOutliers`
{: .no_toc }

![img_downsample](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/cmds/cockroach_removestatisticaloutlier.jpg
?raw=true)

This command removes the statistical outliers from a point cloud. It means that it removes the points that are too far away from the average distance of the point cloud. [`Outliers`](https://en.wikipedia.org/wiki/Outlier) are those points can be considered as noise or errors in the point cloud. This command is very useful to clean up a point cloud before processing it.


THe function is implemented from [`Open3D::RemoveStatisticalOutliers()`](http://www.open3d.org/docs/0.6.0/cpp_api/namespaceopen3d_1_1geometry.html#add56e2ec673de3b9289a25095763af6d).

**Command options:**
```
Neighbours=200
```
{: .fs-6 .fw-300 }
It corresponds to the number of points to calculate the standard deviation distance between points to point.

```
Ratio=1.9
```
{: .fs-6 .fw-300 }
This is the threshold based on the stadard deviation of the mean distances among the entire point cloud. The lower, the more aggressive.

