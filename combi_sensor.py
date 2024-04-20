import serial

# Define your serial port settings (update with the appropriate values)
ser = serial.Serial(port='COM2', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

# Define the request command for each sensor
request_commands = [
    bytes.fromhex('0002000101E5E8'),  # Sensor with address code 02
    bytes.fromhex('0003000101E414'),  # Sensor with address code 03
    bytes.fromhex('0004000101E560'),  # Sensor with address code 04
    bytes.fromhex('0005000101E49C'),  # Sensor with address code 05
    bytes.fromhex('0006000101E4D8'),  # Sensor with address code 06
    # Add two more sensors here:
    # bytes.fromhex('0007000101E5XX'),  # Sensor with address code 07
    # bytes.fromhex('0008000101E6XX')   # Sensor with address code 08
]

# Initialize available spaces for each sensor
available_spaces = [0, 0, 0, 0, 0, 0, 0, 0]  # Initialize with 0 spaces for the additional sensors

try:
    for i, request_command in enumerate(request_commands):
        ser.write(request_command)

        # Read the response (14 bytes, as you provided)
        received_data = ser.read(15)

        if len(received_data) == 15:
            # Extract the 13th byte (index 12) from the received data
            status_byte = received_data[12]

            if status_byte == 0x00:
                print(f"Sensor {i} reports: parking space is available (green light)")
                available_spaces[i] += 1
            elif status_byte == 0x01:
                print(f"Sensor {i} reports: parking space is not available (red light)")
            else:
                print(f"Sensor {i} reports: Unknown status: {hex(status_byte)}")
        else:
            print(f"Sensor {i} reports: Incomplete data received")

    total_available_spaces = sum(available_spaces)
    print(f"Total available parking spaces: {total_available_spaces}")

except KeyboardInterrupt:
    ser.close()
