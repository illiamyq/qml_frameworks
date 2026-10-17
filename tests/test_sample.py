import numpy as np
import pennylane as qp

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


def test_qiskit_simulator():
    circuit = QuantumCircuit(1)
    circuit.h(0)

    probs = Statevector.from_instruction(
        circuit
    ).probabilities()

    assert np.allclose(probs, [0.5, 0.5])


def test_pennylane_simulator():
    dev = qp.device("default.qubit", wires=1)

    @qp.qnode(dev)
    def circuit():
        qp.Hadamard(wires=0)
        return qp.probs(wires=0)

    probs = circuit()
    assert np.allclose(probs, [0.5, 0.5])