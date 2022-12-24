#!/usr/bin/env python3

import pandas as pd

def cities():
    return pd.DataFrame([[643272, 715.48],[279044, 528.03],
    [231853, 689.59],[223027, 240.35],[201810,3817.52]],
    index= ["Helsinki","Espoo","Tampere","Vantaa","Oulu"],
    columns=["Population","Total area"])
    
def main():
    return
    
if __name__ == "__main__":
    main()
