'''A module created by Joey Taylor & Nicholas Zieleniewski of Durham University to implement
some basic numerical calculus'''

import numpy

#############################################################################################################
###                                        Differentiation Routines                                       ###
#############################################################################################################

def dif_cd(func, n, dx):
    '''Estimates the gradient at n using the central difference method. For this
    method to work the array has to have at least three entries and n must not be the
    first or last point in the array
    
    func -   1-D Numpy array, represents the values of the function at equally
             spaced values of x
    n    -   Int, index of point at which to work out the gradient
    dx   -   float, the space between each x value

    Return: float'''

    #The central difference formula is: f'(x1)=[f(x2)-f(x0)]/[2.dx]
    #It has a truncation error of {[-dx^2]/6}*f'''(c) for c in (x0,x2)
    #For proof expand f(x0) and f(x2) about x1 using a Taylor series upto f'''
    #and remember that x0=x1-dx and x2=x1+dx

    #Check input:
    if type(func) != numpy.ndarray:
        raise TypeError("Expected <type 'numpy.ndarray'> for func but got "+ str(type(func)))
    if func.ndim != 1:
        raise TypeError('func has to be a 1D array but got a %dD array' %func.ndim)
    if func.dtype.name not in ('float32', 'float64', 'float96', 'float128'):
        raise TypeError('The values in func have to be floats but got '+func.dtype.name)
    if len(func) <3:
        raise ValueError('func has to have at least 3 entries')
    if type(n) != int:
        raise TypeError("Expected <type 'int'> for n but got "+str(type(n)))
    if not -len(func)<=n<len(func):
        raise ValueError("n has to be a valid index, i.e. -len(func)<=n<len(func)")
    if n in (0,len(func)-1,-1,-len(func)):
        raise ValueError("n cannot refer to the first or last value in func")
    if type(dx) != float:
        raise TypeError("Expected <type 'float'> for dx but got "+str(type(dx)))
    if dx <= 0:
        raise ValueError("dx has to be positive but got " +str(dx))
    
    #Perform calculation
    dif_value = (func[n+1]-func[n-1])/(2*dx)
    return dif_value


def dif_fd(func, n, dx):
    '''Estimates the gradient at n using the forward difference method. For this
    method to work the array has to have at least two entries and n must not be the
    last point in the array
    
    func -   1-D Numpy array, represents the values of the function at equally
             spaced values of x
    n    -   Int, index of point at which to work out the gradient
    dx   -   float, the space between each x value

    Return: float'''

    #The forward difference formula is: f'(x1)=[f(x2)-f(x1)]/dx
    #It has a truncation error of {[-dx]/2}*f''(c) for c in (x1,x2)
    #For proof expand f(x2) about x1 using a Taylor series upto f'' and remember
    #that x2=x1+dx

    #Check input:
    if type(func) != numpy.ndarray:
        raise TypeError("Expected <type 'numpy.ndarray'> for func but got "+ str(type(func)))
    if func.ndim != 1:
        raise TypeError('func has to be a 1D array but got a %dD array' %func.ndim)
    if func.dtype.name not in ('float32', 'float64', 'float96', 'float128'):
        raise TypeError('The values in func have to be floats but got '+func.dtype.name)
    if len(func) <2:
        raise ValueError('func has to have at least 2 entries')
    if type(n) != int:
        raise TypeError("Expected <type 'int'> for n but got "+str(type(n)))
    if not -len(func)<=n<len(func):
        raise ValueError("n has to be a valid index, i.e. -len(func)<=n<len(func)")
    if n in (len(func)-1,-1):
        raise ValueError("n cannot refer to the last value in func")
    if type(dx) != float:
        raise TypeError("Expected <type 'float'> for dx but got "+str(type(dx)))
    if dx <= 0:
        raise ValueError("dx has to be positive but got " +str(dx))
    
    #Perform calculation
    dif_value = (func[n+1]-func[n])/(dx)
    return dif_value

