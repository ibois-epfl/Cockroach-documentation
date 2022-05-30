---
layout: default
title: Digital twin of masonry stone wall (Rhino) - c
parent: Tutorial
nav_order: 3
---

# Digital twin of masonry stone wall (Rhino) - Wall reconstruction
{: .no_toc }

<br />

For more info: [andrea.settimi@epfl.ch](andrea.settimi@epfl.ch)

This tutorial has been realized by IBOIS by the collaboration with the laboratory EESD (PI: [savvas.saloustros@epfl.ch](savvas.saloustros@epfl.ch)) in a joint effort of digitzing a masonry wall. The goal of this tutorial series is to help users to reconstruct step by step the process of post-processing cleaning, segmentation, and reconstruction of scanned point cloud data to reconstruct a twin digital wall of a physical masonry artifact.

The tutorial is divided in 3 parts **(a,b,c)**. The first part **(a)** illustrates how to digitize and build a stone data set, the second **(b)** shows how to reallign multiple scans into the same coordinate system and finally **(c)** we relocate the stone model into the wall landscape.

💬 To be able to reproduce these tutorials you will need the *WIP* version of Cockroach. Download Cockroach from [food4rhino](https://www.food4rhino.com/en/app/cockroach) and replace the `.rhp` file with this [one here](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/assets/fjoint/Cockroach.rhp). This version will be soon stable and released.

![wallrec](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/wall_reconstruct.gif?raw=true)
 <font size="2"><i> The objective of the tutorial is to show how identify each stone's pose within the each wall layer. </i></font>

{: .fs-6 .fw-300 }

---

## Prepare the wall layer cloud before registration

The objective here is to relocate each point cloud of the stones' data set into each wall layer.

We probably do not need the full resolution of the wall layer, so first thing let's reduce the point cloud with `Cockroach_VoxelDownsample` (VoxelSize=0.003). Keep the full-res cloud in a seperate layer and hide the layer. We need to be sure that the layer is ready for the stone registration. To do this we need to estimate normals of the cloud layer with the command `Cockroach_ComputePointCloudNormals`. This might take a bit of time, let it work.

---

## Register stones into the wall layer

Here we apply the same procedures for the registration of the stone dataset. Try to import a stone belonging to the layer and run `Cockroach_RegistrationRIManual`. If it works amazing, you're done for this step.

![regrimanual](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/registration_ri.gif?raw=true)
 <font size="2"><i> Figure 1: the supervised registration to relocate the rock in the wall scene. </i></font>

Now, `Cockroach_RegistrationRIManual` is under development and needs to be more robust. If it does not work go for the troubleshooting: the supervised manual placing. You move the rock with the gumball, approximate a position and run the `Cockroach_RegistrationICPPtPl`. This should refine its position.

---

## Remove the points of the placed rock from the wall layer scene

Now that the rock is placed we need to remove its corresponding points in the wall layer. To do so we use `Cockroach_SubstractCloud` (RadiusSearch=0.01) which removes close points to the one of the newly registered stone. Before running the previous command copy the stone (`Ctrl + C`), you will need to re-paste it once the command is done (`Ctrl + V`).

![removecloud](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/remove_cloud.gif?raw=true)
 <font size="2"><i> Figure 2: the removal of the point in the correspondence of the reconstructed stone. </i></font>

---

## Remove the points of the placed rock from the wall layer scene

when you will go up in reconstructing the wall it might help the registration if you make a copy of the scan. **First** execute the first part of this section and **then**, delete the lower part which is not presenting new stones. This will reduce the number of possible combinations for the registration algorithms.

![erasecloud](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/chop_if_needed.gif?raw=true)
 <font size="2"><i> Figure 3: Do not run registration algorithms on the entirety of the point cloud. The less points are fed the better performance you will obtain. </i></font>

---

![wallrec](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/wall_reconstruct.gif?raw=true)