# grover_search.py
from qiskit import Aer, QuantumCircuit, transpile, assemble
from qiskit.visualization import plot_histogram

# Database size (N = number of items in the database)
N = 16  # Example: database with 16 items
target_index = 5  # Example: target item is at index 5

# Create a quantum circuit
qc = QuantumCircuit(N)

# Create superposition of all possible states
qc.h(range(N))

# Oracle to mark the target state
qc.cz(target_index, target_index)

# Inversion about the mean (diffusion operator)
qc.h(range(N))
qc.x(range(N))
qc.h(N-1)
qc.cx(range(N-1), N-1)
qc.h(range(N))
qc.x(range(N))

# Measure the result
qc.measure_all()

# Simulate the circuit
backend = Aer.get_backend('qasm_simulator')
tqc = transpile(qc, backend)
qobj = assemble(tqc)
result = backend.run(qobj).result()

# Display the result
counts = result.get_counts()
print(f"Result: {counts}")
plot_histogram(counts)