def dif_bd(func, n, dx):
    '''Estimates the gradient at n using the backward difference method. For this
    method to work the array has to have at least two entries and n must not be the
    first point in the array
    
    func -   1-D Numpy array, represents the values of the function at equally
             spaced values of x
    n    -   Int, index of point at which to work out the gradient
    dx   -   float, the space between each x value

    Return: float'''

    #The backward difference formula is: f'(x1)=[f(x1)-f(x0)]/dx
    #It has a truncation error of {dx/2}*f''(c) for c in (x1,x2)
    #For proof expand f(x0) about x1 using a Taylor series upto f'' and remember
    #that x0=x1-dx

    #Check input:
    if type(func) != numpy.ndarray:
        raise TypeError("Expected <type 'numpy.ndarray'> for func but got "+ str(type(func)))
    if func.ndim != 1:
        raise TypeError('func has to be a 1D array but got a %dD array' %func.ndim)
    if func.dtype.name not in ('float32', 'float64', 'float96', 'float128'):
        raise TypeError('The values in func have to be floats but got '+func.dtype.name)
    if len(func) <2:
        raise ValueError('func has to have at least 2 entries')
    if type(n) != int:
        raise TypeError("Expected <type 'int'> for n but got "+str(type(n)))
    if not -len(func)<=n<len(func):
        raise ValueError("n has to be a valid index, i.e. -len(func)<=n<len(func)")
    if n in (0,-len(func)):
        raise ValueError("n cannot refer to the first value in func")
    if type(dx) != float:
        raise TypeError("Expected <type 'float'> for dx but got "+str(type(dx)))
    if dx <= 0:
        raise ValueError("dx has to be positive but got " +str(dx))
    
    #Perform calculation
    dif_value = (func[n]-func[n-1])/(dx)
    return dif_value

def dif_bdbd(func,n,dx):
    '''Estimates the second derivative at point n using the double backward difference formula
    func -   1-D Numpy array, represents the values of the function at equally
             spaced values of x. Needs to have at least 3 values
    n    -   Int, index of point at which to work out the second derivative
    dx   -   float, the space between each x value

    Return: float'''

    #Check input:
    if type(func) != numpy.ndarray:
        raise TypeError("Expected <type 'numpy.ndarray'> for func but got "+ str(type(func)))
    if func.ndim != 1:
        raise TypeError('func has to be a 1D array but got a %dD array' %func.ndim)
    if func.dtype.name not in ('float32', 'float64', 'float96', 'float128'):
        raise TypeError('The values in func have to be floats but got '+func.dtype.name)
    if len(func) <3:
        raise ValueError('func has to have at least 3 entries')
    if type(n) != int:
        raise TypeError("Expected <type 'int'> for n but got "+str(type(n)))
    if not -len(func)<=n<len(func):
        raise ValueError("n has to be a valid index, i.e. -len(func)<=n<len(func)")
    if n in (0,1,-len(func),-len(func)+1):
        raise ValueError("n cannot refer to the first or second value in func")
    if type(dx) != float:
        raise TypeError("Expected <type 'float'> for dx but got "+str(type(dx)))
    if dx <= 0:
        raise ValueError("dx has to be positive but got " +str(dx))
    
    #Perform calculation
    dif_value = (func[n-2] + func[n] -2*func[n-1])/(dx**2)
    return dif_value

def dif_fdfd(func,n,dx):
    '''Estimates the second derivative at point n using the double forward difference formula
    func -   1-D Numpy array, represents the values of the function at equally
             spaced values of x. Needs to have at least 3 values
    n    -   Int, index of point at which to work out the second derivative
    dx   -   float, the space between each x value

    Return: float'''

    #Check input:
    if type(func) != numpy.ndarray:
        raise TypeError("Expected <type 'numpy.ndarray'> for func but got "+ str(type(func)))
    if func.ndim != 1:
        raise TypeError('func has to be a 1D array but got a %dD array' %func.ndim)
    if func.dtype.name not in ('float32', 'float64', 'float96', 'float128'):
        raise TypeError('The values in func have to be floats but got '+func.dtype.name)
    if len(func) <3:
        raise ValueError('func has to have at least 3 entries')
    if type(n) != int:
        raise TypeError("Expected <type 'int'> for n but got "+str(type(n)))
    if not -len(func)<=n<len(func):
        raise ValueError("n has to be a valid index, i.e. -len(func)<=n<len(func)")
    if n in (-1,-2,len(func)-1,len(func)-2):
        raise ValueError("n cannot refer to the last or second to last value in func")
    if type(dx) != float:
        raise TypeError("Expected <type 'float'> for dx but got "+str(type(dx)))
    if dx <= 0:
        raise ValueError("dx has to be positive but got " +str(dx))
    
    #Perform calculation
    dif_value = (func[n+2] + func[n] -2*func[n+1])/(dx**2)
    return dif_value

