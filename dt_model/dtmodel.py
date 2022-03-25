import math
import numpy as np
from utils.bin_file_io import write_dict2bin, read_dict_from_bin

M_PI = 3.14159265358979323846

# Coefficient files: (C1, C2) 
#   model_mradian2maxdt_file: \Delta t_p^-(\Delta \theta)
#   model_dv2maxdt_file:      \Delta t_p^-(\Delta v)
# Functions: Equation (3)
#   get_overtake_dt_upper_bound(): \Delta t_p^- 
#   get_giveway_dt_lower_bound(): \Delta t_p^+
class IntearctionMinAbsDtModel():
  def __init__(self, model_mradian2maxdt_file="coef_mradian2maxdt.bin", 
                     model_dv2maxdt_file="coef_dv2maxdt.bin") -> None:
    self.poly_mradian2maxdt = read_dict_from_bin(model_mradian2maxdt_file)
    self.poly_dv2maxdt = read_dict_from_bin(model_dv2maxdt_file)
    print("poly_mradian2maxdt={}".format(self.poly_mradian2maxdt))
    print("poly_dv2maxdt={}".format(self.poly_dv2maxdt))

  def get_overtake_dt_upper_bound(self, dradian = 0., dv = 0.):
    '''
    get overtake interaction delta t, it is a upper bound value 
    since the interaction t is always < 0 (ego go first, and other traffic agent)

    :param draidan: the interaction angle (radian) in interaction zone 
    :param dv: the differential speed (m/s) in interaction zone
    :return: the upper bound of interaction delta t
    '''
    abs_dradian = min(math.fabs(dradian), M_PI)
    upper_bound1 = np.polyval(self.poly_mradian2maxdt, abs_dradian)
    upper_bound2 = np.polyval(self.poly_dv2maxdt, dv)
    # print("upperbound=", upper_bound1, upper_bound2)
    return min(upper_bound1, upper_bound2)

  def get_giveway_dt_lower_bound(self, dradian = 0., dv = 0.):
    '''
    get giveway interaction delta t, it is a lower bound value 
    since the interaction t is always > 0 (ego go after other traffic agent)

    :param draidan: the interaction angle (radian) in interaction zone 
    :param dv: the differential speed (m/s) in interaction zone
    :return: the lower bound of interaction delta t
    '''
    abs_dradian = min(math.fabs(dradian), M_PI)

    # map to giveway coordination: v = -dv; radian= input_radian
    lowerbound1 = -np.polyval(self.poly_mradian2maxdt, abs_dradian)
    lowerbound2 = -np.polyval(self.poly_dv2maxdt, -dv)
    # print("lowerbound=", lowerbound1, lowerbound2)
    return max(lowerbound1, lowerbound2)
