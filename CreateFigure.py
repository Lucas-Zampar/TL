from R2 import *
from R3 import *

import matplotlib.pyplot as plt

def create_figure(vector3d, vector2d):    
    fig = plt.figure(figsize=(10, 5));
    ax3d = fig.add_subplot(121, projection='3d')
    ax2d = fig.add_subplot(122)
    
    octante = define_octante(vector3d)
    
    set_lim_3d(ax3d, vector3d, octante)
    set_label_3d(ax3d)
    add_cartesian_3d(ax3d)
    add_annotations_3d(ax3d, vector3d)
    plot_vector_3d(ax3d, vector3d)

    set_lim_2d(ax2d, vector2d)
    set_label_2d(ax2d)
    add_annotations_2d(ax2d, vector2d)
    add_cartesian_2d(ax2d)
    plot_vector_2d(ax2d, vector2d)
    return fig 