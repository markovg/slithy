def curve( x1, y1, x2, y2, x ):
    x = (x-x1)/(x2-x1)
    y = 3*x*x - 2*x*x*x
    y = y * (y2-y1) + y1
    return y

pts = (
    (-0.1, 0.1),
    (0.1, -0.1),
    (0.7, 1.1),
    (0.85, 0.95),
    #(0.9, 1.05),
    (1, 1)
    )

pts = zip( pts[:-1], pts[1:] )

def rubbermap( x ):
    x = 1-x
    for (x1,y1),(x2,y2) in pts:
        if x <= x2:
            return 1-curve( x1, y1, x2, y2, x )

def split_sequence_rubber( n, u, v = 0.0 ):
    if u <= 0.0:
        return (0.0,) * n
    elif u >= 1.0:
        return (1.0,) * n
    
    l = 1.0 / ((n-1)*(1-v) + 1)
    f = l * (1-v)

    vec = []
    s = 0.0
    for i in range(n):
        if u < s:
            vec.append( 0.0 )
        elif u < s+l:
            x = (u-s) / l
            vec.append( rubbermap( x ) )
        else:
            vec.append( 1.0 )
        s += f

    return tuple(vec)


#f = open( 'out.dat', 'w' )
#for i in range( 0, 201 ):
#    x = i * 0.005
#    print >> f, '%f %f' % (x, rubbermap(x))
#f.close()

    
