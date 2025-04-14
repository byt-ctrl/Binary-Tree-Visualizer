# START
from PIL import ImageGrab  # for capturing images
import tkinter as tk # for gui
from tkinter import messagebox,filedialog # for message box and file dialog



""" -------------------------- Binary Search Tree Classes -------------------------- """
    
 

class tree_nodes :
    def __init__(self, value) :
        self.value=value
        self.left_child=None
        self.right_child=None


class binary_search_tree :
    def __init__(self) :
        self.root=None  # Starting root of the tree

    # Insert a value into the tree (METHOD)

    def insert(self,value) :
        def recursive(current_node,value) :
            if current_node is None :  # if current node is empty , create a new node
                return tree_nodes(value)
            
            # if value is less than current node's value , goes to the left subtree
            if value<current_node.value :
                current_node.left_child = recursive(current_node.left_child, value)

            # if value is greater than current node's value , goes to the right subtree
            else :

                current_node.right_child=recursive(current_node.right_child,value)
            return current_node  # return the current node after insertion

        self.root=recursive(self.root , value)  # insert the value starting from the root

    # for clearing the tree (METHOD)
    def clear(self) :
        self.root = None  


"""  --------------------------  GUI Tree Visualizer  -------------------------- """

class tree_visualizer:
    def __init__(self,tree) :
        self.tree=tree  
        self.window=tk.Tk()  
        self.window.title(" Binary Search Tree Visualizer ")

        # canvas
        self.canvas=tk.Canvas(self.window,width=900,height=700,bg="white") # canvas width and height can be change as per requirement
        self.canvas.pack()

       # frame
        self.control_frame=tk.Frame(self.window)
        self.control_frame.pack()

        # input field for value
        self.value_entry=tk.Entry(self.control_frame,width=11)
        self.value_entry.pack(side=tk.LEFT,padx=6)

        # button to insert value into the tree
        self.insert_button=tk.Button(self.control_frame,text=" Insert Value ",command=self.insert_value)
        self.insert_button.pack(side=tk.LEFT,padx=6)

        # button for clearing the tree
        self.clear_button=tk.Button(self.control_frame, text=" Clear Tree ",command=self.clear_tree)
        self.clear_button.pack(side=tk.LEFT,padx=6)

        # Button to save the tree as an image
        self.save_button=tk.Button(self.control_frame, text=" Save Tree as Image ",command=self.saving_tree_locally)
        self.save_button.pack(side=tk.LEFT,padx=6)




    # insert value into the tree (METHOD)
    def insert_value(self) :
        try:
            value=self.value_entry.get()
            if value.isdigit() :                     # checking if the value is a digit
                self.tree.insert(int(value))         # inserting the value in tree
                self.value_entry.delete(0,tk.END)    # clear input field
                self.redraw_tree()                   # redraw the tree on canvas
                
            else :
                raise ValueError(" Please enter a valid integer. ")  # error raise if value is not a digit
        except ValueError as error:
            messagebox.showerror("Invalid Input",str(error))          # dialog box for error message

    # redraw the tree on canvas (METHOD)

    def redraw_tree(self) : 
        self.canvas.delete("all")                         # clears exsisting drawing on canvas
        if self.tree.root :                                # if there is root node in tree it will draw the tree afterwards
            self._draw_node(self.tree.root,500,50,250)

    # recursive method to draw the tree nodes and lines (METHOD)

    def _draw_node(self,node,x,y,x_offset) :
        node_radius=20  # radius of the node circle
        self.canvas.create_oval(x-node_radius,y-node_radius,x+node_radius,y+node_radius,fill="lightgreen")
        self.canvas.create_text(x,y,text=str(node.value),font=("Arial",14)) 

        # draw the left child if it exists
        if node.left_child :
            x_left=x-x_offset                                                    # calculate new position for the left child
            y_left=y+80                                                          # adjust vertical position
            self.canvas.create_line(x,y+node_radius,x_left,y_left-node_radius)   # draw line to left child
            self._draw_node(node.left_child,x_left,y_left,x_offset//2)           # recursive call to draw left child

        # draw the right child if it exists
        if node.right_child :
            x_right=x+x_offset                                                    # calculate new position for the right child
            y_right=y+80                                                          # adjust vertical position
            self.canvas.create_line(x,y+node_radius,x_right,y_right-node_radius)  # draw line to right child
            self._draw_node(node.right_child,x_right,y_right,x_offset//2)    # recursive call to draw right child




    # save the tree as an image (METHOD)

    def saving_tree_locally(self) :
        
        filename=filedialog.asksaveasfilename(defaultextension=".png",filetypes=[(" PNG files ","*.png")])
        if not filename :
            return 

        # coordinates of the canvas to capture the image
        x=self.window.winfo_rootx()+self.canvas.winfo_x()
        y=self.window.winfo_rooty()+self.canvas.winfo_y()
        x1=x+self.canvas.winfo_width()
        y1=y+self.canvas.winfo_height()

       # capture the image of the canvas and save it
        ImageGrab.grab().crop((x,y,x1,y1)).save(filename)
        print(f" Tree saved as {filename} ")




    # clear the tree (METHOD)

    def clear_tree(self) :
        self.tree.clear()   # clear the tree
        self.redraw_tree()  # redraw the canvas to show the cleared tree

    
    def run(self) :
        self.window.mainloop()


"""   -------------------------- RUN THE APPLICATION -------------------------- """


if __name__=="__main__" :
    binary_tree=binary_search_tree() 
    visualizer=tree_visualizer(binary_tree)
    visualizer.run()


# END

