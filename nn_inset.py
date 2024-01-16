import random
import time

nodes = []

weights = [0.8001862893468211, 0.9283233198152867, 1.3425986083342858, 0.7013994251329144, 0.7216632663341146, 0.10518363969226024, 0.3936497560113054, 0.8106192308918223, -0.5637398366287638, 0.023971499555866343, 0.03892618091636121, -0.5970274639416575, 0.4105316224114141, 0.034856864214237566, 0.4670548315159229, 0.23293979674927145, -0.09411502217455492, 0.7632714463016228, -0.05697520703984963, 0.05277228296113587, 1.7926983953094378, 0.20664668108056944, -0.0024360562523389195, -0.16653230534768992, -0.08795133525334946, 1.3164100074423362, 0.03890585570822553, 0.28770257416647876, -0.12297912195201081, -0.003378178776821997, 1.0706520820545558, 0.7667338535933171, 1.8117935275331791, 1.0571920807688517, 1.3515885585216632, 0.970081171391864, 0.5950809399919074, -0.571700224291175, 0.42830045313938514, 0.5690471633456065, 0.3118040496216153, 0.9900094423083303, 0.1051767050516718, 0.10764365993360218, 0.6980018975180771, -0.1324416617380499, 0.6408440887557736, 0.5564804692213495, 0.847816413712478, -0.5291921399898268, 0.40826545033309136, -0.16311168896056338, 0.9706378117796485, 1.0121055546679771, 0.6853896294601882, -0.7767881417415127, 0.3973962502478446, 0.9630862635890947, 0.2750657147386993, 0.30256233405126093, 0.5426479477445394, 0.5022227617399847, 0.3681790091243817, 0.7341211112107482, -0.13933864829807643, 0.8135827374515099, 0.6832982150126512, 1.1321023093680052, 1.550539945782327, 1.4026356712189518, 0.6103321576419157, 1.014136423930706, 1.2069830150634493, 1.0984262381645091, -0.08408820664344654, 0.427771131298359, 0.10106896200088998, 0.4710115725228995, 0.18522670852956485, 0.5984379749658643, 0.7476804964849326, 2.0188047561100126, 0.2868577563893259, 0.11834192602601476, 0.8038232891216092, -0.10874599844994841, 0.28770793698528, -0.24115913720709242, 0.2531013862267858, 0.5668806180090495, 0.12812704732828434, -0.0887371662130796, 0.2898824174685416, -0.46681397951673287, 0.0742188896429147, 0.4704717215824824, 0.15206704179023892, 0.8892857282413553, 0.3322913867261914, 1.6150385168146817, 0.13092304914840017, 0.018447535195835404, 0.5849075037265542, 0.9444460706458713, 0.9697432847621679, 1.1873962715093878, 1.1396622489546633, 0.8805412251874897, 0.9877884595922707, 0.18685320568768513, -0.687747245074572, 0.403518651568057, 0.5574129493318742, -0.6374573377929568, 1.0199957353859688, 0.09296908335312282, 0.0013158975454214063, 0.09658019451311715, 0.1597527393219014, -1.044326158554604, 0.425647018509239, -0.09569276375225215, 1.035361080355116, 0.48006021997230686, 0.5230387619805548, 1.475483842654488, 0.7727074789900749, 0.9536254104232996, 0.7465867419735005, 0.3820891567821116, 0.14238921528377046, 0.7666844235283633, 0.6120262943799025, 0.3529688399913593, 0.911460567177212, -0.03745327328362859, -0.09419763359887544, 1.1575830868709474, 1.304470599061844, 0.9996507813455069, 0.9422265116426871, 1.2000295742798208, 1.0905103639806066, 0.7317709455161925, 0.9062262986875316, 0.7833671218012318, 1.1230545168446535, 0.4985354800397884, 0.7291348021665938, 0.5538576164095231, 0.8652309646597974, 0.5232163986505083, 1.1747118140478447, 0.5838076620377166, 1.1004507080351957, 0.9052843811932225, 0.6081458647733752, 0.9831218217227257, 1.0551976931626488, 1.6893036907961505, 0.9918326170084032, 1.130796747307397, 0.6521538834925434, 1.1339680859558654, 1.1974921279677881, 0.8141872716991079, 1.0043140454806476, 0.4711281096214784, 0.5080528913607043, 0.26231144683466534, 0.4047986247410251, -0.04611147575686831, -0.020558982124250984, -0.10212500496687943, 0.8443091220491812, 0.8111298957977814, 0.9803587159421066, 0.6673243314077034, 0.7568607454102624, 0.7110221266557482]


weights_trial = []
loss_best = 100000000000000
itC = 0
species = 0
data_examples = 1000

# 6x6 neural network with a bias node for each layer. Rectified linear function will be used.


len_weights = 6*6*5
for i in range(0, len_weights):
    #weights.append(1)
    weights_trial.append(1)

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
    for i in range(0, data_examples):
        x = extracted_numbers[i][0]
        y = extracted_numbers[i][1]
        a = extracted_numbers[i][2]
        a_guess = ff(x, y, weights_in, nodes_in)
        loss = ((a - a_guess) ** 2) / data_examples * 100
        sum += loss

    return sum

#print(loss(nodes, weights))

while True:
    #print(loss(nodes, weights))
    for i in range(0, len_weights):
        weights_trial[i] = weights[i]
    random_mag = 10 ** random.randint(-11, -1)
    for i in range(0, len_weights):
        if(random.uniform(0, 1) < 2 / len_weights):
            weights_trial[i] += random.uniform(-1,1) * random_mag
    
    #print(weights_trial)
    loss_trial = loss(nodes, weights_trial)
    if(loss_trial < loss_best):
        loss_best = loss_trial
        print("\n\n\n\n" + str(weights_trial))
        print("\n\n" + str(loss_best))
        for i in range(0, len_weights):
            weights[i] = weights_trial[i]

        species += 1
    itC += 1





