import random
import time
import pygame

pygame.init()

nodes = []

weights = [-0.21263279928227932, 0.03316779223719374, 0.03291901987936425, -0.11122465040519575, 0.03238870161821709, -0.20437005587865356, -0.182710146386878, 0.6026897448685452, 0.1712416977723996, -0.30400932911918144, 0.09077308521447698, -0.024613161346148, -0.038098863781436745, -0.020472858222442127, 0.24279919305821862, -0.5486451756590476, -0.24182595637705395, -0.2985102475235712, 0.053297211053268706, 0.1044036804079083, 0.03239809258124234, -0.17592035134322037, -0.10533879770577895, 0.02237043188469023, -0.41676500315829385, -0.09448350427554254, 0.10227005825925241, -0.13555187181170714, -0.20318570876147055, -0.11447025717667733, 0.1202586338892312, 0.25352073721445445, 0.12680082873932377, -0.24752778712435441, 0.10511278226564692, -0.13906055099947853, -0.10151640272792908, -0.1362442251496265, -0.06137523396391273, -0.1932764586585706, 0.09613021318013185, -0.3961022944860231, -0.04885233662855372, -0.4081159561272678, -0.28405116435334665, -0.28479618110935323, -0.5164963916996126, -0.17733876637222518, -0.49752789126759805, -0.15424587492188901, -0.20610527417276225, -0.22951120914359804, -0.36118695947572754, -0.23877256296455285, -0.3643699108969631, 0.1166460923466235, -0.05134195501937632, -0.20767661107590257, -0.32190345388976044, -0.2619451249958248, -0.33894209361472916, -0.04058781416273706, -0.11661962315613798, -0.30529026119764424, -0.028054192072884097, 0.1073554658068295, 0.35688305195174547, 0.2917854831014758, -0.26128096177330307, -0.08339219736788218, 0.3929191775674705, -0.026602300767446484, -0.5243144236176572, -0.3082499889026873, -0.35320905083597054, -0.29972203103860945, -0.46595555979926173, -0.34775364658094404, -0.14150902178962624, -0.03561575500455617, -0.46335666840448153, -0.23514280397711698, -0.213323232836667, -0.4405916120785471, 0.07576255062173975, -0.47703241564870624, -0.36259270357347123, -0.3103170126043164, -0.33870907529061045, -0.1278268528185452, -0.2446216994995262, -0.15366163557303875, -0.43540055345274886, -0.5862638614351606, -0.3359794753741498, -0.1536053362426506, -0.6239170136742255, -0.31402973008078955, -0.09883165189217545, -0.43290890931245435, -0.10197972420753715, -0.19603239152305477, 0.14651389448830068, 0.12314717588299008, 0.09468327699163112, 0.06243259896925896, 0.25311680214700355, -0.0911245248593864, -0.2630791706499663, -0.4195981764547538, -0.461370984502193, -0.21583893024029407, -0.7103615840194819, -0.5738497515238744, -0.5387824504427717, -0.3500151483557831, -0.5559016614039842, -0.31559754167625936, -0.17760839962204497, -0.5634495292467337, -0.5387735635860401, -0.8776931368594738, -0.5678652254309582, -0.3413014984093851, -0.4047362037498039, -0.39105436029411456, -0.503819767646368, -0.27928226004670753, -0.13053433377848384, -0.23881615630537714, -0.20783061327247035, -0.23029680428387128, -0.37876794854321666, -0.173973340982932, -0.7331028296173325, -0.15444963993893024, -0.41308811553668157, -0.3314084100214135, 0.16038159636111562, -0.05973019859983397, -0.2019353519923867, -0.04493347453223694, 0.049326030669342005, -0.12922638638289838, -0.09407132474558798, 0.024038916768610072, -0.01617031676937627, 0.05962251230618721, 0.06646205425564221, 0.01794512215424286, -0.14773971507625236, 0.010743738604280436, -0.05004379092806612, -0.17808578564332964, 0.007167966506344982, 0.10818283987293444, -0.2747337524119639, -0.034887953511719916, 0.23784026698090907, 0.39675559270657146, 0.27678574541927947, -0.30943369971184276, -0.11277245983864025, -0.16051151753794773, 0.21653168079945537, -0.05344245568405158, 0.2817364350412716, -0.1599238807198073, 0.5334491906384353, 0.27501089217525204, 0.715384403645519, 0.6228196367129806, 0.4812865842819514, 0.7405274339065231, 0.0971165691791795, -0.2688884012755512, 0.1820184745198246, 0.13787315981800932, 0.14593159983145232, 0.06992215141954108]



