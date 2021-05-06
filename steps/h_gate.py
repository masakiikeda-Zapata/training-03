from qiskit import execute, Aer, ClassicalRegister, QuantumCircuit, QuantumRegister
import json


def main():
    # Define registers and circuit
    # MISSING
    # MISSING
    circuit = QuantumCircuit(q, c)

    # Quantum circuit starts here
    # MISSING
    circuit.measure(q, c)
    # End quantum circuit

    # Execute with qiskit
    result = execute(circuit, Aer.get_backend("qasm_simulator"), shots=10000).result()
    counts = result.get_counts(circuit)

    with open("results.json", "w") as outfile:
        json.dump(counts, outfile)