def dif_cdcd(func,n,dx):
    '''Estimates the second derivative at point n using the double central difference formula
    func -   1-D Numpy array, represents the values of the function at equally
             spaced values of x. Needs to have at least 3 values
    n    -   Int, index of point at which to work out the second derivative
    dx   -   float, the space between each x value

    Return: float'''

    #Check input:
    if type(func) != numpy.ndarray:
        raise TypeError("Expected <type 'numpy.ndarray'> for func but got "+ str(type(func)))
    if func.ndim != 1:
        raise TypeError('func has to be a 1D array but got a %dD array' %func.ndim)
    if func.dtype.name not in ('float32', 'float64', 'float96', 'float128'):
        raise TypeError('The values in func have to be floats but got '+func.dtype.name)
    if len(func) <3:
        raise ValueError('func has to have at least 3 entries')
    if type(n) != int:
        raise TypeError("Expected <type 'int'> for n but got "+str(type(n)))
    if not -len(func)<=n<len(func):
        raise ValueError("n has to be a valid index, i.e. -len(func)<=n<len(func)")
    if n in (0,-1,len(func)-1):
        raise ValueError("n cannot refer to the first or last value in func")
    if type(dx) != float:
        raise TypeError("Expected <type 'float'> for dx but got "+str(type(dx)))
    if dx <= 0:
        raise ValueError("dx has to be positive but got " +str(dx))
    
    #Perform calculation
    dif_value = (func[n+1] + func[n-1] -2*func[n])/(dx**2)
    return dif_value    

#############################################################################################################
###                                   Fast Differentiation Routines                                       ###
#############################################################################################################

def dif_fn(func, dx):
    '''Estimates the derivative of the function by applying the forward difference
    method to the first point in the array, the central difference method to the
    'middle' points in the array and the backward difference method to the end point
    in the array. For this method to work the array has to have at least two points
    
    func -   1-D Numpy array, represents the values of the function at equally
             spaced values of x
    dx   -   float, the space between each x value

    Return: numpy.ndarray'''

    #Check input:
    if type(func) != numpy.ndarray:
        raise TypeError("Expected <type 'numpy.ndarray'> for func but got "+ str(type(func)))
    if func.ndim != 1:
        raise TypeError('func has to be a 1D array but got a %dD array' %func.ndim)
    if func.dtype.name not in ('float32', 'float64', 'float96', 'float128'):
        raise TypeError('The values in func have to be floats but got '+func.dtype.name)
    if len(func) <2:
        raise ValueError('func has to have at least 2 entries')
    if type(dx) != float:
        raise TypeError("Expected <type 'float'> for dx but got "+str(type(dx)))
    if dx <= 0:
        raise ValueError("dx has to be positive but got " +str(dx))
    
    #Perform calculation
    output_array = numpy.zeros(len(func))
    output_array[:-1][2::2] = numpy.diff(func[1::2]) #use central difference for middle entries
    output_array[:-1][1::2] = numpy.diff(func[::2])
    output_array/=(2*dx)
    output_array[0] = numpy.diff(func[0:2])/dx #use forward dif for first entry
    output_array[-1] = numpy.diff(func[-2:])/dx #use backward dif for last entry
    return output_array


def dif_array_2D(func, dx, dy):
    '''Performs the grad operator. Remember, arrays are addressed from the top left entry
    (which would be [0,0]. Moving to the right we have [0,1], [0,2], etc and moving down we have [1,0], [2,0].
    In other words the format of the array is: my_array[y_value,x_value]. If you just want grad in one direction only
    then you can just specify some float for the increment you are not interested in when you call the function.  

    func -   2-D Numpy array, represents the values of the function at equally
             spaced values of x and y (for respective x and y directions).
    dx   -   float, the space between each x value
    dy   -   float, the space between each y value'''
    
    # Check input:
    if type(func) != numpy.ndarray:
        raise TypeError("Expected <type 'numpy.ndarray'> for func but got "+ str(type(func)))
    if func.ndim != 2:
        raise TypeError('func has to be a 2D array but got a %dD array' %func.ndim)
    if func.dtype.name not in ('float32', 'float64', 'float96', 'float128'):
        raise TypeError('The values in func have to be floats but got '+func.dtype.name)
    if len(func) <2:
        raise ValueError('func has to have at least 2 entries')
    if type(dx) != float:
        raise TypeError("Expected <type 'float'> for dx but got "+str(type(dx)))
    if type(dy) != float:
        raise TypeError("Expected <type 'float'> for dy but got "+str(type(dy)))
    if dx <= 0:
        raise ValueError("dx has to be positive but got " +str(dx))
    if dy <= 0:
        raise ValueError("dy has to be positive but got " +str(dy))

    #Perform calculation
    output_array_x = numpy.zeros(func.shape)
    output_array_y = numpy.zeros(func.shape)
    #dif x direction
    output_array_x[:,:-1][:,2::2] = numpy.diff(func[:,1::2])
    output_array_x[:,:-1][:,1::2] = numpy.diff(func[:,::2])
    output_array_x/=(2*dx)
    output_array_x[:,0:1] = numpy.diff(func[:,0:2])/dx
    output_array_x[:,-1:] = numpy.diff(func[:,-2:])/dx
    #dif y direction
    output_array_y[:-1,:][2::2,:] = numpy.diff(func[1::2,:],axis=0)
    output_array_y[:-1,:][1::2,:] = numpy.diff(func[::2,:],axis=0)
    output_array_y/=(2*dy)
    output_array_y[0:1,:] = numpy.diff(func[0:2,:],axis=0)/dy
    output_array_y[-1:,:] = numpy.diff(func[-2:,:],axis=0)/dy
    return output_array_x, output_array_y


