import r2r_adc as r2r
import adc_plot as plot
import time

adc = r2r.R2R_ADC([22, 27, 17, 26, 25, 21, 20, 16], 3.3, 0.0001, True)

voltage_values = []
time_values = []

duration = 3.0

try:
    start_time = time.time()
    
    print(f"Measuring voltage for {duration} seconds... Press Ctrl+C to stop early")
    
    while (time.time() - start_time) < duration:
        current_time = time.time() - start_time
        
        voltage = adc.get_voltage()
        
        time_values.append(current_time)
        voltage_values.append(voltage)
        
        time.sleep(0.001)
    
    print(f"Measurements completed. Total samples: {len(voltage_values)}")
    
    plot.plot_voltage_vs_time(time_values, voltage_values, 3.3)
    
except KeyboardInterrupt:
    print("\nMeasurement stopped by user")
    print(f"Collected {len(voltage_values)} samples")
    
    if voltage_values:
        plot.plot_voltage_vs_time(time_values, voltage_values, 3.3)
    
finally:
    adc.deinit()
    print("ADC deinitialized")