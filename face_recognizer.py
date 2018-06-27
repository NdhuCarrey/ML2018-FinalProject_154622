
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
from keras.models import Sequential, load_model
from keras.layers import Dense, Activation, Conv2D, MaxPooling2D, Flatten, Dropout
from keras.utils import to_categorical
from PIL import Image, ImageTk
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import tkinter as Tk
from tkinter import filedialog


def Load(x_data):
    x = []
    for data in x_data:
        f = np.array(Image.open(data).resize((100, 150)))
        x.append(f)
    x = np.array(x)
    tx = x / 255.0
    print(len(x_data))
    y = [i for i in range(50) for j in range((int)(x.shape[0] / 50))]
    y = to_categorical(y, num_classes=50)
    y = np.array(y)
    return x,tx, y


def Model(x):
    global model

    model.add(Conv2D(8, (3, 3), input_shape=x[0].shape, padding='same', activation='relu'))
    model.add(Dropout(0.25))
    model.add(MaxPooling2D((2, 2)))

    model.add(Conv2D(16, (3, 3), padding='same', activation='relu'))
    model.add(Dropout(0.25))
    model.add(MaxPooling2D((2, 2)))

    model.add(Flatten())
    model.add(Dense(units=1024, activation='relu'))
    model.add(Dropout(0.25))
    model.add(Dense(units=50, activation='softmax'))
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])


def train(x, y):
    global model
    model.fit(x, y, epochs=1, batch_size=50)
    model.save('my_model.h5')


def evaluate(x, y):
    global model
    score = model.evaluate(x, y)
    var1 = score[0]
    var2 = score[1]
    Tk.Label(win, text ="Test data Evaluate").pack()
    Tk.Label(win, text="Total loss: " + str(var1)).pack()
    Tk.Label(win, text="Accuracy: {0}".format(str(var2))).pack()

def predict():
    global model
    global x,tx
    global panel

    im = Image.fromarray(tx[0])
    img = ImageTk.PhotoImage(im)
    canvas.itemconfig(face[0],image=img)
#     test = []
#     filesname = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("jpeg files", "*.jpg"),("all files", "*.*")))
#     test.append(np.array(Image.open(filesname).resize((100, 150))))
#     test = np.array(test)
#     test = test/255.0
#     ac = model.predict(test)
#     a = np.argsort(ac[0])[-1:-6:-1]
#     temp = 1
#     Tk.Label(win, text = str(ac[0][a] * 100)).pack()
    
#     temp = 0
#     for i in a:
#         print(i)
#         im = Image.fromarray(tx[i*13])
#         img = ImageTk.PhotoImage(im)
#         canvas.itemconfig(face[temp],image=img)
#         temp = temp+1

    
def trainingload():
    global tx,x, y
    global model
    global filesname
    
  
   
    
    filesname = filedialog.askopenfilenames(initialdir="/", title="Select file",
                                            filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    # label.configure(text = win.filename)
    fileslist = list(filesname)
    tx,x, y = Load(fileslist)
    Model(x)
    train(x, y)
   # ybutton.pack(side=Tk.BOTTOM)
    label.config(bg='gray80', text= " ")
    #xbutton.forget()


def testingload():
    global test_x, test_y
    global model
    filesname = filedialog.askopenfilenames(initialdir="/", title="Select file",
                                          filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    # label.configure(text = win.filename)
    fileslist = list(filesname)
    test_x, test_y = Load(fileslist)
    evaluate(test_x, test_y)
   # zbutton.pack(side=Tk.BOTTOM)
   # label.config(text="Choose a testing picture from your computer!")
   # label.destroy()
    #ybutton.forget()


model = Sequential()
x = []
y = []
tx =[]
test_x = []
test_y = []
win = Tk.Tk()
win.title("Final Project")
win.geometry("500x300")
win.configure(background="gray80")
 



label = Tk.Label(win, text="Choose training pictures from your computer!")
xbutton = Tk.Button(win, text="Load Images & Training", width = 20, bg = 'pink', command=trainingload)
ybutton = Tk.Button(win, text="Load Images & Testing", width = 20, bg = 'moccasin', command=testingload)
zbutton = Tk.Button(win, text="Load a Testing Image!", width = 20, bg = 'skyblue',  command=predict)
label.pack()
zbutton.pack(side=Tk.BOTTOM)
ybutton.pack(side=Tk.BOTTOM)
xbutton.pack(side=Tk.BOTTOM)



face = []
pos =0
canvas=Tk.Canvas(win,bg='blue',height=150,width=520)
im = Image.new('RGB',(100, 150))
img = ImageTk.PhotoImage(im)
for i in range(5):
   
    g = canvas.create_image(pos,0,anchor='nw',image=img)
    face.append(g)
    pos += 100

canvas.pack(side=Tk.BOTTOM)

win.mainloop()

