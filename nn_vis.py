import random
import time
import pygame

pygame.init()

nodes = []

weights = [0.7962194427262359, 0.8679136356598196, 1.345672324836952, 0.7107690480459323, 0.7189847086695862, 0.09622256967096318, 0.42791886820574265, 1.3031794297969592, -0.3689764222778109, -0.015442874224206926, -0.07920273673900985, -0.5280142372452709, 0.26634206883452877, 0.0032430609155442514, 0.9178467229570844, 0.27951436956422665, -0.1095795548247234, 0.7691664842621744, -0.05031832331869129, -0.0394776140478494, 1.7979141229402131, 0.15856123770819713, -0.00507558315255628, -0.16340426147575965, -0.13016428241044714, 1.1302766810555767, 0.34627340327790507, 0.19997919675180484, -0.14752148848777072, -0.07664769957986546, 1.1436526589066236, 1.0671646637881214, 2.085862676233181, 0.7958645853459808, 1.1764094455209346, 0.7694987035976301, 0.6216995479379452, -0.47481916806923546, 1.0965130062663526, 0.6085135489805698, 0.1294976219828699, 1.3261138308718043, 0.025436346945815484, 0.16156872118296942, 1.3422329659291012, -0.12733273521912192, 0.5491375978619222, 0.5671193258513063, 0.8457940283299448, -0.5229823728114003, 0.8089812643121039, -0.1594870765579088, 0.9752253633852064, 1.0917765985068948, 0.7164631173246411, -0.5991989957415279, 1.084055978859935, 1.2174296697698737, -0.6803578280586566, 0.7087640109568999, 0.7198969783629129, 0.45427395426052347, -0.25444642860661537, 0.7307941507419792, 0.5262033898050019, 0.819429556952168, 0.6301039521548017, 1.1770499763897888, 1.5499290650089628, 1.3647090236245787, 0.5586087823279018, 1.2082936422181374, 1.2953320405889115, 1.3500282047571817, 0.056912961871348006, -0.2638961363604728, 0.2185039117991345, 0.37555002835887186, 0.2851073126949273, 0.06540392283032595, 0.5829592845344722, 2.2360759283395097, 0.2449155642489743, 0.13803978705747413, 0.854719524215686, 0.13471279469880237, 0.5591455507283938, -1.1481894253026923, 0.3539200393378668, 0.4938995045494968, 0.21185921704676913, 0.169414792682728, 0.2914889868413274, -0.6947977228082256, 0.1906634263868198, 0.40041538107418967, 0.1188822883544649, 0.6417426120605517, 0.32147701341618506, 2.4826227875332108, 0.1272732883723633, -0.012603704495031794, 0.3663733928805913, 0.8473542656174747, 1.063344612273713, 0.8654906398679084, 0.8112849873414726, 1.0009288895070596, 1.0590307262275316, 0.25071605042332556, -0.7203910088062605, 0.36565539965631205, 0.5261612162869103, -0.9272305977134786, 1.0303954371541884, 0.10278691223570148, -0.008066049596298216, 0.10585113498922742, 0.16435953578179463, -1.2154315785410013, 0.692649654112871, -0.059815484738408115, 1.3253223903373705, 0.5273584584532695, 0.4285343798307263, 2.1324643575516293, 0.6205121810506705, 0.9588653412639484, 0.9159110256044164, 0.19671139332996326, -0.11127627040439694, 1.1631364458448505, 0.60523898481079, 0.3343835275787304, 1.2816630449419317, -0.13188165037572758, -0.0026406245936370382, 1.1278221961639927, 1.4786204587157044, 1.0094078912430473, 0.8072776374696843, 0.9407892660083346, 1.2091939679322443, 0.7939001728000052, 1.007002448538206, 1.0406663892138723, 1.1665661199242818, 0.41911491230277814, 0.7300162099388413, 0.5074402143773588, 0.785236412526618, 0.658677455126833, 1.2805641330254538, 0.281512927752482, 1.2162029938930778, 1.1768194480466572, 0.8338955386950271, 0.903834475129456, 0.9737794694045684, 1.7734539769575541, 0.840631480326589, 1.030452793529139, 0.6779911409757606, 1.1643529480607535, 1.1424731183150767, 0.7861559555608123, 1.1175347992357827, 0.5812378350183479, 0.4712619346187793, 0.2911856460307302, 0.45970440471282853, -0.04885593600332515, -0.02017399113397975, -0.11131071739237292, 0.7107231503166969, 1.0892071618205381, 0.9110701723766078, 0.6091903101522917, 0.7762570844429182, 0.6603167273420392]


