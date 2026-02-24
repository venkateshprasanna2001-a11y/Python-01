print('1. Stress')
print('2. Torque')
print('3. Efficiency')
print('4. Cylinder Volume')
choice = input('Choose option: ')

if choice == '1':
                 force = float(input('Enter Force (N): '))
                 area = float(input('Enter Area (mm^2): '))
                 stress = force / area
                 print('Stess =', stress, 'N/mm^2')

elif choice == '2':
                   force = float(input('Enter Force (N): '))
                   radius = float(input('Enter Radius (m): '))
                   torque = force * radius
                   print('Torque =', torque, 'Nm')

elif choice == '3':
                    output_power = float(input('Enter Output Power: '))
                    input_power = float(input('Enter Input Power: '))

                    efficiency = (output_power / input_power)*100

                    print('Efficency =', efficiency, '%')
                    

elif choice == '4':
                    pi = 3.1416
                    radius = float(input('Enter Radius (m): '))
                    height = float (input("Enter Height (m): "))

                    Volume = pi * radius * radius * height

                    print("Cylinder Volume =", Volume, "m^3")
else:
    print('Invalid choice')
                    
2
