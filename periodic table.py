# Periodic table program

# -------------------------
# Subprograms
# -------------------------

element = input('Enter the symbol or name of an element:')

def periodic_table(element):
    if element == ('Li') or element == ('Lithium'):
        print('Element symbol: Li')
        print('Element: Lithium')
        print('Atomic weight: 6.94')
        print('Group: Alkali metal')
        
    elif element == ('Na') or element == ('Sodium'):
        print('Element symbol: Na')
        print('Element: Sodium')
        print('Atomic weight: 22.99')
        print('Group: Alkali metal')


    elif element == ('K') or element == ('Potassium'):
        print('Element symbol: K')
        print('Element: Potassium')
        print('Atomic weight: 39.098')
        print('Group: Alkali metal')
    
    elif element == ('F') or element == ('Fluorine'):
        print('Element symbol: F')
        print('Element: Fluorine')
        print('Atomic weight: 18.998')
        print('Group: Halogen')

        
        
    elif element == ('Cl') or element == ('Chlorine'):
        print('Element symbol: Cl')
        print('Element: Chlorine')
        print('Atomic weight: 35.45')
        print('Group: Halogen')

    
    elif element == ('Br') or element == ('Bromine'):
        print('Element symbol: Br')
        print('Element: Bromine')
        print('Atomic weight: 79.904')
        print('Group: Halogens')
    else:
        print('Element is not in the catalogue')
        
        
        
        
        




# -------------------------
# Main program
# -------------------------
print(periodic_table(element))
