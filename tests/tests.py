import sys

sys.path.append('../OpenMiChroM')

from ChromDynamics import MiChroM
from Optimization import FullTraining, CustomMiChroMTraining



class testMichrom():
    def runDefault(self):
        a = MiChroM(name="test", temperature=1.0, time_step=0.01)
        a.setup(platform="cuda", integrator="Langevin", precision='single')
        a.saveFolder('output')
        myChrom = a.create_springSpiral(type_list=sys.path[0]+'/chr10/chr10_beads.txt')
        a.loadStructure(myChrom, center=True)
        a.addFENEBonds(k=30.0) 
        a.addAngles(k=2.0)
        a.addRepulsiveSoftCore(Ecut=4.0)
        a.addTypetoType(mi=3.22, rc=1.78)
        a.addIdealChromosome(mi=3.22, rc=1.78)
        a.addSphericalHarmonic(kr=5*10**-2, raddi=10)

        for _ in range(10):
            a.doBlock(10000, increment=False)
    
        a.printForces()            
run = testMichrom()

run.runDefault()
