import tkinter as tk
from tkinter import *



root= tk.Tk()
width=root.winfo_screenwidth()
height=root.winfo_screenheight()

root.geometry("%dx%d" % (width,height))
root.title("Cafe Menu")
root.config(bg='#bc6c25')


cs=tk.Label(root, text='Sunrise Cafe', font=('Arial',35,'bold'),fg='black',bg='#dda15e')
cs.place(x=610,y=30)





lft=tk.Frame(root, bg='#ffecd1')
lft.place(x=40,y=150,width=450,height=600)
middle=tk.Frame(root, bg='#ffecd1')
middle.place(x=530,y=150,width=450,height=600)
right=tk.Frame(root, bg='#ffecd1')
right.place(x=1020,y=150,width=450,height=600)



# =============================================================================
# e1=eoe_e.get()
# e2=cc_e.get()
# e3=fc_e.get()
# e4=cl_e.get()
# e5=ic_e.get()
# e6=tc_e.get()
# e7=vc_e.get()
# e8=tl_e.get()
# e9=mac_e.get()
# e10=ca_e.get()
# e11=cm_e.get()
# e12=ac_e.get()
# e13=ec_e.get()
# =============================================================================

eoe_v=tk.IntVar()
cc_v=tk.IntVar()
fc_v=tk.IntVar()
cl_v=tk.IntVar()
ic_v=tk.IntVar()
tc_v=tk.IntVar()
vc_v=tk.IntVar()
tl_v=tk.IntVar()
mac_v=tk.IntVar()
ca_v=tk.IntVar()
cm_v=tk.IntVar()
ac_v=tk.IntVar()
ec_v=tk.IntVar()
tot1_v=tk.IntVar()
tot2_v=tk.IntVar()
tot_v=tk.IntVar()
cod_v=tk.StringVar()
gtot_v=tk.IntVar()
op1_v=BooleanVar()


class calall:
        def __init__ (self,name,realPrice,price):
            self.name=name
            self.realPrice=realPrice
            self.priceMark=price
            
            
        def calcs(self):
            
            if int(self.name) == 0 or str(self.name) == '':
                self.price=0
            else:
                self.price=(int(self.name))*self.realPrice
                
                
                

#======================== Functions =====================================================

