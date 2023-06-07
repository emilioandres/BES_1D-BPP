import numpy as np
import time
import problem

def BES(weight,c,nVars,pop_size,a_factor,R_factor,alpha,low,high,c1,c2,maxIter,seed):
    t=0
    P_best = np.ones(nVars) 
    P_g = nVars
    start_time = time.time()
    P_new = np.zeros(nVars)
    P_g_time=[]
    x=population(pop_size,seed,nVars)
    while (t<maxIter):
        x_list, y_list, x1_list, y1_list = create_x_y_x1_y1__(pop_size,a_factor,R_factor)
        P_new = np.zeros(nVars)
        #selección de espacio
        for i in x:
            for j in range(0,i.size,1):
                P_new[j] = P_best[j] + alpha*np.random.rand()*(np.mean(i)-i[j])     

            if (problem.check_constraint(problem.real2bin(P_new),c, weight) == True):
                if(problem.compute_fitness(problem.real2bin(P_new))<problem.compute_fitness(problem.real2bin(P_best))):
                    P_best=P_new
            if (problem.check_constraint(problem.real2bin(i),c, weight) == True):
                if(problem.compute_fitness(problem.real2bin(i))<problem.compute_fitness(problem.real2bin(P_best))):
                    P_best=i

        #búsqueda en el espacio
        for i in range(0,pop_size,1):
            P_new = np.zeros(nVars)
            #generamos valores aleatorios por el tamaño de pop size
            for j in range(0,P_best.size,1):
                if (j!=len(P_best)-1):
                    P_new[j]=P_best[j]+y_list[i]*(P_best[j]-P_best[j+1])+x_list[i]*(P_best[j]-np.mean(P_best))
                else:
                    P_new[j]=P_best[j]+y_list[i]*(P_best[j]-P_best[-1])+x_list[i]*(P_best[j]-np.mean(P_best))

            if (problem.check_constraint(problem.real2bin(P_new),c, weight) == True):
                if(problem.compute_fitness(problem.real2bin(P_new))<problem.compute_fitness(problem.real2bin(P_best))):
                    P_best=P_new

        #swoop en el espacio
        for i in range(0,pop_size,1):
            P_new = np.zeros(nVars)
            for j in range(0,P_best.size,1):
                P_new[j]=np.random.uniform(0,1)*(P_best[j])+x1_list[i]*(P_best[j]-c1*np.mean(P_best))+y1_list[i]*(P_best[j]-c2*(P_best[j]))

            if (problem.check_constraint(problem.real2bin(P_new),c, weight) == True):
                if(problem.compute_fitness(problem.real2bin(P_new))<problem.compute_fitness(problem.real2bin(P_best))):
                    P_best=P_new
        if (problem.check_constraint(problem.real2bin(P_best),c, weight) == True):
            if(problem.compute_fitness(problem.real2bin(P_best))<P_g):
                P_g=problem.compute_fitness(problem.real2bin(P_best))
        P_g_time.append(P_g)
        t=t+1
    end_time = time.time()
    execution_time = end_time - start_time
    return P_g_time[-1],P_g_time,execution_time
def population(pop_size,seed,nVars):
    np.random.seed(seed)
    x=[]
    for i in range(0,pop_size,1):
        x.append(np.random.uniform(-1, 1, nVars))
    x=np.array(x)
    return(x)
def create_x_y_x1_y1__(pop_size,a_factor,R_factor):
    phi = a_factor * np.pi * np.random.uniform(0, 1, pop_size)
    r = phi + R_factor * np.random.uniform(0, 1, pop_size)
    xr, yr = r * np.sin(phi), r * np.cos(phi)
    r1 = phi1 = a_factor * np.pi * np.random.uniform(0, 1, pop_size)
    xr1, yr1 = r1 * np.sinh(phi1), r1 * np.cosh(phi1)
    x_list = xr / np.max(xr)
    y_list = yr / np.max(yr)
    x1_list = xr1 / np.max(xr1)
    y1_list = yr1 / np.max(yr1)
    return x_list, y_list, x1_list, y1_list