def dif_array_3D(func, dx, dy, dz):
    '''Performs the grad operator. Remember, arrays are addressed from the top left entry
    (which would be [0,0,0]. Moving to the right we have [0,0,1], [0,0,2], etc and moving down we have [0,1,0], [0,2,0].
    Moving thorugh the z-direction ('through the layers of the array') we go [0,0,0], [1,0,0], [2,0,0] etc. In other
    words the format of the array is: my_array[z_value,y_value,x_value]. If you just want grad in one direction only
    then you can just specify some float for the increment(s) you are not interested in when you call the function.  

    func -   3-D Numpy array, represents the values of the function at equally
             spaced values of x, y and z (for respective x, y directions and z).
    dx   -   float, the space between each x value
    dy   -   float, the space between each y value
    dz   -   float, the space between each z value'''
    
    # Check input:
    if type(func) != numpy.ndarray:
        raise TypeError("Expected <type 'numpy.ndarray'> for func but got "+ str(type(func)))
    if func.ndim != 3:
        raise TypeError('func has to be a 3D array but got a %dD array' %func.ndim)
    if func.dtype.name not in ('float32', 'float64', 'float96', 'float128'):
        raise TypeError('The values in func have to be floats but got '+func.dtype.name)
    if len(func) <2:
        raise ValueError('func has to have at least 2 entries')
    if type(dx) != float:
        raise TypeError("Expected <type 'float'> for dx but got "+str(type(dx)))
    if type(dy) != float:
        raise TypeError("Expected <type 'float'> for dy but got "+str(type(dy)))
    if type(dz) != float:
        raise TypeError("Expected <type 'float'> for dz but got "+str(type(dz)))
    if dx <= 0:
        raise ValueError("dx has to be positive but got " +str(dx))
    if dy <= 0:
        raise ValueError("dy has to be positive but got " +str(dy))
    if dz <= 0:
        raise ValueError("dz has to be positive but got " +str(dz))
    
    #Perform calculation
    output_array_x = numpy.zeros(func.shape)
    output_array_y = numpy.zeros(func.shape)
    output_array_z = numpy.zeros(func.shape)
    #dif x direction
    output_array_x[:,:,:-1][:,:,2::2] = numpy.diff(func[:,:,1::2])
    output_array_x[:,:,:-1][:,:,1::2] = numpy.diff(func[:,:,::2])
    output_array_x/=(2*dx)
    output_array_x[:,:,0:1] = numpy.diff(func[:,:,0:2])/dx
    output_array_x[:,:,-1:] = numpy.diff(func[:,:,-2:])/dx
    #dif y direction
    output_array_y[:,:-1,:][:,2::2,:] = numpy.diff(func[:,1::2,:],axis=1)
    output_array_y[:,:-1,:][:,1::2,:] = numpy.diff(func[:,::2,:],axis=1)
    output_array_y/=(2*dy)
    output_array_y[:,0:1,:] = numpy.diff(func[:,0:2,:],axis=1)/dy
    output_array_y[:,-1:,:] = numpy.diff(func[:,-2:,:],axis=1)/dy
    #dif z direction
    output_array_z[:-1,:,:][2::2,:,:] = numpy.diff(func[1::2,:,:],axis=0)
    output_array_z[:-1,:,:][1::2,:,:] = numpy.diff(func[::2,:,:],axis=0)
    output_array_z/=(2*dz)
    output_array_z[0:1,:,:] = numpy.diff(func[0:2,:,:],axis=0)/dz
    output_array_z[-1:,:,:] = numpy.diff(func[-2:,:,:],axis=0)/dz
    return output_array_x, output_array_y, output_array_z


def dif_laplace_1D(func, dx):
    '''Estimates the laplacian of the function(which in 1D is the second derivative) by
    applying the double forward difference method to the first point in the array,
    the double central difference method to the 'middle' points in the array and the
    double backward difference method to the end point in the array.
    For this method to work the array has to have at least three points
    
    func -   1-D Numpy array, represents the values of the function at equally
             spaced values of x
    dx   -   float, the space between each x value

    Return: numpy.ndarray'''

    #Check input:
    if type(func) != numpy.ndarray:
        raise TypeError("Expected <type 'numpy.ndarray'> for func but got "+ str(type(func)))
    if func.ndim != 1:
        raise TypeError('func has to be a 1D array but got a %dD array' %func.ndim)
    if func.dtype.name not in ('float32', 'float64', 'float96', 'float128'):
        raise TypeError('The values in func have to be floats but got '+func.dtype.name)
    if len(func) <3:
        raise ValueError('func has to have at least 3 entries')
    if type(dx) != float:
        raise TypeError("Expected <type 'float'> for dx but got "+str(type(dx)))
    if dx <= 0:
        raise ValueError("dx has to be positive but got " +str(dx))
    
    #Perform calculation
    dif_array = numpy.zeros(func.shape)
    dif_array[1:-1] +=numpy.diff(func,n=2,axis=0) #central difference
    dif_array[0:1] +=numpy.diff(func[0:3],n=2,axis=0) #forward difference
    dif_array[-1:] +=numpy.diff(func[-3:],n=2,axis=0) #backward difference
    
    dif_array/=dx**2
    
    return dif_array