#[0.7962194427262359, 0.8679136356598196, 1.345672324836952, 0.7107690480459323, 0.7189847086695862, 0.09622256967096318, 0.42791886820574265, 1.3031794297969592, -0.3689764222778109, -0.015442874224206926, -0.07920273673900985, -0.5280142372452709, 0.26634206883452877, 0.0032430609155442514, 0.9178467229570844, 0.27951436956422665, -0.1095795548247234, 0.7691664842621744, -0.05031832331869129, -0.0394776140478494, 1.7979141229402131, 0.15856123770819713, -0.00507558315255628, -0.16340426147575965, -0.13016428241044714, 1.1302766810555767, 0.34627340327790507, 0.19997919675180484, -0.14752148848777072, -0.07664769957986546, 1.1436526589066236, 1.0671646637881214, 2.085862676233181, 0.7958645853459808, 1.1764094455209346, 0.7694987035976301, 0.6216995479379452, -0.47481916806923546, 1.0965130062663526, 0.6085135489805698, 0.1294976219828699, 1.3261138308718043, 0.025436346945815484, 0.16156872118296942, 1.3422329659291012, -0.12733273521912192, 0.5491375978619222, 0.5671193258513063, 0.8457940283299448, -0.5229823728114003, 0.8089812643121039, -0.1594870765579088, 0.9752253633852064, 1.0917765985068948, 0.7164631173246411, -0.5991989957415279, 1.084055978859935, 1.2174296697698737, -0.6803578280586566, 0.7087640109568999, 0.7198969783629129, 0.45427395426052347, -0.25444642860661537, 0.7307941507419792, 0.5262033898050019, 0.819429556952168, 0.6301039521548017, 1.1770499763897888, 1.5499290650089628, 1.3647090236245787, 0.5586087823279018, 1.2082936422181374, 1.2953320405889115, 1.3500282047571817, 0.056912961871348006, -0.2638961363604728, 0.2185039117991345, 0.37555002835887186, 0.2851073126949273, 0.06540392283032595, 0.5829592845344722, 2.2360759283395097, 0.2449155642489743, 0.13803978705747413, 0.854719524215686, 0.13471279469880237, 0.5591455507283938, -1.1481894253026923, 0.3539200393378668, 0.4938995045494968, 0.21185921704676913, 0.169414792682728, 0.2914889868413274, -0.6947977228082256, 0.1906634263868198, 0.40041538107418967, 0.1188822883544649, 0.6417426120605517, 0.32147701341618506, 2.4826227875332108, 0.1272732883723633, -0.012603704495031794, 0.3663733928805913, 0.8473542656174747, 1.063344612273713, 0.8654906398679084, 0.8112849873414726, 1.0009288895070596, 1.0590307262275316, 0.25071605042332556, -0.7203910088062605, 0.36565539965631205, 0.5261612162869103, -0.9272305977134786, 1.0303954371541884, 0.10278691223570148, -0.008066049596298216, 0.10585113498922742, 0.16435953578179463, -1.2154315785410013, 0.692649654112871, -0.059815484738408115, 1.3253223903373705, 0.5273584584532695, 0.4285343798307263, 2.1324643575516293, 0.6205121810506705, 0.9588653412639484, 0.9159110256044164, 0.19671139332996326, -0.11127627040439694, 1.1631364458448505, 0.60523898481079, 0.3343835275787304, 1.2816630449419317, -0.13188165037572758, -0.0026406245936370382, 1.1278221961639927, 1.4786204587157044, 1.0094078912430473, 0.8072776374696843, 0.9407892660083346, 1.2091939679322443, 0.7939001728000052, 1.007002448538206, 1.0406663892138723, 1.1665661199242818, 0.41911491230277814, 0.7300162099388413, 0.5074402143773588, 0.785236412526618, 0.658677455126833, 1.2805641330254538, 0.281512927752482, 1.2162029938930778, 1.1768194480466572, 0.8338955386950271, 0.903834475129456, 0.9737794694045684, 1.7734539769575541, 0.840631480326589, 1.030452793529139, 0.6779911409757606, 1.1643529480607535, 1.1424731183150767, 0.7861559555608123, 1.1175347992357827, 0.5812378350183479, 0.4712619346187793, 0.2911856460307302, 0.45970440471282853, -0.04885593600332515, -0.02017399113397975, -0.11131071739237292, 0.7107231503166969, 1.0892071618205381, 0.9110701723766078, 0.6091903101522917, 0.7762570844429182, 0.6603167273420392]


itC = 0
species = 0

# 6x6 neural network with a bias node for each layer. Rectified linear function will be used.


len_weights = 6*6*5

len_nodes = 6*6
for i in range(0,len_nodes):
    nodes.append(0)



def sigmoid(x):
    if(x > 20):
        x = 20
    if(x < -20):
        x = -20
    sigma = (1 / (1 + 2 ** x))
    return sigma
    #if(x > 0):
        #return x
    #else:
        #return 0


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
        if(c > 0.0 and c < 1):
            color = (255 * c, 255 * c, 255 * c)  # White for points in the set
        elif(c <= 0):
            color = (0, 0, 0)       # Black for points not in the set
        else:
            color = (255, 255, 255)

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

