def define_octante(vector):
    
    x, y, z = vector 
    
    if x>=0 and y>=0 and z>=0:
        return 1 #(+,+,+)
    
    if x>=0 and y>=0 and z<0:
        return 2 #(+,+,-)
    
    if x>=0 and y<0 and z>=0:
        return 3 #(+,-,+)
    
    if x>=0 and y<0 and z<0:
        return 4 #(+,-,-)
    
    if x<0 and y>=0 and z>=0:
        return 5 #(-,+,+)
    
    if x<0 and y>=0 and z<0:
        return 6 #(-,+,-)
    
    if x<0 and y<0 and z>=0:
        return 7 #(-,-,+)
    
    if x<0 and y<0 and z<0:
        return 8 #(-,-,-)

def set_lim_3d(ax, vector, octante):
    
    x, y, z = vector
    aux = 1
    
    if octante == 1: 
        start_x, start_y, start_z = (0,0,0)
        end_x, end_y, end_z = (x+aux, y+aux, z+aux)
        ax.view_init(20,60)
    
    if octante == 2: 
        start_x, start_y, start_z = (0,0,z-aux)
        end_x, end_y, end_z = (x+aux, y+aux, 0)
        ax.view_init(20,60)
        
    if octante == 3: 
        start_x, start_y, start_z = (0,y-aux,0)
        end_x, end_y, end_z = (x+aux, 0, z+aux)
        ax.view_init(20,-60)
    
    if octante == 4: 
        start_x, start_y, start_z = (0,y-aux,z-aux)
        end_x, end_y, end_z = (x+aux, 0, 0)
        ax.view_init(20,-60)
        
    if octante == 5:
        start_x, start_y, start_z = (x-aux,0,0)
        end_x, end_y, end_z = (0, y+aux, z+aux)
        ax.view_init(20,120)
    
    if octante == 6:
        start_x, start_y, start_z = (x-aux,0,z-aux)
        end_x, end_y, end_z = (0, y+aux,0)
        ax.view_init(20,120)
        
    if octante == 7:
        start_x, start_y, start_z = (x-aux,y-aux,0)
        end_x, end_y, end_z = (0, 0,z+aux)
        ax.view_init(20,-120)
    
    if octante == 8:
        start_x, start_y, start_z = (x-aux,y-aux,z-aux)
        end_x, end_y, end_z = (0, 0, 0)
        ax.view_init(20,-120)
    
    
        
    ax.set_xlim(start_x, end_x)
    ax.set_ylim(start_y, end_y)
    ax.set_zlim(start_z, end_z)

def set_label_3d(ax):
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('R3')

def add_cartesian_3d(ax):
    x_lim = ax.get_xlim()
    y_lim = ax.get_ylim()
    z_lim = ax.get_zlim()
    
    #plot eixos cartesianos
    ax.plot3D(x_lim, (0,0), (0,0), color='black')
    ax.plot3D((0,0), y_lim, (0,0), color='black')
    ax.plot3D((0,0), (0,0), z_lim, color='black')    

def add_annotations_3d(ax, vector):
    
    x,y,z = vector
    
    ax.scatter3D(x,0,0, c='b', label=f'x: ( {x:.2f}, 0.0, 0.0 )')
    ax.scatter3D(0,y,0, c='g', label=f'y: ( 0.0, {y:.2f}, 0.0 )')
    ax.scatter3D(0,0,z, c='r', label=f'z: ( 0.0, 0.0, {z:.2f} )')
    
    ax.plot3D((0,x), (0,0), (0,0), c='g')
    ax.plot3D((0,0), (0,y), (0,0), c='b')
    ax.plot3D((0,0), (0,0), (0,z), c='r')
    
    ax.plot3D((x,x), (0,y), (0,0), 'g--')
    ax.plot3D((0,x), (y,y), (0,0), 'b--')
    ax.plot3D((x,x), (y,y), (0,z), 'r--')
    ax.legend()

def plot_vector_3d(ax, vector):
    
    x, y, z = vector
    
    ax.plot3D((0,x), (0,y), (0,z), c='c')
    ax.scatter3D(0,0,0, c='c')
    ax.scatter3D(x,y,z, c='c')

