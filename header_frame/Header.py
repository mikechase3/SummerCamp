"""Header"""
import tkinter as tk
import os
from tkinter import ttk


class Header(ttk.Frame):
  # Instance Variables

  # Custom Methods
  @staticmethod
  def find_photo():
    """
    Gets the path of the current directory and points to wherever the photo should be.
    TODO: IMPLEMENT/FIX because it's broken?
    """
    path = os.getcwd().split('/')
    if path[-1] == "SummerCamp":
      path = os.getcwd().join("header_frame").join("logo.png")
    elif (path[-1] == "header_frame"):
      path = os.getcwd().join("logo.png")
    else:
      raise FileNotFoundError("Cannot find logo")
    return "header_frame/logo.png"

  # Magic Methods
  def __init__(self, parent, *args, **kwargs):

    # Function Variables

    # System
    super().__init__(parent, *args, **kwargs)

    # Layout
    photo_path = self.find_photo()
    pi_logo = tk.PhotoImage(file=photo_path)
    l_logo = tk.Label(self, image=pi_logo, bg="light blue")
    l_logo.pack(side=tk.LEFT)

    l_program = ttk.Label(self,
                          text="STEM Summer Camp",
                          font=('Arial', 24, 'bold'))
    l_program.pack(side=tk.LEFT)


if __name__ == "__main__":
  root = tk.Tk()
  instance_header = Header(root)
  instance_header.pack()
  root.mainloop()
