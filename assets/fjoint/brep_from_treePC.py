"""Author: Joseph Tannous, PhD student IBOIS EPFL
This small piece of code was made in the context of a workshop given at IBOIS (directed by dr. Agathe Mignon and Prof. Yves Weinand).
"""
import Rhino
import rhinoscriptsyntax as sc
import scriptcontext as scr
import Rhino.Geometry as rg
from System.Collections.Generic import List


crvs = []
bboxes = []
centers = []
circles = []
points = []


def skeleton():
    #Gets two inputs: 
    #The ratio, a parameter that checks if all the cross-sections that are given are somewhat similar.
        #if one cross-section is much larger than the next one, the cross-section is skipped. (see line 40-43)
    #The cross sections, as closed curves.
    
    input_ratio = sc.GetReal("Admitted ratio for contour Bounding rectangle", 1.6)
    input_crvs = sc.GetObjects("Pick set of curves" , sc.filter.curve , True , True)
    if not input_crvs: return
    
    for crv in input_crvs:
        crvs.append(sc.coercegeometry(crv))
    #Now we create bounding boxes of the cross sections, and check the ratio
    for crv in crvs:
        bboxes.append(crv.GetBoundingBox(rg.Plane.WorldXY))

    for bbox in bboxes:
        lines = bbox.GetEdges()
        line = lines[:2]
        ratio = line[0].Length / line[1].Length
        
        #Now, for the valid cross-sections, we simplify them to fitted circles.
        
        if ratio > 1/input_ratio and ratio < input_ratio:
            centers.append(bbox.Center)
            circles.append(rg.Circle(bbox.Center, (line[0].Length + line[1].Length)/4).ToNurbsCurve())
    for c in centers:
        points.append(c.Z)
    
    comb=zip(points,circles)
    comb.sort() #sorts by first element, i.e. points
    points_sorted,circles_sorted=zip(*comb)
    
    #At last we loft and output the circles
    
    loft_result = rg.Brep.CreateFromLoft(circles_sorted,rg.Point3d.Unset,rg.Point3d.Unset,rg.LoftType.Tight,False)
    capped = loft_result[-1].CapPlanarHoles(0.0001)
    scr.doc.Objects.AddBrep(capped)
    
    sc.EnableRedraw(enable=False)


if __name__ == "__main__":
    skeleton()
