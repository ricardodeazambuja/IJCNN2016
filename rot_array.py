
def rot_array(a,r):
    return numpy.round(numpy.array([a[0]*numpy.cos(r)-a[1]*numpy.sin(r),a[0]*numpy.sin(r)+a[1]*numpy.cos(r)]),2)