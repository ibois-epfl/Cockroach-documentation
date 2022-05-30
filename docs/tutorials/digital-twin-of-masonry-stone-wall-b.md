---
layout: default
title: Digital twin of masonry stone wall (Rhino) - b
parent: Tutorial
nav_order: 2
---

# Digital twin of masonry stone wall (Rhino) - Layers allignment
{: .no_toc }

<br />

For more info: [andrea.settimi@epfl.ch](andrea.settimi@epfl.ch)

This tutorial has been realized by IBOIS by the collaboration with the laboratory EESD (PI: [savvas.saloustros@epfl.ch](savvas.saloustros@epfl.ch)) in a joint effort of digitzing a masonry wall. The goal of this tutorial series is to help users to reconstruct step by step the process of post-processing cleaning, segmentation, and reconstruction of scanned point cloud data to reconstruct a twin digital wall of a physical masonry artifact.

The tutorial is divided in 3 parts **(a,b,c)**. The first part **(a)** illustrates how to digitize and build a stone data set, the second **(b)** shows how to reallign multiple scans into the same coordinate system and finally **(c)** we relocate the stone model into the wall landscape.

![layerrec](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/layer_reconstruction.gif?raw=true)
 <center><font size="2"><i> The objective of the tutorial is to show how to bring all the scans into the same coordinate system. </i></font></center>

{: .fs-6 .fw-300 }

---

## Scanning of wall layers

This second section of the tutorial illustrates how to allign all the scans of the wall layers to the same coordinate system.

During the fabrication of the wall, each layer needs to be digitized. It is often the case that, independently from the scanning technique you are using, scans will be offset one to another. Our goal here is to re-align all the scanss to the same coordinate system in order to reconstruct a wall layer by layer. To help in this task we are going to use fiducial markers which have been designed to be detected in any point cloud, independently from the hardware employed to obtain it.

![markerone](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/snapper111.PNG?raw=true)
![markertwo](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/snapper222.PNG?raw=true)
 <center><font size="2"><i> Figure 1: manual cleaning of the point cloud. </i></font></center>

Be sure to include the markers in the field of view during the scanning: they need to be present in the scan.

---

## Cleaning of point cloud layers

First we need to clean the part of the point cloud that we don't need and occupy needless memory. We need to keep the markers and the walls. What is underneath, we erase it. You can move your camera view to a lateral position where you can have a nice selection of the portion we want to delete. 

To select, press `Ctrl + Alt` while dragging a selection with your left mouse button. See the image below to see the type of selection we need to clean. Next, you just click `delete` or `erase space`.

![layerwallone](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/layer_1.PNG?raw=true)
 <center><font size="2"><i> Figure 1: manual cleaning of the point cloud. </i></font></center>

 Now we need to divide each scan in 2 portions. 

* The two parts containing the circle markers
* The central part containing the wall

To do so we are going first to draw a box with command:
```Terminal
Box
```
Place the box in a way to contain the central part of the wall. 

Then, type the following in the command bar of Rhino:
```Terminal
Cockroach_crop
```
Select first the point cloud and then the box, at that's it we divided the cloud in two parts. This is what it should like once you finished with the command. Now you can either delete the box or move it to the next cloud to repeat the same procedure.

![croplayer](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/croping_layer.gif?raw=true)
 <center><font size="2"><i> Figure 2: The scene is divided into two parts: the central wall and the fiducial marker two areas. </i></font></center>

---

## Marker detection


---

![layerrec](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/layer_reconstruction.gif?raw=true)