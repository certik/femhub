=========================
FEMhub Examples: Hermes2D
=========================

This tutorial should give you a good idea of how to use different FEM codes in FEMhub.
The document is under continuous development - if you find bugs or would like us to 
improve something, let us know through the `mailing list <http://groups.google.com/group/femhub/>`_.


What is Hermes2D
----------------
`Hermes2D <http://hpfem.org/hermes2d>`_ is a C++ library for rapid prototyping
of space and space-time adaptive hp-FEM solvers, and it is one of the FEM engines
included in FEMhub. Although Hermes2D is written in C++ you do not need to know anything about C++ besides
basic python when you use Hermes2D within FEMhub. For details on how to use Hermes2D itself please refer to `Hermes2D documentation <http://hpfem.org/hermes2d/doc/index.html>`_.

Finite Element Mesh
-------------------

Every finite element computation starts with partitioning the domain
into a finite element mesh. Hermes uses triangles and quadrilaterals, and 
can combine both element types in one mesh. While complicated meshes need 
to be constructed using specialized mesh generation software, in many cases 
we only need a simple initial mesh that can be created by hand. In Hermes, all you 
need to do is partition the domain very coarsely into several large elements,
and the adaptivity will take care of the rest. 

.. image:: ../img/mesh.png
   :align: center
   :width: 600
   :height: 450
   :alt: Sample finite element mesh

The domain is defined via four macroelements -- two
quadrilaterals and two curvilinear triangles. The elements are enumerated from 0 to 3. 
One also needs to enumerate all mesh vertices and assign markers to all boundary edges. 
Boundary markers are used to link boundary conditions with the boundary edges.
The following example Mesh will make clear about how to create mesh in FEMhub.

Example Mesh
------------

First import the required modules
::

    # Import modules
    from hemres2d import Mesh, MeshView

Then you can use Mesh.create() method to create a mesh. It takes four lists
(vertices, elements, boundaries, and curves) as arguments.
::

    # Creates a mesh from a list of vertices, elements, boundaries and curves.
    mesh = Mesh()
    mesh.create([
            [0, -1],
            [1, -1],
            [-1, 0],
            [0, 0],
            [1, 0],
            [-1, 1],
            [0, 1],
            [0.707106781, 0.707106781]
        ], [
            [0, 1, 4, 3, 0],
            [3, 4, 7, 0],   
            [3, 7, 6, 0],
            [2, 3, 6, 5, 0]
        ], [
            [0, 1, 1],
            [1, 4, 2],
            [3, 0, 4],
            [4, 7, 2],
            [7, 6, 2],
            [2, 3, 4],
            [6, 5, 2],
            [5, 2, 3]
        ], [
            [4, 7, 45],
            [7, 6, 45]
        ])

The list of ``vertices`` defines the coordinates of all mesh vertices (in any order). 
The list of ``elements`` contains all elements in the mesh via zero-based indices of their vertices in counter-clockwise order, plus an extra number denoting the element (material) marker. Element markers allow you to use different material parameters in areas with different material parameters. Moreover, Hermes allows you to assign different weak formulations to those areas, which can be very useful for some types of multiphysics problems. If the domain is composed of only one material, as in our case, all elements may be assigned a zero marker:

The last mandatory list, ``boundaries``, defines boundary markers for all
boundary edges. By default, all edges have zero markers. Only those with
positive markers are considered to be part of the domain boundary and can be
assigned a boundary condition, as we will see later. An edge is identified by
two vertex indices.

Finally, the the list of ``curves``, contains all curved edges.  Each curved edge is 
described by one NURBS curve, defined by its degree, control points and knot vector. 
Simplified syntax is available for circular arcs.


The following portion of code illustrates various types of initial mesh refinements.
It does not matter if the mesh becomes irregular, in fact, arbitrarily irregular
meshes are at the heart of Hermes:
::

      # perform some sample initial refinements
      mesh.refine_all_elements()          # refines all elements
      mesh.refine_towards_vertex(3, 4)    # refines mesh towards vertex #3 (4x)
      mesh.refine_towards_boundary(2, 4)  # refines all elements along boundary 2 (4x)
      #mesh.refine_element(86, 0);        # Refines element #86 isotropically.
      #mesh.refine_element(112, 0);       # Refines element #112 isotropically.
      #mesh.refine_element(84, 2);        # Refines element #84 anisotropically.
      #mesh.refine_element(114, 1);       # Refines element #114 anisotropically.

