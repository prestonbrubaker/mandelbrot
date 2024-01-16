import random
import time
import pygame

pygame.init()

nodes = []

weights = [0.7358027841338968, 0.6151775919555372, 1.256904241814905, 0.5721403474217536, 0.6121259289883032, 0.09143919648955527, 0.4034727930648704, 0.6758698794824227, -0.23773175346379954, 0.17763478213225306, 0.08704221100955441, -0.5531551442562237, 0.2532148835499021, 0.1592276557168938, -0.20736618281481004, 0.20844379251003337, -0.19860751934152915, 0.6055950344316401, -0.02967884908075644, 0.372053912898077, 1.5346091933401536, 0.18756540336848512, -0.01686995335581146, -0.031533290722479575, -0.06750929432193598, 0.8710275871055208, 0.251161648688126, 0.310823319535918, -0.1290351945858978, -0.030641129073643802, 1.0178353651336085, 0.6714001691812786, 1.3785491619695982, 1.0194580857761921, 1.3642404186754515, 0.9643093144709974, 0.65345388137622, -0.6459695820136695, 0.3239477799073823, 0.5093084247504431, 0.060990905732253964, 0.6802315785388734, 0.35907671323755924, 0.2582563351085727, 0.36134108437263857, -0.034386702072690505, 0.5642722626358955, 0.15367158067356568, 0.9156598980765961, -0.4674743311000947, 0.15328007249928663, -0.07873477235859754, 1.0117702071402848, 0.5913392331415233, 0.6575831410295748, -0.522645775764376, 0.00808267285758349, 1.0187259881629267, 0.2962397728605371, 0.42237033729592804, 0.4432818601745291, 0.2531345464072275, 0.6537293321053885, 0.36571391091933664, 0.19329687539179372, 0.9194180489523351, 0.5831370515073898, 1.0260643668558735, 1.3756632497642691, 1.3815938801973655, 0.7289278531237164, 0.8600865048646019, 1.0847503260564324, 0.980553987680145, 0.12021988811989577, 0.581615250940153, 0.18977925825358138, 0.520872953757581, 0.26613222236879225, 0.6682845672580137, 0.5174033021029654, 0.5220505950236499, 0.12717178967608112, 0.2963043513548053, 0.6043396556884655, -0.1694077587293857, 0.40141293504995174, 0.05979179625770438, 0.3997193971315544, 0.47152228686046904, 0.011639393174863422, 0.17914293808398093, 0.3141497816309067, 0.15391954583485687, 0.08126051988177597, 0.4231059284539506, 0.35314562416926454, 0.6298545153759931, 0.0007876154721081951, 1.0810925263816613, 0.18184873822613826, 0.031532737842553345, 0.6915347254291545, 0.7182199439119745, 1.020121901132658, 1.198295614106558, 0.9878115777384343, 0.6890476821659671, 0.7274335995077188, 0.12782681069605834, -0.3070089782120883, 0.36444139059436875, 0.37977138197100213, -0.3443171433549602, 0.7629104890269581, 0.13056897702993883, 0.20389929887369856, 0.04204534585395366, 0.10994546599127275, -0.6262543428763698, 0.8349725447925941, 0.07650115837667364, 0.6089589061134955, 0.5976518630576045, 0.29999910365710825, 1.0583452749335385, 0.8121450142297056, 0.9972183323624916, 0.5266498606988302, 0.49178772235798973, -0.28336308104071384, 0.6709549054206807, 0.754871111120107, 0.2770293363607346, 0.6422704485410669, 0.014509679380710584, -0.15029787280988297, 0.5662997848638383, 1.097534217894041, 1.1271312065969146, 1.1920219252019941, 1.4345727672854949, 1.110638426790885, 0.7761195854942083, 0.9299994484787909, 0.8563903370438264, 1.018915772180299, 0.3612103490306178, 0.7525463166001818, 0.5955693760433288, 0.7136343189704515, 0.46140963161715526, 1.2533601701436006, 0.38751941153594993, 0.9811129927551869, 0.99847096390831, 0.7774160278359592, 1.1665350739009133, 0.9842551560964983, 1.4974036146075653, 0.796006517906165, 1.2784775267309423, 0.8220568898983311, 1.045882577030392, 1.0119760004649399, 0.9450324267465076, 1.083360099240471, 0.7003913483034248, 0.47460621124196367, 0.15185437024074994, 0.12678906806755996, -0.031621797384615284, -0.015232070173045082, -0.08565176640916718, 0.6611557866412873, 0.8009363557825954, 1.0137570465028143, 0.6071139335637138, 0.7744729801972906, 0.7578216961390799]

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

