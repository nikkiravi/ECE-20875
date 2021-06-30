from cluster import *
from point import *

def kmeans(pointdata, clusterdata) :
    #Fill in
    
    #1. Make list of points using makePointList and pointdata
    points = makePointList(pointdata)

    #2. Make list of clusters using createClusters and clusterdata
    clusters = createClusters(clusterdata)

    #3. As long as points keep moving:
    move_cluster = -1
    while(move_cluster != 0):
        move_cluster = 0

        for p in points:
            centers = []

            for c in clusters:
                centers.append(c.center)

            closest = p.closest(centers)
            for c in clusters:
                if(c.center == closest):
                    if(p.moveToCluster(c) == True):
                        move_cluster += 1

            for c in clusters:
                c.updateCenter()

    
        #A. Move every point to its closest cluster (use Point.closest and
        #   Point.moveToCluster)
        #   Hint: keep track here whether any point changed clusters by
        #         seeing if any moveToCluster call returns "True"
        
        #B. Update the centers for each cluster (use Cluster.updateCenter)
            
    #4. Return the list of clusters, with the centers in their final positions
    return clusters
    
    
    
if __name__ == '__main__' :
    data = np.array([[0.5, 2.5], [0.3, 4.5], [-0.5, 3], [0, 1.2], [10, -5], [11, -4.5], [8, -3]], dtype=float)
    centers = np.array([[0, 0], [1, 1]], dtype=float)
    
    clusters = kmeans(data, centers)
    for c in clusters :
        c.printAllPoints()
