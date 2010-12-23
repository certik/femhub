How to Use FEMhub Online Lab
============================
FEMhub online lab can be used on your local machine, after you install FEMhub.
Alternatively, if you do not want to download and install
anything you can use FEMhub online lab hosted in the `server of hp-FEM group at
University of Nevada, Reno <http://lab.femhub.org/>`_ (UNR).

FEMhub Online Lab in the Server at UNR
---------------------------------------------------------------
If you want to use FEMhub online lab hosted at the server of hp-FEM group, University of Nevada Reno,
please follow the follwing instructions:

Step 1: To sign up for a new account go to the `Online Lab
<http://lab.femhub.org/>`_ main page, and click **"Create account"** button at the
bottom of the login window.
This is automatic and fast. Report any problems to **femhub@googlegroups.com**.

Step 2: Log into the `online lab <http://lab.femhub.org/>`_. Click the
**"Browser"** icon. After the browser opens, click **"Fork Worksheet"** and
then after selecting any published worksheet just click **"Fork"** button.
Forking will copy the published worksheet to your online lab browser, and you
can play with it, and save your changes in it.

Step 3: Once the selected worksheet is forked, it will appear on the right part
of the online lab "Browser". Click it and scroll down the first input box, and click
**"Evaluate"** at the bottom of each input box. Then the output will appear below
the input box.

Step 4: There are multiple other worksheets to begin with. Try them out and give us your feedback!

Step 5: You can try out worksheets related to Hermes, FiPy, PHAML etc. that allow you
to solve finite element problems via the internet. Feel free to adjust the
existing worksheets to fit your own needs. We are working on expanding the
possibilities.

To write your own code in Python and evaluate, click the **"New Worksheet"**
button in the online lab "Browser".


FEMhub Online Lab on Your Local Machine
---------------------------------------

First download and Install FEMhub following the instructions `here
<http://femhub.org/doc/src/install_run.html>`_.
Then go to the femhub top directory, and just execute **./femhub** from the command line,
and after that type **lab()**.
::
    $ ./femhub
    ----------------------------------------------------------------
    | Femhub Version 0.9.10, Release Date: November 21, 2010       |
    | Type lab() for the GUI.                                      |
    ----------------------------------------------------------------
    In [1]: lab()

Then open your web browser at http://localhost:8000/

.. image:: img/femhub_lab.png
   :align: center
   :width: 800
   :height: 600
   :alt: Screenshot of FEMhub Online Lab

After you create an account and log in you will see a desktop like interface
with a few icons. Click **"Browser"** icon and then click **"New Worksheet"**
to open a new worksheet. In the text input window of the worksheet copy-paste the following:
::
    # Import libraries.
    from sympy import Symbol, lambdify, cos, sin, exp, log
    from numpy import abs

    # Define symbolic variable.
    x = Symbol("x")

    # The Newton's method.
    def newton(f, dfdx, x, x0, eps = 1e-8):
	f = lambdify(x, f, modules=["math"])
	dfdx = lambdify(x, dfdx, modules=["math"])

	x_k = x0

	counter = 0
	while True:
	    counter += 1
	    x_k_plus_one = x_k - f(x_k) / dfdx(x_k)
	    print "Next approximation:", x_k_plus_one
	    # Stopping criterion 1:
	    if abs(x_k_plus_one - x_k) < eps: break
	    # Stopping criterion 2:
	    #if abs(f(x_k_plus_one)) < eps: break
	    x_k = x_k_plus_one
	print "Steps taken:", counter

    # Example 1 (standard behavior). Enter function f(x), its derivative f'(x), symbol x, initial guess x_0, and tolerance epsilon:
    newton(cos(x) - x, -sin(x) - 1, x, 1, 1e-8)

    # Example 2 (standard behavior):
    newton(1/(1+x**2) - x, -1 / (1+x**2) / (1+x**2) * 2*x - 1, x, 5, 1e-8)

    # Example 3 (linear problems):
    newton(x - 2, 1, x, 4, 1e-8)

    # Example 4 (failure if initial guess is far from true solution):
    newton(log(x), 1/x, x, 10, 1e-8)

    # Example 5 (problems with flat functions)
    newton(x**8., 8.*x**7., x, 1, 1e-8)

Click "Evaluate" button and you will see the output below the input box.

.. image:: img/femhub_lab/worksheet.png
   :align: center
   :width: 800
   :height: 600
   :alt: Screenshot of FEMhub Online Lab

Basic Online Lab Help
---------------------
Following is the overview of basic features and helpful hints for running the online lab:

1. Desktop
~~~~~~~~~~
Desktop currently consists of five launchers:

**Browser**
    Manage folders and worksheets.
**Settings**
    Configure your work environment.
**Console**
    Display system messages.
**Help**
    Opens the help window.
**Logout**
    Save settings and quit Online Lab.

2. Browser
~~~~~~~~~~
**Browser** allows you to manage worksheets in various ways. You can create new worksheets and store them in folders. You can also edit, rename or delete existing worksheets.

You can move worksheets between folders and folder between folders, by dragging appropriate items. You will be visually informed if a particular drag is not permitted.

On the top of the **Browser** window you will see the following buttons:

**New Worksheet**
    Opens a new worksheet.
**New Folder**
    Creates a new folder in which you can add new worksheets.
**Import Worksheet**
    Allows to import worksheets in RST and SAGE formats.
**Fork Worksheet**
    Opens a window with published worksheets. Then you can select any worksheet and click "Fork". Clicking the "Fork" button copies the published worksheet to your online lab browser.
**Refresh**
    Refreshes the Browser.
**Rename**
    Renames the selected folder or worksheet.
**Delete**
    Deletes the selected folder or worksheet.

3. Worksheet
~~~~~~~~~~~~
**Worksheet** allows for interaction with a Python interpreter that is running on a remote server. Every open worksheet has an interpreter assigned, in which you can evaluate Python code and import many well know libraries, e.g. SciPy, NumPy, Matplotlib, SymPy.

Every worksheet consists of a sequence of cells. There are three kinds of cells:

**text cells**
    Additional non-evaluable content.
**input cells**
    Allows for entering Python source code.
**output cells**
    Used for displaying results of computations.

To manage cells efficiently, the following shortcuts can be used:

**Shift+Enter**
    Evaluate current input cell and move to the following one.
**Ctrl+Enter**
    Evaluate current input cell and stay there.
**Up**
    Move focus to the input cell above.
**Down**
    Move focus to the input cell below.
**Ctrl+Up**
    Move focus fast to the input cell above.
**Ctrl+Down**
    Move focus fast to the input cell below.
**Alt+Up**
    Create a new input cell above the current one.
**Alt+Down**
    Create a new input cell below the current one.
**Shift+Alt+Up**
    Create a new text cell above the current one.
**Shift+Alt+Down**
    Create a new text cell below the current one.
**Alt+Left**
    Collapse the current cell.
**Alt+Right**
    Expand the current cell.
**Shift+Ctrl+Alt+Up**
    Merge current input cell with the input cell above.
**Shift+Ctrl+Alt+Down**
    Merge current input cell with the input cell below.

The same can be done in most cases, by clicking on a cell with right mouse button and choosing an appropriate item from the context menu.

To edit a text cell, use context menu and choose Edit. An editor will be opened where you will be able to enter contents in either WYSIWYG or HTML modes.

On the top of the **Worksheet** window you will see a menu and different buttons for various functionalities. You can publish any worksheet by clicking **Publish** button.

4. Logout
~~~~~~~~~
When done with your work in Online Lab, click **Logout** icon on the desktop. This will save settings and terminate current session.
