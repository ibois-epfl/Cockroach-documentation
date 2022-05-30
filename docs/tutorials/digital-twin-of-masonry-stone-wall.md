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

Stones need to be scanned on both sides and labeled if necessary for the reconstruction. See the iamge below:

![stonestablescanning](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/Stone_scanning_distribution_D.jpg?raw=true)

Open a Rhinoceros 7 new file and be sure that the unit system is set to meter as measurement unit. To do so type `Option` on the `Rhino Shell` and click `enter`, go to section `unit` and select `meter`.




```python
print()
```