def plotline(w,b,plt):
    x1=np.linspace(1,2,2)
    x2=-(b+w[0]*x1)/w[1]
    plt.plot(x1,x2)

(array([[ 1.1,  0.1],
        [ 1.9,  3.1],
        [ 1.8,  0.8]]), array([-2,  1]), 2)

plt.scatter(x[:,0],x[:,1],c=y)
w=np.array([-2,1])
b=2
plotline(w,b,plt)
plt.show()
