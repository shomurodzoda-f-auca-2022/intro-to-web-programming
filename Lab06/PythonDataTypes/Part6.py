# Byte types
byte_data = b"Hello"
print(byte_data, type(byte_data))

# ByteArray types
mutable_byte_data = bytearray([65, 66, 67])
print(mutable_byte_data, type(mutable_byte_data))
mutable_byte_data[0] = 68
print(mutable_byte_data, type(mutable_byte_data))