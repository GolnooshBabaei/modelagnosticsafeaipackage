import pandas as pd
import numpy as np
import scipy
from .check_accuracy import rga
from .utils.util import _delta_function, _rga

def rgr(yhat, yhat_pert):
    """
    RANK GRADUATION Robustness (RGR) MEASURE
    Function for the RGR measure computation regarding perturbation of a single variable

    Inputs:
    yhat    : Predicted values generated by the full model  
    yhat_pert : Predicted values generated by the model including the perturbed selected variable
    
    Returns:
    RGR  : Calculated RGR measure
    """ 
    rgr = rga(yhat, yhat_pert)
    return rgr


def rgr_statistic_test(yhat, yhat_mod2, yhat_pert, yhat_mode2_pert):
    """
    RGR based test for comparing the robustness of a model with that of a further model when a variable is perturbed.
    
    Inputs:
    yhat    : Predicted values from the first model
    yhat_mod2 : Predicted values from the second model 
    yhat_pert    : Predicted values from the first model including the perturbed selected variable
    yhat_mod2_pert : Predicted values from the second model including the perturbed selected variable

    Returns:
    p_value : p-value for the statistical test
    """
    yhat = pd.DataFrame(yhat)
    yhat_mod2 = pd.DataFrame(yhat_mod2)
    yhat_pert = pd.DataFrame(yhat_pert)
    yhat_mode2_pert = pd.DataFrame(yhat_mode2_pert)
    
    # Compute jackknife results
    jk_mat = pd.concat([yhat,yhat_mod2,yhat_pert,yhat_mode2_pert], axis=1)
    jk_mat.columns = ["yhat_mod1", "yhat_mode2", "yhat_pert_mode1", "yhat_pert_mode2"]
    n = len(jk_mat)
    index = np.arange(n)
    jk_results = []
    for i in range(n):
        jk_sample = jk_mat.iloc[[x for x in index if x != i],:]
        jk_sample.reset_index(drop=True, inplace=True)
        jk_statistic = _delta_function(jk_sample, _rga)
        jk_results.append(jk_statistic)
    se = np.sqrt(((n-1)/n)*(sum([(x-np.mean(jk_results))**2 for x in jk_results])))
    z = (_rga(yhat, yhat_pert)- _rga(yhat_mod2, yhat_mode2_pert))/se
    p_value = 2*scipy.stats.norm.cdf(-abs(z))
        
    return p_value