def dif_laplace_2D(func, h):
    '''Estimates the laplacian of the function
    For this method to work the array has to be at least 3x3
    
    func -   2-D Numpy array, represents the values of the function at equally
             spaced values of x/y
    h    -   float, the space between each x/y value

    Return: numpy.ndarray'''

    #Check input:
    if type(func) != numpy.ndarray:
        raise TypeError("Expected <type 'numpy.ndarray'> for func but got "+ str(type(func)))
    if func.ndim != 2:
        raise TypeError('func has to be a 2D array but got a %dD array' %func.ndim)
    if func.dtype.name not in ('float32', 'float64', 'float96', 'float128'):
        raise TypeError('The values in func have to be floats but got '+func.dtype.name)
    if func.shape[0] <3 or func.shape[1]<3:
        raise ValueError('func has to be at least 3x3')
    if type(h) != float:
        raise TypeError("Expected <type 'float'> for h but got "+str(type(h)))
    if h <= 0:
        raise ValueError("h has to be positive but got " +str(h))
    
    #Perform calculation
    dif_array = numpy.zeros(func.shape)
    dif_array[1:-1,:] +=numpy.diff(func,n=2,axis=0) #central difference
    dif_array[0:1,:] +=numpy.diff(func[0:3,:],n=2,axis=0) #forward difference
    dif_array[-1:,:] +=numpy.diff(func[-3:,:],n=2,axis=0) #backward difference
    
    dif_array[:,1:-1] +=numpy.diff(func,n=2,axis=1)
    dif_array[:,0:1] +=numpy.diff(func[:,0:3],n=2,axis=1)
    dif_array[:,-1:] +=numpy.diff(func[:,-3:],n=2,axis=1)
    
    dif_array/=h**2
    
    return dif_array


def dif_laplace_3D(func, h):
    '''Estimates the laplacian of the function
    For this method to work the array has to be at least 3x3x3
    
    func -   3-D Numpy array, represents the values of the function at equally
             spaced values of x/y
    h    -   float, the space between each x/y value

    Return: numpy.ndarray'''

    #Check input:
    if type(func) != numpy.ndarray:
        raise TypeError("Expected <type 'numpy.ndarray'> for func but got "+ str(type(func)))
    if func.ndim != 3:
        raise TypeError('func has to be a 3D array but got a %dD array' %func.ndim)
    if func.dtype.name not in ('float32', 'float64', 'float96', 'float128'):
        raise TypeError('The values in func have to be floats but got '+func.dtype.name)
    if func.shape[0] <3 or func.shape[1]<3 or func.shape[2]<3:
        raise ValueError('func has to be at least 3x3x3')
    if type(h) != float:
        raise TypeError("Expected <type 'float'> for h but got "+str(type(h)))
    if h <= 0:
        raise ValueError("h has to be positive but got " +str(h))
    
    #Perform calculation
    dif_array = numpy.zeros(func.shape)
    dif_array[1:-1,:,:] +=numpy.diff(func,n=2,axis=0) #central difference
    dif_array[0:1,:,:] +=numpy.diff(func[0:3,:,:],n=2,axis=0) #forward difference
    dif_array[-1:,:,:] +=numpy.diff(func[-3:,:,:],n=2,axis=0) #backward difference
    
    dif_array[:,1:-1,:] +=numpy.diff(func,n=2,axis=1)
    dif_array[:,0:1,:] +=numpy.diff(func[:,0:3,:],n=2,axis=1)
    dif_array[:,-1:,:] +=numpy.diff(func[:,-3:,:],n=2,axis=1)
    
    dif_array[:,:,1:-1] +=numpy.diff(func,n=2,axis=2)
    dif_array[:,:,0:1] +=numpy.diff(func[:,:,0:3],n=2,axis=2)
    dif_array[:,:,-1:] +=numpy.diff(func[:,:,-3:],n=2,axis=2)
    dif_array/=h**2
    
    return dif_array

#############################################################################################################
###                                   Fast Integration Routines                                           ###
#############################################################################################################