def calculate():
    #================ bringing all values for calculations ==============================
    listbox1_string="__________________________________________________________________"
    listbox1.insert(1,listbox1_string)
                
    c1=calall(eoe_v.get(),98,0)
    c2=calall(cc_v.get(),110,0)
    c3=calall(fc_v.get(),110,0)
    c4=calall(cl_v.get(),115,0)
    c5=calall(ic_v.get(),139,0)
    c6=calall(tc_v.get(),133,0)
    c7=calall(vc_v.get(),133,0)
    c8=calall(tl_v.get(),144,0)
    c9=calall(mac_v.get(),121,0)
    c10=calall(ca_v.get(),124,0)
    c11=calall(cm_v.get(),139,0)
    c12=calall(ac_v.get(),159,0)
    c13=calall(ec_v.get(),159,0)
    
    
    c1.calcs()
    c2.calcs()
    c3.calcs()
    c4.calcs()
    c5.calcs()
    c6.calcs()
    c7.calcs()
    c8.calcs()
    c9.calcs()
    c10.calcs()
    c11.calcs()
    c12.calcs()
    c13.calcs()
    
    
        
    #===================== menu 1, menu 2 and total calculations =============================
        
    menu1_sum= c1.price + c2.price + c3.price + c4.price + c5.price + c6.price + c7.price + c8.price
    menu2_sum= c9.price + c10.price + c11.price + c12.price + c13.price
    
    tot1_v.set(menu1_sum)
    tot2_v.set(menu2_sum)
    total=menu1_sum+menu2_sum
    tot_v.set(total)

    
    
    #==================== Coupon code discount calculation =========================================
    
    cod_lst=['CAFBTGKP','CAF3BH7P','CAFBAAAH','CAFCDZX6','CAF4XERP','CAF7NO5Z','CAFDNGJH','CAFWP52X','CAFSD8YK','CAFN4Q4W']
    
    
    disc=0
    if cod_e.get() == '':
        disc=0
    else:
        x=cod_e.get()
        if x not in cod_lst:
            tk.messagebox.showerror('Error','This coupon code is expired or does not exist')
        else:
            disc=10
            
            
            
    #================== parcel checkbox calculations ==========================================
    
    if (op1_v.get() == 1):
        parc_cost=20
    else:
        parc_cost=0
        
    
    
    #================ Final Price Calculations ================================================
    
    
    grand_tot= (total-(total*(disc/100)))+parc_cost
    gtot_v.set(grand_tot)
    
    #================ Listbox ==================================================================
    
    op_list=[]
    
    menu_list={'Eye_Opener_Espresso':[(eoe_v.get()),c1.price],
                   'Classic_Cappuccino':[(cc_v.get()),c2.price],
                   'Filter_Coffee':[(fc_v.get()),c3.price],
                   'Cafe_Latte':[(cl_v.get()),c4.price],
                   'Inverted_Cappuccino':[(ic_v.get()),c5.price],
                   'Toffee_Cappuccino':[(tc_v.get()),c6.price],
                   'Vanilla_Cappuccino':[(vc_v.get()),c7.price],
                   'Toffee_Latte':[(tl_v.get()),c8.price],
                   'Macchiato':[(mac_v.get()),c9.price],
                   'Cafe_Americano':[(ca_v.get()),c10.price],
                   'Cafe_Mocha':[(cm_v.get()),c11.price],
                   'Aztec_Coffee':[(ac_v.get()),c12.price],
                   'Ethiopian_Coffee':[(ec_v.get()),c13.price]}
    for i,j in menu_list.items():
        if int(j[0])>0:
            a=[i,j[1],j[0]]
            op_list.append(a)
    print(op_list)
            
          
    for p in op_list:
        n=op_list.index(p)
        print(n)
        list_text=('{:-<30s} {} ------ {}'.format(p[0], p[2], (p[1])))
        print(list_text)
        listbox1.insert(n+1,list_text)
    parcel_text='{:-<30s} --------------- {}'.format('Parcel',parc_cost)
    total_text='{:-<30s} --------------- {}'.format('total',grand_tot)
    listbox1.insert((len(op_list)+1),parcel_text)
    listbox1.insert((len(op_list)+2),total_text)
    
    #========================== Function Ends =================================================

def clear():
    eoe_v.set(0)
    cc_v.set(0)
    fc_v.set(0)
    cl_v.set(0)
    ic_v.set(0)
    tc_v.set(0)
    vc_v.set(0)
    tl_v.set(0)
    mac_v.set(0)
    ca_v.set(0)
    cm_v.set(0)
    ac_v.set(0)
    ec_v.set(0)
    tot1_v.set(0)
    tot2_v.set(0)
    tot_v.set(0)
    cod_v.set('')
    gtot_v.set(0)
    op1_v.set(False)
    




def plus(x,z):
    if(x.get()) == '':
        z.set(0)
    if int(x.get()) >= 0 :
        y=(int(x.get()))+1
        (z.set(y))
    
        
def minus(x,z):
    if (x.get()) == '':
        (z.set(1))
    if int(x.get()) >= 1:
        y=(int(x.get()))-1
        (z.set(y))
    
        
        
def one_plus():
    plus(eoe_e,eoe_v)
def one_minus():
    minus(eoe_e,eoe_v)
    
def two_plus():
    plus(cc_e,cc_v)
def two_minus():
    minus(cc_e,cc_v)
    
def three_plus():
    plus(fc_e,fc_v)
def three_minus():
    minus(fc_e,fc_v)   

def four_plus():
    plus(cl_e,cl_v)
def four_minus():
    minus(cl_e,cl_v)
    
def five_plus():
    plus(ic_e,ic_v)
def five_minus():
    minus(ic_e,ic_v)
    
def six_plus():
    plus(tc_e,tc_v)
def six_minus():
    minus(tc_e,tc_v)    


def seven_plus():
    plus(vc_e,vc_v)
def seven_minus():
    minus(vc_e,vc_v)
    
def eight_plus():
    plus(tl_e,tl_v)
def eight_minus():
    minus(tl_e,tl_v)
    
def nine_plus():
    plus(mac_e,mac_v)
def nine_minus():
    minus(mac_e,mac_v)

def ten_plus():
    plus(ca_e,ca_v)
def ten_minus():
    minus(ca_e,ca_v)
    
def eleven_plus():
    plus(cm_e,cm_v)
