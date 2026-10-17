import qiskit
import qiskit_machine_learning

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

print("Qiskit:", qiskit.__version__)
print("Qiskit ML:",
      qiskit_machine_learning.__version__)

circuit = QuantumCircuit(1)
circuit.h(0)

state = Statevector.from_instruction(circuit)
print("probabilities:", state.probabilities())