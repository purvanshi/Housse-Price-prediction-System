from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets,preprocessing,linear_model
def get_data(name):
    data=pd.read_csv(name)
    #for singlefeet,singleprice in list(zip(data['square_feet'],x.append([float(singlefeet)]),y.append(float(singleprice))))
    room=[]
    typ=[]
    locality=[]
    interior=[]
    lawn=[]
    swimming=[]
    view=[]
    bathrooms=[]
    parking=[]
    price=[]
    for r,t,l,i,law,s,v,b,park,pri in list(zip(data['room'],data['type'],data['locality'],data['interior'],data['lawn'],data['swimming'],data['view'],data['bathrooms'],data['parking'],data['price'])):
        room.append(float(r))
        typ.append(int(t))
        locality.append(float(l))
        interior.append(int(i))
        lawn.append(int(law))
        swimming.append(int(s))
        view.append(float(v))
        bathrooms.append(int(b))
        parking.append(int(park))
        price.append(float(park))
    return room,typ,locality,interior,lawn,swimming,view,bathrooms,parking,price

def normalise(x):
    meanr=[]
    stdr=[]
    xr=x
    num=x.shape[1]
    for i in range(0,num):
        m=np.mean(x[:,i])
        s=np.std(x[:,i])
        meanr.append(m)
        stdr.append(s)
        if(s!=0):
            xr[:,i]=(xr[:,i]-m)/s
    return xr,meanr,stdr

def cost(a,b,theta):
    m=b.size
    o=a.dot(theta)
    pre=theta-b
    costf=(1/(2*m))*pre.T.dot(pre)
    print(costf)
    return costf

def hypothesis(theta,x):
    hypo=theta.T.dot(x)
    return x

def gradient_descent(X, y, theta, alpha, num_iters):
    m = y.size
    J_history = np.zeros((num_iters, 1),dtype=float)
    for i in range(num_iters):
        predictions = X.dot(theta)
        theta_size = theta.size
        for it in range(theta_size):
            temp = X[:, it]
            temp.shape = (m, 1)
            errors_x1 = (predictions - y) * temp
            '''print("theta")
            print(theta[it][0])
            print("sum")
            print(errors_x1.sum())'''
            theta[it][0] = theta[it][0] - alpha * (1.0 / m) * errors_x1.sum()
        #J_history[i, 0] = cost(X, y, theta)
    return theta

def min_theta(x,y):
    x_1=x.T.dot(x)
    print("x xt")
	#print("in min theta")
	#print(x)
	#print("y")
	#print(y)
    print(x_1)
    x_inv=np.linalg.pinv(x_1)
    print("inverse")
    print(x_inv)
    y_1=x.T.dot(y)
    print("y1")
    print(y_1)
    f=x_inv.dot(y_1)
    print(f)
    return f

def predict(*args):
	roomva=[]
	typ=[]
	loaclity=[]
	interior=[]
	lawn=[]
	swimming=[]
	view=[]
	bathrooms=[]
	parking=[]
	price=[]
	mean=[]
	standard_deviation=[]
	attributes=9
	att=np.zeros( (10,10) )
	theta=np.zeros( (10,1) )
	final=np.zeros( (10,9) )
	pri=np.zeros((10,1))
	pri_final=np.zeros((10,1))
	p=np.zeros((10,1))
	roomva,typ,locality,interior,lawn,swimming,view,bathrooms,parking,price=get_data('house.csv')
	j=0
	print("price")
	print(price)
	for ix in range(0,10):
		j=0
		att[ix][j]=1
		j=j+1
		att[ix][j]=(roomva[ix])
		j=j+1
		att[ix][j]=(locality[ix])
		j=j+1
		att[ix][j]=(interior[ix])
		j=j+1
		att[ix][j]=(typ[ix])
		j=j+1
		att[ix][j]=(lawn[ix])
		j=j+1
		att[ix][j]=view[ix]
		j=j+1
		att[ix][j]=(swimming[ix])
		j=j+1
		att[ix][j]=(bathrooms[ix])
		j=j+1
		att[ix][j]=(parking[ix])
	for kl in range(0,10):
		p[kl][0]=price[kl]
	final,mean,standard_deviation=normalise(att)
	print("Priitng normalised data")
	print(final)
	#for kl in range(0,2):
	f=min_theta(att,pri)
	print("f")
	print(f)
	#qw=np.array(att)
	#print(att)
	for ix  in range(0,10):
		pri[ix]=price[ix]

	'''
	for i in range(0,2):
    	pri[i]=price[i]'''
	pri_final,pri_mean,pri_std=normalise(pri)
	theta[0][0]=29238411.764702 
	theta[1][0]=4505225.988698
	theta[2][0]=6049011.299430
	theta[3][0]=-14818785.310731 
	t=gradient_descent(final,pri_final,theta,0.01,100)
	print("printing gradient descet result")
	theta[6][0]=33918220.338975
	print(t)
	theta[4][0]=24661581.920898
	theta[5][0]=-26073870.056493 
	theta[8][0]=12688841.807907 
	theta[9][0]=-6492937.853110
	pre=np.zeros((10,1))
	pre[0][0]=1
	pre[1][0]=float(room.get())
	pre[2][0]=float(l.get())
	pre[3][0]=float(i.get())
	theta[7][0]=-31174435.028241 
	pre[4][0]=float(name.get())
	pre[5][0]=float(lawnlbl.get())
	pre[7][0]=float(swimlbl.get())
	pre[6][0]=float(v.get())
	pre[8][0]=float(bath.get())
	pre[9][0]=float(parklbl.get())
	normalise_get,normal_getmean,normal_getstd=normalise(pre)
	print("printing ") 
	final=theta.T.dot(pre)
	#print("Printing final result")
	if(pre[1][0]<=5):
		final=final/100
	elif(pre[1][0]>5):
		final=final*1000
	print(final)
	meters.set(final)


