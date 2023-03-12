import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from FileReader import FileReader
from Clusters import Clusters
from threadwrapper import ThreadWrapper
from tkinter import messagebox
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)


class Form:
    def __init__(self):
        self.data = FileReader.read_file('s1.txt')

        # Defining threads
        self.t1 = ThreadWrapper(target=Clusters.kmeans, args=(self.data,))
        self.t2 = ThreadWrapper(target=Clusters.affinity_propagation, args=(self.data,))
        self.t3 = ThreadWrapper(target=Clusters.mean_shift, args=(self.data,))
        self.t4 = ThreadWrapper(target=Clusters.agglomerative_clustering, args=(self.data,))
        self.t5 = ThreadWrapper(target=Clusters.dbscan, args=(self.data,))

        self.t1.start()
        self.t2.start()
        self.t3.start()
        self.t4.start()
        self.t5.start()

        self.fig, self.axs = plt.subplots()
        self.fig.subplots_adjust(bottom=0.2)

        # Axes for buttons
        kmeans_ax = self.fig.add_axes([0.01, 0.05, 0.1, 0.05])
        affinity_propagation_ax = self.fig.add_axes([0.12, 0.05, 0.25, 0.05])
        mean_shift_ax = self.fig.add_axes([0.38, 0.05, 0.12, 0.05])
        agglomerative_clustering_ax = self.fig.add_axes([0.51, 0.05, 0.30, 0.05])
        dbscan_ax = self.fig.add_axes([0.82, 0.05, 0.17, 0.05])

        # Buttons
        b_kmeans = Button(kmeans_ax, 'K-means')
        b_affinity_propagation = Button(affinity_propagation_ax, 'Affinity Propagation')
        b_mean_shift = Button(mean_shift_ax, 'Mean Shift')
        b_agglomerative_clustering = Button(agglomerative_clustering_ax, 'Agglomerative Clustering')
        b_dbscan = Button(dbscan_ax, 'DBSCAN')

        # OnClickButtons
        b_kmeans.on_clicked(self.kmeans_on_click)
        b_affinity_propagation.on_clicked(self.affinity_propagation_on_click)
        b_mean_shift.on_clicked(self.mean_shift_on_click)
        b_agglomerative_clustering.on_clicked(self.agglomerative_clustering_on_click)
        b_dbscan.on_clicked(self.dbscan_on_click)

        self.axs.clear()

        plt.show()

    def kmeans_on_click(self, event):
        try:
            affiliation = self.t1.join()

            self.axs.clear()
            self.axs.set_title("K-means")
            self.axs.scatter(self.data[:, 0], self.data[:, 1], 1, c=affiliation, cmap='Spectral')
        except Exception as ex:
            messagebox.showinfo("Error", ex)

    def affinity_propagation_on_click(self, event):
        try:
            affiliation = self.t2.join()

            self.axs.clear()
            self.axs.set_title("AffinityPropagation")
            self.axs.scatter(self.data[:, 0], self.data[:, 1], 1, c=affiliation, cmap='nipy_spectral')
        except Exception as ex:
            messagebox.showinfo("Error", ex)

    def mean_shift_on_click(self, event):
        try:
            affiliation = self.t3.join()

            self.axs.clear()
            self.axs.set_title("MeanShift")
            self.axs.scatter(self.data[:, 0], self.data[:, 1], 1, c=affiliation, cmap='rainbow')
        except Exception as ex:
            messagebox.showinfo("Error", ex)

    def agglomerative_clustering_on_click(self, event):
        try:
            affiliation = self.t4.join()

            self.axs.clear()
            self.axs.set_title("AgglomerativeClustering")
            self.axs.scatter(self.data[:, 0], self.data[:, 1], 1, c=affiliation, cmap='twilight_shifted')
        except Exception as ex:
            messagebox.showinfo("Error", ex)

    def dbscan_on_click(self, event):
        try:
            affiliation = self.t5.join()

            self.axs.clear()
            self.axs.set_title("DBSCAN")
            self.axs.scatter(self.data[:, 0], self.data[:, 1], 1, c=affiliation, cmap='Accent')
        except Exception as ex:
            messagebox.showinfo("Error", ex)


form = Form()
