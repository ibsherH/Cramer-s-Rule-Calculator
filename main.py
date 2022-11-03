# This program takes in the equations of three planes. It then solves it using cramer's rule and plots the planes on a graph

import matplotlib.pyplot as plt
import numpy as np

from tkinter import *

root = Tk()
root.title = ("Planes")

#matplotlib is for plotting math stuff
import matplotlib.pyplot as plt

def find_point(a,b,c,d):
  # ax + by + cz + d = 0
  # setting x = 0, y = 0, to solve for z
  # cz + d = 0
  # z = -d/c
  return [0, 0, -d/c]

def linearly_dependent(row1, row2):
    # Returns True if linearly dependent, False otherwise
    _row1 = []
    for row in row1:
        _row1.append(row/row1[0])
    _row2 = []
    for row in row2:
        _row2.append(row/row2[0])
    
    for index in [0,1,2,3]:
        if _row1[index] != _row2[index]:
            return False
    return True
    
def has_no_solutions(row1, row2, row3):
    # Returns True if has zero solutions or False if there is infinite solutions
    if linearly_dependent(row1, row2):
        return False
    if linearly_dependent(row1, row3):
        return False
    if linearly_dependent(row2, row3):
        return False
    return True

def get_determinant(col1, col2, col3):
  a1 = int(col1[0].get())
  a2 = int(col1[1].get())
  a3 = int(col1[2].get())
  b1 = int(col2[0].get())
  b2 = int(col2[1].get())
  b3 = int(col2[2].get())
  c1 = int(col3[0].get())
  c2 = int(col3[1].get())
  c3 = int(col3[2].get())
  return a1*((b2*c3)-(c2*b3)) - b1*((a2*c3)-(c2*a3)) + c1*((a2*b3)-(a3*b2))

def plot_planes():
  
  xx, yy = np.meshgrid(range(20), range(20))

  # plot plane 1
  point = find_point(
    int(a1.get()), int(b1.get()), 
    int(c1.get()), int(d1.get()))
  point = np.array(point)
  normal = [int(a1.get()), int(b1.get()), int(c1.get())]
  normal = np.array(normal)
  d = -point.dot(normal)
  
  zz1 = (-normal[0] * xx - normal[1] * yy - d) * 1. / normal[2]

  # plot plane 2
  point = find_point(
    int(a2.get()),
    int(b2.get()), 
    int(c2.get()),
    int(d2.get()))
  normal = [int(a2.get()), int(b2.get()), int(c2.get())]
  zz2 = (-normal[0] * xx - normal[1] * yy - d) * 1. / normal[2]

  # plot plane 3
  point = find_point(
    int(a3.get()),
    int(b3.get()), 
    int(c3.get()),
    int(d3.get()))
  normal = [int(a3.get()), int(b3.get()), int(c3.get())]
  zz3 = (-normal[0] * xx - normal[1] * yy - d) * 1. / normal[2]

  # test plot
  fig = plt.figure()
  plt3d = fig.add_subplot(111,projection='3d')
  plt3d.plot_surface(xx, yy, zz1)
  plt3d.plot_surface(xx, yy, zz2)
  plt3d.plot_surface(xx, yy, zz3)
  plt.show()

  # find the solution
  deter = get_determinant([a1, a2, a3], [b1, b2, b3], [c1, c2, c3])
  deter_x = get_determinant([d1, d2, d3], [b1, b2, b3], [c1, c2, c3])
  deter_y = get_determinant([a1, a2, a3], [d1, d2, d3], [c1, c2, c3])
  deter_z = get_determinant([a1, a2, a3], [b1, b2, b3], [d1, d2, d3])

  # Special cases
  if deter == 0:
    # No solution or infinte solution
    row1 = [int(a1.get()), int(b1.get()), int(c1.get()), int(d1.get())]
    row2 = [int(a2.get()), int(b2.get()), int(c2.get()), int(d2.get())]
    row3 = [int(a3.get()), int(b3.get()), int(c3.get()), int(d3.get())]
    if has_no_solutions(row1, row2, row3):
      output.insert(0, "Has no solutions.")
    else:
      output.insert(0, "Has infinite number of solutions.")
    
  else:
    sol_x = deter_x/deter
    sol_y = deter_y/deter
    sol_z = deter_z/deter

    output.insert(0, "The solution is x="+str(sol_x)+", y="+str(sol_y)+", z="+str(sol_z))


