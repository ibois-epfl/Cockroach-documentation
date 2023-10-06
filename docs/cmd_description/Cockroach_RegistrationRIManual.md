---
layout: default
title: Cockroach_RegistrationRIManual
parent: Cmd Description
---

# `Cockroach_RegistrationRIManual`
{: .no_toc }

![cockroach_reg](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/cmds/cockroach_registrationrimanual.jpg?raw=true)

This command stich two clouds together.
This is also called a *registration* or *alignement* of two point clouds. To be working correctly the two clouds should share app. 1/3 of their points. The command will output a cloud that is the result of the registration of the two input clouds.
Note that this is a *supervised* algorithm, meaning that you will need to press `Space` to repeat the algorithm. The algorithm will stop when you decide after each step to stop. Besides visual clous of a good point cloud match, you can also check the log output in the terminal. This is what you will see:
```
-------------------------0 / 21-------------  👈 the number of iterations
Registration RI took: 0.0971272 seconds  👈 the time it took to compute the registration
Registration fitness result: 0.464567  👈 fitness is how well the two clouds match
Registration RMSE result: 0.0108833  👈 the RMSE is the distance between the two clouds
```
For the *fitness* values: the closer to `1` the better the match. For the *RMSE* values: the smaller the better the match.

![cockroach_reg_demo](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/cmds/cmd_registrationrimanual_demo.gif?raw=true)

 <font size="2"><i> The rhino command will show you the red as the source cloud and green as the target cloud. At each iteration you can decide to stop or continue untill satisfied with the result. For example of application check out this <a href="http://localhost:4000/Cockroach-documentation/docs/tutorials/digital-twin-of-masonry-stone-wall-c/#register-stones-into-the-wall-layer" >digital-twin-masonry-tutorial</a>. </i></font>

The function is an iterative loop based on the registration algorithms from Open3d [`open3d::pipelines::registration::RegistrationRANSACBasedOnFeatureMatching`](http://www.open3d.org/html/cpp_api/namespaceopen3d_1_1pipelines_1_1registration.html), and ICP (Point to plane), [`open3d::pipelines::registration::RegistrationICP`](http://www.open3d.org/html/cpp_api/namespaceopen3d_1_1pipelines_1_1registration.htmll) combined.


> 🔎 There is also a command version full authomatic `Cockroach_RegistrationRI`. But we reccomand to use this manual one since you can stop the stiching process whenever you want.


**Command options:**
```
VoxelSize=0.005
```
{: .fs-6 .fw-300 }
When we perform the registration we are not performing the algorithm on the full resolution point cloud, but on a downsampled one. The computed rigid transformation will be applied to the full resolution though. If the  cloud is already downsampled, set this value to `0`.

```
NnumberRepetion=20
```
{: .fs-6 .fw-300 }
It's the number of total repetitions of the registration algorithm. 

```
ColorPointCloud=False
```
{: .fs-6 .fw-300 }
Whether to color the output cloud with random colors or keep the original colors.