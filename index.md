---
layout: default
title: Home
nav_order: 1
description: "Just the Docs is a responsive Jekyll theme with built-in search that is easily customizable and hosted on GitHub Pages."
permalink: /
---

# Cockroach, point cloud and mesh processing library
{: .fs-9 }

Cockroach is an open-source project for making point cloud processing more accessible to designers and makers.
{: .fs-6 .fw-300 }

[Get started now](#getting-started){: .btn .btn-green .fs-5 .mb-4 .mb-md-0 .mr-2 } [View it on GitHub](https://github.com/9and3/Cockroach){: .btn .fs-5 .mb-4 .mb-md-0 } [View it on Food4Rhino](https://www.food4rhino.com/en/app/cockroach){: .btn .fs-5 .mb-4 .mb-md-0 } [Make a donation](https://en.wikipedia.org/wiki/Scrooge_McDuck){: .btn .btn-green .fs-5 .mb-4 .mb-md-0 }

---

## Getting started

### An umbrella library

Cockroach is a collection of the most interesting and useful point cloud and mesh functions from various libraries: [Open3D](http://www.open3d.org/), [Cilantro](https://github.com/kzampog/cilantro), [CGAL](https://www.cgal.org/), [PCL](https://pointclouds.org/). There are many libraries out there about point cloud (and mesh) processing, often one library is missing particular useful functions that another has. This way the development it's continuously stoped by adding, compiling, referencing and converting elements through different libraries. Cockroach lets you use all these libraries seamlessly all at once.

### Quick start: Use Cockroach as Rhinoceros® and Grasshopper

If you don't want to type one single line of code but you want all the functionalities and a nice user interface, we made Cockroach as a plug-in for [Rinoceros®](https://www.rhino3d.com/download/), a very versatile, simple and lean CAD program. We are also planning to add a standalone version of Cockroach, at least for Windows machines. [Go to the Rhino installation]({{ site.baseurl }}{% link docs/installation/Rhino-Plug-in-installation.md %}).
If you want to take it up a notch, you can also use Cockroach in Grasshopper, a visual scripting language shiped with Rhinoceros® 7.

<small>Cockroach is compatible with Rhinoceros 7 and Rhinoceros 6, preavious versions are not supported. [See the downloadable versions](https://www.rhino3d.com/download/)</small>

### Cockroach vanilla

If you are developer and you are familiar with C++ environment you can install Cockroach Vanilla flavour, the core version of the library. For now there are no wrappers for higher level languages such as Python but this is in our Roadmap. Follow the installation and configuration for the [C++ version].

- [See configuration options]({{ site.baseurl }}{% link docs/configuration.md %})

---

## About the project

2020-{{ "now" | date: "%Y" }} by [Petras Vestartas](https://github.com/petrasvestartas) and [Andrea Settimi](https://github.com/9and3).

### Acknowledgements

The laboratory for Timber Construction (IBOIS) at École Polytechnique Fédérale de Lausanne (EPFL) financially supports the authors contribution to the current researchof point cloud processing tools.

### License

Cockroach is distributed by an [LGPL-3.0 Licence](https://github.com/9and3/Cockroach/blob/Cockroach/LICENSE). Cockroach is released under LGPL. If you use Cockroach in published work, please also cite the third-party libraries we used: Open3D, CGAL, Open3D. The code is fully open, complying with CGAL (LGPL license). We encourage use for research purposes, as long as proper attribution is given. Feel free to send us an email and let us know how Cockroach has been useful to you and how it can be improved.

### Contributing

Cockroach is an open-source project and everybody is welcomed to constribute. When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change. We are more than welcoming in having contribution to Cockroach. We have also a Slack channel. Just send an email to [Petras Vestartas](petras.vestartas@epfl.ch) or [Andrea Settimi](andrea.settimi@epfl.ch).

Otherwise, you can always make a donation, via this [link(to be updated)](https://en.wikipedia.org/wiki/Scrooge_McDuck).

### Code of Conduct and Citation

Cockroach is committed to fostering a welcoming community interested in computer vision and computer graphics for AEC (and not only).To know more about our researches visit the [IBOIS official website](https://www.epfl.ch/labs/ibois/). Please use this citation if you use Cockroach in published work. Also, please also cite the third-party libraries we used: [Open3D](http://www.open3d.org/), [Cilantro](https://github.com/kzampog/cilantro), [CGAL](https://www.cgal.org/), [PCL](https://pointclouds.org/).

Bibitex citation:

```
 @misc{IBOIS2020,
    author = {Petras Vestartas and Andrea Settimi},
    title = {Cockroach: A plug-in for point cloud post-processing and meshing in Rhino environment},
    journal = {EPFL ENAC ICC IBOIS},
    url = {https://github.com/9and3/Cockroach},
    year = {2020} }
```
Citation (no Bibtex): 
```
Petras Vestartas and Andrea Settimi, Cockroach: A Plug-in for Point Cloud Post-Processing and Meshing in Rhino Environment, EPFL ENAC ICC IBOIS, 2020, https://github.com/9and3/Cockroach.
```