def eleven_minus():
    minus(cm_e,cm_v)
    
def twelve_plus():
    plus(ac_e,ac_v)
def twelve_minus():
    minus(ac_e,ac_v)
    
def thirteen_plus():
    plus(ec_e,ec_v)
def thirteen_minus():
    minus(ec_e,ec_v)



        
            





#====================== all time classics ==================================================


title1=tk.Label(lft, text='All Time Classics', font=('Arial',25,'bold'),fg='black',bg='#dda15e')
title1.place(x=80,y=10)

eoe=tk.Label(lft, text='Eye_Opener Espresso', font=('Times New Roman',14,'bold'),fg='black',bg='#ffecd1')
eoe.place(x=10,y=100)
eoe_e=tk.Entry(lft, textvariable=eoe_v, font=('Times New Roman',12,'bold'),fg='black')
eoe_e.place(x=200,y=100)


cc=tk.Label(lft, text='Classic Cappuccino', font=('Times New Roman',14,'bold'),fg='black',bg='#ffecd1')
cc.place(x=10,y=140)
cc_e=tk.Entry(lft, textvariable=cc_v, font=('Times New Roman',12,'bold'),fg='black')
cc_e.place(x=200,y=140)


fc=tk.Label(lft, text='Filter Coffee', font=('Times New Roman',14,'bold'),fg='black',bg='#ffecd1')
fc.place(x=10,y=180)
fc_e=tk.Entry(lft, textvariable=fc_v, font=('Times New Roman',12,'bold'),fg='black')
fc_e.place(x=200,y=180)


cl=tk.Label(lft, text='Cafe Latte', font=('Times New Roman',14,'bold'),fg='black',bg='#ffecd1')
cl.place(x=10,y=220)
cl_e=tk.Entry(lft, textvariable=cl_v, font=('Times New Roman',12,'bold'),fg='black')
cl_e.place(x=200,y=220)

ic=tk.Label(lft, text='Inverted Cappuccino', font=('Times New Roman',14,'bold'),fg='black',bg='#ffecd1')
ic.place(x=10,y=260)
ic_e=tk.Entry(lft, textvariable=ic_v, font=('Times New Roman',12,'bold'),fg='black')
ic_e.place(x=200,y=260)

tc=tk.Label(lft, text='Toffee Cappuccino', font=('Times New Roman',14,'bold'),fg='black',bg='#ffecd1')
tc.place(x=10,y=300)
tc_e=tk.Entry(lft, textvariable=tc_v, font=('Times New Roman',12,'bold'),fg='black')
tc_e.place(x=200,y=300)

vc=tk.Label(lft, text='Vanilla Cappuccino', font=('Times New Roman',14,'bold'),fg='black',bg='#ffecd1')
vc.place(x=10,y=340)
vc_e=tk.Entry(lft, textvariable=vc_v, font=('Times New Roman',12,'bold'),fg='black')
vc_e.place(x=200,y=340)

tl=tk.Label(lft, text='Toffee Latte', font=('Times New Roman',14,'bold'),fg='black',bg='#ffecd1')
tl.place(x=10,y=380)
tl_e=tk.Entry(lft, textvariable=tl_v, font=('Times New Roman',12,'bold'),fg='black')
tl_e.place(x=200,y=380)


#======================== Selections =================================================


title2=tk.Label(middle, text='Selections', font=('Arial',25,'bold'),fg='black',bg='#dda15e')
title2.place(x=130,y=10)

mac=tk.Label(middle, text='Macchiato', font=('Times New Roman',14,'bold'),fg='black',bg='#ffecd1')
mac.place(x=10,y=100)
mac_e=tk.Entry(middle, textvariable=mac_v, font=('Times New Roman',12,'bold'),fg='black')
mac_e.place(x=200,y=100)


ca=tk.Label(middle, text='Cafe Americano', font=('Times New Roman',14,'bold'),fg='black',bg='#ffecd1')
ca.place(x=10,y=140)
ca_e=tk.Entry(middle, textvariable=ca_v, font=('Times New Roman',12,'bold'),fg='black')
ca_e.place(x=200,y=140)


cm=tk.Label(middle, text='Cafe Mocha', font=('Times New Roman',14,'bold'),fg='black',bg='#ffecd1')
cm.place(x=10,y=180)
cm_e=tk.Entry(middle, textvariable=cm_v, font=('Times New Roman',12,'bold'),fg='black')
cm_e.place(x=200,y=180)


