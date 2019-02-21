import ModelEntities as Cls
import InputData as D
import ModelParameters as P

# create an urgent care
myUrgentCare = Cls.UrgentCare(id=1, parameters=P.Parameters())

# simulate the urgent care
myUrgentCare.simulate(sim_duration=D.SIM_DURATION)

print('Total patients served:', myUrgentCare.nPatientsServed)
print('Patients received mental health consultation',  myUrgentCare.nPatientsReceivedConsult)
