import math
import numpy as np

M_PI = 3.14159265358979323846

class IntearctionMinAbsDtModel():
  def __init__(self) -> None:
    self.l_poly_mradian2maxdt = [-0.17106961, 0.09499304, -1.2734661 ]
    self.l_poly_dv2maxdt = [-3.73132913e-05, 7.21087592e-06, -1.23657133e-02, 3.38347447e-02, -1.16506280e+00]
    self.u_poly_mradian2maxdt = [0.18237564, -0.14051625, 1.40760894]
    self.u_poly_dv2maxdt = [6.26375360e-05, 3.43049200e-04, 1.32386831e-02, 3.97324890e-02, 1.27294369e+00]

  def get_overtake_dt_upper_bound(self, dradian = 0., dv = 0.):
    '''
    get overtake interaction delta t, it is a upper bound value 
    since the interaction t is always < 0 (ego go first, and other traffic agent)

    :param draidan: the interaction angle (radian) in interaction zone 
    :param dv: the differential speed (m/s) in interaction zone
    :return: the upper bound of interaction delta t
    '''
    abs_dradian = min(math.fabs(dradian), M_PI)
    upper_bound1 = np.polyval(self.l_poly_mradian2maxdt, abs_dradian)
    upper_bound2 = np.polyval(self.l_poly_dv2maxdt, dv)
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
    lowerbound1 = np.polyval(self.u_poly_mradian2maxdt, abs_dradian)
    lowerbound2 = np.polyval(self.u_poly_dv2maxdt, dv)
    # print("lowerbound=", lowerbound1, lowerbound2)
    return max(lowerbound1, lowerbound2)