ac=tk.Label(middle, text='Aztec Coffee', font=('Times New Roman',14,'bold'),fg='black',bg='#ffecd1')
ac.place(x=10,y=220)
ac_e=tk.Entry(middle, textvariable=ac_v, font=('Times New Roman',12,'bold'),fg='black')
ac_e.place(x=200,y=220)

ec=tk.Label(middle, text='Ethiopian Coffee', font=('Times New Roman',14,'bold'),fg='black',bg='#ffecd1')
ec.place(x=10,y=260)
ec_e=tk.Entry(middle, textvariable=ec_v, font=('Times New Roman',12,'bold'),fg='black')
ec_e.place(x=200,y=260)


#================== plus minus buttons ================================================

eoe_p=tk.Button(lft, text=' + ', font=('Times New Roman',10,'bold'),fg='black',bg='#dda15e', command=one_plus)
eoe_p.place(x=370,y=100)

eoe_m=tk.Button(lft, text=' - ', font=('Times New Roman',10,'bold'),fg='black',bg='#dda15e', command=one_minus)
eoe_m.place(x=400,y=100)


cc_p=tk.Button(lft, text=' + ', font=('Times New Roman',10,'bold'),fg='black',bg='#dda15e',command=two_plus)
cc_p.place(x=370,y=140)

cc_m=tk.Button(lft, text=' - ', font=('Times New Roman',10,'bold'),fg='black',bg='#dda15e',command=two_minus)
cc_m.place(x=400,y=140)


fc_p=tk.Button(lft, text=' + ', font=('Times New Roman',10,'bold'),fg='black',bg='#dda15e',command=three_plus)
fc_p.place(x=370,y=180)

fc_m=tk.Button(lft, text=' - ', font=('Times New Roman',10,'bold'),fg='black',bg='#dda15e',command=three_minus)
fc_m.place(x=400,y=180)

cl_p=tk.Button(lft, text=' + ', font=('Times New Roman',10,'bold'),fg='black',bg='#dda15e',command=four_plus)
cl_p.place(x=370,y=220)

cl_m=tk.Button(lft, text=' - ', font=('Times New Roman',10,'bold'),fg='black',bg='#dda15e',command=four_minus)
cl_m.place(x=400,y=220)


ic_p=tk.Button(lft, text=' + ', font=('Times New Roman',10,'bold'),fg='black',bg='#dda15e',command=five_plus)
ic_p.place(x=370,y=260)

ic_m=tk.Button(lft, text=' - ', font=('Times New Roman',10,'bold'),fg='black',bg='#dda15e',command=five_minus)
ic_m.place(x=400,y=260)


tc_p=tk.Button(lft, text=' + ', font=('Times New Roman',10,'bold'),fg='black',bg='#dda15e',command=six_plus)
tc_p.place(x=370,y=300)

tc_m=tk.Button(lft, text=' - ', font=('Times New Roman',10,'bold'),fg='black',bg='#dda15e',command=six_minus)
tc_m.place(x=400,y=300)


vc_p=tk.Button(lft, text=' + ', font=('Times New Roman',10,'bold'),fg='black',bg='#dda15e',command=seven_plus)
vc_p.place(x=370,y=340)

vc_m=tk.Button(lft, text=' - ', font=('Times New Roman',10,'bold'),fg='black',bg='#dda15e',command=seven_minus)
vc_m.place(x=400,y=340)


tl_p=tk.Button(lft, text=' + ', font=('Times New Roman',10,'bold'),fg='black',bg='#dda15e',command=eight_plus)
tl_p.place(x=370,y=380)

tl_m=tk.Button(lft, text=' - ', font=('Times New Roman',10,'bold'),fg='black',bg='#dda15e',command=eight_minus)
tl_m.place(x=400,y=380)


mac_p=tk.Button(middle, text=' + ', font=('Times New Roman',10,'bold'),fg='black',bg='#dda15e',command=nine_plus)
mac_p.place(x=370,y=100)

mac_m=tk.Button(middle, text=' - ', font=('Times New Roman',10,'bold'),fg='black',bg='#dda15e',command=nine_minus)
mac_m.place(x=400,y=100)

ca_p=tk.Button(middle, text=' + ', font=('Times New Roman',10,'bold'),fg='black',bg='#dda15e',command=ten_plus)
ca_p.place(x=370,y=140)

