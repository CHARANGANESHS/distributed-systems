class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.lamport_clock = 0

    def send_message(self, receiver, message_text):
        self.lamport_clock += 1
        message = Message(self.node_id, message_text, self.lamport_clock)
        receiver.receive_message(message)

    def receive_message(self, message):
        self.lamport_clock = max(self.lamport_clock, message.lamport_clock) + 1
        print(f"Node {self.node_id} received message: {message.text}")
        print(f"Updated Lamport clock: {self.lamport_clock}")

    def __str__(self):
        return f"Node {self.node_id} - Lamport Clock: {self.lamport_clock}"

class Message:
    def __init__(self, sender_id, text, lamport_clock):
        self.sender_id = sender_id
        self.text = text
        self.lamport_clock = lamport_clock

class DistributedSystem:
    def __init__(self, num_nodes):
        self.nodes = [Node(i) for i in range(num_nodes)]

    def simulate(self):
        for i in range(len(self.nodes)):
            sender = self.nodes[i]
            receiver = self.nodes[(i + 1) % len(self.nodes)]
            sender.send_message(receiver, f"Hello from Node {sender.node_id}")

        for node in self.nodes:
            print(node)


if __name__ == "__main__":
    num_nodes = 3  
    system = DistributedSystem(num_nodes)
    system.simulate()