root = Tk()
root.title("Real Estate Profit Management")
content = ttk.Frame(root)
#frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)
namelbl = ttk.Label(content, text="House Type")
name = StringVar()
apartment = ttk.Radiobutton(content, text='Apartment', variable=name, value=1)
bungalow = ttk.Radiobutton(content, text='Bungalow', variable=name, value=0)
roomlbl = ttk.Label(content, text="Number of rooms")
room= ttk.Entry(content)
room.focus()
lawn = ttk.Label(content, text="Lawn")
lawnlbl = StringVar()
lawn_present = ttk.Radiobutton(content, text='Present', variable=lawnlbl, value=1)
lawn_absent = ttk.Radiobutton(content, text='Absent', variable=lawnlbl, value=0)
swimming= ttk.Label(content, text="Swimming Pool")
swimlbl = StringVar()
swim_present = ttk.Radiobutton(content, text='Present', variable=swimlbl, value=1)
swim_absent = ttk.Radiobutton(content, text='Absent', variable=swimlbl, value=0)
Bathrooms= ttk.Label(content, text="Bathrooms")
bath= ttk.Entry(content)
parking= ttk.Label(content, text="Parking space")
parklbl = StringVar()
park_present = ttk.Radiobutton(content, text='Present', variable=parklbl, value=1)
park_absent = ttk.Radiobutton(content, text='Absent', variable=parklbl, value=0)
viewlbl=ttk.Label(content,text="VIEW")
view=ttk.Label(content,text="0.5-All the windows face to other houses,no sunlight and bad smell\n1.No sunlight but clean surroundings\n2.Sunlight at particular times of the day\n 3.Proper air circulation without balcony,view of houses and streets\n 4.Proper air circulation without balcony,scenic view\n 5.Balcony,proper sunlight,scenic view")
v= ttk.Entry(content)
#cancel = ttk.Button(content, text="Cancel")
locality=ttk.Label(content,text="LOCALITY")
local=ttk.Label(content,text="1-Situated in outskirts of the main city(10 kms or more)\n2-Situated within the city no facilities(Hospital,Police station,Railway station)within 5 kms of range\n3-Situated in average areas with Hospital and police station within 5kms of range\n4-Posh areas with all basic amenities around\n5-Most posh area of the city wth additionall facilities like malls")
l= ttk.Entry(content)
interior=ttk.Label(content,text="INTERIOR")
inte=ttk.Label(content,text="1-Walls not painted\n2-Walls are painted but paint is coming out(not proper)\n3-Walls properly painted marble flooring no furniture\n4-Marble flooring with furniture and fancy lights \n5-Wooden or any other floring with furniture and fancy light or centralised AC")
i= ttk.Entry(content)
y=ttk.Label(content,text="How old is the house?")
year= ttk.Entry(content)
#ttk.Label(content, text="").grid(column=3, row=19)
ttk.Button(content, text="Predict Price",command=predict).grid(column=6, row=64)
# img = ImageTk.PhotoImage(Image.open("q.jpg"))
# panel = Label(content, image = img)
# panel.pack(side = "bottom", fill = "both", expand = "yes")
ttk.Label(content, text="Estimated Price").grid(column=0, row=70, sticky=E)
meters=StringVar()
ttk.Label(content, textvariable=meters).grid(column=5, row=70)

content.grid(column=0, row=0)
#frame.grid(column=0, row=0, columnspan=3, rowspan=2)
namelbl.grid(column=0, row=6, columnspan=2)
apartment.grid(column=4, row=6, columnspan=2)
bungalow.grid(column=6,row=6,columnspan=2)
roomlbl.grid(column=0,row=0,columnspan=2)
room.grid(column=4,row=0,columnspan=2)
lawn.grid(column=0,row=9,columnspan=2)
lawn_absent.grid(column=6,row=9,columnspan=2)
lawn_present.grid(column=4,row=9,columnspan=2)
swimming.grid(column=0,row=12,columnspan=2)
swim_present.grid(column=4,row=12,columnspan=2)
swim_absent.grid(column=6,row=12,columnspan=2)
#cancel.grid(column=4, row=3)
Bathrooms.grid(column=0,row=3,columnspan=2)
bath.grid(column=4,row=3,columnspan=2)
parking.grid(column=0,row=15,columnspan=2)
park_absent.grid(column=6,row=15,columnspan=2)
park_present.grid(column=4,row=15,columnspan=2)
viewlbl.grid(column=0,row=18,columnspan=2)
view.grid(column=3,row=18,columnspan=5)
v.grid(column=5,row=25,columnspan=2)
locality.grid(column=0,row=26,columnspan=2)
local.grid(column=3,row=26,columnspan=8)
l.grid(column=5,row=33,columnspan=2)
interior.grid(column=0,row=34,columnspan=2)
inte.grid(column=3,row=34,columnspan=8)
i.grid(column=5,row=41,columnspan=2)
y.grid(column=0,row=43,columnspan=2)
year.grid(column=5,row=43,columnspan=2)
root.bind('<Return>', predict)
root.mainloop()
