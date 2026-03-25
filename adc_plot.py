import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):

    plt.figure(figsize=(10, 6))
    
    plt.plot(time, voltage, 'b-', linewidth=1.5)
    
    plt.title('Voltage vs Time on 8-bit R2R DAC', fontsize=14)
    plt.xlabel('Time (s)', fontsize=12)
    plt.ylabel('Voltage (V)', fontsize=12)
    
    plt.xlim(0, max(time) if time else 1)
    plt.ylim(0, max_voltage)
    
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.show()