class Node:
    def __init__(self, node_id, num_nodes):
        self.node_id = node_id
        self.vector_clock = [0] * num_nodes
        self.num_nodes = num_nodes

    def increment_clock(self):
        self.vector_clock[self.node_id] += 1

    def send_message(self, receiver, message_text):
        self.increment_clock()
        message = Message(self.node_id, message_text, self.vector_clock.copy())
        receiver.receive_message(message)

    def receive_message(self, message):
        for i in range(self.num_nodes):
            self.vector_clock[i] = max(self.vector_clock[i], message.vector_clock[i])
        self.increment_clock()
        print(f"Node {self.node_id} received message: {message.text}")
        print(f"Updated Vector clock: {self.vector_clock}")

    def __str__(self):
        return f"Node {self.node_id} - Vector Clock: {self.vector_clock}"

class Message:
    def __init__(self, sender_id, text, vector_clock):
        self.sender_id = sender_id
        self.text = text
        self.vector_clock = vector_clock

class DistributedSystem:
    def __init__(self, num_nodes):
        self.nodes = [Node(i, num_nodes) for i in range(num_nodes)]

    def simulate(self):
        for i in range(len(self.nodes)):
            for j in range(i+1, len(self.nodes)):
                self.nodes[i].send_message(self.nodes[j], f"Hello from Node {i}")
                self.nodes[j].send_message(self.nodes[i], f"Hello from Node {j}")

        for node in self.nodes:
            print(node)
        
if __name__ == "__main__":
    system = DistributedSystem(3)
    system.simulate()