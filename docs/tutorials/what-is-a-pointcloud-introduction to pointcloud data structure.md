---
layout: default
title: What is a pointcloud
parent: Tutorial
nav_order: 1
---

# What is a pointcloud - Introduction to pointcloud data structure
{: .no_toc }

<br />

Author: [andrea.settimi@epfl.ch](andrea.settimi@epfl.ch)

This post introduces the concept of pointcloud and its properties. It is meant to be a starting point for users that are not familiar with the concept of pointcloud.
We are quickly going through the basics and introduce a generic data structure of a point cloud and the most common format files used to store its information.

{: .fs-6 .fw-300 }



![img_downsample](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/whatispcd/ptvideo_intro.gif?raw=true)
 <font size="2"><i>A point cloud of a forest in Rossinière, Switzerland. IBOIS@EPFL(2018), point cloud captured, processed and animated by Petras Vestartas, for more info visit the research page of the IBOIS research on  <a href="https://www.epfl.ch/labs/ibois/research/ongoingresearch/non-standard-timber-elements/" >"Woodworking Joints and Assembly Methods for Locally Sawn SOlid Timber Elements in Free-form Structures".</a>. </i></font>

---

![](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/photocloud.png?raw=true)

## 0 What is a point cloud?

Point clouds represent the shape and characteristics of a physical object or environment by a collection of data points in three dimensions. 
This object can be anything, at any scale.

## 1 Point cloud properties
Here we are going to list only 3 of the most common and used properties of a point cloud.
### 1.1 Space Coordinates
A point cloud is nothing than a set of data points in space with properties. The most used property of a point in a point cloud is its `position` or `coordinates` and it is very convinient to store a very precise space information.

```
Point = [x, y, z]
```
{: .fs-6 .fw-300 }

### 1.2 Color
A point cloud can also have `colors`. This value is also in a 3-value vector just as the position. The color is usually stored in the RGB format, where each value is a number between 0 and 255. This is the same format used to store colors in images. Colors in images could also represent the [`reflectivity value`](https://en.wikipedia.org/wiki/Reflectance) if the point cloud was captured by a e.g. LiDAR sensor ([for more info about sensors](https://ibois-epfl.github.io/Cockroach-documentation/docs/tutorials/a-guide-to-3D-sensors/)).

```
Point = [R, G, B]
```
{: .fs-6 .fw-300 }

### 1.3 Normal
A point cloud can also have `normals`. This value is also in a 3-value vector just as the position and color. The normal is a vector that is perpendicular to the surface of the object. This value is very useful for many algorithms that require the knowledge of the surface orientation. For example, the normal can be used to compute the curvature of the surface. For more info visit our description of the command [`Cockroach_ComputePointCloudNormals`](http://localhost:4000/Cockroach-documentation/docs/cmd_description/Cockroach_ComputePointCloudNormals/).

```
Point = [Nx, Ny, Nz]
```
{: .fs-6 .fw-300 }

## 2 Point cloud data structure
The simplest data structure of a point cloud is a **Raw Point List**. This is an unorganized list of points carrying each some properties. This data structure is very simple and easy to understand. It is also very easy to implement and to use. However, it is not very efficient in terms of memory and computational time. This is because the points are not organized in any way. This means that if we want to access a point we need to go through the whole list and check if the point is the one we are looking for. This is why it exists other more advanced way to store point clouds such as [Voxel Grid](https://en.wikipedia.org/wiki/Voxel) or [Octree](https://en.wikipedia.org/wiki/Octree) or [Kd-tree](https://en.wikipedia.org/wiki/K-d_tree).
Let's go back to our **Raw Point List**..

If we consider a point that has location, color and normals:
```
Point = [[x, y, z],
         [R, G, B],
         [Nx, Ny, Nz]]
```
{: .fs-6 .fw-300 }

Now, as we said our point cloud can ba a list of points:
```
Point Cloud = [Point1, Point2, Point3, ...]
```
{: .fs-6 .fw-300 }

Here you go, you have a point cloud 🌩️ !

## 3 Point cloud file formats
How do we store point clouds? 
There are many ways to do so. The most common way is to store them in a file. There are many file formats that can be used to store point clouds. The most common are:
* [PLY](https://en.wikipedia.org/wiki/PLY_(file_format))
* [XYZ](https://en.wikipedia.org/wiki/XYZ_file_format)
* [E57](https://en.wikipedia.org/wiki/E57_format)
* [LAS](https://en.wikipedia.org/wiki/LAS_file_format)
* [PTS](https://en.wikipedia.org/wiki/PTS_file_format)
* [PCD](https://en.wikipedia.org/wiki/Point_Cloud_Library)
* [OBJ](https://en.wikipedia.org/wiki/Wavefront_.obj_file)

In general, a point cloud can be written to these files in two ways:
* **ASCII**: the point cloud is written in a human-readable format. This means that the file can be opened with a text editor and the content can be read. This is very useful for debugging and for small point clouds. However, this format is not very efficient in terms of memory and computational time. This is because the file is written in a human-readable format and this means that the file size is bigger than the binary format. This is why it is not recommended to use this format for big point clouds.

```
# .xyz example
0.9375 0.9375 0.9375 10 255 255
0.9375 0.9375 0.9675 255 5 255
0.9375 0.9245 0.9375 255 255 255
0.9375 0.9375 0.9775 5 255 255
```

* **Binary**: the point cloud is written in a binary format. This means that the file cannot be read as text. This is very useful for big point clouds. This is because the file is written in a binary format and this means that the file size is smaller than the ASCII format, thus easier for the machine to read. This is why it is recommended to use this format for big point clouds.

## 4 Next steps
Now that you know what is a point cloud and how it is structured, you can start to play with it. You can start by downloading a point cloud from the internet and open it with a text editor. You can also try to open it with Rhino, visualize it and use [`Cockroach`](http://localhost:4000/Cockroach-documentation/docs/installation/rhino-installation/).

If you want to know more about point clouds and why we created Cockroach, have a look at our ![paper](https://papers.cumincad.org/cgi-bin/works/paper/caadria2022_215).