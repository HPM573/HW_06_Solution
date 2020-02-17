import UrgentCareModel as M
import InputData as D
import ModelParameters as P

# create an urgent care model
urgentCareModel = M.UrgentCareModel(id=1, parameters=P.Parameters())

# simulate the urgent care
urgentCareModel.simulate(sim_duration=D.SIM_DURATION)

print('Total patients arrived:', urgentCareModel.urgentCare.nPatientsArrived)
print('Total patients served:', urgentCareModel.urgentCare.nPatientsServed)
print('Patients received mental health consultation',  urgentCareModel.urgentCare.nPatientsReceivedConsult)
