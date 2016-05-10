#Implementation of stochastic gradient descent
import numpy as np
def hyp(theta , x):
	return (1/(1+np.exp(-1*(np.dot(x , theta)))))

def grad(theta , x):#Gradient of cost function w.r.t transpose(Theta)*X
	h=hyp(theta,x)
	return np.multiply(h,(np.ones(np.shape(h))-h))

def SGD(x , y , hyp , grad):
	ts = np.shape(x)
	theta = np.random.randn(ts[1],1)
	# print theta , '\n'

	learning_rate = 0.0001
	k = np.dot(x,theta) - y
	cost_prev = (float(1.0/float(2.0*float(ts[0]))))*np.dot(np.transpose(k) , k)
	cost=10000
	# print 'here ! '

	flag=True


	while flag:
		for i in xrange(0,ts[0]):
			for j in range(0,ts[1]):
				# theta[j][0] -= learning_rate*grad(theta , np.array([x[i]]))*(float)(1.0/float(ts[0]))*(hyp(theta , np.array([x[i]])) - y[i])*(-x[i][j])
				theta[j][0] -= float(learning_rate)*(float)(1.0/float(ts[0]))*float(hyp(theta , np.array([x[i]])) - y[i])*float(-x[i][j])
				k = np.dot(x,theta) - y
				cost = (float(1.0/float(2.0*float(ts[0]))))*np.dot(np.transpose(k) , k)	

				lr_sign = learning_rate/abs(learning_rate)

				print str(cost) + ' , ' + str(cost-cost_prev)

				if cost[0][0]>40.0:
					learning_rate=float(lr_sign)*5.0
				elif cost[0][0]>20.0:
					learning_rate=float(lr_sign)*2.5
				elif cost[0][0]>10.0:
					learning_rate=float(lr_sign)*1.0
				elif cost[0][0]>5.0:
					learning_rate=float(lr_sign)*0.5
				elif cost[0][0]>1.0:
					learning_rate=float(lr_sign)*0.3
				else:
					learning_rate=float(lr_sign)*0.001

				# if cost>=cost_prev:
				# 	learning_rate = -1.0*learning_rate

				if 	abs(cost[0][0]-cost_prev[0][0])<=0.00001 :
					flag=False
					break
				cost_prev = cost	

				# print cost

				# if cost > cost_prev:
				# 	learning_rate= -1*learning_rate

	return theta			