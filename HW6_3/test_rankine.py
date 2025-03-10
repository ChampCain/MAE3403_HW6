#Champ Cain
#MAE 3403
#HW6 part 3

# I used AI to help once again with the integration from .txt documents
# I also was unsure if I was supposed to make a graph or not of the outputs. My attmepts at doing so
# were not looking very good unfortunately.


from rankine import rankine

def main():
    # Rankine cycle with saturated vapor entering the turbine
    rankine_cycle_1 = rankine(p_low=8, p_high=8000, t_high=None, name='Rankine Cycle 1')
    rankine_cycle_1.calc_efficiency()
    rankine_cycle_1.print_summary()

    # Rankine cycle with superheated steam entering the turbine
    rankine_cycle_2 = rankine(p_low=8, p_high=8000, t_high=1.7 * 295.06, name='Rankine Cycle 2')  # Tsat at 8000 kPa is 295.06°C
    rankine_cycle_2.calc_efficiency()
    rankine_cycle_2.print_summary()

if __name__ == "__main__":
    main()