def int_trap(func, dx, n0=0, n1=-1):
    '''Estimates the area under func between n0 and n1 by applying the composite Trapezium
    rule. n1 MUST refer to a value after n0 in the array however negative addressing IS
    supported. Further, func must have at least 2 values.

    func -   1-D Numpy array, represents the values of the function at equally
             spaced values of x
    dx   -   float, the space between each x value
    n0   -   int, index of the first element to integrate from
    n1   -   int, index of the last element to include

    Return: float'''

    #The composite trapezium rule is: {[xn-x0]/2n}* {f(x0) + 2f(x1) +...+2f(xn-1) +f(xn)}
    #where n is the number of trapeziums used, in our case n = (xn-x0)/dx

    #Check input:
    if type(func) != numpy.ndarray:
        raise TypeError("Expected <type 'numpy.ndarray'> for func but got "+ str(type(func)))
    if func.ndim != 1:
        raise TypeError('func has to be a 1D array but got a %dD array' %func.ndim)
    if func.dtype.name not in ('float32', 'float64', 'float96', 'float128'):
        raise TypeError('The values in func have to be floats but got '+func.dtype.name)
    if len(func) <2:
        raise ValueError('func has to have at least 2 entries')
    if type(dx) != float:
        raise TypeError("Expected <type 'float'> for dx but got "+str(type(dx)))
    if dx <= 0:
        raise ValueError("dx has to be positive but got " +str(dx))
    if type(n0) != int:
        raise TypeError("Expected <type 'int'> for n0 but got "+str(type(n0)))
    if not -len(func)<=n0<len(func):
        raise ValueError("n0 has to be a valid index, i.e. -len(func)<=n0<len(func)")
    if type(n1) != int:
        raise TypeError("Expected <type 'int'> for n1 but got "+str(type(n1)))
    if not -len(func)<=n1<len(func):
        raise ValueError("n1 has to be a valid index, i.e. -len(func)<=n1<len(func)")
    if n0<0: n0=n0+len(func) #turn -ve index into positive
    if n1<0: n1=n1+len(func)
    if n1<=n0:
        raise ValueError("n1 has to refer to an element after n0, got n0 = %d, n1 = %d" %(n0,n1))
    
    
    #Perform calculation
    pattern = numpy.zeros(n1-n0+1)
    pattern.fill(dx)
    pattern[-1]=dx/2.
    pattern[0]=dx/2.
    return numpy.sum(pattern*func[n0:n1+1])
    

def int_simp(func, dx, n0=0, n1=-1):
    '''Estimates the area under func between n0 and n1 by applying the composite Simpsons
    rule. n1 MUST refer to a value after n0 in the array however negative addressing IS
    supported. Further, func must have at least 3 values and n0 -> n1 must span three values.

    func -   1-D Numpy array, represents the values of the function at equally
             spaced values of x
    dx   -   float, the space between each x value
    n0   -   int, index of the first element to integrate from
    n1   -   int, index of the last element to include

    Return: float'''

    #The composite Simpson's rule is: {dx/3}*{f(x0)+4f(x1)+2f(x2)+4f(x3)+...+f(xn)}
    #where dx is spacing between x points and there are at least 3 points

    #Check input:
    if type(func) != numpy.ndarray:
        raise TypeError("Expected <type 'numpy.ndarray'> for func but got "+ str(type(func)))
    if func.ndim != 1:
        raise TypeError('func has to be a 1D array but got a %dD array' %func.ndim)
    if func.dtype.name not in ('float32', 'float64', 'float96', 'float128'):
        raise TypeError('The values in func have to be floats but got '+func.dtype.name)
    if len(func) <3:
        raise ValueError('func has to have at least 3 entries')
    if type(dx) != float:
        raise TypeError("Expected <type 'float'> for dx but got "+str(type(dx)))
    if dx <= 0:
        raise ValueError("dx has to be positive but got " +str(dx))
    if type(n0) != int:
        raise TypeError("Expected <type 'int'> for n0 but got "+str(type(n0)))
    if not -len(func)<=n0<len(func):
        raise ValueError("n0 has to be a valid index, i.e. -len(func)<=n0<len(func)")
    if type(n1) != int:
        raise TypeError("Expected <type 'int'> for n1 but got "+str(type(n1)))
    if not -len(func)<=n1<len(func):
        raise ValueError("n1 has to be a valid index, i.e. -len(func)<=n1<len(func)")
    if n0<0: n0=n0+len(func) #turn -ve index into positive
    if n1<0: n1=n1+len(func)
    if (n0+1)>=n1:
        raise ValueError("n0->n1 has to cover at least three points, got references to n0 = %d, n1 = %d" %(n0,n1))
    
    
    #Perform calculation
    pattern = numpy.zeros(n1-n0+1)
    pattern.fill((4*dx)/3.)
    pattern[2::2]=((2*dx)/3.)
    pattern[-1]=dx/3.
    pattern[0]=dx/3.
    
    return numpy.sum(pattern*func[n0:n1+1])

