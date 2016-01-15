
import numpy

class membrane_lowpass(object):
    
    def __init__(self, Number_of_Neurons, tau):
        '''
        Initializes the neuron membranes.
        Number_of_Neurons: total number of neurons to be simulated
        tau: time constant (in seconds)
        '''
        self.neurons = numpy.zeros(Number_of_Neurons)
        self.times = numpy.zeros(Number_of_Neurons)
        self.tau = tau
    
    def process_spikes(self, spikes, current_time):
        '''
        Processes the received spikes at the current time updating their membrane values.
        spikes: list with the indexes of the neurons who spiked.
        current_time: the time the neurons spiked (float)
        '''
        delta_t = current_time-self.times[spikes] # Calculates the difference between the last time they spiked
        current_values = self.neurons[spikes]*numpy.exp(-delta_t/self.tau) # Calculates the current values
        self.times[spikes]=numpy.ones(len(spikes))*current_time # Updates the last time they spiked
        self.neurons[spikes] = current_values + numpy.ones(len(spikes)) # Updates the neuron membrane values

    def check_values(self, current_time):
        '''
        Returns the current membrane values at the specified time.
        current_time: time used to calculate the membrane values.
        '''
        delta_t = current_time-self.times # Calculates the time since last spike
        return self.neurons*numpy.exp(-delta_t/self.tau) # Calculates the current values
        