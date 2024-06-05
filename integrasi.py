import numpy as np
import time
import matplotlib.pyplot as plt

def trapezoidal_integration(f, a, b, N):
    """
    Approximate the integral of f from a to b using the trapezoidal rule with N segments.
    """
    h = (b - a) / N
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, N):
        integral += f(a + i * h)
    integral *= h
    return integral

def f(x):
    return 4 / (1 + x**2)

def calculate_rms_error(estimated_pi, reference_pi):
    return np.sqrt((estimated_pi - reference_pi)**2)

def main():
    reference_pi = 3.14159265358979323846
    N_values = [10, 100, 1000, 10000]
    estimated_pis = []
    rms_errors = []
    execution_times = []
    
    for N in N_values:
        start_time = time.time()
        estimated_pi = trapezoidal_integration(f, 0, 1, N)
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        rms_error = calculate_rms_error(estimated_pi, reference_pi)
        
        estimated_pis.append(estimated_pi)
        rms_errors.append(rms_error)
        execution_times.append(elapsed_time)
        
        print(f"N = {N}")
        print(f"Estimated pi: {estimated_pi}")
        print(f"RMS Error: {rms_error}")
        print(f"Execution Time: {elapsed_time} seconds")
        print()
    
    # Plotting the results
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 3, 1)
    plt.plot(N_values, estimated_pis, 'o-')
    plt.axhline(y=reference_pi, color='r', linestyle='--')
    plt.xscale('log')
    plt.xlabel('N')
    plt.ylabel('Estimated Pi')
    plt.title('Estimated Pi vs N')
    
    plt.subplot(1, 3, 2)
    plt.plot(N_values, rms_errors, 'o-')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('N')
    plt.ylabel('RMS Error')
    plt.title('RMS Error vs N')
    
    plt.subplot(1, 3, 3)
    plt.plot(N_values, execution_times, 'o-')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('N')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution Time vs N')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
