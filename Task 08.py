shift_time = 480 # minutes

breakdown = float(input("Enter breakdown time (minutes): "))
setup = float(input("Enter setup time (minutes): "))
idle_time = float(input("Enter idle time (minutes): "))

total_time = breakdown + setup + idle_time
running_time = shift_time - total_time

availability = (running_time / shift_time) * 100

print("Total Downtime:", total_time, "minutes")
print("Running Time:", running_time, "minutes")
print("Availability:", availability, "%")

ideal_rate = 120 # parts per hour
running_time = running_time / 60 

ideal_output = ideal_rate * running_time

actual_output = float(input("Enter actual parts produced: "))

efficiency = (actual_output / ideal_output) * 100

print("Ideal Output:", ideal_output)
print("Efficiency:", efficiency, "%")

if availability < 85:
 print("Trigger: Critical Performance")

elif availability < 90:
 print("Trigger: Need Improvement") 

    
