import qiskit
import qiskit_machine_learning
import pennylane as qp
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

print("Qiskit:", qiskit.__version__)
print("Qiskit ML:",
      qiskit_machine_learning.__version__)

circuit = QuantumCircuit(1)
circuit.h(0)

state = Statevector.from_instruction(circuit)
print("Qiskit probabilities:", state.probabilities())

print("\nPennyLane:", qp.__version__)
dev = qp.device("default.qubit", wires=1)

@qp.qnode(dev)
def circuit_pl():
    qp.Hadamard(wires=0)
    return qp.probs(wires=0)

print("PennyLane probabilities:", circuit_pl())