You can also convert triangles to quads and vice versa
::
  mesh.convert_triangles_to_quads()
  mesh.convert_quads_to_triangles()

The following code illustrates how to visualize the mesh using the class MeshView:
::

    # Display the Mesh
    mesh.plot(filename="a.png")

and you will see the following output

    .. image:: img/meshlab.png
       :align: center
       :width: 400
       :height: 400
       :alt: Image of the mesh created via the MeshView class.

To view this example published on FEMhub online lab click `here <http://nb.femhub.org/pub/62>`_.


Example Poisson Equation
------------------------

Let us solve the Poisson equation

.. math::
    :label: poisson1

       -\Delta u = CONST_F

on the L-shaped domain $\Omega$ from the previous example,
equipped with a homogeneous (zero) Dirichlet boundary condition

.. math::
    :label: poisson2

       u = 0\ \ \  \mbox{on}\  \partial \Omega,

where $CONST_F$ is a real number. The weak formulation 
is derived in the standard way, first by multiplying equation :eq:`poisson1` with a test
function $v$, then integrating over the domain $\Omega$, and then applying the Green's
theorem (integration by parts) to the second derivatives.
Because of the homogeneous Dirichlet condition :eq:`poisson2`,
the proper space for the solution is $V = H^1_0(\Omega)$. The weak formulation reads:
Find $u \in V$ such that

.. math::
    :label: poissonweak

         \int_\Omega \nabla u \cdot \nabla v \;\mbox{d\bfx} = CONST_F \int_\Omega v \;\mbox{d\bfx} \ \ \ \mbox{for all}\ v \in V.


To run this example let us first import the required modules::

    # Import modules
    from hermes2d import Mesh, MeshView, H1Shapeset, PrecalcShapeset, H1Space, \
        WeakForm, Solution, ScalarView, LinSystem, DummySolver
    from hermes2d.forms import set_forms
    from hermes2d.examples.c03 import set_bc

Then you can use Mesh.create() method to create a mesh. It takes four lists
(vertices, elements, boundaries, and curves) as arguments.::

    # Creates a mesh from a list of vertices, elements, boundaries and curves.
    mesh = Mesh()
    mesh.create([
            [0, -1],
            [1, -1],
            [-1, 0],
            [0, 0],
            [1, 0],
            [-1, 1],
            [0, 1],
            [0.707106781, 0.707106781]
        ], [
            [0, 1, 4, 3, 0],
            [3, 4, 7, 0],   
            [3, 7, 6, 0],
            [2, 3, 6, 5, 0]
        ], [
            [0, 1, 1],
            [1, 4, 2],
            [3, 0, 4],
            [4, 7, 2],
            [7, 6, 2],
            [2, 3, 4],
            [6, 5, 2],
            [5, 2, 3]
        ], [
            [4, 7, 45],
            [7, 6, 45]
        ])

You can try various types of initial mesh refinements.
::

      # perform some sample initial refinements
      mesh.refine_all_elements()          # refines all elements
      mesh.refine_towards_vertex(3, 4)    # refines mesh towards vertex #3 (4x)
      mesh.refine_towards_boundary(2, 4)  # refines all elements along boundary 2 (4x)


We can now state our problem in the following way:

::

    # Initialize the weak formulation
    wf = WeakForm(1) 
    set_forms(wf) 

The class WeakForm represents the weak formulation of the PDE and must be
initialized with the number of equations in the system, in our case one.

Given the weak formulation and the discretization determined by the space and its mesh,
we can proceed to the approximate solution of the problem by the Galerkin method.
This method is the core of Hermes and provides a way to obtain a sparse linear
system of equations, represented by the class LinSystem in the code. The solution
of the linear system then yields an approximate solution of the original problem.

The class LinSystem needs three things: your weak formulation, your spaces and
finally an external sparse matrix solver, for example CG or UMFPACK. The following lines
create the linear solver, initialize the LinSystem class and pass a pointer to
the H1Space we have created in the previous section.
::

    # initialize the linear system and solver
    solver = DummySolver()
    sys = LinSystem(wf, solver)
    sys.set_spaces(space)
    sys.set_pss(pss) 

The last line must be included for historical reasons. During matrix assembly,
Hermes caches the values of all shape function polynomials for better performance.
The cache is represented by the class PrecalcShapeset and you have to
include the following lines at the beginning of your program:
::

    shapeset = H1Shapeset()
    pss = PrecalcShapeset(shapeset) 