# this function would allow you to pull data from first_X field
# currently it is unused, and unneeded for this assignment
def enteredVal():
    return


# creation of entry fields
a1 = Entry(root, width=5, borderwidth=5, command=enteredVal())
a1_label = Label(root, text="X + ")

b1 = Entry(root, width=5, borderwidth=5)
b1_label = Label(root, text="Y + ")

c1 = Entry(root, width=5, borderwidth=5)
c1_label = Label(root, text="Z + ")

d1 = Entry(root, width=5, borderwidth=5)
d1_label = Label(root, text=" = 0")


a2 = Entry(root, width=5, borderwidth=5, command=enteredVal())
a2_label = Label(root, text="X + ")

b2 = Entry(root, width=5, borderwidth=5)
b2_label = Label(root, text="Y + ")

c2 = Entry(root, width=5, borderwidth=5)
c2_label = Label(root, text="Z + ")

d2 = Entry(root, width=5, borderwidth=5)
d2_label = Label(root, text=" = 0")


a3 = Entry(root, width=5, borderwidth=5, command=enteredVal())
a3_label = Label(root, text="X + ")

b3 = Entry(root, width=5, borderwidth=5)
b3_label = Label(root, text="Y + ")

c3 = Entry(root, width=5, borderwidth=5)
c3_label = Label(root, text="Z + ")

d3 = Entry(root, width=5, borderwidth=5)
d3_label = Label(root, text=" = 0")



# creation of output field
output = Entry(root,width=45,borderwidth=5,)

# output placement of entry field by row and column
a1.grid(row=0, column=0)
a1_label.grid(row=0, column=1, padx=1, pady=1)

b1.grid(row=0, column=2, padx=1, pady=1)
b1_label.grid(row=0, column=3, padx=1, pady=1)

c1.grid(row=0, column=4, padx=1, pady=1)
c1_label.grid(row=0, column=5, padx=1, pady=1)

d1.grid(row=0, column=6, padx=1, pady=1)
d1_label.grid(row=0, column=7, padx=1, pady=1)


a2.grid(row=1, column=0)
a2_label.grid(row=1, column=1, padx=1, pady=1)

b2.grid(row=1, column=2, padx=1, pady=1)
b2_label.grid(row=1, column=3, padx=1, pady=1)

c2.grid(row=1, column=4, padx=1, pady=1)
c2_label.grid(row=1, column=5, padx=1, pady=1)

d2.grid(row=1, column=6, padx=1, pady=1)
d2_label.grid(row=1, column=7, padx=1, pady=1)


a3.grid(row=2, column=0)
a3_label.grid(row=2, column=1, padx=1, pady=1)

b3.grid(row=2, column=2, padx=1, pady=1)
b3_label.grid(row=2, column=3, padx=1, pady=1)

c3.grid(row=2, column=4, padx=1, pady=1)
c3_label.grid(row=2, column=5, padx=1, pady=1)

d3.grid(row=2, column=6, padx=1, pady=1)
d3_label.grid(row=2, column=7, padx=1, pady=1)



# output placement of output field by row and column
output.grid(row=5, column=1, columnspan=8, padx=8, pady=8)
# We can have deault text in the input field to help the user enter info
a1.insert(0, "a1")
b1.insert(0, "b1")
c1.insert(0, "c1")
d1.insert(0, "d1")

a2.insert(0, "a2")
b2.insert(0, "b2")
c2.insert(0, "c2")
d2.insert(0, "d2")

a3.insert(0, "a3")
b3.insert(0, "b3")
c3.insert(0, "c3")
d3.insert(0, "d3")


button_1 = Button(root, text="process", padx="10", pady="10",command=plot_planes)
button_1.grid(row=5, column=0)

root.mainloop()
