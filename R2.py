def set_lim_2d(ax, vector):
    x, y = vector 
    aux = 1
        
    start_x, end_x = (x-aux, -x+aux) if x < 0 else  (-x-aux, x+aux)
    start_y, end_y = (y-aux, -y+aux) if y < 0 else  (-y-aux, y+aux)
    
    ax.set_xlim(start_x,end_x)
    ax.set_ylim(start_y,end_y)

def set_label_2d(ax):
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('R2')

def add_cartesian_2d(ax):
    x_lim = ax.get_xlim()
    y_lim = ax.get_ylim()
    
    #plot eixos cartesianos
    ax.plot(x_lim, (0,0), color='black')
    ax.plot((0,0), y_lim, color='black')

def add_annotations_2d(ax, vector):
    
    x,y = vector
    
    ax.scatter(x,0, c='b', label=f'x: ( {x:.2f}, 0.0 )'  )
    ax.scatter(0,y, c='g', label=f'y: ( 0.0, {y:.2f} )')
    
    ax.plot((x,x), (0,y), 'b--')
    ax.plot((0,x), (y,y), 'g--')
    
    ax.legend()

def plot_vector_2d(ax, vector):
    x, y = vector
    
    ax.plot((0,x), (0,y), c='c')
    ax.scatter(0,0, c='c')
    ax.scatter(x,y, c='c')

