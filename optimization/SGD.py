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

	learning_rate = 0.00001
	k = np.dot(x,theta) - y
	cost_prev = (float(1.0/float(2.0*float(ts[0]))))*np.dot(np.transpose(k) , k)
	cost=10000
	# print 'here ! '



	while abs(cost-cost_prev) > 0.00001:
		for i in xrange(0,ts[0]):
			for j in range(0,ts[1]):
				# theta[j][0] -= learning_rate*grad(theta , np.array([x[i]]))*(float)(1.0/float(ts[0]))*(hyp(theta , np.array([x[i]])) - y[i])*(-x[i][j])
				theta[j][0] -= learning_rate*(float)(1.0/float(ts[0]))*(hyp(theta , np.array([x[i]])) - y[i])*(-x[i][j])
				k = np.dot(x,theta) - y
				cost = (float(1.0/float(2.0*float(ts[0]))))*np.dot(np.transpose(k) , k)
				cost_prev = cost

				if cost > cost_prev:
					learning_rate= -1*learning_rate

	return theta			