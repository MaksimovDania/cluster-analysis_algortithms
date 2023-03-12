from sklearn.cluster import KMeans, AffinityPropagation, MeanShift, AgglomerativeClustering, estimate_bandwidth, DBSCAN


class Clusters:
    @staticmethod
    def kmeans(data):
        kmeans = KMeans(n_clusters=15)
        kmeans.fit(data)
        return kmeans.labels_

    @staticmethod
    def affinity_propagation(data):
        affinity_propagation = AffinityPropagation()
        affinity_propagation.fit(data)
        return affinity_propagation.labels_

    @staticmethod
    def mean_shift(data):
        mean_shift =  MeanShift(bandwidth=estimate_bandwidth(data, quantile=0.2))
        mean_shift.fit(data)
        return mean_shift.labels_

    @staticmethod
    def agglomerative_clustering(data):
        agglomerative_clustering = AgglomerativeClustering(n_clusters=15)
        agglomerative_clustering.fit(data)
        return agglomerative_clustering.labels_

    @staticmethod
    def dbscan(data):
        dbscan = DBSCAN(eps=35000, min_samples=50)
        dbscan.fit(data)
        return dbscan.labels_
