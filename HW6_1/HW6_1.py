#Champ Cain
#MAE3403
#HW6 part 1

#across HW6 part 1 I used AI mainly to help me implement pulling the data from the .txt files and inserting
# it into the coded functions

#region imports
from ResistorNetwork import ResistorNetwork, ResistorNetwork_2
#endregion

# region Function Definitions
def main():
    """
    This program solves for the unknown currents in the circuit of the homework assignment.
    :return: nothing
    """
    print("Network 1:")
    Net = ResistorNetwork()  # Instantiate a ResistorNetwork object
    Net.BuildNetworkFromFile("ResistorNetwork.txt")  # Call the function from Net that builds the resistor network from a text file
    IVals = Net.AnalyzeCircuit()

    print("\nNetwork 2:")
    Net_2 = ResistorNetwork_2()  # Instantiate a ResistorNetwork_2 object
    Net_2.BuildNetworkFromFile("ResistorNetwork_2.txt")  # Call the function from Net that builds the resistor network from a text file
    IVals_2 = Net_2.AnalyzeCircuit()
# endregion

# region function calls
if __name__ == "__main__":
    main()
# endregion