def int_trap_2d(func,h):
    '''Estimates the volume under a surface by approximating each spatial grid as a plane whose height is is the average
    of its four corners. The input array must be at least 2x2.

    func -   2-D Numpy array, represents the values of the function at equally
             spaced values of (x,y)
    h   -   float, the space between each x(or y) value

    Return: float'''
    #Check input:
    if type(func) != numpy.ndarray:
        raise TypeError("Expected <type 'numpy.ndarray'> for func but got "+ str(type(func)))
    if func.ndim != 2:
        raise TypeError('func has to be a 2D array but got a %dD array' %func.ndim)
    if func.dtype.name not in ('float32', 'float64', 'float96', 'float128'):
        raise TypeError('The values in func have to be floats but got '+func.dtype.name)
    if func.shape[0] <2 or func.shape[1]<2:
        raise ValueError('func has to be at least 2x2')
    if type(h) != float:
        raise TypeError("Expected <type 'float'> for h but got "+str(type(h)))
    if h <= 0:
        raise ValueError("h has to be positive but got " +str(h))
    #perform calculation
    pattern = numpy.zeros(func.shape)
    pattern.fill(4)
    pattern[0,:]=2
    pattern[-1,:]=2
    pattern[:,0]=2
    pattern[:,-1]=2
    pattern[0,0]=1
    pattern[-1,-1]=1
    pattern[0,-1]=1
    pattern[-1,0]=1
    integral_array = func*pattern*.25*h**2
    return numpy.sum(numpy.sum(integral_array))

def int_trap_3d(func,h):
    '''Estimates the amount of something bounded by a surface by averaging each spatial grid 
    using its eight corners. The input array must be at least 2x2x2.

    func -   3-D Numpy array, represents the values of the function at equally
             spaced values of (x,y,z)
    h   -   float, the space between each x(or y or z) value

    Return: float'''
    #Check input:
    if type(func) != numpy.ndarray:
        raise TypeError("Expected <type 'numpy.ndarray'> for func but got "+ str(type(func)))
    if func.ndim != 3:
        raise TypeError('func has to be a 3D array but got a %dD array' %func.ndim)
    if func.dtype.name not in ('float32', 'float64', 'float96', 'float128'):
        raise TypeError('The values in func have to be floats but got '+func.dtype.name)
    if func.shape[0] <2 or func.shape[1]<2 or func.shape[2]<2:
        raise ValueError('func has to be at least 2x2x2')
    if type(h) != float:
        raise TypeError("Expected <type 'float'> for h but got "+str(type(h)))
    if h <= 0:
        raise ValueError("h has to be positive but got " +str(h))
    #perform calculation
    #centre points counted eight times
    #face points counted four times
    #edge points counted two times
    #corner points counted once
    pattern = numpy.zeros(func.shape)
    pattern.fill(8) #centre points
    pattern[0,:,:]=4 #face points
    pattern[:,:,0]=4
    pattern[:,0,:]=4
    pattern[-1,:,:]=4
    pattern[:,:,-1]=4
    pattern[:,-1,:]=4
    
    pattern[0,0,:]=2 #edge points
    pattern[0,:,0]=2
    pattern[0,:,-1]=2
    pattern[0,-1,:]=2
    
    pattern[-1,0,:]=2
    pattern[-1,:,0]=2
    pattern[-1,:,-1]=2
    pattern[-1,-1,:]=2
    
    pattern[:,0,0]=2
    pattern[:,0,-1]=2
    pattern[:,-1,0]=2
    pattern[:,-1,-1]=2

    pattern[0,0,0]=1
    pattern[0,0,-1]=1
    pattern[0,-1,0]=1
    pattern[-1,0,0]=1
    pattern[-1,-1,0]=1
    pattern[-1,0,-1]=1
    pattern[0,-1,-1]=1
    pattern[-1,-1,-1]=1
    integral_array = func*pattern*.125*h**3 #volume of one cube is h^3, the 1/8th is there to average each cube(8pts)
    return numpy.sum(numpy.sum(numpy.sum(integral_array)))

#############################################################################################################
###                              Fast Complex Integration Routines                                        ###
#############################################################################################################