Finally, we tell LinSystem to assemble the stiffness matrix and the right-hand
side and solve the resulting linear system: 
::

    # Assemble the stiffness matrix and solve the system
    sys.assemble()
    A = sys.get_matrix()
    b = sys.get_rhs()
    from scipy.sparse.linalg import cg
    x, res = cg(A, b)
    sln = Solution()
    sln.set_fe_solution(space, pss, x) 

For the Poisson problem, we are finished. The last two lines can be repeated many 
times in time-dependent problems. The instance of the class Solution, upon the
completion of LinSystem::solve(), contains the approximate solution of
the PDE. You can ask for its values or you can visualize the solution immediately 
using the ScalarView class:
::

    # Visualize the solution
    view = ScalarView("Solution")
    view.show(sln, lib="mayavi", filename="a.png", notebook=True)

You can visualize the mesh using the MeshView class:
::
    # Display the Mesh
    mesh.plot(filename="b.png")
 
Furthermore, you can position the images by using the following html codes:
::
    # Positioning the images
    print """<html><table border=1><tr><td><span style="position: relative;"><img src="cell://a.png" ></span></td><td><img src="cell://b.png" width="540" height="405"></td></tr></table></html>"""

The following figure shows the output.

.. image:: ../img/poissonlab.png
   :align: center
   :width: 625
   :height: 400
   :alt: Solution of the Poisson equation.

To view this example published on FEMhub online lab click `here <http://nb.femhub.org/pub/56>`_.

Example Dirichlet BC
--------------------
This example illustrates how to use non-homogeneous(nonzero) Dirichlet boundary conditions. 
Suppose we would like to modify the previous Poisson model problem in the following way:

.. math::
         -\Delta u = CONST_F,\ u(x,y) = -\frac{CONST_F}{4}(x^2 + y^2)\,\ \mbox{on}\,\ \partial \Omega.

where CONST_F is a constant right-hand side. 

It is easy to see that the solution to this problem is the function

.. math::
         u(x,y) = -\frac{CONST_F}{4}(x^2 + y^2). 

Since also the Dirichlet boundary conditions are chosen to match u(x,y), this function is the exact solution.

Note that since the exact solution is a quadratic polynomial, Hermes will compute it exactly if all mesh elements are quadratic or higher (then the exact solution lies in the finite element space).  If some elements in the mesh are linear, Hermes will only find  an approximation. 

Since essential conditions restrict degrees of freedom (DOF) in the FE space,
they need to be incorporated while the space is set up.
The user can set boundary conditions by:
::

  set_bc(space)

The space initialization can look as follows:
::

  space = H1Space(mesh, shapeset)
  space.set_uniform_order(P_INIT)      # PINIT is initial polynomial degree in all elements

Following is the full code that you can run in the Online Lab:
::

  P_INIT = 2              # Initial polynomial degree in all elements
  UNIFORM_REF_LEVEL = 2   # Number of initial uniform mesh refinements

  # Import modules
  from hermes2d import (Mesh, MeshView, H1Shapeset, PrecalcShapeset, H1Space,
         LinSystem, Solution, ScalarView, WeakForm, DummySolver)
  from hermes2d.examples.c04 import set_bc
  from hermes2d.forms import set_forms

  # Initialize the mesh
  mesh = Mesh()

  # Create a mesh from a list of nodes, elements, boundary and nurbs.
  mesh.create([
         [0, -1],
         [1, -1],
         [-1, 0],
         [0, 0],
         [1, 0],
         [-1, 1],
         [0, 1],
         [0.707106781, 0.707106781]
     ], [
         [0, 1, 4, 3, 0],
         [3, 4, 7, 0],  
         [3, 7, 6, 0],
         [2, 3, 6, 5, 0]
     ], [
         [0, 1, 1],
         [1, 4, 2],
         [3, 0, 4],
         [4, 7, 2],
         [7, 6, 2],
         [2, 3, 4],
         [6, 5, 2],
         [5, 2, 6]
     ], [
         [4, 7, 45],
         [7, 6, 45]
     ])

  # Initial mesh refinements
  for i in range(UNIFORM_REF_LEVEL): mesh.refine_all_elements()
 
  # Initialize the shapeset and the cache
  shapeset = H1Shapeset()
  pss = PrecalcShapeset(shapeset)

  # Create an H1 space
  space = H1Space(mesh, shapeset)
  space.set_uniform_order(P_INIT)

  # Set boundary conditions
  set_bc(space)

  # Enumerate degrees of freedom
  space.assign_dofs()

  # Initialize the discrete problem
  wf = WeakForm()
  set_forms(wf, -4)

  # Initialize the linear system and solver
  solver = DummySolver()
  sys = LinSystem(wf, solver)
  sys.set_spaces(space)
  sys.set_pss(pss)

  # Assemble the stiffness matrix and solve the system
  sys.assemble()
  sln = Solution()
  sys.solve_system(sln)

  # Display the solution
  sln.plot(filename="a.png")

  # Display the mesh
  mesh.plot(space=space, filename="b.png")

  # Positioning the images
  print """<html><table border=1><tr><td><img src="cell://a.png"></span></td><td><img src="cell://b.png" width="540" height="405"></td></tr></table></html>"""

