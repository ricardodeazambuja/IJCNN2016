
# Generates the movements according to:
# Flash, Tamar and Neville Hogan. 1985. The Coordination of Arm Movements: An Experimentally Confirmed 
# Mathematical Model. The Journal of Neuroscience 5 (7): 1688-1703
def movement_generation_training(xstart,xdest,MT,t):
    '''
    xstart,ystart: initial position of the trajectory
    MT: total time spent doing the trajectory
    t: current time
    
    returns a matrix: [[x0,y0],[x1,y1],...]
    '''
    x_t=xstart+(xstart-xdest)*(15*(t/MT)**4-6*(t/MT)**5-10*(t/MT)**3)
    return numpy.array(x_t)