def int_trap_complex(func, dt, n0=0, n1=-1):
    '''Estimates the the integral of the complex valued 'func'  between n0 and n1 which was sampled at regular
    real intervals of size dt by applying the composite Trapezium rule. n1 MUST refer to a value after n0 in
    the array however negative addressing IS supported. Further, func must have at least 2 values.

    func -   1-D Numpy array, represents the values of the function at equally
             spaced values of t(real variable)
    dt   -   float, the space between each t value
    n0   -   int, index of the first element to integrate from
    n1   -   int, index of the last element to include

    Return: float'''

    #This is just a wrapper for the real valued version but to use that we need to split up
    #func into real and imaginary components

    #Check input:
    if type(func) != numpy.ndarray:
        raise TypeError("Expected <type 'numpy.ndarray'> for func but got "+ str(type(func)))
    if func.ndim != 1:
        raise TypeError('func has to be a 1D array but got a %dD array' %func.ndim)
    if func.dtype.name not in ('complex64','complex128','complex192','complex256','float32', 'float64', 'float96', 'float128'):
        raise TypeError('The values in func have to be complex floats but got '+func.dtype.name)
    if len(func) <2:
        raise ValueError('func has to have at least 2 entries')
    if type(dt) != float:
        raise TypeError("Expected <type 'float'> for dt but got "+str(type(dt)))
    if dt <= 0:
        raise ValueError("dt has to be positive but got " +str(dt))
    if type(n0) != int:
        raise TypeError("Expected <type 'int'> for n0 but got "+str(type(n0)))
    if not -len(func)<=n0<len(func):
        raise ValueError("n0 has to be a valid index, i.e. -len(func)<=n0<len(func)")
    if type(n1) != int:
        raise TypeError("Expected <type 'int'> for n1 but got "+str(type(n1)))
    if not -len(func)<=n1<len(func):
        raise ValueError("n1 has to be a valid index, i.e. -len(func)<=n1<len(func)")
    if n0<0: n0=n0+len(func) #turn -ve index into positive
    if n1<0: n1=n1+len(func)
    if n1<=n0:
        raise ValueError("n1 has to refer to an element after n0, got n0 = %d, n1 = %d" %(n0,n1))
    
    
    #Split into real and imag then integrate one at a time
    func_real = numpy.real(func)
    func_imag = numpy.imag(func)
    return int_trap(func_real,dt,n0,n1) + 1j*int_trap(func_imag,dt,n0,n1)
    

def int_simp_complex(func, dt, n0=0, n1=-1):
    '''Estimates the the integral of the complex valued 'func'  between n0 and n1 which was sampled at regular
    real intervals of size dt by applying the composite Simpsons rule. n1 MUST refer to a value after n0 in the
    array however negative addressing IS supported. Further, func must have at least 3 values and n0 -> n1 must
    span at least three values.

    func -   1-D Numpy array, represents the values of the function at equally
             spaced values of t(real variable)
    dt   -   float, the space between each t value
    n0   -   int, index of the first element to integrate from
    n1   -   int, index of the element to integrate to

    Return: float'''

    #The composite Simpson's rule is: {dx/3}*{f(x0)+4f(x1)+2f(x2)+4f(x3)+...+f(xn)}
    #where dx is spacing between x points and there are at least 3 points

    #Check input:
    if type(func) != numpy.ndarray:
        raise TypeError("Expected <type 'numpy.ndarray'> for func but got "+ str(type(func)))
    if func.ndim != 1:
        raise TypeError('func has to be a 1D array but got a %dD array' %func.ndim)
    if func.dtype.name not in ('complex64','complex128','complex192','complex256','float32', 'float64', 'float96', 'float128'):
        raise TypeError('The values in func have to be complex floats but got '+func.dtype.name)
    if len(func) <3:
        raise ValueError('func has to have at least 3 entries')
    if type(dt) != float:
        raise TypeError("Expected <type 'float'> for dt but got "+str(type(dt)))
    if dt <= 0:
        raise ValueError("dt has to be positive but got " +str(dt))
    if type(n0) != int:
        raise TypeError("Expected <type 'int'> for n0 but got "+str(type(n0)))
    if not -len(func)<=n0<len(func):
        raise ValueError("n0 has to be a valid index, i.e. -len(func)<=n0<len(func)")
    if type(n1) != int:
        raise TypeError("Expected <type 'int'> for n1 but got "+str(type(n1)))
    if not -len(func)<=n1<len(func):
        raise ValueError("n1 has to be a valid index, i.e. -len(func)<=n1<len(func)")
    if n0<0: n0=n0+len(func) #turn -ve index into positive
    if n1<0: n1=n1+len(func)
    if (n0+1)>=n1:
        raise ValueError("n0->n1 has to cover at least three points, got references to n0 = %d, n1 = %d" %(n0,n1))
    
    
    #Split into real and imag then integrate one at a time
    func_real = numpy.real(func)
    func_imag = numpy.imag(func)
    return int_simp(func_real,dt,n0,n1) + 1j*int_simp(func_imag,dt,n0,n1)
