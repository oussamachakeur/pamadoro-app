from tkinter import *
import time 
reps = 0
my_timer=None
import math



window = Tk()
window.title("pamadoro")
window.minsize(500 ,500 )
window.config(padx=100 ,pady=100 , bg='#000000')



def start_count():
    global reps
    reps+=1

    WORk_sec = 20 *60
    short_break= 5*60
    long_break = 20*60

    if reps% 8 == 0:
        count_down(long_break) 
        timer.config(text="BREAK" , fg="green")

    elif reps %2 ==0:
        count_down(short_break)
        timer.config(text="BREAK" , fg="pink")
    else:
        count_down(WORk_sec)
        timer.config(text="WORK" , fg="red")

def reset_timer():
    window.after_cancel(my_timer)
    canvas.itemconfigure(time_text , text="00:00")
    check_mark.config(text="")
    global reps 
    reps = 0

    
        


#####################################################33

canvas= Canvas(width=300 , height=300 , bg="#000000" , highlightthickness=0)
pic=PhotoImage(file='C:/Users/lenovo/Desktop/python bootcamp/PROJECTS/intermediat/download.png ')
canvas.create_image(150,150 ,image=pic)
time_text=canvas.create_text(150,180 , text="00:00",fill="yellow", font=("alias",24,"bold"))
canvas.grid(column=1,row=1)


#############buttom#########
start_buttom = Button(text="start" ,command=start_count, highlightthickness=0 ,fg="yellow" , bg="black" ,font=("alias" , 15 , 'bold'))
start_buttom.grid(column=0,row=2)

reset_buttom = Button(text="reset",highlightthickness=0,command=reset_timer, fg="yellow" , bg="black",font=("alias" , 15 , 'bold'))
reset_buttom.grid(column=2,row=2)
##############################

timer= Label(text="Timer" , font=("alias" ,24,'bold' ) , fg="yellow" ,bg="black",)
timer.grid(column=1,row=0)


check_mark= Label(text="" ,highlightthickness=0 ,font=("alias" ,24 ,"bold") ,fg="yellow" , bg="black" )
check_mark.grid(column=1 , row=2)



#########################################################################333
def count_down(count):
    count_min= math.floor(count/60)
    count_sec = count % 60
    if count_sec ==0:
        count_sec="00"
    elif count_sec <10:
        count_sec=f"0{count_sec}"
    elif count_min <10 :
        count_min=f"0{count_min}"

    canvas.itemconfig(time_text , text=f"{count_min}:{count_sec}")
    if count>0:
        global my_timer
        my_timer=window.after(1000 , count_down , count-1)

    else :
        start_count()
        mark =""
        for _ in range(math.floor(reps/2)):
            mark+="☑"
        check_mark.config(text=mark)
















window.mainloop() 

