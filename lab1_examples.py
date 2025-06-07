from qiskit import *
import matplotlib.pyplot as plt
from qiskit.circuit import Parameter



'''Building the circuit'''

# Create a Quantum Circuit acting on a quantum register of three qubits
circ = QuantumCircuit(3)
# Add a H gate on qubit 0, putting this qubit in superposition.
circ.h(0)
# Add a CX (CNOT) gate on control qubit 0 and target qubit 1, putting
# the qubits in a Bell state.
circ.cx(0, 1)
# Add a CX (CNOT) gate on control qubit 0 and target qubit 2, putting
# the qubits in a GHZ state.
circ.cx(0, 2)

'''Visualize Circuit'''

circ.draw('mpl')
plt.show()

'''Composition'''

phi = Parameter('phi')

sub_circ1 = QuantumCircuit(2, name='sc_1')
sub_circ1.rz(phi, 0)
sub_circ1.rx(phi, 1)

sub_circ2 = QuantumCircuit(2, name='sc_2')
sub_circ2.rx(phi, 0)
sub_circ2.rz(phi, 1)

qc = QuantumCircuit(4)
qr = qc.qregs[0]

qc.append(sub_circ1.to_instruction(), [qr[0], qr[1]])
qc.append(sub_circ2.to_instruction(), [qr[0], qr[1]])

qc.append(sub_circ2.to_instruction(), [qr[2], qr[3]])

qc.draw('mpl')
plt.show()

'''Complete example'''

# Below, we add q1 + q0 and measure the result into classical bits c2c1
# The other qubits, q2 and q3 are only there to help

# Make a circuit with 4 qubits and 2 classical bits
qc_ha = QuantumCircuit(4,2)  

# encode inputs to perform q_1 + q_0 = 1 + 1 
qc_ha.x(0)          
qc_ha.x(1)          

qc_ha.barrier()   

# Code the algorithm 
qc_ha.cx(0,2)       # CNOT with q0 as control and q2 as target
qc_ha.cx(1,2)       # CNOT with q1 as control and q2 as target
qc_ha.ccx(0,1,3)    # CCNOT with q0, q1 as controls and q3 as target

qc_ha.barrier()

# extract outputs 
qc_ha.measure(2,0)  # Measure qubit 2 into classical bit 0
qc_ha.measure(3,1)  # Measure qubit 3 into classical bit 1

# initial_state=True displays (doesn't set) the left-most values of qubits
qc_ha.draw(output = 'mpl', initial_state=True)  
plt.show()