ca_m=tk.Button(middle, text=' - ', font=('Times New Roman',10,'bold'),fg='black',bg='#dda15e',command=ten_minus)
ca_m.place(x=400,y=140)


cm_p=tk.Button(middle, text=' + ', font=('Times New Roman',10,'bold'),fg='black',bg='#dda15e',command=eleven_plus)
cm_p.place(x=370,y=180)

cm_m=tk.Button(middle, text=' - ', font=('Times New Roman',10,'bold'),fg='black',bg='#dda15e',command=eleven_minus)
cm_m.place(x=400,y=180)


ac_p=tk.Button(middle, text=' + ', font=('Times New Roman',10,'bold'),fg='black',bg='#dda15e',command=twelve_plus)
ac_p.place(x=370,y=220)

ac_m=tk.Button(middle, text=' - ', font=('Times New Roman',10,'bold'),fg='black',bg='#dda15e',command=twelve_minus)
ac_m.place(x=400,y=220)


ec_p=tk.Button(middle, text=' + ', font=('Times New Roman',10,'bold'),fg='black',bg='#dda15e',command=thirteen_plus)
ec_p.place(x=370,y=260)

ec_m=tk.Button(middle, text=' - ', font=('Times New Roman',10,'bold'),fg='black',bg='#dda15e',command=thirteen_minus)
ec_m.place(x=400,y=260)






#==================== Calculations ============================================================

title3=tk.Label(right, text='Calculations', font=('Arial',25,'bold'),fg='black',bg='#dda15e')
title3.place(x=120,y=10)


tot1=tk.Label(right, text='All Time classics Total', font=('Times New Roman',14,'bold'),fg='black',bg='#ffecd1')
tot1.place(x=10,y=100)
tot1_e=tk.Entry(right, textvariable=tot1_v, font=('Times New Roman',12,'bold'),fg='black')
tot1_e.place(x=250,y=100)


tot2=tk.Label(right, text='Selections Total', font=('Times New Roman',14,'bold'),fg='black',bg='#ffecd1')
tot2.place(x=10,y=140)
tot2_e=tk.Entry(right, textvariable=tot2_v, font=('Times New Roman',12,'bold'),fg='black')
tot2_e.place(x=250,y=140)


tot=tk.Label(right, text='Total', font=('Times New Roman',14,'bold'),fg='black',bg='#ffecd1')
tot.place(x=10,y=180)
tot_e=tk.Entry(right, textvariable=tot_v, font=('Times New Roman',12,'bold'),fg='black')
tot_e.place(x=250,y=180)


cod=tk.Label(right, text='Coupon Code', font=('Times New Roman',14,'bold'),fg='black',bg='#ffecd1')
cod.place(x=10,y=220)
cod_e=tk.Entry(right, textvariable=cod_v, font=('Times New Roman',12,'bold'),fg='black')
cod_e.place(x=250,y=220)


parc=tk.Label(right, text='Parcel', font=('Times New Roman',14,'bold'),fg='black',bg='#ffecd1')
parc.place(x=10,y=260)

op1_v=tk.IntVar()
op2_v=tk.IntVar()


op1_btn=tk.Checkbutton(right, text="Yes", variable=op1_v, onvalue=1, offvalue=0, font=('Times New Roman',14,'bold'),fg='black',bg='#ffecd1').place(x=250,y=260)


gtot=tk.Label(right, text='Grand Total', font=('Times New Roman',14,'bold'),fg='black',bg='#ffecd1')
gtot.place(x=10,y=310)
gtot_e=tk.Entry(right, textvariable=gtot_v, font=('Times New Roman',12,'bold'),fg='black')
gtot_e.place(x=250,y=310)

cal_b=tk.Button(right, text='Calculate', font=('Times New Roman',15,'bold'),fg='black',bg='#dda15e', command=calculate)
cal_b.place(x=100,y=350)

clr_b=tk.Button(right, text='Clear', font=('Times New Roman',15,'bold'),fg='black',bg='#dda15e', command=clear)
clr_b.place(x=250,y=350)



listbox1 = tk.Listbox(middle, height = 12, width = 47, bg = "white",activestyle = 'dotbox',font = "black", fg = "black")
listbox1.place(x=10,y=300)


root.mainloop()