---
layout: default
title: Cockroach_SubstractCloud
parent: Cmd Description
---

# `Cockroach_SubstractCloud`
{: .no_toc }

![cockroach_connectedcomponent](https://github.com/ibois-epfl/Cockroach-documentation/blob/docu-alpha/img/cmds/cockroach_substractcloud.jpg?raw=true)

The command will substract a cloud from another cloud. The command will output a cloud that is the result of the substraction of the two input clouds. The clouds can have a different number of points. Select first a *cutter* cloud and then a *to be cut* cloud. The *cutter* cloud will do a radius search for each of its points on the other *to be cut* cloud. If the distance between the two points is smaller than the `RadiusSearch` value, the point will be removed from the *to be cut* cloud.

**Command options:**
```
RadiusSearch=0.003
```
{: .fs-6 .fw-300 }
The radius of the search for each point of the *cutter* cloud. The bigger the value the more rough the substraction will be.