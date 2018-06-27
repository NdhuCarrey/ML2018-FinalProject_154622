import numpy as np
from keras.models import Sequential, load_model
from keras.layers import Dense, Activation, Conv2D, MaxPooling2D, Flatten, Dropout
from keras.utils import to_categorical
from PIL import Image, ImageTk
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
    model.fit(x, y, epochs=15, batch_size=50)
    model.save('my_model.h5')


def evaluate(x, y):
    global model
    score = model.evaluate(x, y)
    var1 = score[0]
    var2 = score[1]
    label1.config(bg='white',text= "Test data Evaluate")
    label2.config(bg='white',text= "Total loss: " + str(var1))
    label3.config(bg='white',text= "Accuracy: {0}".format(str(var2)))


def testingload():
    global test_x, test_y
    global model
    filesname = filedialog.askopenfilenames(initialdir="/", title="Select file",
                                          filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    fileslist = list(filesname)
    k ,test_x, test_y = Load(fileslist)
    evaluate(test_x, test_y)

def trainingload():
    global tx,x, y
    global model
    global filesname
    global face
    
    filesname = filedialog.askopenfilenames(initialdir="/", title="Select file",
                                            filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    label.config(bg='gray80', text= "Loading...")
    fileslist = list(filesname)
    tx,x, y = Load(fileslist)
    
    for i in tx:
        face.append(ImageTk.PhotoImage(Image.fromarray(i)))
        
    Model(x)
    train(x, y)
    label.config(bg='gray80', text= "Load test images / image")
    
def predict():
    global model
    global x
    global tx
    global panel
    global face
    global canvas
    label.config(bg='gray80', text= "Loading...")
    label1.config(bg='gray80',text= "")
    label2.config(bg='gray80',text= "")
    label3.config(bg='gray80',text= "")
    test = []
    filesname = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("jpeg files", "*.jpg"),("all files", "*.*")))
    test.append(np.array(Image.open(filesname).resize((100, 150))))
    test = np.array(test)
    test = test/255.0
    ac = model.predict(test)
    a = np.argsort(ac[0])[-1:-6:-1]
    temp = 1
    label4.config(bg='white', text= str(ac[0][a] * 100))

    temp = 1
    for i in a:
        canvas.itemconfig(temp,image=face[i*13])
        temp = temp+1 
    label.config(bg='gray80', text= "Load test images / image")

model = Sequential()
x = []
y = []
tx =[]
test_x = []
test_y = []
face = []
win = Tk.Tk()
win.title("Final Project")
win.geometry("500x350")
win.configure(background="gray80")
 

label = Tk.Label(win, text="Choose training pictures from your computer!")
label.config(bg='gray80', text= "Choose training pictures from your computer!")
label.pack()
label1 = Tk.Label(win, text ="")
label2 = Tk.Label(win, text ="")
label3 = Tk.Label(win, text ="")
label4 = Tk.Label(win, text ="")
label1.config(bg='gray80',text= " ")
label2.config(bg='gray80',text= " ")
label3.config(bg='gray80',text= " ")
label4.config(bg='gray80',text= " ")
label1.pack()
label2.pack()
label3.pack()
label4.pack()

xbutton = Tk.Button(win, text="Load Images & Training", width = 20, bg = 'pink', command=trainingload)
ybutton = Tk.Button(win, text="Load Images & Testing", width = 20, bg = 'moccasin', command=testingload)
zbutton = Tk.Button(win, text="Load a Testing Image!", width = 20, bg = 'skyblue',  command=predict)
zbutton.pack(side=Tk.BOTTOM)
ybutton.pack(side=Tk.BOTTOM)
xbutton.pack(side=Tk.BOTTOM)
    

canvas=Tk.Canvas(win,bg='blue',height=150,width=520)
im = Image.new('RGB',(100, 150))
img = ImageTk.PhotoImage(im)
pos =0
for i in range(5):
    canvas.create_image(pos,0,image=img, anchor='nw')
    pos += 100
canvas.pack(side=Tk.BOTTOM)

win.mainloop()

