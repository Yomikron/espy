import logging, random, time
from espy.simulation.packet import Packet


class Router(object):
    """	Delivers packets from one client to another. 
		There is a probability of dropping a packet. This might be due to full buffer or lost connection. """

    def __init__(self, env, drop_probability, speed):
        self.env = env
        self.drop_probability = drop_probability

        self.log = logging.getLogger("Router")
        self.delay = 1 / speed
        self.clients = []

    def store_clients(self, clients):
        self.clients = clients

    def deliver_packet(self, packet):
        time.sleep(self.delay)
        if random.random() > self.drop_probability:
            self.log.debug(
                "Delivered packet from %d to %d: %s",
                packet.sender,
                packet.dest,
                packet.msg,
            )
            self.clients[packet.dest].incoming.interrupt(packet)
        else:
            self.log.warning(
                "Dropped packet from %d to %d: %s",
                packet.sender,
                packet.dest,
                packet.msg,
            )