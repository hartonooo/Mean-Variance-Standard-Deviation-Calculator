import numpy as np

def calculate(list):

    if len(list) == 9:
        
        n_1 = np.reshape(list, (3,3))
            
        calculations = {}        
            

        calculations["mean"] = [[np.mean(n_1, 0)[i] for i in range(len(np.mean(n_1, 0)))],
                               [np.mean(n_1, 1)[i] for i in range(len(np.mean(n_1, 1)))],
                               np.mean(list)]
        
        calculations["variance"] = [[np.var(n_1, 0)[i] for i in range(len(np.var(n_1, 0)))],
                               [np.var(n_1, 1)[i] for i in range(len(np.var(n_1, 1)))],
                               np.var(list)]
        
        calculations["standard deviation"] = [[np.std(n_1, 0)[i] for i in range(len(np.std(n_1, 0)))],
                               [np.std(n_1, 1)[i] for i in range(len(np.std(n_1, 1)))],
                               np.std(list)]
        
        calculations["max"] = [[np.max(n_1, 0)[i] for i in range(len(np.max(n_1, 0)))],
                               [np.max(n_1, 1)[i] for i in range(len(np.max(n_1, 1)))],
                               np.max(list)]
        
        calculations["min"] = [[np.min(n_1, 0)[i] for i in range(len(np.min(n_1, 0)))],
                               [np.min(n_1, 1)[i] for i in range(len(np.min(n_1, 1)))],
                               np.min(list)]
        
        calculations["sum"] = [[np.sum(n_1, 0)[i] for i in range(len(np.sum(n_1, 0)))],
                               [np.sum(n_1, 1)[i] for i in range(len(np.sum(n_1, 1)))],
                               np.sum(list)]
        return calculations


    else:
        raise ValueError("List must contain nine numbers.")


    
