from math import prod

with (open("day16.txt", "r")) as f:
    sample_input = [f.read()]


def read_packet(binary_str, o=0):
	version = int(binary_str[o:o+3],2)
	ID = int(binary_str[o+3:o+6],2)
	o += 6

	if ID == 4:
		# Process Literal Packets
		num = ''
		while True:
			o += 5
			num += binary_str[o-4:o]
			if binary_str[o - 5] == '0': break		
		return int(num,2), o, version
	else:
		# Process Operator Packets

		# Get subpacket info
		packet_len, packet_num = None, None
		if int(binary_str[o]):
			o += 12
			packet_num = int(binary_str[o-11:o], 2)
		else:
			o += 16
			packet_len = int(binary_str[o-15:o], 2)

		# Read Subpackets
		packets = binary_str[o:o + packet_len if packet_len else None]
		packet_vals = []
		num_counter, len_counter = 0, 0
		while (packet_len and len_counter < packet_len) or (packet_num and num_counter < packet_num):
			value, len_counter, sub_version = read_packet(packets, len_counter)
			num_counter += 1
			version += sub_version
			packet_vals.append(value)

		# Apply Function to subpackets and return
		func = [sum, prod, min, max, None, lambda x: x[0] > x[1], lambda x: x[0] < x[1], lambda x: x[0] == x[1]]
		return int(func[ID](packet_vals)), o+len_counter, version

# Iteration used for testing
for x in sample_input:
	binary_str = "".join([bin(int(c,16))[2:].rjust(4,'0') for c in x])
	packet, bytes_read, version_total = read_packet(binary_str)
	print("version_total (pt1) : ", version_total, "\npacket value (pt2) : ", packet)

# answer 1549026292886

sample_input = [
# version 6 ID 4 value 2021
"D2FE28",
# Example 1
"38006F45291200",
# Example 2
"EE00D40C823060",
# represents an operator packet (version 4) which contains an operator packet (version 1) which contains an operator packet (version 5) which contains a literal value (version 6); this packet has a version sum of 16.
"8A004A801A8002F478",
# represents an operator packet (version 3) which contains two sub-packets; each sub-packet is an operator packet that contains two literal values. This packet has a version sum of 12.
"620080001611562C8802118E34",
# has the same structure as the previous example, but the outermost packet uses a different length type ID. This packet has a version sum of 23.
"C0015000016115A2E0802F182340",
# is an operator packet that contains an operator packet that contains an operator packet that contains five literal values; it has a version sum of 31.
"A0016C880162017C3686B18A3D4780",
]

sample_input = [
"C200B40A82",
"04005AC33890",
"880086C3E88112",
"CE00C43D881120",
"D8005AC2A8F0",
"F600BC2D8F",
"9C005AC2F8F0",
"9C0141080250320F1802104A08"
]
