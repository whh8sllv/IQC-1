from qiskit import QuantumCircuit, transpile
import qiskit_aer

def toffoli(shem, c1, c2, c_trgt):
    shem.h(c_trgt)
    shem.cx(c2, c_trgt)
    shem.tdg(c_trgt)
    shem.cx(c1, c_trgt)
    shem.t(c_trgt)
    shem.cx(c2, c_trgt)
    shem.tdg(c_trgt)
    shem.cx(c1, c_trgt)
    shem.t(c2)
    shem.t(c_trgt)
    shem.h(c_trgt)
    shem.cx(c1, c2)
    shem.t(c1)
    shem.tdg(c2)
    shem.cx(c1, c2)

def margolus(shem, c1, c2, c_trgt):
    shem.t(c_trgt)
    shem.h(c_trgt)
    shem.cx(c2, c_trgt)
    shem.tdg(c_trgt)
    shem.cx(c1, c_trgt)
    shem.t(c_trgt)
    shem.cx(c2, c_trgt)
    shem.tdg(c_trgt)
    shem.h(c_trgt)

qc = QuantumCircuit(13, 4)

qc.x(1)
qc.x(2)
qc.x(4)
qc.x(7)

def adder(qc, a, b, c_in, c_out):
    qc.cx(a, b)
    qc.cx(c_in, b)
    toffoli(qc, a, c_in, c_out)

    # margolus(qc, a, c_in, c_out)

for i in range(4):
    a = i
    b = i + 4
    c_in = i + 8
    c_out = i + 9
    adder(qc, a, b, c_in, c_out)

qc.measure(4, 0)
qc.measure(5, 1)
qc.measure(6, 2)
qc.measure(7, 3)

simulation = qiskit_aer.AerSimulator()
shem_comp = transpile(qc, simulation)
res = simulation.run(shem_comp, shots=1).result()
print(res.get_counts())