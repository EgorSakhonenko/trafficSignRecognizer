import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy
#load the trained model to classify sign
from keras.models import load_model
model = load_model('traffic_classifier.h5')
classes = { 1:'Ограничение скорости (20 км/ч)',
            2:'Ограничение скорости (30 км/ч)',
            3:'Ограничение скорости (50 км/ч)',
            4:'Ограничение скорости (60 км/ч)',
            5:'Ограничение скорости (70 км/ч)',
            6:'Ограничение скорости (80 км/ч)',
            7:'Конец ограничения скорости (80 км/ч)',
            8:'Ограничение скорости (100 км/ч)',
            9:'Ограничение скорости (120 км/ч)',
           10:'Обгон запрещен',
           11:'Обгон грузовым автомобилям запрещен',
           12:'Пересечение со второстепенной дорогой',
           13:'Главная дорога',
           14:'Уступи дорогу',
           15:'Движение без остановки - запрещено',
           16:'Движение - запрещено',
           17:'Движение грузовых автомобилей - запрещено',
           18:'Въезд запрещен',
           19:'Прочие опасности',
           20:'Опасный поворот налево',
           21:'Опасный поворот направо',
           22:'Опасные повороты',
           23:'Неровная дорога',
           24:'Скользкая дорога',
           25:'Сужение дороги',
           26:'Дорожные работы',
           27:'Светофорное регулирование',
           28:'Пешеходный переход',
           29:'Осторожно - дети',
           30:'Велопешеходная дорожка',
           31:'Осторожно лед/снег',
           32:'Дикие животные',
           33:'Конец зоны всех ограничений',
           34:'Движение направо',
           35:'Движение налево',
           36:'движение прямо',
           37:'Движение прямо или направо',
           38:'Движение прямо или налево',
           39:'Объезд препятствия справа',
           40:'Объезд препятствия слева',
           41:'Круговое движение',
           42:'Конец зоны запрещения обгона',
           43:'Конец зоны запрещения обгона грузовым автомобилям' }
#initialise GUI
top=tk.Tk()
top.geometry('600x600')
top.title('Определение дорожного знака')
top.configure(background='#CDCDCD')
label=Label(top,background='#CDCDCA', font=('arial',20,'bold'))
sign_image = Label(top)

def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30,30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    print(image.shape)
    pred = model.predict_classes([image])[0]
    sign = classes[pred+1]
    print(sign)
    label.configure(foreground='#011638', text=sign)
def show_classify_button(file_path):
    classify_b=Button(top,text="Определить знак",command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#367156', foreground='blue',font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)
def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass
upload=Button(top,text="Загрузить изображение",command=upload_image,padx=10,pady=5)
upload.configure(background='#364159', foreground='red',font=('arial',10,'bold'))
upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Определение дорожного знака",pady=20, font=('arial',20,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
top.mainloop()