The output of the above code in the Online Lab is like this:

.. image:: ../img/dirichlet.png
   :align: center
   :width: 883 
   :height: 450
   :alt: Solution of the Dirichlet problem.

Example Neumann BC
------------------
This example shows how to define Neumann boundary conditions. In addition, you will see how a Filter is used to visualize gradient of the solution 

For this new model problem will have the form

.. math::
    :nowrap:

    \begin{eqnarray*}   -\Delta u = CONST_F,\ \ \ \ \ &&u = 0\,\ \mbox{on}\,\ \Gamma_4,\\                            &&\dd{u}{n} = C_1\,\ \mbox{on}\,\ \Gamma_1,\\                            &&\dd{u}{n} = C_2\,\ \mbox{on}\,\ \Gamma_2,\\                            &&\dd{u}{n} = C_3\,\ \mbox{on}\,\ \Gamma_3. \end{eqnarray*}

where $\Gamma_1 \dots \Gamma_4$ correspond to the edges marked $1 \dots 4$. Now, the weak formulation contains some surface integrals:

.. math::

    \int_\Omega \nabla u \cdot \nabla v \;\mbox{d\bfx} =   CONST_F\int_\Omega v \;\mbox{d\bfx}   + C_1\int_{\Gamma_1} \!v \;\mbox{d}l   + C_2\int_{\Gamma_2} \!v \;\mbox{d}l   + C_3\int_{\Gamma_3} \!v \;\mbox{d}l


In Hermes, all forms in the standard weak formulation $a(u,v) = l(v)$
are in fact defined as a sum of contributions from volume integrals and from
surface integrals. In the case of the linear form $l(v)$, this means

.. math::

    l(v) = \sum_m l_m^{\,\rm vol}(v) + \sum_n l_n^{\,\rm surf}(v).

We have already seen volumetric linear forms in example 03-poisson. 
Surface linear forms are implemented similarly, and will be added to the WeakForm by the following code:

::

  # Initialize the discrete problem
  wf = WeakForm(1)
  set_forms(wf, -1)
  set_forms_surf(wf) 


Note that the mesh is refined towards the re-entrant corner in order to 
capture the singular gradient.
::

	# Initial mesh refinements
	mesh.refine_towards_vertex(3, CORNER_REF_LEVEL) 

The full code that you can run in the Online Lab is as follows:
::
	# Import modules
	from hermes2d import Mesh, MeshView, H1Shapeset, PrecalcShapeset, H1Space, \
		LinSystem, Solution, ScalarView, WeakForm, DummySolver
	from hermes2d.examples.c05 import set_bc, set_forms
	from hermes2d.examples.c05 import set_forms as set_forms_surf
	from hermes2d.forms import set_forms

        P_INIT = 4              # Initial polynomial degree in all elements
        CORNER_REF_LEVEL = 12   # Number of mesh refinements towards the re-entrant corner

	# Initialize the mesh
	mesh = Mesh()

	# Create a mesh from a list of nodes, elements, boundary and nurbs.
	mesh.create([
	       [0, -1],
	       [1, -1],
	       [-1, 0],
	       [0, 0],
	       [1, 0],
	       [-1, 1],
	       [0, 1],
	       [0.707106781, 0.707106781]
	   ], [
	       [0, 1, 4, 3, 0],
	       [3, 4, 7, 0],  
	       [3, 7, 6, 0],
	       [2, 3, 6, 5, 0]
	   ], [
	       [0, 1, 1],
	       [1, 4, 2],
	       [3, 0, 4],
	       [4, 7, 2],
	       [7, 6, 2],
	       [2, 3, 4],
	       [6, 5, 2],
	       [5, 2, 3]
	   ], [
	       [4, 7, 45],
	       [7, 6, 45]
	   ])

	# Initial mesh refinements
	mesh.refine_towards_vertex(3, CORNER_REF_LEVEL)

	# Initialize the shapeset and the cache
	shapeset = H1Shapeset()
	pss = PrecalcShapeset(shapeset)

	# Create an H1 space
	space = H1Space(mesh, shapeset)
	space.set_uniform_order(P_INIT)

	# Set boundary conditions
	set_bc(space)

	# Enumerate degrees of freedom
	space.assign_dofs()

	# Initialize the discrete problem
	wf = WeakForm(1)
	set_forms(wf, -1)
	set_forms_surf(wf)

	# Initialize the linear system and solver
	solver = DummySolver()
	sys = LinSystem(wf, solver)
	sys.set_spaces(space)
	sys.set_pss(pss)

	# Assemble the stiffness matrix and solve the system
	sln = Solution()
	sys.assemble()
	sys.solve_system(sln)

	# Show the solution
	sln.plot(filename="a.png")

	# Show the mesh
	mesh.plot(space=space, filename="b.png")

	# Positioning the images
	print """<html><table border=1><tr><td><img src="cell://a.png"></span></td><td><img src="cell://b.png" width="540" height="405"></td></tr></table></html>"""