itC = 0
species = 0

# 6x6 neural network with a bias node for each layer. Rectified linear function will be used.


len_weights = 6*6*5

len_nodes = 6*6
for i in range(0,len_nodes):
    nodes.append(0)



def sigmoid(x):
    if(x > 0):
        return x
    else:
        return 0


def ff(x_in, y_in, weights_in, nodes_in):
    nodes_in[0] = 1
    nodes_in[1] = x_in
    nodes_in[2] = y_in
    nodes_in[3] = 1
    nodes_in[4] = 1
    nodes_in[5] = 1

    for i in range(6,len_nodes):
        if(i % 6 == 0):
            nodes_in[i] = 1
        else:
            nodes_in[i] = 0
            for j in range(0, 6):
                # Add and weight all nodes in previous layer
                node_index = j + (i - i % 6) - 6
                weight_index = (i - 7) * 6 + j
                #print("node " + str(node_index) + " connected by " + str(weight_index) + " to " + str(i))
                nodes_in[i] += nodes_in[node_index] * weights_in[weight_index]
            nodes_in[i] = sigmoid(nodes[i])
    return nodes_in[-1]

#print(ff(1, 1, weights, nodes))

def extract_numbers_from_file(file_path):
    numbers = []
    try:
        with open(file_path, 'r') as file:
            for i, line in enumerate(file):
                if i >= 1000:  # Process only the first 1000 lines
                    break

                parts = line.split()  # Split the line into parts
                
                # Extract and store the first three numbers
                try:
                    first_three_numbers = [float(parts[j]) for j in range(3)]
                    numbers.append(first_three_numbers)
                except (IndexError, ValueError):
                    print(f"Line {i + 1} is malformed or doesn't contain enough numbers.")

    except FileNotFoundError:
        print(f"File not found: {file_path}")

    return numbers

# Example usage
file_path = 'train_data.txt'  # Replace with your file path
extracted_numbers = extract_numbers_from_file(file_path)
#print(extracted_numbers)


def loss(nodes_in, weights_in):
    sum = 0
    for i in range(0, 100):
        x = extracted_numbers[i][0]
        y = extracted_numbers[i][1]
        a = extracted_numbers[i][2]
        a_guess = ff(x, y, weights_in, nodes_in)
        loss = ((a - a_guess) ** 2) / 100
        sum += loss

    return sum

#print(loss(nodes, weights))


# Window dimensions
maxW = 800
maxH = 800
window = pygame.display.set_mode((maxW, maxH))

# Plotting dimensions
pCX = 200
pCY = 200

pSX = maxW / pCX
pSY = maxH / pCY

minX = -2
minY = -2
maxX = 2
maxY = 2

def is_in_mandelbrot(c, max_iter=100):
    z = 0
    for i in range(max_iter):
        z = z * z + c
        if abs(z) > 2:
            return False
    return True

window.fill((100, 100, 100))

for y in range(pCY):
    for x in range(pCX):
        # Convert pixel coordinate to complex number
        xSet = x / pCX * (maxX - minX) + minX
        ySet = y / pCY * (maxY - minY) + minY
        c = ff(xSet, ySet, weights, nodes)
        print(c)

        # Check if the complex number is in the Mandelbrot set
        if(c > 0.0):
            color = (255 * c, 255 * c, 255 * c)  # White for points in the set
        else:
            color = (0, 0, 0)       # Black for points not in the set

        # Draw the point
        pygame.draw.rect(window, color, (x * pSX, y * pSY, pSX, pSY))

# Update the display
pygame.display.flip()

# Keep the window open until it is closed by the user
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

