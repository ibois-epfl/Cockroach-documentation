---
layout: default
title: Digital twin of masonry stone wall - a
parent: Tutorial
nav_order: 1
---

# Digital twin of masonry stone wall
{: .no_toc }

<br />

For more info: [andrea.settimi@epfl.ch](andrea.settimi@epfl.ch)

This tutorial has been realized by IBOIS by the collaboration with the laboratory EESD (PI: [savvas.saloustros@epfl.ch](savvas.saloustros@epfl.ch)) in a joint effort of digitzing a masonry wall. The goal of this tutorial series is to help users to reconstruct step by step the process of post-processing cleaning, segmentation, and reconstruction of scanned point cloud data to reconstruct a twin digital wall of a physical masonry artifact.

The tutorial is divided in 3 parts **(a,b,c)**. The first part **(a)** illustrates how to digitize and build a stone data set, the second **(b)** shows how to reallign multiple scans into the same coordinate system and finally **(c)** we relocate the stone model into the wall landscape.

{: .fs-6 .fw-300 }

---

This first section of the tutorial illustrates how to digitize and build a catalog of irregular geometries with Cockroach.

Stones need to be scanned on both sides and labeled if necessary for the reconstruction. See the image below:

![stonestablescanning](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/Stone_scanning_distribution_D.jpg?raw=true)
 <center><font size="2"><i> Figure 1: photo of one side of the stone batch. RAD markers are just specific to the laser scanning technique employed in our case but are not necessary. </i></font></center>

---

Open a Rhinoceros 7 new file and be sure that the unit system is set to meter as measurement unit. To do so type `Option` on the `Rhino Shell` and click `enter`, go to section `unit` and select `meter`. Now we can import the output point cloud fro mthe scanner as a format .e57. It is enough to drag and drop the file into Rhino worksapce canvas. On the option prompt select import and wait for the downloading, it might take a while. Now we have imported our "raw" point cloud. As you can see, we need first to clean the raw point cloud. Let's tackle this point first.

![stonebatchone](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/stone_batch_1.PNG?raw=true)
 <center><font size="2"><i> Figure 2: A raw point cloud of one side of the batch. </i></font></center>






```python
print()
```