After running the above code in the Online Lab you should see the following output:

.. image:: ../img/neumann.png
   :align: left
   :width:75% 
   :alt: Solution of the Neumann problem.

Example BC-Newton
-----------------
This example explains how to use Newton boundary condition (sometimes called Robin) which is of the form

.. math::

    \dd{u}{n} + c_1 u = c_2, \ \ \ \ c_1 \ne 0.

The Laplace equation describes, among
many other things, stationary heat transfer in a homogeneous linear
material.
Analogous to Neumann conditions, Newton conditions yield surface integrals. However,
this time they are both in the bilinear form and in the linear form.

The following parameters can be changed
::
	P_INIT = 3               # uniform polynomial degree in the mesh
	UNIFORM_REF_LEVEL = 2    # number of initial uniform mesh refinements
	CORNER_REF_LEVEL = 12    # number of mesh refinements towards the re-entrant corner

The full code for the example is:
::
	# Import modules
	from hermes2d import Mesh, MeshView, H1Shapeset, PrecalcShapeset, H1Space, \
		LinSystem, WeakForm, DummySolver, Solution, ScalarView
	from hermes2d.examples.c06 import set_bc, set_forms

	# Initialize the mesh
	mesh = Mesh()

	# Create a mesh from a list of nodes, elements, boundary and nurbs.
	mesh.create([
	       [0, -1],
	       [1, -1],
	       [-1, 0],
	       [0, 0],
	       [1, 0],
	       [-1, 1],
	       [0, 1],
	       [0.707106781, 0.707106781]
	   ], [
	       [0, 1, 4, 3, 0],
	       [3, 4, 7, 0],  
	       [3, 7, 6, 0],
	       [2, 3, 6, 5, 0]
	   ], [
	       [0, 1, 1],
	       [1, 4, 2],
	       [3, 0, 4],
	       [4, 7, 2],
	       [7, 6, 2],
	       [2, 3, 4],
	       [6, 5, 2],
	       [5, 2, 3]
	   ], [
	       [4, 7, 45],
	       [7, 6, 45]
	   ])
	   
	# Mesh refinements
	for i in range(UNIFORM_REF_LEVEL): mesh.refine_all_elements()
	mesh.refine_towards_vertex(3, CORNER_REF_LEVEL)

	# Initialize shapeset and cache
	shapeset = H1Shapeset()
	pss = PrecalcShapeset(shapeset)

	# Create an H1 space
	space = H1Space(mesh, shapeset)
	space.set_uniform_order(P_INIT)

	# Set boundary conditions
	set_bc(space)

	# Enumerate degrees of freedom
	space.assign_dofs()

	# Initialize the discrete problem
	wf = WeakForm(1)
	set_forms(wf)

	# Initialize the linear system and solver
	solver = DummySolver()
	sys = LinSystem(wf, solver)
	sys.set_spaces(space)
	sys.set_pss(pss)

	# Assemble the stiffness matrix and solve the system
	sln = Solution()
	sys.assemble()
	sys.solve_system(sln)

	# Display the solution
	sln.plot(filename="a.png")

	# Display the mesh
	mesh.plot(space=space, filename="b.png")

After running the above code in the Online Lab you should see the following output:

.. image:: ../img/newton.png
   :align: left
   :width: 75%
   :alt: Solution of the Newton problem.
