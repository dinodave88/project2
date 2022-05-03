import math
import textwrap
from tokenize import Double
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_3D(request):
    return render(request,"App1.html")

def run_3D(request):
    Width = float(request.POST["Width"])
    Height = float(request.POST["Height"])
    Slope = float(request.POST["Slope"])
    FS_Slope = float(request.POST["FS_Slope"])
    Ridge_distance = float(request.POST["Ridge_distance"])

    SW_spacing1 = request.POST["SW_spacing"]
    A_list = SW_spacing1.split()
    map_object = map(float, A_list)
    SW_spacing = list(map_object)

    EW_spacing1 = request.POST["EW_spacing"]
    A_list = EW_spacing1.split()
    map_object = map(float, A_list)
    EW_spacing = list(map_object)

    NSR_Breaks1 = request.POST["NSR_Breaks"]
    A_list = NSR_Breaks1.split()
    map_object = map(float, A_list)
    NSR_Breaks = list(map_object)

    FSR_Breaks1 = request.POST["FSR_Breaks"]
    A_list = FSR_Breaks1.split()
    map_object = map(float, A_list)
    FSR_Breaks = list(map_object)

    ICO_spacing1 = request.POST["ICO_spacing"]
    A_list = ICO_spacing1.split()
    map_object = map(float, A_list)
    ICO_spacing = list(map_object)

    Braced_bay_location1 = request.POST["Braced_bay_location"]
    A_list = Braced_bay_location1.split()
    map_object = map(int, A_list)
    Braced_bay_location = list(map_object)

    NSC_SUPPORT = request.POST["NSC_SUPPORT"]


    FSC_SUPPORT = request.POST["FSC_SUPPORT"]
    

    WC_SUPPORT = request.POST["WC_SUPPORT"]
   

    ICO_SUPPORT = request.POST["ICO_SUPPORT"]
 

    DL = float(request.POST["DL"])
    LL = float(request.POST["LL"])
    CL = float(request.POST["CL"])

    WL = float(request.POST["WL"])
    Cpi = float(request.POST["Cpi"])

    Zone_factor = float(request.POST["Zone_factor"])
    Response_reduction_factor = float(request.POST["Response_reduction_factor"])
    Importance_factor = float(request.POST["Importance_factor"])
    Rock_and_soil_site_factor = float(request.POST["Rock_and_soil_site_factor"])
    Damping_ratio = float(request.POST["Damping_ratio"])


    LOADS_REQUIRED = request.POST["LOADS_REQUIRED"]
    SEISMIC_CODE = request.POST["SEISMIC_CODE"]


    FS_Height = Height  + (Ridge_distance*Slope ) - ((Width - Ridge_distance)*FS_Slope )

    Dslope=math.degrees(math.atan(Slope))
    FS_Dslope=math.degrees(math.atan(FS_Slope))
    print(Dslope)


    #####################################

    def Side_wall_sp():
        Sidewall = []
        x = 0
        for i in SW_spacing:
            x = x+i
            Sidewall.append(round(x, 4))
        Sidewall.insert(0, 0)
        return Sidewall

    SW1 = Side_wall_sp()
    print('SW1')
    print(SW1)

    Length = SW1[-1]
    print('Length')
    print(Length)
    #####################################

    #####################################


    def Side_wall_sp1():
        Sidewall1 = []
        for x in SW_spacing:
            Sidewall1.append(x)
        Sidewall1.insert(0, 0)
        Sidewall1.append(0)
        return Sidewall1


    SW2 = Side_wall_sp1()
    print('SW2')
    print(SW2)
    #####################################

    #####################################
    Diff_bay_sp = []
    x = 0
    while x < (len(SW2)-1):
        Diff_bay_sp.append(((SW2[x+1]+SW2[x])/2))
        x = x+1

    print('Diff_bay_sp')
    print(Diff_bay_sp)

    Unique_bay_sp = set(Diff_bay_sp)
    print('Unique_bay_sp')
    print(Unique_bay_sp)
    #####################################


    #####################################
    def NS_Rafter_Breaks():
        NS_Rafter = []
        y = []
        x = 0
        for i in NSR_Breaks:
            x = (x+i)
            y.append(x)
        y.reverse()

        for j in y:
            r = math.degrees(math.atan(Slope))
            xx = j*(math.cos(math.radians(r)))
            z = (Ridge_distance)-xx
            NS_Rafter.append(round(z, 4))
        return NS_Rafter


    NSR = NS_Rafter_Breaks()
    print('NSR')
    print(NSR)
    #####################################


    #####################################
    def FS_Rafter_Breaks():
        FS_Rafter = []
        y = []
        x = 0
        for i in FSR_Breaks:
            x = (x+i)
            y.append(x)

        for j in y:
            r = math.degrees(math.atan(Slope))
            xx = j*(math.cos(math.radians(r)))
            z = (Ridge_distance)+xx
            FS_Rafter.append(round(z, 4))
        return FS_Rafter


    FSR = FS_Rafter_Breaks()
    print('FSR')
    print(FSR)
    #####################################


    #####################################
    Rafter_Breaks = NSR+FSR
    print('Rafter_Breaks')
    print(Rafter_Breaks)
    #####################################


    #####################################
    def End_wall_sp():
        Endwall = []
        x = 0
        for i in EW_spacing:
            x = x+i
            Endwall.append(round(x, 4))
        return Endwall


    EW1 = End_wall_sp()
    print('EW1')
    print(EW1)

    #####################################

    #####################################
    EW11 = []
    for x in EW1:
        EW11.append(x)

    for x in Rafter_Breaks:
        if x not in EW11:
            EW11.append(x)
        EW11.sort()
    print('EW11')
    print(EW11)
    #####################################


    #####################################
    EW2 = []
    for x in EW1:
        EW2.append(x)
    if Width in EW2:
        EW2.remove(Width)

    print('EW2')
    print(EW2)
    #####################################

    #####################################


    def End_wall_sp2():
        Endwall2 = []
        for x in EW_spacing:
            Endwall2.append(x)
        Endwall2.insert(0, 0)
        Endwall2.append(0)
        return Endwall2


    EW3 = End_wall_sp2()
    print('EW3')
    print(EW3)
    #####################################

    #####################################
    Diff_EW_bay_sp = []
    x = 0
    while x < (len(EW3)-1):
        Diff_EW_bay_sp.append(((EW3[x+1]+EW3[x])/2))
        x = x+1

    print('Diff_EW_bay_sp')
    print(Diff_EW_bay_sp)

    Unique_EW_bay_sp = set(Diff_EW_bay_sp)
    print('Unique_EW_bay_sp')
    print(Unique_EW_bay_sp)
    #####################################

    #####################################


    def ICO_column_sp():
        Int_column = []
        x = 0
        for i in ICO_spacing:
            x = x+i
            Int_column.append(x)
        if Width in Int_column:
            Int_column.remove(Width)
        return Int_column


    ICO = ICO_column_sp()
    print('ICO')
    print(ICO)

    #####################################

    #####################################
    ICO_for_rafter_Lz = []
    Final_ICO_Dist = 0
    for x in ICO_spacing:
        ICO_for_rafter_Lz.append(x)
        Final_ICO_Dist = Final_ICO_Dist + x

    ICO_for_rafter_Lz.append(Width-Final_ICO_Dist)

    print('ICO_for_rafter_Lz')
    print(ICO_for_rafter_Lz)

    #####################################

    #####################################
    EW3 = []
    for x in EW2:
        EW3.append(x)
    for x in EW3:
        if x in ICO:
            EW3.remove(x)

    print('EW3')
    print(EW3)
    #####################################
    #####################################
    EW_for_WC_Lz = []
    for x in EW3:
        if x <= Ridge_distance:
            EW_for_WC_Lz.append(x)
        else:
            EW_for_WC_Lz.append(Width-x)
    print('EW_for_WC_Lz')
    print(EW_for_WC_Lz)
    #####################################

    #####################################


    def End_wall_sp1():
        Endwall1 = []
        for x in EW_spacing:
            Endwall1.append(x)
        Endwall1.insert(0, 0)
        Endwall1.append(0)
        return Endwall1


    EW4 = End_wall_sp1()
    print('EW4')
    print(EW4)
    #####################################

    #####################################


    def Frame_X_Coordinate():
        X_Coordinate = []
        for i in EW1:
            X_Coordinate.append(i)

        X_Coordinate.append(0)
        X_Coordinate.append(Ridge_distance)
        X_Coordinate.append(Width)
        X_Coordinate = list(dict.fromkeys(X_Coordinate))
        X_Coordinate.sort()
        X_Coordinate.insert(0, 0)
        X_Coordinate.append(Width)
        return X_Coordinate


    EWX = Frame_X_Coordinate()
    print('EWX')
    print(EWX)

    #####################################

    #####################################
    for x in Rafter_Breaks:
        if x not in EWX:
            EWX.append(x)
        EWX.sort()
    print(EWX)
    #####################################


    #####################################
    def Frame_Y_Coordinate():
        Y_Coordinate = []
        if (Ridge_distance) not in EW11:
            EW11.append(Ridge_distance)
            EW11.sort()
        for i in EW11:
            if i > Ridge_distance:
                y = ((Width-i)*FS_Slope)+FS_Height
                Y_Coordinate.append(y)
            else:
                y = (i*Slope)+Height
                Y_Coordinate.append(y)
        Y_Coordinate.insert(0, 0)
        Y_Coordinate.insert(1, Height)
        Y_Coordinate.append(0)
        return Y_Coordinate


    EWY = Frame_Y_Coordinate()
    print('EWY')
    print(EWY)
    #####################################

    #####################################


    def ICO_Nodes():
        ICO_Nodes = []
        j = 0
        while j < len(ICO):
            i = 0
            while i < len(EWX):
                if ICO[j] == EWX[i]:
                    ICO_Nodes.append(i+1)
                i = i+1
            j = j+1
        return ICO_Nodes


    ICO_Nodes = ICO_Nodes()
    print('ICO_Nodes')
    print(ICO_Nodes)
    #####################################

    #####################################
    ICO_nodes_for_Rafter_Lz = [2]

    for x in ICO_Nodes:
        ICO_nodes_for_Rafter_Lz.append(x)

    ICO_nodes_for_Rafter_Lz.append(len(EWX)-1)

    print('ICO_nodes_for_Rafter_Lz')
    print(ICO_nodes_for_Rafter_Lz)
    #####################################

    #####################################
    x = 0
    while x < len(EWX):
        if EWX[x] == Ridge_distance:
            Ridge_node = x
        x = x+1

    print('Ridge_node')
    print(Ridge_node)
    #####################################

    #####################################


    def Bracing_Nodes():
        BR_Nodes = []
        j = 0
        while j < len(EW1):
            i = 0
            while i < len(EWX):
                if EW1[j] == EWX[i]:
                    BR_Nodes.append(i+1)
                i = i+1
            j = j+1
        BR_Nodes.append(2)
        BR_Nodes.remove(len(EWX))
        x = 0
        while x < len(EWX):
            if EWX[x] == Ridge_distance:
                k = x+1
            x = x+1
        if k not in BR_Nodes:
            BR_Nodes.append(k)
        BR_Nodes.sort()
        return BR_Nodes


    BR_Nodes = Bracing_Nodes()
    print('BR_Nodes')
    print(BR_Nodes)
    #####################################

    #####################################


    def Bracing_Nodes1():
        BR_Nodes1 = []
        j = 0
        while j < len(EW1):
            i = 0
            while i < len(EWX):
                if EW1[j] == EWX[i]:
                    BR_Nodes1.append(i+1)
                i = i+1
            j = j+1
        BR_Nodes1.append(2)
        BR_Nodes1.remove(len(EWX))
        BR_Nodes1.sort()
        return BR_Nodes1


    BR_Nodes1 = Bracing_Nodes1()
    print('BR_Nodes1')
    print(BR_Nodes1)
    #####################################

    #####################################


    def ICO_Nodes1():
        x = 0
        ICO_Nodes1 = []
        while x < len(ICO_Nodes):
            y = 0
            while y < len(BR_Nodes):
                if ICO_Nodes[x] == BR_Nodes[y]:
                    ICO_Nodes1.append(y)
                y = y+1
            x = x+1
        return ICO_Nodes1


    ICO_Nodes1 = ICO_Nodes1()
    print('ICO_Nodes1')
    print(ICO_Nodes1)
    #####################################

    #####################################


    def ICO_Nodes2():
        x = 0
        ICO_Nodes2 = []
        while x < len(ICO_Nodes):
            y = 0
            while y < len(BR_Nodes1):
                if ICO_Nodes[x] == BR_Nodes1[y]:
                    ICO_Nodes2.append(y)
                y = y+1
            x = x+1
        return ICO_Nodes2


    ICO_Nodes2 = ICO_Nodes2()
    print('ICO_Nodes2')
    print(ICO_Nodes2)
    #####################################

    #####################################


    def WC_Nodes():
        WC_Nodes = []
        j = 0
        while j < len(EW2):
            i = 0
            while i < len(EWX):
                if EW2[j] == EWX[i]:
                    WC_Nodes.append(i+1)
                i = i+1
            j = j+1
        return WC_Nodes


    WC_Nodes = WC_Nodes()
    print('WC_Nodes')
    print(WC_Nodes)
    #####################################

    #####################################


    def Only_WC_Nodes():
        for x in ICO_Nodes:
            if x in WC_Nodes:
                WC_Nodes.remove(x)
        return WC_Nodes


    Only_WC_Nodes = Only_WC_Nodes()
    print('Only_WC_Nodes')
    print(Only_WC_Nodes)
    #####################################


    #####################################
    def Only_WC_Distance():
        for x in ICO:
            if x in EW2:
                EW2.remove(x)
        return EW2


    Only_WC_Distance = Only_WC_Distance()
    print('Only_WC_Distance')
    print(Only_WC_Distance)
    #####################################

    #####################################


    def Pieces():
        Pieces = []
        j = 0
        while j < len(Rafter_Breaks):
            i = 0
            while i < len(EW11):
                if Rafter_Breaks[j] == EW11[i]:
                    Pieces.append(i+2)
                i = i+1
            j = j+1
        return Pieces


    Pieces = Pieces()
    print('Pieces')
    print(Pieces)
    #####################################

    #####################################
    if Length >= Width:
        Length1 = Length
        Width1 = Width
    else:
        Length1 = Width
        Width1 = Length


    # (H/W <= 1/2) & (1 < L/W <= 3/2)
    ISW1 = [0.7, -0.2, -0.5, -0.5]
    ISW2 = [-0.5, -0.5, 0.7, -0.2]

    if Height/Width1 <= 1/2:
        if Length1/Width1 >= 1 and Length1/Width1 <= 3/2:
            Cpe1 = ISW1[0]
            Cpe4 = ISW1[1]
            Cpe5 = ISW1[2]
            Cpe6 = ISW1[3]

            Cpe1a = ISW2[0]
            Cpe4a = ISW2[1]
            Cpe5a = ISW2[2]
            Cpe6a = ISW2[3]

    # (H/W <= 1/2) & (3/2 < L/W < 4)
    ISW11 = [0.7, -0.25, -0.6, -0.6]
    ISW12 = [-0.5, -0.5, 0.7, -0.1]

    if Height/Width1 <= 1/2:
        if Length1/Width1 >= 3/2 and Length1/Width1 < 4:
            Cpe1 = ISW11[0]
            Cpe4 = ISW11[1]
            Cpe5 = ISW11[2]
            Cpe6 = ISW11[3]

            Cpe1a = ISW12[0]
            Cpe4a = ISW12[1]
            Cpe5a = ISW12[2]
            Cpe6a = ISW12[3]

    # (1/2 < H/W <= 3/2) & (1 <= L/W <= 3/2)
    ISW21 = [0.7, -0.25, -0.6, -0.6]
    ISW22 = [-0.6, -0.6, 0.7, -0.25]

    if Height/Width1 > 1/2 and Height/Width1 <= 3/2:
        if Length1/Width1 >= 1 and Length1/Width1 <= 3/2:
            Cpe1 = ISW21[0]
            Cpe4 = ISW21[1]
            Cpe5 = ISW21[2]
            Cpe6 = ISW21[3]

            Cpe1a = ISW22[0]
            Cpe4a = ISW22[1]
            Cpe5a = ISW22[2]
            Cpe6a = ISW22[3]

    # (1/2 < H/W <= 3/2) & (3/2 <= L/W < 4)
    ISW31 = [0.7, -0.3, -0.7, -0.7]
    ISW32 = [-0.5, -0.5, 0.7, -0.1]

    if Height/Width1 > 1/2 and Height/Width1 <= 3/2:
        if Length1/Width1 >= 3/2 and Length1/Width1 < 4:
            Cpe1 = ISW31[0]
            Cpe4 = ISW31[1]
            Cpe5 = ISW31[2]
            Cpe6 = ISW31[3]

            Cpe1a = ISW32[0]
            Cpe4a = ISW32[1]
            Cpe5a = ISW32[2]
            Cpe6a = ISW32[3]

    # (3/2 < H/W < 6) & (1 < L/W <= 3/2)
    ISW41 = [0.8, -0.25, -0.8, -0.8]
    ISW42 = [-0.8, -0.8, 0.8, -0.25]

    if Height/Width1 > 3/2 and Height/Width1 < 6:
        if Length1/Width1 > 1 and Length1/Width1 <= 3/2:
            Cpe1 = ISW41[0]
            Cpe4 = ISW41[1]
            Cpe5 = ISW41[2]
            Cpe6 = ISW41[3]

            Cpe1a = ISW42[0]
            Cpe4a = ISW42[1]
            Cpe5a = ISW42[2]
            Cpe6a = ISW42[3]

    # (3/2 < H/W < 6) & (3/2 <= L/W < 4)
    ISW51 = [0.7, -0.4, -0.7, -0.7]
    ISW52 = [-0.5, -0.5, 0.8, -0.1]

    if Height/Width1 > 3/2 and Height/Width1 < 6:
        if Length1/Width1 >= 3/2 and Length1/Width1 < 4:
            Cpe1 = ISW51[0]
            Cpe4 = ISW51[1]
            Cpe5 = ISW51[2]
            Cpe6 = ISW51[3]

            Cpe1a = ISW52[0]
            Cpe4a = ISW52[1]
            Cpe5a = ISW52[2]
            Cpe6a = ISW52[3]

    # (H/W >= 6) & (L/W = 3/2)
    ISW61 = [0.95, -1.85, -0.9, -0.9]
    ISW62 = [-0.8, -0.8, 0.9, -0.85]

    if Height/Width1 >= 6:
        if Length1/Width1 == 3/2:
            Cpe1 = ISW61[0]
            Cpe4 = ISW61[1]
            Cpe5 = ISW61[2]
            Cpe6 = ISW61[3]

            Cpe1a = ISW62[0]
            Cpe4a = ISW62[1]
            Cpe5a = ISW62[2]
            Cpe6a = ISW62[3]

    # (H/W >= 6) & (L/W = 1)
    ISW71 = [0.95, -1.25, -0.7, -0.7]
    ISW72 = [-0.7, -0.7, 0.95, -1.25]

    if Height/Width1 >= 6:
        if Length1/Width1 == 1:
            Cpe1 = ISW71[0]
            Cpe4 = ISW71[1]
            Cpe5 = ISW71[2]
            Cpe6 = ISW71[3]

            Cpe1a = ISW72[0]
            Cpe4a = ISW72[1]
            Cpe5a = ISW72[2]
            Cpe6a = ISW72[3]

    # (H/W >= 6) & (L/W = 2)
    ISW81 = [0.85, -0.75, -0.75, -0.75]
    ISW82 = [-0.75, -0.75, 0.85, -0.75]

    if Height/Width1 >= 6:
        if Length1/Width1 == 2:
            Cpe1 = ISW81[0]
            Cpe4 = ISW81[1]
            Cpe5 = ISW81[2]
            Cpe6 = ISW81[3]

            Cpe1a = ISW82[0]
            Cpe4a = ISW82[1]
            Cpe5a = ISW82[2]
            Cpe6a = ISW82[3]

    ######

    # (H/W <= 1/2)
    ISR1 = [0, -0.8, -0.4, -0.8, -0.4]
    ISR2 = [5, -0.9, -0.4, -0.8, -0.4]
    ISR3 = [10, -1.2, -0.4, -0.8, -0.6]
    ISR4 = [20, -0.4, -0.4, -0.7, -0.6]
    ISR5 = [30, 0, -0.4, -0.7, -0.6]
    ISR6 = [45, 0.3, -0.5, -0.7, -0.6]
    ISR7 = [60, 0.7, -0.6, -0.7, -0.6]

    if Height/Width1 <= 1/2:
        if Dslope > 0 and Dslope <= 5:
            Cpe2 = (((ISR2[1]-ISR1[1])/(ISR2[0]-ISR1[0]))*Dslope) + ISR1[1]
            Cpe3 = (((ISR2[2]-ISR1[2])/(ISR2[0]-ISR1[0]))*Dslope) + ISR1[2]

            Cpe2a = (((ISR2[3]-ISR1[3])/(ISR2[0]-ISR1[0]))*Dslope) + ISR1[3]
            Cpe3a = (((ISR2[4]-ISR1[4])/(ISR2[0]-ISR1[0]))*Dslope) + ISR1[4]

        if Dslope > 5 and Dslope <= 10:
            Cpe2 = (((ISR3[1]-ISR2[1])/(ISR3[0]-ISR2[0]))*(Dslope-5)) + ISR2[1]
            Cpe3 = (((ISR3[2]-ISR2[2])/(ISR3[0]-ISR2[0]))*(Dslope-5)) + ISR2[2]

            Cpe2a = (((ISR3[3]-ISR2[3])/(ISR3[0]-ISR2[0]))*(Dslope-5)) + ISR2[3]
            Cpe3a = (((ISR3[4]-ISR2[4])/(ISR3[0]-ISR2[0]))*(Dslope-5)) + ISR2[4]

        if Dslope > 10 and Dslope <= 20:
            Cpe2 = (((ISR4[1]-ISR3[1])/(ISR4[0]-ISR3[0]))*(Dslope-10)) + ISR3[1]
            Cpe3 = (((ISR4[2]-ISR3[2])/(ISR4[0]-ISR3[0]))*(Dslope-10)) + ISR3[2]

            Cpe2a = (((ISR4[3]-ISR3[3])/(ISR4[0]-ISR3[0]))*(Dslope-10)) + ISR3[3]
            Cpe3a = (((ISR4[4]-ISR3[4])/(ISR4[0]-ISR3[0]))*(Dslope-10)) + ISR3[4]

        if Dslope > 20 and Dslope <= 30:
            Cpe2 = (((ISR5[1]-ISR4[1])/(ISR5[0]-ISR4[0]))*(Dslope-20)) + ISR4[1]
            Cpe3 = (((ISR5[2]-ISR4[2])/(ISR5[0]-ISR4[0]))*(Dslope-20)) + ISR4[2]

            Cpe2a = (((ISR5[3]-ISR4[3])/(ISR5[0]-ISR4[0]))*(Dslope-20)) + ISR4[3]
            Cpe3a = (((ISR5[4]-ISR4[4])/(ISR5[0]-ISR4[0]))*(Dslope-20)) + ISR4[4]

        if Dslope > 30 and Dslope <= 45:
            Cpe2 = (((ISR6[1]-ISR5[1])/(ISR6[0]-ISR5[0]))*(Dslope-30)) + ISR5[1]
            Cpe3 = (((ISR6[2]-ISR5[2])/(ISR6[0]-ISR5[0]))*(Dslope-30)) + ISR5[2]

            Cpe2a = (((ISR6[3]-ISR5[3])/(ISR6[0]-ISR5[0]))*(Dslope-30)) + ISR5[3]
            Cpe3a = (((ISR6[4]-ISR5[4])/(ISR6[0]-ISR5[0]))*(Dslope-30)) + ISR5[4]

        if Dslope > 45 and Dslope <= 60:
            Cpe2 = (((ISR7[1]-ISR6[1])/(ISR7[0]-ISR6[0]))*(Dslope-45)) + ISR6[1]
            Cpe3 = (((ISR7[2]-ISR6[2])/(ISR7[0]-ISR6[0]))*(Dslope-45)) + ISR6[2]

            Cpe2a = (((ISR7[3]-ISR6[3])/(ISR7[0]-ISR6[0]))*(Dslope-45)) + ISR6[3]
            Cpe3a = (((ISR7[4]-ISR6[4])/(ISR7[0]-ISR6[0]))*(Dslope-45)) + ISR6[4]


    # (1/2 <= H/W <= 3/2)
    ISR11 = [0, -0.8, -0.6, -1.0, -0.6]
    ISR12 = [5, -0.9, -0.6, -0.9, -0.6]
    ISR13 = [10, -1.1, -0.6, -0.8, -0.6]
    ISR14 = [20, -0.7, -0.5, -0.8, -0.6]
    ISR15 = [30, -0.2, -0.5, -0.8, -0.8]
    ISR16 = [45, 0.2, -0.5, -0.8, -0.8]
    ISR17 = [60, 0.6, -0.5, -0.8, -0.8]


    if Height/Width1 > 1/2 and Height/Width1 <= 3/2:
        if Dslope > 0 and Dslope <= 5:
            Cpe2 = (((ISR12[1]-ISR11[1])/(ISR12[0]-ISR11[0]))*Dslope) + ISR11[1]
            Cpe3 = (((ISR12[2]-ISR11[2])/(ISR12[0]-ISR11[0]))*Dslope) + ISR11[2]

            Cpe2a = (((ISR12[3]-ISR11[3])/(ISR12[0]-ISR11[0]))*Dslope) + ISR11[3]
            Cpe3a = (((ISR12[4]-ISR11[4])/(ISR12[0]-ISR11[0]))*Dslope) + ISR11[4]

        if Dslope > 5 and Dslope <= 10:
            Cpe2 = (((ISR13[1]-ISR12[1])/(ISR13[0]-ISR12[0]))
                    * (Dslope-5)) + ISR12[1]
            Cpe3 = (((ISR13[2]-ISR12[2])/(ISR13[0]-ISR12[0]))
                    * (Dslope-5)) + ISR12[2]

            Cpe2a = (((ISR13[3]-ISR12[3])/(ISR13[0]-ISR12[0]))
                    * (Dslope-5)) + ISR12[3]
            Cpe3a = (((ISR13[4]-ISR12[4])/(ISR13[0]-ISR12[0]))
                    * (Dslope-5)) + ISR12[4]

        if Dslope > 10 and Dslope <= 20:
            Cpe2 = (((ISR14[1]-ISR13[1])/(ISR14[0]-ISR13[0]))
                    * (Dslope-10)) + ISR13[1]
            Cpe3 = (((ISR14[2]-ISR13[2])/(ISR14[0]-ISR13[0]))
                    * (Dslope-10)) + ISR13[2]

            Cpe2a = (((ISR14[3]-ISR13[3])/(ISR14[0]-ISR13[0]))
                    * (Dslope-10)) + ISR13[3]
            Cpe3a = (((ISR14[4]-ISR13[4])/(ISR14[0]-ISR13[0]))
                    * (Dslope-10)) + ISR13[4]

        if Dslope > 20 and Dslope <= 30:
            Cpe2 = (((ISR15[1]-ISR14[1])/(ISR15[0]-ISR14[0]))
                    * (Dslope-20)) + ISR14[1]
            Cpe3 = (((ISR15[2]-ISR14[2])/(ISR15[0]-ISR14[0]))
                    * (Dslope-20)) + ISR14[2]

            Cpe2a = (((ISR15[3]-ISR14[3])/(ISR15[0]-ISR14[0]))
                    * (Dslope-20)) + ISR14[3]
            Cpe3a = (((ISR15[4]-ISR14[4])/(ISR15[0]-ISR14[0]))
                    * (Dslope-20)) + ISR14[4]

        if Dslope > 30 and Dslope <= 45:
            Cpe2 = (((ISR16[1]-ISR15[1])/(ISR16[0]-ISR15[0]))
                    * (Dslope-30)) + ISR15[1]
            Cpe3 = (((ISR16[2]-ISR15[2])/(ISR16[0]-ISR15[0]))
                    * (Dslope-30)) + ISR15[2]

            Cpe2a = (((ISR16[3]-ISR15[3])/(ISR16[0]-ISR15[0]))
                    * (Dslope-30)) + ISR15[3]
            Cpe3a = (((ISR16[4]-ISR15[4])/(ISR16[0]-ISR15[0]))
                    * (Dslope-30)) + ISR15[4]

        if Dslope > 45 and Dslope <= 60:
            Cpe2 = (((ISR17[1]-ISR16[1])/(ISR17[0]-ISR16[0]))
                    * (Dslope-45)) + ISR16[1]
            Cpe3 = (((ISR17[2]-ISR16[2])/(ISR17[0]-ISR16[0]))
                    * (Dslope-45)) + ISR16[2]

            Cpe2a = (((ISR17[3]-ISR16[3])/(ISR17[0]-ISR16[0]))
                    * (Dslope-45)) + ISR16[3]
            Cpe3a = (((ISR17[4]-ISR16[4])/(ISR17[0]-ISR16[0]))
                    * (Dslope-45)) + ISR16[4]

    # (3/2 < H/W < 6)
    ISR21 = [0, -0.7, -0.6, -0.9, -0.7]
    ISR22 = [5, -0.7, -0.6, -0.8, -0.8]
    ISR23 = [10, -0.7, -0.6, -0.8, -0.8]
    ISR24 = [20, -0.8, -0.6, -0.8, -0.8]
    ISR25 = [30, -1.0, -0.5, -0.8, -0.7]
    ISR26 = [40, -0.2, -0.5, -0.8, -0.7]
    ISR27 = [50, 0.2, -0.5, -0.8, -0.7]
    ISR28 = [60, 0.5, -0.5, -0.8, -0.7]

    if Height/Width1 > 3/2 and Height/Width1 < 6:
        if Dslope > 0 and Dslope <= 5:
            Cpe2 = (((ISR22[1]-ISR21[1])/(ISR22[0]-ISR21[0]))*Dslope) + ISR21[1]
            Cpe3 = (((ISR22[2]-ISR21[2])/(ISR22[0]-ISR21[0]))*Dslope) + ISR21[2]

            Cpe2a = (((ISR22[3]-ISR21[3])/(ISR22[0]-ISR21[0]))*Dslope) + ISR21[3]
            Cpe3a = (((ISR22[4]-ISR21[4])/(ISR22[0]-ISR21[0]))*Dslope) + ISR21[4]

        if Dslope > 5 and Dslope <= 10:
            Cpe2 = (((ISR23[1]-ISR22[1])/(ISR23[0]-ISR22[0]))
                    * (Dslope-5)) + ISR22[1]
            Cpe3 = (((ISR23[2]-ISR22[2])/(ISR23[0]-ISR22[0]))
                    * (Dslope-5)) + ISR22[2]

            Cpe2a = (((ISR23[3]-ISR22[3])/(ISR23[0]-ISR22[0]))
                    * (Dslope-5)) + ISR22[3]
            Cpe3a = (((ISR23[4]-ISR22[4])/(ISR23[0]-ISR22[0]))
                    * (Dslope-5)) + ISR22[4]

        if Dslope > 10 and Dslope <= 20:
            Cpe2 = (((ISR24[1]-ISR23[1])/(ISR24[0]-ISR23[0]))
                    * (Dslope-10)) + ISR23[1]
            Cpe3 = (((ISR24[2]-ISR23[2])/(ISR24[0]-ISR23[0]))
                    * (Dslope-10)) + ISR23[2]

            Cpe2a = (((ISR24[3]-ISR23[3])/(ISR24[0]-ISR23[0]))
                    * (Dslope-10)) + ISR23[3]
            Cpe3a = (((ISR24[4]-ISR23[4])/(ISR24[0]-ISR23[0]))
                    * (Dslope-10)) + ISR23[4]

        if Dslope > 20 and Dslope <= 30:
            Cpe2 = (((ISR25[1]-ISR24[1])/(ISR25[0]-ISR24[0]))
                    * (Dslope-20)) + ISR24[1]
            Cpe3 = (((ISR25[2]-ISR24[2])/(ISR25[0]-ISR24[0]))
                    * (Dslope-20)) + ISR24[2]

            Cpe2a = (((ISR25[3]-ISR24[3])/(ISR25[0]-ISR24[0]))
                    * (Dslope-20)) + ISR24[3]
            Cpe3a = (((ISR25[4]-ISR24[4])/(ISR25[0]-ISR24[0]))
                    * (Dslope-20)) + ISR24[4]

        if Dslope > 30 and Dslope <= 40:
            Cpe2 = (((ISR26[1]-ISR25[1])/(ISR26[0]-ISR25[0]))
                    * (Dslope-30)) + ISR25[1]
            Cpe3 = (((ISR26[2]-ISR25[2])/(ISR26[0]-ISR25[0]))
                    * (Dslope-30)) + ISR25[2]

            Cpe2a = (((ISR26[3]-ISR25[3])/(ISR26[0]-ISR25[0]))
                    * (Dslope-30)) + ISR25[3]
            Cpe3a = (((ISR26[4]-ISR25[4])/(ISR26[0]-ISR25[0]))
                    * (Dslope-30)) + ISR25[4]

        if Dslope > 40 and Dslope <= 50:
            Cpe2 = (((ISR27[1]-ISR26[1])/(ISR27[0]-ISR26[0]))
                    * (Dslope-40)) + ISR26[1]
            Cpe3 = (((ISR27[2]-ISR26[2])/(ISR27[0]-ISR26[0]))
                    * (Dslope-40)) + ISR26[2]

            Cpe2a = (((ISR27[3]-ISR26[3])/(ISR27[0]-ISR26[0]))
                    * (Dslope-40)) + ISR26[3]
            Cpe3a = (((ISR27[4]-ISR26[4])/(ISR27[0]-ISR26[0]))
                    * (Dslope-40)) + ISR26[4]

        if Dslope > 50 and Dslope <= 60:
            Cpe2 = (((ISR28[1]-ISR27[1])/(ISR28[0]-ISR27[0]))
                    * (Dslope-50)) + ISR27[1]
            Cpe3 = (((ISR28[2]-ISR27[2])/(ISR28[0]-ISR27[0]))
                    * (Dslope-50)) + ISR27[2]

            Cpe2a = (((ISR28[3]-ISR27[3])/(ISR28[0]-ISR27[0]))
                    * (Dslope-50)) + ISR27[3]
            Cpe3a = (((ISR28[4]-ISR27[4])/(ISR28[0]-ISR27[0]))
                    * (Dslope-50)) + ISR27[4]

##########################################################################

    response = HttpResponse(content_type='text/plain')
    response['content-Disposition'] = 'attachement; filename = staad.std'

    response.writelines("STAAD SPACE\n")


    response.writelines("START JOB INFORMATION\n")
    response.writelines("ENGINEER DATE 10/6/2021\n")
    response.writelines("END JOB INFORMATION\n")
    response.writelines("INPUT WIDTH 79\n")
    response.writelines("UNIT METER KN\n")

    ##############################################################################
    #JOINT COORDINATES
    ##############################################################################

    response.writelines("JOINT COORDINATES")

    #FRAME CO-COORDINATES#########################################################

    j = 0
    while j < len(SW1):
        i = 0
        while i < len(EWX):
            if i % 2 == 0:
                response.writelines(f"\n")
            response.writelines(
                f"{(len(EWX)*j)+i+1} {round(EWX[i],5)} {round(EWY[i],5)} {round(SW1[j],5)};")

            i = i+1
        j = j+1

    #ICO CO-COORDINATES###########################################################


    j = 0
    while j < len(SW1):
        i = 0
        while i < len(ICO):
            if i % 3 == 0:
                response.writelines(f"\n")
            response.writelines(
                f"{(len(EWX)*len(SW1))+i+(j*len(ICO))+1} {ICO[i]} {0} {SW1[j]};")
            i = i+1
        j = j+1

    #WC CO-COORDINATES############################################################

    j = 0
    while j < len(SW1):
        i = 0
        while i < len(Only_WC_Nodes):
            if j == 0:
                if i % 3 == 0:
                    response.writelines(f"\n")
                response.writelines(
                    f"{(len(EWX)*len(SW1))+(len(ICO)*len(SW1))+i+(j*len(Only_WC_Nodes))+1} {Only_WC_Distance[i]} {0} {SW1[j]};")
            if j == (len(SW1)-1):
                if i % 3 == 0:
                    response.writelines(f"\n")
                response.writelines(
                    f"{(len(EWX)*len(SW1))+(len(ICO)*len(SW1))+i+(1*len(Only_WC_Nodes))+1} {Only_WC_Distance[i]} {0} {SW1[j]};")
            i = i+1
        j = j+1


    ##############################################################################

    #MEMBER INCIDENCES
    ##############################################################################
    response.writelines("\n")
    response.writelines("MEMBER INCIDENCES")

    #FRAME INCIDENCES############################################################

    j = 0
    while j < len(SW1):
        i = 0
        while i < (len(EWX)-1):
            if i % 4 == 0:
                response.writelines(f"\n")
            response.writelines(
                f"{((len(EWX)-1)*j)+i+1} {((len(EWX)-1)*j)+i+1+j} {((len(EWX)-1)*j)+i+2+j};")
            i = i+1
        j = j+1

    #ICO INCIDENCES###############################################################

    j = 0
    while j < len(SW1):
        i = 0
        while i < len(ICO_Nodes):
            if i % 4 == 0:
                response.writelines(f"\n")
            response.writelines(
                f"{((len(EWX)-1)*len(SW1))+(j*len(ICO_Nodes))+i+1} {(len(EWX)*len(SW1))+(j*len(ICO_Nodes))+1+i} {(j*len(EWX))+ICO_Nodes[i]};")
            i = i+1
        j = j+1

    #WC INCIDENCES###############################################################


    j = 0
    while j < len(SW1):
        i = 0
        while i < len(Only_WC_Nodes):
            if j == 0:
                if i % 4 == 0:
                    response.writelines(f"\n")
                response.writelines(
                    f"{((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(j*len(Only_WC_Nodes))+i+1} {(len(EWX)*len(SW1))+(len(ICO)*len(SW1))+(j*len(Only_WC_Nodes))+1+i} {(j*len(EWX))+Only_WC_Nodes[i]};")
            if j == (len(SW1)-1):
                if i % 4 == 0:
                    response.writelines(f"\n")
                response.writelines(
                    f"{((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(1*len(Only_WC_Nodes))+i+1} {(len(EWX)*len(SW1))+(len(ICO)*len(SW1))+(1*len(Only_WC_Nodes))+1+i} {(j*len(EWX))+Only_WC_Nodes[i]};")

            i = i+1
        j = j+1


    #COLDFORM MEMBERS INCIDENCES###############################################################

    j = 0
    while j < len(BR_Nodes):
        i = 0
        while i < (len(SW1)-1):
            if i % 4 == 0:
                response.writelines(f"\n")
            response.writelines(
                f"{((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(len(EW3)*2)+i+1+(j*(len(SW1)-1))} {BR_Nodes[j]+(i*len(EWX))} {BR_Nodes[j]+((i+1)*len(EWX))};")
            i = i+1
        j = j+1

    #BRACING MEMBERS INCIDENCES###############################################################

    j = 0
    while j < len(Braced_bay_location):
        i = 0
        while i < (len(BR_Nodes)-1):
            if i % 4 == 0:
                response.writelines(f"\n")
            response.writelines(
                f"{((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(len(Only_WC_Nodes)*2)+(len(BR_Nodes)*(len(SW1)-1))+i+1+(j*(len(BR_Nodes)-1))} {BR_Nodes[i]+((Braced_bay_location[j]-1)*len(EWX))} {BR_Nodes[i+1]+(Braced_bay_location[j])*len(EWX)};")
            i = i+1
        j = j+1

    j = 0
    while j < len(Braced_bay_location):
        i = 0
        while i < (len(BR_Nodes)-1):
            if i % 4 == 0:
                response.writelines(f"\n")
            response.writelines(
                f"{((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(len(Only_WC_Nodes)*2)+(len(BR_Nodes)*(len(SW1)-1))+((len(BR_Nodes)-1)*len(Braced_bay_location))+i+1+(j*(len(BR_Nodes)-1))} {BR_Nodes[i+1]+((Braced_bay_location[j]-1)*len(EWX))} {BR_Nodes[i]+(Braced_bay_location[j])*len(EWX)};")
            i = i+1
        j = j+1

    response.writelines(f"\n")
    j = 0
    while j < len(Braced_bay_location):
        i = 1
        while i <= 2:
            if i == 1:
                response.writelines(
                    f"{((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(len(Only_WC_Nodes)*2)+(len(BR_Nodes)*(len(SW1)-1))+((len(BR_Nodes)-1)*len(Braced_bay_location)*2)+i+(j*2)} {i+((Braced_bay_location[j]-1)*len(EWX))} {(i+1)+(Braced_bay_location[j])*len(EWX)};\n")
            if i == 2:
                response.writelines(
                    f"{((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(len(Only_WC_Nodes)*2)+(len(BR_Nodes)*(len(SW1)-1))+((len(BR_Nodes)-1)*len(Braced_bay_location)*2)+i+(j*2)} {i+((Braced_bay_location[j]-1)*len(EWX))} {(i-1)+(Braced_bay_location[j])*len(EWX)};\n")
            i = i+1
        j = j+1

    j = 0
    while j < len(Braced_bay_location):
        i = 1
        while i <= 2:
            if i == 1:
                response.writelines(
                    f"{((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(len(Only_WC_Nodes)*2)+(len(BR_Nodes)*(len(SW1)-1))+((len(BR_Nodes)-1)*len(Braced_bay_location)*2)+(len(Braced_bay_location)*2)+i+(j*2)} {i+(len(EWX)-2)+((Braced_bay_location[j]-1)*len(EWX))} {(i+1)+(len(EWX)-2)+(Braced_bay_location[j])*len(EWX)};\n")
            if i == 2:
                response.writelines(
                    f"{((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(len(Only_WC_Nodes)*2)+(len(BR_Nodes)*(len(SW1)-1))+((len(BR_Nodes)-1)*len(Braced_bay_location)*2)+(len(Braced_bay_location)*2)+i+(j*2)} {i+(len(EWX)-2)+((Braced_bay_location[j]-1)*len(EWX))} {(i-1)+(len(EWX)-2)+(Braced_bay_location[j])*len(EWX)};\n")
            i = i+1
        j = j+1

    ##############################################################################

    response.writelines("DEFINE MATERIAL START\n")
    response.writelines("ISOTROPIC STEEL\n")
    response.writelines("E 2.05e+08\n")
    response.writelines("POISSON 0.3\n")
    response.writelines("DENSITY 76.8195\n")
    response.writelines("ALPHA 1.2e-05\n")
    response.writelines("DAMP 0.03\n")
    response.writelines("TYPE STEEL\n")
    response.writelines("STRENGTH FY 253200 FU 407800 RY 1.5 RT 1.2\n")
    response.writelines("END DEFINE MATERIAL\n")

    response.writelines("MEMBER PROPERTY\n")

    response.writelines("********************************************************************\n")
    response.writelines("*MAIN FRAME MEMBERS\n")
    response.writelines("********************************************************************\n")


    x=0
    while x<(len(EWX)-1):
        i=0
        CRET=[]
        while i<(len(SW1)):
            CRET.insert(i,(x+1)+(i*(len(EWX)-1)))
            i=i+1
        print(CRET)
        CRET1=[]
        y=1
        while y<=len(CRET):
            if len(CRET)>=15:
                CRET1.append(CRET[y-1])
                if y%15==0 or y%len(CRET)==0:
                    st=' '.join(map(str,CRET1))
                    response.writelines(f"{st} -\n")
                    print(CRET1)
                    print(st)
                    CRET1=[]
            else:
                if y==len(CRET):
                    st=' '.join(map(str,CRET))
                    response.writelines(f"{st} -\n")
            y=y+1
        response.writelines(f"TAPERED 0.27 0.005 0.27 0.15 0.008\n")
        x=x+1

    if len(ICO)>0:

        response.writelines("********************************************************************\n")
        response.writelines("*INTERIOR COLUMNS\n")
        response.writelines("********************************************************************\n")

        x=0
        CRET=[]
        while x<(len(ICO)*len(SW1)):
            CRET.insert(x,((len(EWX)-1)*len(SW1))+x+1)
            x=x+1
        print(CRET)
        CRET1=[]
        x=1
        while x<=len(CRET):
            if len(CRET)>=15:
                CRET1.append(CRET[x-1])
                if x%15==0 or x%len(CRET)==0:
                    st=' '.join(map(str,CRET1))
                    response.writelines(f"{st} -\n")
                    print(CRET1)
                    print(st)
                    CRET1=[]
            else:
                if x==len(CRET):
                    st=' '.join(map(str,CRET))
                    response.writelines(f"{st} -\n")
            x=x+1
        response.writelines(f"TAPERED 0.27 0.005 0.27 0.15 0.008\n")


    response.writelines("********************************************************************\n")
    response.writelines("*WIND COLUMNS\n")
    response.writelines("********************************************************************\n")

    x=0
    while x<2:
        i=0
        CRET=[]
        while i<(len(Only_WC_Nodes)):
            CRET.insert(i,((len(EWX)-1)*len(SW1))+((len(ICO))*len(SW1))+1+i+(x*len(Only_WC_Nodes)))
            i=i+1
        print(CRET)
        CRET1=[]
        y=1
        while y<=len(CRET):
            if len(CRET)>=15:
                CRET1.append(CRET[y-1])
                if y%15==0 or y%len(CRET)==0:
                    st=' '.join(map(str,CRET1))
                    response.writelines(f"{st} -\n")
                    print(CRET1)
                    print(st)
                    CRET1=[]
            else:
                if y==len(CRET):
                    st=' '.join(map(str,CRET))
                    response.writelines(f"{st} -\n")
            y=y+1
        x=x+1
    response.writelines(f"TAPERED 0.27 0.005 0.27 0.15 0.008\n")

    response.writelines("********************************************************************\n")
    response.writelines("*ROOF BRACINGS\n")
    response.writelines("********************************************************************\n")
    response.writelines(f"MEMBER PROPERTY INDIAN\n")

    i=((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(len(Only_WC_Nodes)*2)+(len(BR_Nodes)*(len(SW1)-1))
    CRET=[]
    while i<(((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(len(Only_WC_Nodes)*2)+(len(BR_Nodes)*(len(SW1)-1))+(len(Braced_bay_location)*(len(BR_Nodes)-1)*2)):
        CRET.append(i+1)
        i=i+1
    print(CRET)
    CRET1=[]
    x=1
    while x<=len(CRET):
        if len(CRET)>=15:
            CRET1.append(CRET[x-1])
            if x%15==0 or x%len(CRET)==0:
                st=' '.join(map(str,CRET1))
                response.writelines(f"{st} -\n")
                print(CRET1)
                print(st)
                CRET1=[]
        else:
            if x==len(CRET):
                st=' '.join(map(str,CRET))
                response.writelines(f"{st} -\n")
        x=x+1

    response.writelines(f"TABLE ST PIP1937M\n")


    response.writelines("********************************************************************\n")
    response.writelines("*WALL BRACINGS\n")
    response.writelines("********************************************************************\n")

    i=(((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(len(Only_WC_Nodes)*2)+(len(BR_Nodes)*(len(SW1)-1))+(len(Braced_bay_location)*(len(BR_Nodes)-1)*2))
    CRET=[]
    while i<(((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(len(Only_WC_Nodes)*2)+(len(BR_Nodes)*(len(SW1)-1))+(len(Braced_bay_location)*(len(BR_Nodes)-1)*2)+(len(Braced_bay_location)*2*2)):
        CRET.append(i+1)
        i=i+1
    print(CRET)
    CRET1=[]
    x=1
    while x<=len(CRET):
        if len(CRET)>=15:
            CRET1.append(CRET[x-1])
            if x%15==0 or x%len(CRET)==0:
                st=' '.join(map(str,CRET1))
                response.writelines(f"{st} -\n")
                print(CRET1)
                print(st)
                CRET1=[]
        else:
            if x==len(CRET):
                st=' '.join(map(str,CRET))
                response.writelines(f"{st} -\n")
        x=x+1
    response.writelines(f"TABLE ST PIP1937M\n")


    response.writelines("********************************************************************\n")
    response.writelines("*FORCE TRANSFER MEMBERS\n")
    response.writelines("********************************************************************\n")
    response.writelines("MEMBER PROPERTY COLDFORMED INDIAN\n")

    x=0
    CRET=[]
    while x<(len(BR_Nodes)):
        i=0

        while i<(len(SW1)-1):

            CRET.insert(i,((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(len(EW3)*2)+i+1+(x*(len(SW1)-1)))
            i=i+1
        x=x+1
    print(CRET)
    CRET1=[]
    x=1
    while x<=len(CRET):
        if len(CRET)>=15:
            CRET1.append(CRET[x-1])
            if x%15==0 or x%len(CRET)==0:
                st=' '.join(map(str,CRET1))
                response.writelines(f"{st} -\n")
                print(CRET1)
                print(st)
                CRET1=[]
        else:
            if x==len(CRET):
                st=' '.join(map(str,CRET))
                response.writelines(f"{st} -\n")
        x=x+1
    response.writelines(f"TABLE ST 200ZS60X2\n")


    response.writelines("********************************************************************\n")
    response.writelines("CONSTANTS\n")


    x=0
    while x<2:
        i=0
        CRET=[]
        while i<(len(Only_WC_Nodes)):
            CRET.insert(i,((len(EWX)-1)*len(SW1))+((len(ICO))*len(SW1))+1+i+(x*len(Only_WC_Nodes)))
            i=i+1
        response.writelines(f"BETA 90 MEMB -\n")
        print(CRET)
        CRET1=[]
        y=1
        while y<=len(CRET):
            if len(CRET)>=15:
                CRET1.append(CRET[y-1])
                if y%15==0 or y%len(CRET)==0:
                    st=' '.join(map(str,CRET1))
                    if y==len(CRET):
                        response.writelines(f"{st}\n")
                    else:
                        response.writelines(f"{st} -\n")
                    print(CRET1)
                    print(st)
                    CRET1=[]
            else:
                if y==len(CRET):
                    st=' '.join(map(str,CRET))
                    response.writelines(f"{st}\n")
            y=y+1

        x=x+1



    response.writelines("MATERIAL STEEL ALL\n")
    response.writelines("********************************************************************\n")

    response.writelines("SUPPORTS\n")

    x=0
    CRET=[]
    while x<1:
        i=0
        while i<(len(SW1)):
            CRET.insert(i,(len(EWX)*i)+1)
            i=i+1
        x=x+1
    print(CRET)
    CRET1=[]
    x=1
    while x<=len(CRET):
        if len(CRET)>=15:
            CRET1.append(CRET[x-1])
            if x%15==0 or x%len(CRET)==0:
                st=' '.join(map(str,CRET1))
                response.writelines(f"{st} -\n")
                print(CRET1)
                print(st)
                CRET1=[]
        else:
            if x==len(CRET):
                st=' '.join(map(str,CRET))
                response.writelines(f"{st} -\n")
        x=x+1
    response.writelines(f"{NSC_SUPPORT}\n")


    x=0
    CRET=[]
    while x<1:
        i=0
        while i<(len(SW1)):
            CRET.insert(i,(len(EWX)*(i+1)))
            i=i+1
        x=x+1
    print(CRET)
    CRET1=[]
    x=1
    while x<=len(CRET):
        if len(CRET)>=15:
            CRET1.append(CRET[x-1])
            if x%15==0 or x%len(CRET)==0:
                st=' '.join(map(str,CRET1))
                response.writelines(f"{st} -\n")
                print(CRET1)
                print(st)
                CRET1=[]
        else:
            if x==len(CRET):
                st=' '.join(map(str,CRET))
                response.writelines(f"{st} -\n")
        x=x+1
    response.writelines(f"{FSC_SUPPORT}\n")

    if len(ICO)>0:

        x=0
        CRET=[]
        while x<len(ICO):
            i=0
            while i<(len(SW1)):
                CRET.insert(i,((len(EWX)*len(SW1))+(i)+1+(x*len(SW1))))
                i=i+1
            x=x+1
        print(CRET)
        CRET1=[]
        x=1
        while x<=len(CRET):
            if len(CRET)>=15:
                CRET1.append(CRET[x-1])
                if x%15==0 or x%len(CRET)==0:
                    st=' '.join(map(str,CRET1))
                    response.writelines(f"{st} -\n")
                    print(CRET1)
                    print(st)
                    CRET1=[]
            else:
                if x==len(CRET):
                    st=' '.join(map(str,CRET))
                    response.writelines(f"{st} -\n")
            x=x+1
        response.writelines(f"{ICO_SUPPORT}\n")



    x=0
    while x<2:
        i=0
        CRET=[]
        while i<(len(Only_WC_Nodes)):
            CRET.insert(i,((len(EWX))*len(SW1))+((len(ICO))*len(SW1))+1+i+(x*len(Only_WC_Nodes)))
            i=i+1
        print(CRET)
        CRET1=[]
        y=1
        while y<=len(CRET):
            if len(CRET)>=15:
                CRET1.append(CRET[y-1])
                if y%15==0 or y%len(CRET)==0:
                    st=' '.join(map(str,CRET1))
                    response.writelines(f"{st} -\n")
                    print(CRET1)
                    print(st)
                    CRET1=[]
            else:
                if y==len(CRET):
                    st=' '.join(map(str,CRET))
                    response.writelines(f"{st} -\n")
            y=y+1
        response.writelines(f"{WC_SUPPORT}\n")
        x=x+1

    response.writelines("********************************************************************\n")

    response.writelines("MEMBER RELEASE\n")

    x=0
    CRET=[]
    while x<2:
        i=0
        while i<(len(Only_WC_Nodes)):
            CRET.insert(i,((len(EWX)-1)*len(SW1))+((len(ICO))*len(SW1))+1+i+(x*len(Only_WC_Nodes)))
            i=i+1
        x=x+1

    print(CRET)
    CRET1=[]
    x=1
    while x<=len(CRET):
        if len(CRET)>=15:
            CRET1.append(CRET[x-1])
            if x%15==0 or x%len(CRET)==0:
                st=' '.join(map(str,CRET1))
                response.writelines(f"{st} -\n")
                print(CRET1)
                print(st)
                CRET1=[]
        else:
            if x==len(CRET):
                st=' '.join(map(str,CRET))
                response.writelines(f"{st} -\n")
        x=x+1
    response.writelines(f"END MY MZ\n")



    response.writelines("********************************************************************\n")

    response.writelines("MEMBER TRUSS\n")

    x=0
    CRET=[]
    while x<(len(BR_Nodes)):
        i=0

        while i<(len(SW1)-1):
            CRET.insert(i,((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(len(EW3)*2)+i+1+(x*(len(SW1)-1)))
            i=i+1
        x=x+1
    print(CRET)
    CRET1=[]
    y=1
    while y<=len(CRET):
        if len(CRET)>=15:
            CRET1.append(CRET[y-1])
            if y%15==0 or y%len(CRET)==0:
                st=' '.join(map(str,CRET1))
                if y==len(CRET):
                    response.writelines(f"{st}\n")
                else:
                    response.writelines(f"{st} -\n")
                print(CRET1)
                print(st)
                CRET1=[]
        else:
            if y==len(CRET):
                st=' '.join(map(str,CRET))
                response.writelines(f"{st}\n")
        y=y+1

    response.writelines("********************************************************************\n")

    response.writelines("MEMBER TENSION\n")

    i=((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(len(Only_WC_Nodes)*2)+(len(BR_Nodes)*(len(SW1)-1))
    CRET=[]
    while i<(((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(len(Only_WC_Nodes)*2)+(len(BR_Nodes)*(len(SW1)-1))+(len(Braced_bay_location)*(len(BR_Nodes)-1)*2)+(len(Braced_bay_location)*2*2)):
        CRET.append(i+1)
        i=i+1
    print(CRET)
    CRET1=[]
    y=1
    while y<=len(CRET):
        if len(CRET)>=15:
            CRET1.append(CRET[y-1])
            if y%15==0 or y%len(CRET)==0:
                st=' '.join(map(str,CRET1))
                if y==len(CRET):
                    response.writelines(f"{st}\n")
                else:
                    response.writelines(f"{st} -\n")
                print(CRET1)
                print(st)
                CRET1=[]
        else:
            if y==len(CRET):
                st=' '.join(map(str,CRET))
                response.writelines(f"{st}\n")
        y=y+1

    if LOADS_REQUIRED == 'EL-DL-RLL-WL':

        response.writelines("********************************************************************\n")
        response.writelines("**SEISMIC PARAMETERS**\n")
        response.writelines("********************************************************************\n")

        if SEISMIC_CODE == 'IS 1893-2002/2005':
            response.writelines("DEFINE 1893 LOAD\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} DM {Damping_ratio}\n")
        if SEISMIC_CODE == 'IS 1893-2002/2005(WITH PART-4)':
            response.writelines("DEFINE 1893 LOAD PART4\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} DM {Damping_ratio}\n")
        if SEISMIC_CODE == 'IS 1893(PART-1)-2016':
            response.writelines("DEFINE IS1893 2016 LOAD\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} DM {Damping_ratio}\n")
        if SEISMIC_CODE == 'IS 1893(PART-4)-2015':
            response.writelines("DEFINE IS1893 2015 LOAD PART4\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} ST 1 DM {Damping_ratio}\n")

        response.writelines("SELFWEIGHT 1.15\n")

        response.writelines("**DEAD LOADS**\n")
        response.writelines("MEMBER WEIGHT\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1

            response.writelines(f"UNI {round((-1*DL*Unique),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 1 EQ+X\n")
        response.writelines("1893 LOAD X 1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 2 EQ-X\n")
        response.writelines("1893 LOAD X -1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 3 EQ+Z\n")
        response.writelines("1893 LOAD Z 1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 4 EQ-Z\n")
        response.writelines("1893 LOAD Z -1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 5 DL\n")
        response.writelines("SELFWEIGHT Y -1.15\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1

            response.writelines(f"UNI GY {round((DL*Unique),4)}\n")

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 6 LL\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI GY {round((LL*Unique),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines(f"***WALL CO-EFF {round(Cpe1,2)} {round(Cpe4,2)} {round(Cpe5,2)} {round(Cpe6,2)}\n")
        response.writelines(f"***            {round(Cpe1a,2)} {round(Cpe4a,2)} {round(Cpe5a,2)} {round(Cpe6a,2)}\n")
        response.writelines(f"***ROOF CO-EFF {round(Cpe2,2)} {round(Cpe3,2)} {round(Cpe2a,2)} {round(Cpe3a,2)}\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 7 WL1\n")
        response.writelines("MEMBER LOAD\n")

        print("222222222222222222222222")
        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<Ridge_node:
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=Ridge_node and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1

            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe1 - Cpi)),4)}\n")

            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe4 + Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            print("CRET4")
            st=' '.join(map(str,CRET4))
            print(CRET5)
            print("CRET5")
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 + Cpi)),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 8 WL2\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<Ridge_node:
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=Ridge_node and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe1 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe4 - Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 - Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 9 WL3\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<Ridge_node:
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=Ridge_node and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4 - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1 + Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 + Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 10 WL4\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<Ridge_node:
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=Ridge_node and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1

            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1 - Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 - Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 11 WL5\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<Ridge_node:
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=Ridge_node and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1a + Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a + Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 12 WL6\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<Ridge_node:
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=Ridge_node and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe1a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe4a - Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a - Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 13 WL7\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<Ridge_node:
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=Ridge_node and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1a + Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a + Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 14 WL8\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<Ridge_node:
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=Ridge_node and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1a - Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a - Cpi)),4)}\n")
            x=x+1
    #############################################
        x1=[['+SLX','-SLX','+SLZ','-SLZ'],['DL'],['RLL'],['WL+X+CPI','WL-X+CPI','WL+X-CPI','WL-X-CPI','WL+Z+CPI','WL-Z+CPI','WL+Z-CPI','WL-Z-CPI']]
        x2=[[1,2,3,4],[5],[6],[7,8,9,10,11,12,13,14]]
        x3=[[4],[1],[1],[8]]
        y1=[
            [[0],[1.5],[1.5],[0]],
            [[0],[1.2],[1.2],[0.6]],
            [[0.6],[1.2],[1.2],[0]],
            [[0],[1.2],[1.2],[1.2]],
            [[1.2],[1.2],[1.2],[0]],
            [[0],[1.5],[0],[1.5]],
            [[1.5],[1.5],[0],[0]],
            [[0],[0.9],[0],[1.5]],
            [[1.5],[0.9],[0],[0]],
            [[0],[1.2],[1.2],[0]],
            [[0],[0.9],[1.2],[0]]
            ]

        y1_12=[
            [[2.5],[1.2],[0.5],[0]],
            [[2.5],[0.9],[0],[0]]
            ]

        y2=[
            [[0],[1.0],[1.0],[0]],
            [[0],[1.0],[0.8],[0.8]],
            [[0.8],[1.0],[0.8],[0]],
            [[0],[1.0],[0],[1.0]],
            [[1.0],[1.0],[0],[0]]
            ]

        response.writelines("********************************************************************\n")
        response.writelines("*************LOAD COMBINATIONS (IS 800:2007 LSD)********************\n")
        response.writelines("****************LOAD COMBINATIONS - STRENGTH************************\n")
        response.writelines("********************************************************************\n")

        Load_no = 100

        y=0
        while y<len(y1):
            rx1=[]
            rx2=[]
            rx3=[]
            ry1=[]
            x=0
            while x<len(y1[y]):
                if y1[y][x][0]!=0:
                    ry1.append(y1[y][x])
                if y1[y][x][0]!=0:
                    rx3.append(x3[x])
                if y1[y][x][0]!=0:
                    rx2.append(x2[x])
                if y1[y][x][0]!=0:
                    rx1.append(x1[x])
                x=x+1


            if len(rx1)==5:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]}\n")
                                    response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]}\n")
                                    Load_no = Load_no + 1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==4:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]}\n")
                                response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]}\n")
                                Load_no = Load_no + 1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==3:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]}\n")
                            response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]}\n")
                            Load_no = Load_no + 1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==2:
                a = 0
                while a < rx3[0][0]:
                    b = 0
                    while b < rx3[1][0]:
                        response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]}\n")
                        response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]}\n")
                        Load_no = Load_no + 1
                        b = b + 1
                    a = a + 1

            y=y+1


        ####################################################

        response.writelines("********************************************************************\n")
        response.writelines("*************LOAD COMBINATIONS (IS 800:2007 LSD)********************\n")
        response.writelines("****************LOAD COMBINATIONS - CHAPTER 12************************\n")
        response.writelines("********************************************************************\n")

        Load_no_12 = 200

        y=0
        while y<len(y1_12):
            rx1=[]
            rx2=[]
            rx3=[]
            ry1=[]
            x=0
            while x<len(y1_12[y]):
                if y1_12[y][x][0]!=0:
                    ry1.append(y1_12[y][x])
                if y1_12[y][x][0]!=0:
                    rx3.append(x3[x])
                if y1_12[y][x][0]!=0:
                    rx2.append(x2[x])
                if y1_12[y][x][0]!=0:
                    rx1.append(x1[x])
                x=x+1


            if len(rx1)==5:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]}\n")
                                    response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]}\n")
                                    Load_no_12 = Load_no_12 + 1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==4:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]}\n")
                                response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]}\n")
                                Load_no_12 = Load_no_12 + 1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==3:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]}\n")
                            response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]}\n")
                            Load_no_12 = Load_no_12 + 1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==2:
                a = 0
                while a < rx3[0][0]:
                    b = 0
                    while b < rx3[1][0]:
                        response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]}\n")
                        response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]}\n")
                        Load_no_12 = Load_no_12 + 1
                        b = b + 1
                    a = a + 1

            y=y+1


        ####################################################

        response.writelines("********************************************************************\n")
        response.writelines("****************LOAD COMBINATIONS - SERVICEABILITY******************\n")
        response.writelines("********************************************************************\n")

        Load_no1 = 300

        y=0
        while y<len(y2):
            rx1=[]
            rx2=[]
            rx3=[]
            ry1=[]
            x=0
            while x<len(y2[y]):
                if y2[y][x][0]!=0:
                    ry1.append(y2[y][x])
                if y2[y][x][0]!=0:
                    rx3.append(x3[x])
                if y2[y][x][0]!=0:
                    rx2.append(x2[x])
                if y2[y][x][0]!=0:
                    rx1.append(x1[x])
                x=x+1


            if len(rx1)==5:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]}\n")
                                    response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]}\n")
                                    Load_no1 = Load_no1 + 1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==4:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]}\n")
                                response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]}\n")
                                Load_no1 = Load_no1 + 1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==3:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]}\n")
                            response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]}\n")
                            Load_no1 = Load_no1 + 1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==2:
                a = 0
                while a < rx3[0][0]:
                    b = 0
                    while b < rx3[1][0]:
                        response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]}\n")
                        response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]}\n")
                        Load_no1 = Load_no1 + 1
                        b = b + 1
                    a = a + 1

            y=y+1

        response.writelines("********************************************************************\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("DEFINE ENVELOPE\n")
        response.writelines(f"100 TO {Load_no-1} 200 TO {Load_no_12-1} ENVELOPE 1 TYPE STRENGTH\n")
        response.writelines(f"300 TO {Load_no1-1} ENVELOPE 2 TYPE SERVICEABILITY\n")
        response.writelines("END DEFINE ENVELOPE\n")
        response.writelines(f"LOAD LIST 100 TO {Load_no-1} 200 TO {Load_no_12-1}\n")


    if LOADS_REQUIRED == 'EL-DL-RLL-MLL-WL':

        response.writelines("********************************************************************\n")
        response.writelines("**SEISMIC PARAMETERS**\n")
        response.writelines("********************************************************************\n")
        if SEISMIC_CODE == 'IS 1893-2002/2005':
            response.writelines("DEFINE 1893 LOAD\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} DM {Damping_ratio}\n")
        if SEISMIC_CODE == 'IS 1893-2002/2005(WITH PART-4)':
            response.writelines("DEFINE 1893 LOAD PART4\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} DM {Damping_ratio}\n")
        if SEISMIC_CODE == 'IS 1893(PART-1)-2016':
            response.writelines("DEFINE IS1893 2016 LOAD\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} DM {Damping_ratio}\n")
        if SEISMIC_CODE == 'IS 1893(PART-4)-2015':
            response.writelines("DEFINE IS1893 2015 LOAD PART4\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} ST 1 DM {Damping_ratio}\n")

        response.writelines("SELFWEIGHT 1.15\n")

        response.writelines("**DEAD LOADS**\n")
        response.writelines("MEMBER WEIGHT\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1

            response.writelines(f"UNI {round((-1*DL*Unique),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 1 EQ+X\n")
        response.writelines("1893 LOAD X 1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 2 EQ-X\n")
        response.writelines("1893 LOAD X -1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 3 EQ+Z\n")
        response.writelines("1893 LOAD Z 1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 4 EQ-Z\n")
        response.writelines("1893 LOAD Z -1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 5 DL\n")
        response.writelines("SELFWEIGHT Y -1.15\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1

            response.writelines(f"UNI GY {round((DL*Unique),4)}\n")
            x=x+1
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 6 LL\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI GY {round((LL*Unique),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 7 MLL\n")

        response.writelines("********************************************************************\n")
        response.writelines(f"***WALL CO-EFF {round(Cpe1,2)} {round(Cpe4,2)} {round(Cpe5,2)} {round(Cpe6,2)}\n")
        response.writelines(f"***            {round(Cpe1a,2)} {round(Cpe4a,2)} {round(Cpe5a,2)} {round(Cpe6a,2)}\n")
        response.writelines(f"***ROOF CO-EFF {round(Cpe2,2)} {round(Cpe3,2)} {round(Cpe2a,2)} {round(Cpe3a,2)}\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 8 WL1\n")
        response.writelines("MEMBER LOAD\n")

        print("222222222222222222222222")
        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1

            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe1 - Cpi)),4)}\n")

            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe4 + Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            print("CRET4")
            st=' '.join(map(str,CRET4))
            print(CRET5)
            print("CRET5")
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 + Cpi)),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 9 WL2\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe1 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe4 - Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 - Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 10 WL3\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4 - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1 + Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 + Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 11 WL4\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1

            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1 - Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 - Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 12 WL5\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1a + Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a + Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 13 WL6\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe1a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe4a - Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a - Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 14 WL7\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1a + Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a + Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 15 WL8\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1a - Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a - Cpi)),4)}\n")
            x=x+1

        ####################################################

        x1=[['+SLX','-SLX','+SLZ','-SLZ'],['DL'],['RLL'],['MLL'],['WL+X+CPI','WL-X+CPI','WL+X-CPI','WL-X-CPI','WL+Z+CPI','WL-Z+CPI','WL+Z-CPI','WL-Z-CPI']]
        x2=[[1,2,3,4],[5],[6],[7],[8,9,10,11,12,13,14,15]]
        x3=[[4],[1],[1],[1],[8]]
        y1=[
            [[0],[1.5],[1.5],[1.05],[0]],
            [[0],[1.5],[1.05],[1.5],[0]],
            [[0],[1.2],[1.2],[1.05],[0.6]],
            [[0],[1.2],[1.05],[1.2],[0.6]],
            [[0.6],[1.2],[1.2],[1.05],[0]],
            [[0.6],[1.2],[1.05],[1.2],[0]],

            [[0],[1.2],[1.2],[0.53],[1.2]],
            [[0],[1.2],[0.53],[1.2],[1.2]],
            [[1.2],[1.2],[1.2],[0.53],[0]],
            [[1.2],[1.2],[0.53],[1.2],[0]],

            [[0],[1.5],[0],[0],[1.5]],
            [[0],[0.9],[0],[0],[1.5]],
            [[1.5],[1.5],[0],[0],[0]],
            [[1.5],[0.9],[0],[0],[0]],
            [[0],[1.2],[1.2],[0],[0]],
            [[0],[1.2],[0],[1.2],[0]],
            [[0],[0.9],[1.2],[0],[0]],
            [[0],[0.9],[0],[1.2],[0]]
            ]

        y1_12=[
            [[2.5],[1.2],[0.5],[0]],
            [[2.5],[0.9],[0],[0]]
            ]

        y2=[
            [[0],[1.0],[1.0],[1.0],[0]],
            [[0],[1.0],[0.8],[0.8],[0.8]],
            [[0.8],[1.0],[0.8],[0.8],[0]],
            [[0],[1.0],[0],[0],[1.0]],
            [[1.0],[1.0],[0],[0],[0]]
            ]

        response.writelines("********************************************************************\n")
        response.writelines("*************LOAD COMBINATIONS (IS 800:2007 LSD)********************\n")
        response.writelines("****************LOAD COMBINATIONS - STRENGTH************************\n")
        response.writelines("********************************************************************\n")

        Load_no = 100

        y=0
        while y<len(y1):
            rx1=[]
            rx2=[]
            rx3=[]
            ry1=[]
            x=0
            while x<len(y1[y]):
                if y1[y][x][0]!=0:
                    ry1.append(y1[y][x])
                if y1[y][x][0]!=0:
                    rx3.append(x3[x])
                if y1[y][x][0]!=0:
                    rx2.append(x2[x])
                if y1[y][x][0]!=0:
                    rx1.append(x1[x])
                x=x+1


            if len(rx1)==5:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]}\n")
                                    response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]}\n")
                                    Load_no = Load_no + 1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==4:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]}\n")
                                response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]}\n")
                                Load_no = Load_no + 1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==3:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]}\n")
                            response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]}\n")
                            Load_no = Load_no + 1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==2:
                a = 0
                while a < rx3[0][0]:
                    b = 0
                    while b < rx3[1][0]:
                        response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]}\n")
                        response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]}\n")
                        Load_no = Load_no + 1
                        b = b + 1
                    a = a + 1

            y=y+1


        ####################################################

        response.writelines("********************************************************************\n")
        response.writelines("*************LOAD COMBINATIONS (IS 800:2007 LSD)********************\n")
        response.writelines("****************LOAD COMBINATIONS - CHAPTER 12************************\n")
        response.writelines("********************************************************************\n")

        Load_no_12 = 200

        y=0
        while y<len(y1_12):
            rx1=[]
            rx2=[]
            rx3=[]
            ry1=[]
            x=0
            while x<len(y1_12[y]):
                if y1_12[y][x][0]!=0:
                    ry1.append(y1_12[y][x])
                if y1_12[y][x][0]!=0:
                    rx3.append(x3[x])
                if y1_12[y][x][0]!=0:
                    rx2.append(x2[x])
                if y1_12[y][x][0]!=0:
                    rx1.append(x1[x])
                x=x+1


            if len(rx1)==5:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]}\n")
                                    response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]}\n")
                                    Load_no_12 = Load_no_12 + 1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==4:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]}\n")
                                response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]}\n")
                                Load_no_12 = Load_no_12 + 1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==3:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]}\n")
                            response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]}\n")
                            Load_no_12 = Load_no_12 + 1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==2:
                a = 0
                while a < rx3[0][0]:
                    b = 0
                    while b < rx3[1][0]:
                        response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]}\n")
                        response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]}\n")
                        Load_no_12 = Load_no_12 + 1
                        b = b + 1
                    a = a + 1

            y=y+1


        ####################################################

        response.writelines("********************************************************************\n")
        response.writelines("****************LOAD COMBINATIONS - SERVICEABILITY******************\n")
        response.writelines("********************************************************************\n")

        Load_no1 = 300

        y=0
        while y<len(y2):
            rx1=[]
            rx2=[]
            rx3=[]
            ry1=[]
            x=0
            while x<len(y2[y]):
                if y2[y][x][0]!=0:
                    ry1.append(y2[y][x])
                if y2[y][x][0]!=0:
                    rx3.append(x3[x])
                if y2[y][x][0]!=0:
                    rx2.append(x2[x])
                if y2[y][x][0]!=0:
                    rx1.append(x1[x])
                x=x+1


            if len(rx1)==5:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]}\n")
                                    response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]}\n")
                                    Load_no1 = Load_no1 + 1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==4:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]}\n")
                                response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]}\n")
                                Load_no1 = Load_no1 + 1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==3:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]}\n")
                            response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]}\n")
                            Load_no1 = Load_no1 + 1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==2:
                a = 0
                while a < rx3[0][0]:
                    b = 0
                    while b < rx3[1][0]:
                        response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]}\n")
                        response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]}\n")
                        Load_no1 = Load_no1 + 1
                        b = b + 1
                    a = a + 1

            y=y+1

        response.writelines("********************************************************************\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("DEFINE ENVELOPE\n")
        response.writelines(f"100 TO {Load_no-1} 200 TO {Load_no_12-1} ENVELOPE 1 TYPE STRENGTH\n")
        response.writelines(f"300 TO {Load_no1-1} ENVELOPE 2 TYPE SERVICEABILITY\n")
        response.writelines("END DEFINE ENVELOPE\n")
        response.writelines(f"LOAD LIST 100 TO {Load_no-1} 200 TO {Load_no_12-1}\n")


    if LOADS_REQUIRED == 'EL-DL-RLL-WL-CRL(1)':

        response.writelines("********************************************************************\n")
        response.writelines("**SEISMIC PARAMETERS**\n")
        response.writelines("********************************************************************\n")
        if SEISMIC_CODE == 'IS 1893-2002/2005':
            response.writelines("DEFINE 1893 LOAD\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} DM {Damping_ratio}\n")
        if SEISMIC_CODE == 'IS 1893-2002/2005(WITH PART-4)':
            response.writelines("DEFINE 1893 LOAD PART4\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} DM {Damping_ratio}\n")
        if SEISMIC_CODE == 'IS 1893(PART-1)-2016':
            response.writelines("DEFINE IS1893 2016 LOAD\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} DM {Damping_ratio}\n")
        if SEISMIC_CODE == 'IS 1893(PART-4)-2015':
            response.writelines("DEFINE IS1893 2015 LOAD PART4\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} ST 1 DM {Damping_ratio}\n")

        response.writelines("SELFWEIGHT 1.15\n")

        response.writelines("**DEAD LOADS**\n")
        response.writelines("MEMBER WEIGHT\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1

            response.writelines(f"UNI {round((-1*DL*Unique),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 1 EQ+X\n")
        response.writelines("1893 LOAD X 1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 2 EQ-X\n")
        response.writelines("1893 LOAD X -1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 3 EQ+Z\n")
        response.writelines("1893 LOAD Z 1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 4 EQ-Z\n")
        response.writelines("1893 LOAD Z -1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 5 DL\n")
        response.writelines("SELFWEIGHT Y -1.15\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1

            response.writelines(f"UNI GY {round((DL*Unique),4)}\n")
            x=x+1
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 6 LL\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI GY {round((LL*Unique),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines(f"***WALL CO-EFF {round(Cpe1,2)} {round(Cpe4,2)} {round(Cpe5,2)} {round(Cpe6,2)}\n")
        response.writelines(f"***            {round(Cpe1a,2)} {round(Cpe4a,2)} {round(Cpe5a,2)} {round(Cpe6a,2)}\n")
        response.writelines(f"***ROOF CO-EFF {round(Cpe2,2)} {round(Cpe3,2)} {round(Cpe2a,2)} {round(Cpe3a,2)}\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 7 WL1\n")
        response.writelines("MEMBER LOAD\n")

        print("222222222222222222222222")
        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1

            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe1 - Cpi)),4)}\n")

            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe4 + Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            print("CRET4")
            st=' '.join(map(str,CRET4))
            print(CRET5)
            print("CRET5")
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 + Cpi)),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 8 WL2\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe1 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe4 - Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 - Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 9 WL3\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4 - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1 + Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 + Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 10 WL4\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1

            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1 - Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 - Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 11 WL5\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1a + Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a + Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 12 WL6\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe1a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe4a - Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a - Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 13 WL7\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1a + Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a + Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 14 WL8\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1a - Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a - Cpi)),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 15 CRL1\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 16 CRL2\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 17 CRL3\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 18 CRL4\n")

        ####################################################
        x1=[['+SLX','-SLX','+SLZ','-SLZ'],['DL'],['RLL'],['WL+X+CPI','WL-X+CPI','WL+X-CPI','WL-X-CPI','WL+Z+CPI','WL-Z+CPI','WL+Z-CPI','WL-Z-CPI'],['CRL1','CRL2','CRL3','CRL4']]
        x2=[[1,2,3,4],[5],[6],[7,8,9,10,11,12,13,14],[15,16,17,18]]
        x3=[[4],[1],[1],[8],[4]]
        y1=[
            [[0],[1.5],[1.5],[0],[1.05]],
            [[0],[1.5],[1.05],[0],[1.5]],
            [[0],[1.2],[1.2],[0.6],[1.05]],
            [[0],[1.2],[1.05],[0.6],[1.2]],
            [[0.6],[1.2],[1.2],[0],[1.05]],
            [[0.6],[1.2],[1.05],[0],[1.2]],

            [[0],[1.2],[1.2],[1.2],[0.53]],
            [[0],[1.2],[0.53],[1.2],[1.2]],
            [[1.2],[1.2],[1.2],[0],[0.53]],
            [[1.2],[1.2],[0.53],[0],[1.2]],

            [[0],[1.5],[0],[1.5],[0]],
            [[0],[0.9],[0],[1.5],[0]],
            [[1.5],[1.5],[0],[0],[0]],
            [[1.5],[0.9],[0],[0],[0]],
            [[0],[1.2],[1.2],[0],[0]],
            [[0],[1.2],[0],[0],[1.2]],
            [[0],[0.9],[1.2],[0],[0]],
            [[0],[0.9],[0],[0],[1.2]]
            ]

        y1_12=[
            [[2.5],[1.2],[0.5],[0]],
            [[2.5],[0.9],[0],[0]]
            ]

        y2=[
            [[0],[1.0],[1.0],[0],[1.0]],
            [[0],[1.0],[0.8],[0.8],[0.8]],
            [[0.8],[1.0],[0.8],[0],[0.8]],
            [[0],[1.0],[0],[1.0],[0]],
            [[1.0],[1.0],[0],[0],[0]]
            ]

        response.writelines("********************************************************************\n")
        response.writelines("*************LOAD COMBINATIONS (IS 800:2007 LSD)********************\n")
        response.writelines("****************LOAD COMBINATIONS - STRENGTH************************\n")
        response.writelines("********************************************************************\n")

        Load_no = 100

        y=0
        while y<len(y1):
            rx1=[]
            rx2=[]
            rx3=[]
            ry1=[]
            x=0
            while x<len(y1[y]):
                if y1[y][x][0]!=0:
                    ry1.append(y1[y][x])
                if y1[y][x][0]!=0:
                    rx3.append(x3[x])
                if y1[y][x][0]!=0:
                    rx2.append(x2[x])
                if y1[y][x][0]!=0:
                    rx1.append(x1[x])
                x=x+1


            if len(rx1)==5:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]}\n")
                                    response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]}\n")
                                    Load_no = Load_no + 1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==4:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]}\n")
                                response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]}\n")
                                Load_no = Load_no + 1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==3:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]}\n")
                            response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]}\n")
                            Load_no = Load_no + 1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==2:
                a = 0
                while a < rx3[0][0]:
                    b = 0
                    while b < rx3[1][0]:
                        response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]}\n")
                        response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]}\n")
                        Load_no = Load_no + 1
                        b = b + 1
                    a = a + 1

            y=y+1


        ####################################################

        response.writelines("********************************************************************\n")
        response.writelines("*************LOAD COMBINATIONS (IS 800:2007 LSD)********************\n")
        response.writelines("****************LOAD COMBINATIONS - CHAPTER 12************************\n")
        response.writelines("********************************************************************\n")

        Load_no_12 = 400

        y=0
        while y<len(y1_12):
            rx1=[]
            rx2=[]
            rx3=[]
            ry1=[]
            x=0
            while x<len(y1_12[y]):
                if y1_12[y][x][0]!=0:
                    ry1.append(y1_12[y][x])
                if y1_12[y][x][0]!=0:
                    rx3.append(x3[x])
                if y1_12[y][x][0]!=0:
                    rx2.append(x2[x])
                if y1_12[y][x][0]!=0:
                    rx1.append(x1[x])
                x=x+1


            if len(rx1)==5:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]}\n")
                                    response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]}\n")
                                    Load_no_12 = Load_no_12 + 1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==4:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]}\n")
                                response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]}\n")
                                Load_no_12 = Load_no_12 + 1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==3:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]}\n")
                            response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]}\n")
                            Load_no_12 = Load_no_12 + 1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==2:
                a = 0
                while a < rx3[0][0]:
                    b = 0
                    while b < rx3[1][0]:
                        response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]}\n")
                        response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]}\n")
                        Load_no_12 = Load_no_12 + 1
                        b = b + 1
                    a = a + 1

            y=y+1


        ####################################################

        response.writelines("********************************************************************\n")
        response.writelines("****************LOAD COMBINATIONS - SERVICEABILITY******************\n")
        response.writelines("********************************************************************\n")

        Load_no1 = 500

        y=0
        while y<len(y2):
            rx1=[]
            rx2=[]
            rx3=[]
            ry1=[]
            x=0
            while x<len(y2[y]):
                if y2[y][x][0]!=0:
                    ry1.append(y2[y][x])
                if y2[y][x][0]!=0:
                    rx3.append(x3[x])
                if y2[y][x][0]!=0:
                    rx2.append(x2[x])
                if y2[y][x][0]!=0:
                    rx1.append(x1[x])
                x=x+1


            if len(rx1)==5:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]}\n")
                                    response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]}\n")
                                    Load_no1 = Load_no1 + 1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==4:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]}\n")
                                response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]}\n")
                                Load_no1 = Load_no1 + 1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==3:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]}\n")
                            response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]}\n")
                            Load_no1 = Load_no1 + 1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==2:
                a = 0
                while a < rx3[0][0]:
                    b = 0
                    while b < rx3[1][0]:
                        response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]}\n")
                        response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]}\n")
                        Load_no1 = Load_no1 + 1
                        b = b + 1
                    a = a + 1

            y=y+1

        response.writelines("********************************************************************\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("DEFINE ENVELOPE\n")
        response.writelines(f"100 TO {Load_no-1} 400 TO {Load_no_12-1} ENVELOPE 1 TYPE STRENGTH\n")
        response.writelines(f"500 TO {Load_no1-1} ENVELOPE 2 TYPE SERVICEABILITY\n")
        response.writelines("END DEFINE ENVELOPE\n")
        response.writelines(f"LOAD LIST 100 TO {Load_no-1} 200 TO {Load_no_12-1}\n")


    if LOADS_REQUIRED == 'EL-DL-RLL-MLL-WL-CRL(1)':

        response.writelines("********************************************************************\n")
        response.writelines("**SEISMIC PARAMETERS**\n")
        response.writelines("********************************************************************\n")
        if SEISMIC_CODE == 'IS 1893-2002/2005':
            response.writelines("DEFINE 1893 LOAD\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} DM {Damping_ratio}\n")
        if SEISMIC_CODE == 'IS 1893-2002/2005(WITH PART-4)':
            response.writelines("DEFINE 1893 LOAD PART4\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} DM {Damping_ratio}\n")
        if SEISMIC_CODE == 'IS 1893(PART-1)-2016':
            response.writelines("DEFINE IS1893 2016 LOAD\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} DM {Damping_ratio}\n")
        if SEISMIC_CODE == 'IS 1893(PART-4)-2015':
            response.writelines("DEFINE IS1893 2015 LOAD PART4\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} ST 1 DM {Damping_ratio}\n")

        response.writelines("SELFWEIGHT 1.15\n")

        response.writelines("**DEAD LOADS**\n")
        response.writelines("MEMBER WEIGHT\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1

            response.writelines(f"UNI {round((-1*DL*Unique),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 1 EQ+X\n")
        response.writelines("1893 LOAD X 1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 2 EQ-X\n")
        response.writelines("1893 LOAD X -1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 3 EQ+Z\n")
        response.writelines("1893 LOAD Z 1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 4 EQ-Z\n")
        response.writelines("1893 LOAD Z -1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 5 DL\n")
        response.writelines("SELFWEIGHT Y -1.15\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1

            response.writelines(f"UNI GY {round((DL*Unique),4)}\n")
            x=x+1
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 6 LL\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI GY {round((LL*Unique),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 7 MLL\n")

        response.writelines("********************************************************************\n")
        response.writelines(f"***WALL CO-EFF {round(Cpe1,2)} {round(Cpe4,2)} {round(Cpe5,2)} {round(Cpe6,2)}\n")
        response.writelines(f"***            {round(Cpe1a,2)} {round(Cpe4a,2)} {round(Cpe5a,2)} {round(Cpe6a,2)}\n")
        response.writelines(f"***ROOF CO-EFF {round(Cpe2,2)} {round(Cpe3,2)} {round(Cpe2a,2)} {round(Cpe3a,2)}\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 8 WL1\n")
        response.writelines("MEMBER LOAD\n")

        print("222222222222222222222222")
        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1

            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe1 - Cpi)),4)}\n")

            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe4 + Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            print("CRET4")
            st=' '.join(map(str,CRET4))
            print(CRET5)
            print("CRET5")
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 + Cpi)),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 9 WL2\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe1 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe4 - Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 - Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 10 WL3\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4 - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1 + Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 + Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 11 WL4\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1

            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1 - Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 - Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 12 WL5\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1a + Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a + Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 13 WL6\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe1a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe4a - Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a - Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 14 WL7\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1a + Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a + Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 15 WL8\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1a - Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a - Cpi)),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 16 CRL1\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 17 CRL2\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 18 CRL3\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 19 CRL4\n")

        ####################################################
        x1=[['+SLX','-SLX','+SLZ','-SLZ'],['DL'],['RLL'],['MLL'],['WL+X+CPI','WL-X+CPI','WL+X-CPI','WL-X-CPI','WL+Z+CPI','WL-Z+CPI','WL+Z-CPI','WL-Z-CPI'],['CRL1','CRL2','CRL3','CRL4']]
        x2=[[1,2,3,4],[5],[6],[7],[8,9,10,11,12,13,14,15],[16,17,18,19]]
        x3=[[4],[1],[1],[1],[8],[4]]
        y1=[
            [[0],[1.5],[1.5],[1.05],[0],[1.05]],
            [[0],[1.5],[1.05],[1.5],[0],[1.05]],
            [[0],[1.5],[1.05],[1.05],[0],[1.5]],

            [[0],[1.2],[1.2],[1.05],[0.6],[1.05]],
            [[0],[1.2],[1.05],[1.2],[0.6],[1.05]],
            [[0],[1.2],[1.05],[1.05],[0.6],[1.2]],
            [[0.6],[1.2],[1.2],[1.05],[0],[1.05]],
            [[0.6],[1.2],[1.05],[1.2],[0],[1.05]],
            [[0.6],[1.2],[1.05],[1.05],[0],[1.2]],

            [[0],[1.2],[1.2],[0.53],[1.2],[0.53]],
            [[0],[1.2],[0.53],[1.2],[1.2],[0.53]],
            [[0],[1.2],[0.53],[0.53],[1.2],[1.2]],
            [[1.2],[1.2],[1.2],[0.53],[0],[0.53]],
            [[1.2],[1.2],[0.53],[1.2],[0],[0.53]],
            [[1.2],[1.2],[0.53],[0.53],[0],[1.2]],

            [[0],[1.5],[0],[0],[1.5],[0]],
            [[0],[0.9],[0],[0],[1.5],[0]],
            [[1.5],[1.5],[0],[0],[0],[0]],
            [[1.5],[0.9],[0],[0],[0],[0]],
            [[0],[1.2],[1.2],[0],[0],[0]],
            [[0],[1.2],[0],[1.2],[0],[0]],
            [[0],[1.2],[0],[0],[0],[1.2]],
            [[0],[0.9],[1.2],[0],[0],[0]],
            [[0],[0.9],[0],[1.2],[0],[0]],
            [[0],[0.9],[0],[0],[0],[1.2]]
            ]

        y1_12=[
            [[2.5],[1.2],[0.5],[0],[0],[0]],
            [[2.5],[0.9],[0],[0],[0],[0]]
            ]

        y2=[
            [[0],[1.0],[1.0],[1.0],[0],[1.0]],
            [[0],[1.0],[0.8],[0.8],[0.8],[0.8]],
            [[0.8],[1.0],[0.8],[0.8],[0],[0.8]],
            [[0],[1.0],[0],[0],[1.0],[0]],
            [[1.0],[1.0],[0],[0],[0],[0]]
            ]

        response.writelines("********************************************************************\n")
        response.writelines("*************LOAD COMBINATIONS (IS 800:2007 LSD)********************\n")
        response.writelines("****************LOAD COMBINATIONS - STRENGTH************************\n")
        response.writelines("********************************************************************\n")

        Load_no = 100

        y=0
        while y<len(y1):
            rx1=[]
            rx2=[]
            rx3=[]
            ry1=[]
            x=0
            while x<len(y1[y]):
                if y1[y][x][0]!=0:
                    ry1.append(y1[y][x])
                if y1[y][x][0]!=0:
                    rx3.append(x3[x])
                if y1[y][x][0]!=0:
                    rx2.append(x2[x])
                if y1[y][x][0]!=0:
                    rx1.append(x1[x])
                x=x+1


            if len(rx1)==5:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]}\n")
                                    response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]}\n")
                                    Load_no = Load_no + 1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==4:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]}\n")
                                response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]}\n")
                                Load_no = Load_no + 1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==3:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]}\n")
                            response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]}\n")
                            Load_no = Load_no + 1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==2:
                a = 0
                while a < rx3[0][0]:
                    b = 0
                    while b < rx3[1][0]:
                        response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]}\n")
                        response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]}\n")
                        Load_no = Load_no + 1
                        b = b + 1
                    a = a + 1

            y=y+1


        ####################################################

        response.writelines("********************************************************************\n")
        response.writelines("*************LOAD COMBINATIONS (IS 800:2007 LSD)********************\n")
        response.writelines("****************LOAD COMBINATIONS - CHAPTER 12************************\n")
        response.writelines("********************************************************************\n")

        Load_no_12 = 500

        y=0
        while y<len(y1_12):
            rx1=[]
            rx2=[]
            rx3=[]
            ry1=[]
            x=0
            while x<len(y1_12[y]):
                if y1_12[y][x][0]!=0:
                    ry1.append(y1_12[y][x])
                if y1_12[y][x][0]!=0:
                    rx3.append(x3[x])
                if y1_12[y][x][0]!=0:
                    rx2.append(x2[x])
                if y1_12[y][x][0]!=0:
                    rx1.append(x1[x])
                x=x+1


            if len(rx1)==5:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]}\n")
                                    response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]}\n")
                                    Load_no_12 = Load_no_12 + 1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==4:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]}\n")
                                response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]}\n")
                                Load_no_12 = Load_no_12 + 1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==3:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]}\n")
                            response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]}\n")
                            Load_no_12 = Load_no_12 + 1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==2:
                a = 0
                while a < rx3[0][0]:
                    b = 0
                    while b < rx3[1][0]:
                        response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]}\n")
                        response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]}\n")
                        Load_no_12 = Load_no_12 + 1
                        b = b + 1
                    a = a + 1

            y=y+1


        ####################################################

        response.writelines("********************************************************************\n")
        response.writelines("****************LOAD COMBINATIONS - SERVICEABILITY******************\n")
        response.writelines("********************************************************************\n")

        Load_no1 = 600

        y=0
        while y<len(y2):
            rx1=[]
            rx2=[]
            rx3=[]
            ry1=[]
            x=0
            while x<len(y2[y]):
                if y2[y][x][0]!=0:
                    ry1.append(y2[y][x])
                if y2[y][x][0]!=0:
                    rx3.append(x3[x])
                if y2[y][x][0]!=0:
                    rx2.append(x2[x])
                if y2[y][x][0]!=0:
                    rx1.append(x1[x])
                x=x+1


            if len(rx1)==5:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]}\n")
                                    response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]}\n")
                                    Load_no1 = Load_no1 + 1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==4:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]}\n")
                                response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]}\n")
                                Load_no1 = Load_no1 + 1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==3:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]}\n")
                            response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]}\n")
                            Load_no1 = Load_no1 + 1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==2:
                a = 0
                while a < rx3[0][0]:
                    b = 0
                    while b < rx3[1][0]:
                        response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]}\n")
                        response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]}\n")
                        Load_no1 = Load_no1 + 1
                        b = b + 1
                    a = a + 1

            y=y+1

        response.writelines("********************************************************************\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("DEFINE ENVELOPE\n")
        response.writelines(f"100 TO {Load_no-1} 500 TO {Load_no_12-1} ENVELOPE 1 TYPE STRENGTH\n")
        response.writelines(f"600 TO {Load_no1-1} ENVELOPE 2 TYPE SERVICEABILITY\n")
        response.writelines("END DEFINE ENVELOPE\n")
        response.writelines(f"LOAD LIST 100 TO {Load_no-1} 500 TO {Load_no_12-1}\n")

    if LOADS_REQUIRED == 'EL-DL-RLL-CL-WL':

        response.writelines("********************************************************************\n")
        response.writelines("**SEISMIC PARAMETERS**\n")
        response.writelines("********************************************************************\n")
        if SEISMIC_CODE == 'IS 1893-2002/2005':
            response.writelines("DEFINE 1893 LOAD\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} DM {Damping_ratio}\n")
        if SEISMIC_CODE == 'IS 1893-2002/2005(WITH PART-4)':
            response.writelines("DEFINE 1893 LOAD PART4\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} DM {Damping_ratio}\n")
        if SEISMIC_CODE == 'IS 1893(PART-1)-2016':
            response.writelines("DEFINE IS1893 2016 LOAD\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} DM {Damping_ratio}\n")
        if SEISMIC_CODE == 'IS 1893(PART-4)-2015':
            response.writelines("DEFINE IS1893 2015 LOAD PART4\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} ST 1 DM {Damping_ratio}\n")

        response.writelines("SELFWEIGHT 1.15\n")

        response.writelines("**DEAD LOADS**\n")
        response.writelines("MEMBER WEIGHT\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1

            response.writelines(f"UNI {round((-1*DL*Unique),4)}\n")
            x=x+1

        response.writelines("**COLLATERAL LOADS**\n")
        response.writelines("MEMBER WEIGHT\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI {round((-1*CL*Unique),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 1 EQ+X\n")
        response.writelines("1893 LOAD X 1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 2 EQ-X\n")
        response.writelines("1893 LOAD X -1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 3 EQ+Z\n")
        response.writelines("1893 LOAD Z 1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 4 EQ-Z\n")
        response.writelines("1893 LOAD Z -1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 5 DL\n")
        response.writelines("SELFWEIGHT Y -1.15\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1

            response.writelines(f"UNI GY {round((DL*Unique),4)}\n")
            x=x+1
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 6 LL\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI GY {round((LL*Unique),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 7 CL\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI GY {round((CL*Unique),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines(f"***WALL CO-EFF {round(Cpe1,2)} {round(Cpe4,2)} {round(Cpe5,2)} {round(Cpe6,2)}\n")
        response.writelines(f"***            {round(Cpe1a,2)} {round(Cpe4a,2)} {round(Cpe5a,2)} {round(Cpe6a,2)}\n")
        response.writelines(f"***ROOF CO-EFF {round(Cpe2,2)} {round(Cpe3,2)} {round(Cpe2a,2)} {round(Cpe3a,2)}\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 8 WL1\n")
        response.writelines("MEMBER LOAD\n")

        print("222222222222222222222222")
        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1

            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe1 - Cpi)),4)}\n")

            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe4 + Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            print("CRET4")
            st=' '.join(map(str,CRET4))
            print(CRET5)
            print("CRET5")
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 + Cpi)),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 9 WL2\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe1 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe4 - Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 - Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 10 WL3\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4 - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1 + Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 + Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 11 WL4\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1

            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1 - Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 - Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 12 WL5\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1a + Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a + Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 13 WL6\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe1a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe4a - Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a - Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 14 WL7\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1a + Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a + Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 15 WL8\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1a - Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a - Cpi)),4)}\n")
            x=x+1

        ####################################################
        x1=[['+SLX','-SLX','+SLZ','-SLZ'],['DL'],['RLL'],['CL'],['WL+X+CPI','WL-X+CPI','WL+X-CPI','WL-X-CPI','WL+Z+CPI','WL-Z+CPI','WL+Z-CPI','WL-Z-CPI']]
        x2=[[1,2,3,4],[5],[6],[7],[8,9,10,11,12,13,14,15]]
        x3=[[4],[1],[1],[1],[8]]
        y1=[
            [[0],[1.5],[1.5],[0],[0]],
            [[0],[1.2],[1.2],[0],[0.6]],
            [[0.6],[1.2],[1.2],[0],[0]],
            [[0],[1.2],[1.2],[0],[1.2]],
            [[1.2],[1.2],[1.2],[0],[0]],
            [[0],[1.5],[0],[0],[1.5]],
            [[1.5],[1.5],[0],[0],[0]],
            [[0],[0.9],[0],[0],[1.5]],
            [[1.5],[0.9],[0],[0],[0]],
            [[0],[1.2],[1.2],[0],[0]],
            [[0],[0.9],[1.2],[0],[0]],

            [[0],[1.5],[1.5],[1.5],[0]],
            [[0],[1.2],[1.2],[1.2],[0.6]],
            [[0.6],[1.2],[1.2],[1.2],[0]],
            [[0],[1.2],[1.2],[1.2],[1.2]],
            [[1.2],[1.2],[1.2],[1.2],[0]],
            [[0],[1.5],[0],[1.5],[1.5]],
            [[1.5],[1.5],[0],[1.5],[0]],
            [[0],[0.9],[0],[0.9],[1.5]],
            [[1.5],[0.9],[0],[0.9],[0]],
            [[0],[1.2],[1.2],[1.2],[0]],
            [[0],[0.9],[1.2],[0.9],[0]]
            ]

        y1_12=[
            [[2.5],[1.2],[0.5],[0],[0]],
            [[2.5],[0.9],[0],[0],[0]],

            [[2.5],[1.2],[0.5],[1.2],[0]],
            [[2.5],[0.9],[0],[0.9],[0]]
            ]

        y2=[
            [[0],[1.0],[1.0],[0],[0]],
            [[0],[1.0],[0.8],[0],[0.8]],
            [[0.8],[1.0],[0.8],[0],[0]],
            [[0],[1.0],[0],[0],[1.0]],
            [[1.0],[1.0],[0],[0],[0]],

            [[0],[1.0],[1.0],[1.0],[0]],
            [[0],[1.0],[0.8],[1.0],[0.8]],
            [[0.8],[1.0],[0.8],[1.0],[0]],
            [[0],[1.0],[0],[1.0],[1.0]],
            [[1.0],[1.0],[0],[1.0],[0]]
            ]

        response.writelines("********************************************************************\n")
        response.writelines("*************LOAD COMBINATIONS (IS 800:2007 LSD)********************\n")
        response.writelines("****************LOAD COMBINATIONS - STRENGTH************************\n")
        response.writelines("********************************************************************\n")

        Load_no = 100

        y=0
        while y<len(y1):
            rx1=[]
            rx2=[]
            rx3=[]
            ry1=[]
            x=0
            while x<len(y1[y]):
                if y1[y][x][0]!=0:
                    ry1.append(y1[y][x])
                if y1[y][x][0]!=0:
                    rx3.append(x3[x])
                if y1[y][x][0]!=0:
                    rx2.append(x2[x])
                if y1[y][x][0]!=0:
                    rx1.append(x1[x])
                x=x+1


            if len(rx1)==5:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]}\n")
                                    response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]}\n")
                                    Load_no = Load_no + 1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==4:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]}\n")
                                response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]}\n")
                                Load_no = Load_no + 1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==3:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]}\n")
                            response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]}\n")
                            Load_no = Load_no + 1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==2:
                a = 0
                while a < rx3[0][0]:
                    b = 0
                    while b < rx3[1][0]:
                        response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]}\n")
                        response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]}\n")
                        Load_no = Load_no + 1
                        b = b + 1
                    a = a + 1

            y=y+1


        ####################################################

        print("********************************************************************\n")
        print("*************LOAD COMBINATIONS (IS 800:2007 LSD)********************\n")
        print("****************LOAD COMBINATIONS - CHAPTER 12************************\n")
        print("********************************************************************\n")

        Load_no_12 = 300

        y=0
        while y<len(y1_12):
            rx1=[]
            rx2=[]
            rx3=[]
            ry1=[]
            x=0
            while x<len(y1_12[y]):
                if y1_12[y][x][0]!=0:
                    ry1.append(y1_12[y][x])
                if y1_12[y][x][0]!=0:
                    rx3.append(x3[x])
                if y1_12[y][x][0]!=0:
                    rx2.append(x2[x])
                if y1_12[y][x][0]!=0:
                    rx1.append(x1[x])
                x=x+1


            if len(rx1)==5:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]}\n")
                                    response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]}\n")
                                    Load_no_12 = Load_no_12 + 1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==4:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]}\n")
                                response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]}\n")
                                Load_no_12 = Load_no_12 + 1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==3:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]}\n")
                            response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]}\n")
                            Load_no_12 = Load_no_12 + 1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==2:
                a = 0
                while a < rx3[0][0]:
                    b = 0
                    while b < rx3[1][0]:
                        response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]}\n")
                        response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]}\n")
                        Load_no_12 = Load_no_12 + 1
                        b = b + 1
                    a = a + 1

            y=y+1


        ####################################################

        response.writelines("********************************************************************\n")
        response.writelines("****************LOAD COMBINATIONS - SERVICEABILITY******************\n")
        response.writelines("********************************************************************\n")

        Load_no1 = 400

        y=0
        while y<len(y2):
            rx1=[]
            rx2=[]
            rx3=[]
            ry1=[]
            x=0
            while x<len(y2[y]):
                if y2[y][x][0]!=0:
                    ry1.append(y2[y][x])
                if y2[y][x][0]!=0:
                    rx3.append(x3[x])
                if y2[y][x][0]!=0:
                    rx2.append(x2[x])
                if y2[y][x][0]!=0:
                    rx1.append(x1[x])
                x=x+1


            if len(rx1)==5:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]}\n")
                                    response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]}\n")
                                    Load_no1 = Load_no1 + 1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==4:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]}\n")
                                response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]}\n")
                                Load_no1 = Load_no1 + 1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==3:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]}\n")
                            response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]}\n")
                            Load_no1 = Load_no1 + 1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==2:
                a = 0
                while a < rx3[0][0]:
                    b = 0
                    while b < rx3[1][0]:
                        response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]}\n")
                        response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]}\n")
                        Load_no1 = Load_no1 + 1
                        b = b + 1
                    a = a + 1

            y=y+1

        response.writelines("********************************************************************\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("DEFINE ENVELOPE\n")
        response.writelines(f"100 TO {Load_no-1} 300 TO {Load_no_12-1} ENVELOPE 1 TYPE STRENGTH\n")
        response.writelines(f"400 TO {Load_no1-1} ENVELOPE 2 TYPE SERVICEABILITY\n")
        response.writelines("END DEFINE ENVELOPE\n")
        response.writelines(f"LOAD LIST 100 TO {Load_no-1} 300 TO {Load_no_12-1}\n")


    if LOADS_REQUIRED == 'EL-DL-RLL-MLL-CL-WL':

        response.writelines("********************************************************************\n")
        response.writelines("**SEISMIC PARAMETERS**\n")
        response.writelines("********************************************************************\n")
        if SEISMIC_CODE == 'IS 1893-2002/2005':
            response.writelines("DEFINE 1893 LOAD\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} DM {Damping_ratio}\n")
        if SEISMIC_CODE == 'IS 1893-2002/2005(WITH PART-4)':
            response.writelines("DEFINE 1893 LOAD PART4\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} DM {Damping_ratio}\n")
        if SEISMIC_CODE == 'IS 1893(PART-1)-2016':
            response.writelines("DEFINE IS1893 2016 LOAD\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} DM {Damping_ratio}\n")
        if SEISMIC_CODE == 'IS 1893(PART-4)-2015':
            response.writelines("DEFINE IS1893 2015 LOAD PART4\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} ST 1 DM {Damping_ratio}\n")

        response.writelines("SELFWEIGHT 1.15\n")

        response.writelines("**DEAD LOADS**\n")
        response.writelines("MEMBER WEIGHT\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1

            response.writelines(f"UNI {round((-1*DL*Unique),4)}\n")
            x=x+1

        response.writelines("**COLLATERAL LOADS**\n")
        response.writelines("MEMBER WEIGHT\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI {round((-1*CL*Unique),4)}\n")
            x=x+1


        response.writelines("********************************************************************\n")
        response.writelines("LOAD 1 EQ+X\n")
        response.writelines("1893 LOAD X 1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 2 EQ-X\n")
        response.writelines("1893 LOAD X -1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 3 EQ+Z\n")
        response.writelines("1893 LOAD Z 1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 4 EQ-Z\n")
        response.writelines("1893 LOAD Z -1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 5 DL\n")
        response.writelines("SELFWEIGHT Y -1.15\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1

            response.writelines(f"UNI GY {round((DL*Unique),4)}\n")
            x=x+1
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 6 LL\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI GY {round((LL*Unique),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 7 MLL\n")

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 8 CL\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI GY {round((CL*Unique),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines(f"***WALL CO-EFF {round(Cpe1,2)} {round(Cpe4,2)} {round(Cpe5,2)} {round(Cpe6,2)}\n")
        response.writelines(f"***            {round(Cpe1a,2)} {round(Cpe4a,2)} {round(Cpe5a,2)} {round(Cpe6a,2)}\n")
        response.writelines(f"***ROOF CO-EFF {round(Cpe2,2)} {round(Cpe3,2)} {round(Cpe2a,2)} {round(Cpe3a,2)}\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 9 WL1\n")
        response.writelines("MEMBER LOAD\n")

        print("222222222222222222222222")
        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1

            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe1 - Cpi)),4)}\n")

            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe4 + Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            print("CRET4")
            st=' '.join(map(str,CRET4))
            print(CRET5)
            print("CRET5")
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 + Cpi)),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 10 WL2\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe1 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe4 - Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 - Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 11 WL3\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4 - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1 + Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 + Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 12 WL4\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1

            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1 - Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 - Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 13 WL5\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1a + Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a + Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 14 WL6\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe1a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe4a - Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a - Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 15 WL7\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1a + Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a + Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 16 WL8\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1a - Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a - Cpi)),4)}\n")
            x=x+1

        ####################################################
        x1=[['+SLX','-SLX','+SLZ','-SLZ'],['DL'],['RLL'],['MLL'],['CL'],['WL+X+CPI','WL-X+CPI','WL+X-CPI','WL-X-CPI','WL+Z+CPI','WL-Z+CPI','WL+Z-CPI','WL-Z-CPI']]
        x2=[[1,2,3,4],[5],[6],[7],[8],[9,10,11,12,13,14,15,16]]
        x3=[[4],[1],[1],[1],[1],[8]]
        y1=[
            [[0],[1.5],[1.5],[1.05],[0],[0]],
            [[0],[1.5],[1.05],[1.5],[0],[0]],
            [[0],[1.2],[1.2],[1.05],[0],[0.6]],
            [[0],[1.2],[1.05],[1.2],[0],[0.6]],
            [[0.6],[1.2],[1.2],[1.05],[0],[0]],
            [[0.6],[1.2],[1.05],[1.2],[0],[0]],

            [[0],[1.2],[1.2],[0.53],[0],[1.2]],
            [[0],[1.2],[0.53],[1.2],[0],[1.2]],
            [[1.2],[1.2],[1.2],[0.53],[0],[0]],
            [[1.2],[1.2],[0.53],[1.2],[0],[0]],

            [[0],[1.5],[0],[0],[0],[1.5]],
            [[0],[0.9],[0],[0],[0],[1.5]],
            [[1.5],[1.5],[0],[0],[0],[0]],
            [[1.5],[0.9],[0],[0],[0],[0]],
            [[0],[1.2],[1.2],[0],[0],[0]],
            [[0],[1.2],[0],[1.2],[0],[0]],
            [[0],[0.9],[1.2],[0],[0],[0]],
            [[0],[0.9],[0],[1.2],[0],[0]],


            [[0],[1.5],[1.5],[1.05],[1.5],[0]],
            [[0],[1.5],[1.05],[1.5],[1.5],[0]],
            [[0],[1.2],[1.2],[1.05],[1.2],[0.6]],
            [[0],[1.2],[1.05],[1.2],[1.2],[0.6]],
            [[0.6],[1.2],[1.2],[1.05],[1.2],[0]],
            [[0.6],[1.2],[1.05],[1.2],[1.2],[0]],

            [[0],[1.2],[1.2],[0.53],[1.2],[1.2]],
            [[0],[1.2],[0.53],[1.2],[1.2],[1.2]],
            [[1.2],[1.2],[1.2],[0.53],[1.2],[0]],
            [[1.2],[1.2],[0.53],[1.2],[1.2],[0]],

            [[0],[1.5],[0],[0],[1.5],[1.5]],
            [[0],[0.9],[0],[0],[0.9],[1.5]],
            [[1.5],[1.5],[0],[0],[1.5],[0]],
            [[1.5],[0.9],[0],[0],[0.9],[0]],
            [[0],[1.2],[1.2],[0],[1.2],[0]],
            [[0],[1.2],[0],[1.2],[1.2],[0]],
            [[0],[0.9],[1.2],[0],[0.9],[0]],
            [[0],[0.9],[0],[1.2],[0.9],[0]]
            ]

        y1_12=[
            [[2.5],[1.2],[0.5],[0],[0],[0]],
            [[2.5],[0.9],[0],[0],[0],[0]],

            [[2.5],[1.2],[0.5],[0],[1.2],[0]],
            [[2.5],[0.9],[0],[0],[0.9],[0]]
            ]

        y2=[
            [[0],[1.0],[1.0],[1.0],[0],[0]],
            [[0],[1.0],[0.8],[0.8],[0],[0.8]],
            [[0.8],[1.0],[0.8],[0.8],[0],[0]],
            [[0],[1.0],[0],[0],[0],[1.0]],
            [[1.0],[1.0],[0],[0],[0],[0]],

            [[0],[1.0],[1.0],[1.0],[1.0],[0]],
            [[0],[1.0],[0.8],[0.8],[1.0],[0.8]],
            [[0.8],[1.0],[0.8],[0.8],[1.0],[0]],
            [[0],[1.0],[0],[0],[1.0],[1.0]],
            [[1.0],[1.0],[0],[0],[1.0],[0]]
            ]

        response.writelines("********************************************************************\n")
        response.writelines("*************LOAD COMBINATIONS (IS 800:2007 LSD)********************\n")
        response.writelines("****************LOAD COMBINATIONS - STRENGTH************************\n")
        response.writelines("********************************************************************\n")

        Load_no = 100

        y=0
        while y<len(y1):
            rx1=[]
            rx2=[]
            rx3=[]
            ry1=[]
            x=0
            while x<len(y1[y]):
                if y1[y][x][0]!=0:
                    ry1.append(y1[y][x])
                if y1[y][x][0]!=0:
                    rx3.append(x3[x])
                if y1[y][x][0]!=0:
                    rx2.append(x2[x])
                if y1[y][x][0]!=0:
                    rx1.append(x1[x])
                x=x+1


            if len(rx1)==5:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]}\n")
                                    response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]}\n")
                                    Load_no = Load_no + 1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==4:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]}\n")
                                response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]}\n")
                                Load_no = Load_no + 1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==3:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]}\n")
                            response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]}\n")
                            Load_no = Load_no + 1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==2:
                a = 0
                while a < rx3[0][0]:
                    b = 0
                    while b < rx3[1][0]:
                        response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]}\n")
                        response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]}\n")
                        Load_no = Load_no + 1
                        b = b + 1
                    a = a + 1

            y=y+1


        ####################################################

        response.writelines("********************************************************************\n")
        response.writelines("*************LOAD COMBINATIONS (IS 800:2007 LSD)********************\n")
        response.writelines("****************LOAD COMBINATIONS - CHAPTER 12************************\n")
        response.writelines("********************************************************************\n")

        Load_no_12 = 300

        y=0
        while y<len(y1_12):
            rx1=[]
            rx2=[]
            rx3=[]
            ry1=[]
            x=0
            while x<len(y1_12[y]):
                if y1_12[y][x][0]!=0:
                    ry1.append(y1_12[y][x])
                if y1_12[y][x][0]!=0:
                    rx3.append(x3[x])
                if y1_12[y][x][0]!=0:
                    rx2.append(x2[x])
                if y1_12[y][x][0]!=0:
                    rx1.append(x1[x])
                x=x+1


            if len(rx1)==5:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]}\n")
                                    response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]}\n")
                                    Load_no_12 = Load_no_12 + 1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==4:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]}\n")
                                response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]}\n")
                                Load_no_12 = Load_no_12 + 1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==3:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]}\n")
                            response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]}\n")
                            Load_no_12 = Load_no_12 + 1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==2:
                a = 0
                while a < rx3[0][0]:
                    b = 0
                    while b < rx3[1][0]:
                        response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]}\n")
                        response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]}\n")
                        Load_no_12 = Load_no_12 + 1
                        b = b + 1
                    a = a + 1

            y=y+1


        ####################################################

        response.writelines("********************************************************************\n")
        response.writelines("****************LOAD COMBINATIONS - SERVICEABILITY******************\n")
        response.writelines("********************************************************************\n")

        Load_no1 = 400

        y=0
        while y<len(y2):
            rx1=[]
            rx2=[]
            rx3=[]
            ry1=[]
            x=0
            while x<len(y2[y]):
                if y2[y][x][0]!=0:
                    ry1.append(y2[y][x])
                if y2[y][x][0]!=0:
                    rx3.append(x3[x])
                if y2[y][x][0]!=0:
                    rx2.append(x2[x])
                if y2[y][x][0]!=0:
                    rx1.append(x1[x])
                x=x+1


            if len(rx1)==5:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]}\n")
                                    response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]}\n")
                                    Load_no1 = Load_no1 + 1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==4:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]}\n")
                                response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]}\n")
                                Load_no1 = Load_no1 + 1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==3:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]}\n")
                            response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]}\n")
                            Load_no1 = Load_no1 + 1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==2:
                a = 0
                while a < rx3[0][0]:
                    b = 0
                    while b < rx3[1][0]:
                        response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]}\n")
                        response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]}\n")
                        Load_no1 = Load_no1 + 1
                        b = b + 1
                    a = a + 1

            y=y+1

        response.writelines("********************************************************************\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("DEFINE ENVELOPE\n")
        response.writelines(f"100 TO {Load_no-1} 300 TO {Load_no_12-1} ENVELOPE 1 TYPE STRENGTH\n")
        response.writelines(f"400 TO {Load_no1-1} ENVELOPE 2 TYPE SERVICEABILITY\n")
        response.writelines("END DEFINE ENVELOPE\n")
        response.writelines(f"LOAD LIST 100 TO {Load_no-1} 300 TO {Load_no_12-1}\n")

    if LOADS_REQUIRED == 'EL-DL-RLL-CL-WL-CRL(1)':

        response.writelines("********************************************************************\n")
        response.writelines("**SEISMIC PARAMETERS**\n")
        response.writelines("********************************************************************\n")
        if SEISMIC_CODE == 'IS 1893-2002/2005':
            response.writelines("DEFINE 1893 LOAD\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} DM {Damping_ratio}\n")
        if SEISMIC_CODE == 'IS 1893-2002/2005(WITH PART-4)':
            response.writelines("DEFINE 1893 LOAD PART4\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} DM {Damping_ratio}\n")
        if SEISMIC_CODE == 'IS 1893(PART-1)-2016':
            response.writelines("DEFINE IS1893 2016 LOAD\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} DM {Damping_ratio}\n")
        if SEISMIC_CODE == 'IS 1893(PART-4)-2015':
            response.writelines("DEFINE IS1893 2015 LOAD PART4\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} ST 1 DM {Damping_ratio}\n")

        response.writelines("SELFWEIGHT 1.15\n")

        response.writelines("**DEAD LOADS**\n")
        response.writelines("MEMBER WEIGHT\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1

            response.writelines(f"UNI {round((-1*DL*Unique),4)}\n")
            x=x+1

        response.writelines("**COLLATERAL LOADS**\n")
        response.writelines("MEMBER WEIGHT\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI {round((-1*CL*Unique),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 1 EQ+X\n")
        response.writelines("1893 LOAD X 1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 2 EQ-X\n")
        response.writelines("1893 LOAD X -1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 3 EQ+Z\n")
        response.writelines("1893 LOAD Z 1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 4 EQ-Z\n")
        response.writelines("1893 LOAD Z -1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 5 DL\n")
        response.writelines("SELFWEIGHT Y -1.15\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1

            response.writelines(f"UNI GY {round((DL*Unique),4)}\n")
            x=x+1
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 6 LL\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI GY {round((LL*Unique),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 7 CL\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI GY {round((CL*Unique),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines(f"***WALL CO-EFF {round(Cpe1,2)} {round(Cpe4,2)} {round(Cpe5,2)} {round(Cpe6,2)}\n")
        response.writelines(f"***            {round(Cpe1a,2)} {round(Cpe4a,2)} {round(Cpe5a,2)} {round(Cpe6a,2)}\n")
        response.writelines(f"***ROOF CO-EFF {round(Cpe2,2)} {round(Cpe3,2)} {round(Cpe2a,2)} {round(Cpe3a,2)}\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 8 WL1\n")
        response.writelines("MEMBER LOAD\n")

        print("222222222222222222222222")
        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1

            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe1 - Cpi)),4)}\n")

            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe4 + Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            print("CRET4")
            st=' '.join(map(str,CRET4))
            print(CRET5)
            print("CRET5")
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 + Cpi)),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 9 WL2\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe1 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe4 - Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 - Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 10 WL3\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4 - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1 + Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 + Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 11 WL4\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1

            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1 - Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 - Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 12 WL5\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1a + Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a + Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 13 WL6\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe1a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe4a - Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a - Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 14 WL7\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1a + Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a + Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 15 WL8\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1a - Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a - Cpi)),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 16 CRL1\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 17 CRL2\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 18 CRL3\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 19 CRL4\n")

        ####################################################

        x1=[['+SLX','-SLX','+SLZ','-SLZ'],['DL'],['RLL'],['CL'],['WL+X+CPI','WL-X+CPI','WL+X-CPI','WL-X-CPI','WL+Z+CPI','WL-Z+CPI','WL+Z-CPI','WL-Z-CPI'],['CRL1','CRL2','CRL3','CRL4']]
        x2=[[1,2,3,4],[5],[6],[7],[8,9,10,11,12,13,14,15],[16,17,18,19]]
        x3=[[4],[1],[1],[1],[8],[4]]
        y1=[
            [[0],[1.5],[1.5],[0],[0],[1.05]],
            [[0],[1.5],[1.05],[0],[0],[1.5]],
            [[0],[1.2],[1.2],[0],[0.6],[1.05]],
            [[0],[1.2],[1.05],[0],[0.6],[1.2]],
            [[0.6],[1.2],[1.2],[0],[0],[1.05]],
            [[0.6],[1.2],[1.05],[0],[0],[1.2]],

            [[0],[1.2],[1.2],[0],[1.2],[0.53]],
            [[0],[1.2],[0.53],[0],[1.2],[1.2]],
            [[1.2],[1.2],[1.2],[0],[0],[0.53]],
            [[1.2],[1.2],[0.53],[0],[0],[1.2]],

            [[0],[1.5],[0],[0],[1.5],[0]],
            [[0],[0.9],[0],[0],[1.5],[0]],
            [[1.5],[1.5],[0],[0],[0],[0]],
            [[1.5],[0.9],[0],[0],[0],[0]],
            [[0],[1.2],[1.2],[0],[0],[0]],
            [[0],[1.2],[0],[0],[0],[1.2]],
            [[0],[0.9],[1.2],[0],[0],[0]],
            [[0],[0.9],[0],[0],[0],[1.2]],


            [[0],[1.5],[1.5],[1.5],[0],[1.05]],
            [[0],[1.5],[1.05],[1.5],[0],[1.5]],
            [[0],[1.2],[1.2],[1.2],[0.6],[1.05]],
            [[0],[1.2],[1.05],[1.2],[0.6],[1.2]],
            [[0.6],[1.2],[1.2],[1.2],[0],[1.05]],
            [[0.6],[1.2],[1.05],[1.2],[0],[1.2]],

            [[0],[1.2],[1.2],[1.2],[1.2],[0.53]],
            [[0],[1.2],[0.53],[1.2],[1.2],[1.2]],
            [[1.2],[1.2],[1.2],[1.2],[0],[0.53]],
            [[1.2],[1.2],[0.53],[1.2],[0],[1.2]],

            [[0],[1.5],[0],[1.5],[1.5],[0]],
            [[0],[0.9],[0],[0.9],[1.5],[0]],
            [[1.5],[1.5],[0],[1.5],[0],[0]],
            [[1.5],[0.9],[0],[0.9],[0],[0]],
            [[0],[1.2],[1.2],[1.2],[0],[0]],
            [[0],[1.2],[0],[1.2],[0],[1.2]],
            [[0],[0.9],[1.2],[0.9],[0],[0]],
            [[0],[0.9],[0],[0.9],[0],[1.2]]
            ]

        y1_12=[
            [[2.5],[1.2],[0.5],[0],[0],[0]],
            [[2.5],[0.9],[0],[0],[0],[0]],

            [[2.5],[1.2],[0.5],[1.2],[0],[0]],
            [[2.5],[0.9],[0],[0.9],[0],[0]]
            ]

        y2=[
            [[0],[1.0],[1.0],[0],[0],[1.0]],
            [[0],[1.0],[0.8],[0],[0.8],[0.8]],
            [[0.8],[1.0],[0.8],[0],[0],[0.8]],
            [[0],[1.0],[0],[0],[1.0],[0]],
            [[1.0],[1.0],[0],[0],[0],[0]],

            [[0],[1.0],[1.0],[1.0],[0],[1.0]],
            [[0],[1.0],[0.8],[1.0],[0.8],[0.8]],
            [[0.8],[1.0],[0.8],[1.0],[0],[0.8]],
            [[0],[1.0],[0],[1.0],[1.0],[0]],
            [[1.0],[1.0],[0],[1.0],[0],[0]]
            ]

        response.writelines("********************************************************************\n")
        response.writelines("*************LOAD COMBINATIONS (IS 800:2007 LSD)********************\n")
        response.writelines("****************LOAD COMBINATIONS - STRENGTH************************\n")
        response.writelines("********************************************************************\n")

        Load_no = 100

        y=0
        while y<len(y1):
            rx1=[]
            rx2=[]
            rx3=[]
            ry1=[]
            x=0
            while x<len(y1[y]):
                if y1[y][x][0]!=0:
                    ry1.append(y1[y][x])
                if y1[y][x][0]!=0:
                    rx3.append(x3[x])
                if y1[y][x][0]!=0:
                    rx2.append(x2[x])
                if y1[y][x][0]!=0:
                    rx1.append(x1[x])
                x=x+1


            if len(rx1)==5:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]}\n")
                                    response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]}\n")
                                    Load_no = Load_no + 1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==4:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]}\n")
                                response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]}\n")
                                Load_no = Load_no + 1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==3:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]}\n")
                            response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]}\n")
                            Load_no = Load_no + 1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==2:
                a = 0
                while a < rx3[0][0]:
                    b = 0
                    while b < rx3[1][0]:
                        response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]}\n")
                        response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]}\n")
                        Load_no = Load_no + 1
                        b = b + 1
                    a = a + 1

            y=y+1


        ####################################################

        response.writelines("********************************************************************\n")
        response.writelines("*************LOAD COMBINATIONS (IS 800:2007 LSD)********************\n")
        response.writelines("****************LOAD COMBINATIONS - CHAPTER 12************************\n")
        response.writelines("********************************************************************\n")

        Load_no_12 = 600

        y=0
        while y<len(y1_12):
            rx1=[]
            rx2=[]
            rx3=[]
            ry1=[]
            x=0
            while x<len(y1_12[y]):
                if y1_12[y][x][0]!=0:
                    ry1.append(y1_12[y][x])
                if y1_12[y][x][0]!=0:
                    rx3.append(x3[x])
                if y1_12[y][x][0]!=0:
                    rx2.append(x2[x])
                if y1_12[y][x][0]!=0:
                    rx1.append(x1[x])
                x=x+1


            if len(rx1)==5:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]}\n")
                                    response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]}\n")
                                    Load_no_12 = Load_no_12 + 1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==4:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]}\n")
                                response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]}\n")
                                Load_no_12 = Load_no_12 + 1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==3:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]}\n")
                            response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]}\n")
                            Load_no_12 = Load_no_12 + 1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==2:
                a = 0
                while a < rx3[0][0]:
                    b = 0
                    while b < rx3[1][0]:
                        response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]}\n")
                        response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]}\n")
                        Load_no_12 = Load_no_12 + 1
                        b = b + 1
                    a = a + 1

            y=y+1


        ####################################################

        response.writelines("********************************************************************\n")
        response.writelines("****************LOAD COMBINATIONS - SERVICEABILITY******************\n")
        response.writelines("********************************************************************\n")

        Load_no1 = 700

        y=0
        while y<len(y2):
            rx1=[]
            rx2=[]
            rx3=[]
            ry1=[]
            x=0
            while x<len(y2[y]):
                if y2[y][x][0]!=0:
                    ry1.append(y2[y][x])
                if y2[y][x][0]!=0:
                    rx3.append(x3[x])
                if y2[y][x][0]!=0:
                    rx2.append(x2[x])
                if y2[y][x][0]!=0:
                    rx1.append(x1[x])
                x=x+1


            if len(rx1)==5:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]}\n")
                                    response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]}\n")
                                    Load_no1 = Load_no1 + 1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==4:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]}\n")
                                response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]}\n")
                                Load_no1 = Load_no1 + 1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==3:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]}\n")
                            response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]}\n")
                            Load_no1 = Load_no1 + 1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==2:
                a = 0
                while a < rx3[0][0]:
                    b = 0
                    while b < rx3[1][0]:
                        response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]}\n")
                        response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]}\n")
                        Load_no1 = Load_no1 + 1
                        b = b + 1
                    a = a + 1

            y=y+1

        response.writelines("********************************************************************\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("DEFINE ENVELOPE\n")
        response.writelines(f"100 TO {Load_no-1} 600 TO {Load_no_12-1} ENVELOPE 1 TYPE STRENGTH\n")
        response.writelines(f"700 TO {Load_no1-1} ENVELOPE 2 TYPE SERVICEABILITY\n")
        response.writelines("END DEFINE ENVELOPE\n")
        response.writelines(f"LOAD LIST 100 TO {Load_no-1} 600 TO {Load_no_12-1}\n")



    if LOADS_REQUIRED == 'EL-DL-RLL-MLL-CL-WL-CRL(1)':

        response.writelines("********************************************************************\n")
        response.writelines("**SEISMIC PARAMETERS**\n")
        response.writelines("********************************************************************\n")
        if SEISMIC_CODE == 'IS 1893-2002/2005':
            response.writelines("DEFINE 1893 LOAD\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} DM {Damping_ratio}\n")
        if SEISMIC_CODE == 'IS 1893-2002/2005(WITH PART-4)':
            response.writelines("DEFINE 1893 LOAD PART4\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} DM {Damping_ratio}\n")
        if SEISMIC_CODE == 'IS 1893(PART-1)-2016':
            response.writelines("DEFINE IS1893 2016 LOAD\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} DM {Damping_ratio}\n")
        if SEISMIC_CODE == 'IS 1893(PART-4)-2015':
            response.writelines("DEFINE IS1893 2015 LOAD PART4\n")
            response.writelines(f"ZONE {Zone_factor} RF {Response_reduction_factor} I {Importance_factor} SS {Rock_and_soil_site_factor} ST 1 DM {Damping_ratio}\n")

        response.writelines("SELFWEIGHT 1.15\n")

        response.writelines("**DEAD LOADS**\n")
        response.writelines("MEMBER WEIGHT\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1

            response.writelines(f"UNI {round((-1*DL*Unique),4)}\n")
            x=x+1

        response.writelines("**COLLATERAL LOADS**\n")
        response.writelines("MEMBER WEIGHT\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI {round((-1*CL*Unique),4)}\n")
            x=x+1


        response.writelines("********************************************************************\n")
        response.writelines("LOAD 1 EQ+X\n")
        response.writelines("1893 LOAD X 1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 2 EQ-X\n")
        response.writelines("1893 LOAD X -1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 3 EQ+Z\n")
        response.writelines("1893 LOAD Z 1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 4 EQ-Z\n")
        response.writelines("1893 LOAD Z -1\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("CHANGE\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 5 DL\n")
        response.writelines("SELFWEIGHT Y -1.15\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1

            response.writelines(f"UNI GY {round((DL*Unique),4)}\n")
            x=x+1
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 6 LL\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI GY {round((LL*Unique),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 7 MLL\n")

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 8 CL\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<(len(EWX)-1):
                        if i>1 and i<len(EWX):
                            CRET.append(i+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            CRET1=[]
            y=1
            while y<=len(CRET):
                if len(CRET)>=15:
                    CRET1.append(CRET[y-1])
                    if y%15==0 or y%len(CRET)==0:
                        st=' '.join(map(str,CRET1))
                        if y==len(CRET):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRET1)
                        print(st)
                        CRET1=[]
                else:
                    if y==len(CRET):
                        st=' '.join(map(str,CRET))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI GY {round((CL*Unique),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines(f"***WALL CO-EFF {round(Cpe1,2)} {round(Cpe4,2)} {round(Cpe5,2)} {round(Cpe6,2)}\n")
        response.writelines(f"***            {round(Cpe1a,2)} {round(Cpe4a,2)} {round(Cpe5a,2)} {round(Cpe6a,2)}\n")
        response.writelines(f"***ROOF CO-EFF {round(Cpe2,2)} {round(Cpe3,2)} {round(Cpe2a,2)} {round(Cpe3a,2)}\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 9 WL1\n")
        response.writelines("MEMBER LOAD\n")

        print("222222222222222222222222")
        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1

            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe1 - Cpi)),4)}\n")

            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe4 + Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            print("CRET4")
            st=' '.join(map(str,CRET4))
            print(CRET5)
            print("CRET5")
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 + Cpi)),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 10 WL2\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe1 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe4 - Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 - Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 11 WL3\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4 - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1 + Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 + Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 12 WL4\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1

            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4 + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3 - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe2 - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1 - Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5 + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6 - Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 13 WL5\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1a + Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a + Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 14 WL6\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe1a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe4a - Cpi)),4)}\n")

        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a - Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 15 WL7\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a + Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1a + Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a - Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a + Cpi)),4)}\n")

            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 16 WL8\n")
        response.writelines("MEMBER LOAD\n")

        for Unique in Unique_bay_sp:
            CRET=[]
            CRET1=[]
            CRET2=[]
            CRET3=[]
            x=0
            while x < len(Diff_bay_sp):
                if Diff_bay_sp[x]==Unique:
                    i=0
                    while i<=(len(EWX)-1):
                        if i==0:
                            CRET.append(1+((len(EWX)-1)*x))
                        if i>0 and i<((len(EWX)-1)/2):
                            CRET1.append((i+1)+((len(EWX)-1)*x))
                        if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                            CRET2.append((i+1)+((len(EWX)-1)*x))
                        if i==len(EWX)-1:
                            CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
                        i=i+1
                x=x+1
            print(CRET)
            st=' '.join(map(str,CRET))
            print(CRET1)
            st1=' '.join(map(str,CRET1))
            print(CRET2)
            st2=' '.join(map(str,CRET2))
            print(CRET3)
            st3=' '.join(map(str,CRET3))
            print(st)
            response.writelines(f"{st} UNI GX {round((WL*Unique* (Cpe4a + Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET1):
                if len(CRET1)>=15:
                    CRETA1.append(CRET1[y-1])
                    if y%15==0 or y%len(CRET1)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET1):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET1):
                        st=' '.join(map(str,CRET1))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            CRETA1=[]
            y=1
            while y<=len(CRET2):
                if len(CRET2)>=15:
                    CRETA1.append(CRET2[y-1])
                    if y%15==0 or y%len(CRET2)==0:
                        st=' '.join(map(str,CRETA1))
                        if y==len(CRET2):
                            response.writelines(f"{st} -\n")
                        else:
                            response.writelines(f"{st} -\n")
                        print(CRETA1)
                        print(st)
                        CRETA1=[]
                else:
                    if y==len(CRET2):
                        st=' '.join(map(str,CRET2))
                        response.writelines(f"{st} -\n")
                y=y+1
            response.writelines(f"UNI Y {round((WL*Unique* (-Cpe3a - Cpi)),4)}\n")
            response.writelines(f"{st3} UNI GX {round((WL*Unique* (-Cpe1a - Cpi)),4)}\n")


        x=0
        while x<2:
            i=0
            CRET4=[]
            CRET5=[]
            while i<((len(EW4)-1)-len(ICO)-2):
                if x==0:
                    CRET4.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                if x==1:
                    CRET5.append((i+1)+((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(x*((len(EW4)-1)-len(ICO)-2)))
                i=i+1
            CRET4.sort()
            CRET5.sort()
            if x==0:
                CRET4.insert(0,1)
                CRET4.insert((len(EW4)-2),len(EWX)-1)
                z=0
                while z<len(ICO):
                    CRET4.insert(ICO_Nodes2[z],((len(EWX)-1)*len(SW1))+(1+z))
                    z=z+1
            if x==1:
                CRET5.insert(0,1+((len(EWX)-1)*(len(SW1)-1)))
                CRET5.insert((len(EW4)-2),(len(EWX)-1)+((len(EWX)-1)*(len(SW1)-1)))
                z=1
                while z<=len(ICO):
                    CRET5.insert(ICO_Nodes2[z-1],((len(EWX)-1)*len(SW1))+(z+ (len(ICO)*(len(SW1)-1)) ))
                    z=z+1

            print(CRET4)
            st=' '.join(map(str,CRET4))
            print(CRET5)
            st1=' '.join(map(str,CRET5))
            print(st)

            if x==0:
                for Unique in Unique_EW_bay_sp:
                    CRET4A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET4A.append(CRET4[y])
                        y=y+1
                    st1=' '.join(map(str,CRET4A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (Cpe5a + Cpi)),4)}\n")

            if x==1:
                for Unique in Unique_EW_bay_sp:
                    CRET5A=[]
                    y=0
                    while y<len(Diff_EW_bay_sp):
                        if Diff_EW_bay_sp[y]==Unique:
                            CRET5A.append(CRET5[y])
                        y=y+1
                    st1=' '.join(map(str,CRET5A))
                    response.writelines(f"{st1}-\n")
                    response.writelines(f"UNI GZ {round((WL*Unique* (-Cpe6a - Cpi)),4)}\n")
            x=x+1

        response.writelines("********************************************************************\n")
        response.writelines("LOAD 17 CRL1\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 18 CRL2\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 19 CRL3\n")
        response.writelines("********************************************************************\n")
        response.writelines("LOAD 20 CRL4\n")

        ####################################################

        x1=[['+SLX','-SLX','+SLZ','-SLZ'],['DL'],['RLL'],['MLL'],['CL'],['WL+X+CPI','WL-X+CPI','WL+X-CPI','WL-X-CPI','WL+Z+CPI','WL-Z+CPI','WL+Z-CPI','WL-Z-CPI'],['CRL1','CRL2','CRL3','CRL4']]
        x2=[[1,2,3,4],[5],[6],[7],[8],[9,10,11,12,13,14,15,16],[17,18,19,20]]
        x3=[[4],[1],[1],[1],[1],[8],[4]]
        y1=[
            [[0],[1.5],[1.5],[1.05],[0],[0],[1.05]],
            [[0],[1.5],[1.05],[1.5],[0],[0],[1.05]],
            [[0],[1.5],[1.05],[1.05],[0],[0],[1.5]],

            [[0],[1.2],[1.2],[1.05],[0],[0.6],[1.05]],
            [[0],[1.2],[1.05],[1.2],[0],[0.6],[1.05]],
            [[0],[1.2],[1.05],[1.05],[0],[0.6],[1.2]],
            [[0.6],[1.2],[1.2],[1.05],[0],[0],[1.05]],
            [[0.6],[1.2],[1.05],[1.2],[0],[0],[1.05]],
            [[0.6],[1.2],[1.05],[1.05],[0],[0],[1.2]],

            [[0],[1.2],[1.2],[0.53],[0],[1.2],[0.53]],
            [[0],[1.2],[0.53],[1.2],[0],[1.2],[0.53]],
            [[0],[1.2],[0.53],[0.53],[0],[1.2],[1.2]],
            [[1.2],[1.2],[1.2],[0.53],[0],[0],[0.53]],
            [[1.2],[1.2],[0.53],[1.2],[0],[0],[0.53]],
            [[1.2],[1.2],[0.53],[0.53],[0],[0],[1.2]],

            [[0],[1.5],[0],[0],[0],[1.5],[0]],
            [[0],[0.9],[0],[0],[0],[1.5],[0]],
            [[1.5],[1.5],[0],[0],[0],[0],[0]],
            [[1.5],[0.9],[0],[0],[0],[0],[0]],
            [[0],[1.2],[1.2],[0],[0],[0],[0]],
            [[0],[1.2],[0],[1.2],[0],[0],[0]],
            [[0],[1.2],[0],[0],[0],[0],[1.2]],
            [[0],[0.9],[1.2],[0],[0],[0],[0]],
            [[0],[0.9],[0],[1.2],[0],[0],[0]],
            [[0],[0.9],[0],[0],[0],[0],[1.2]],


            [[0],[1.5],[1.5],[1.05],[1.5],[0],[1.05]],
            [[0],[1.5],[1.05],[1.5],[1.5],[0],[1.05]],
            [[0],[1.5],[1.05],[1.05],[1.5],[0],[1.5]],

            [[0],[1.2],[1.2],[1.05],[1.2],[0.6],[1.05]],
            [[0],[1.2],[1.05],[1.2],[1.2],[0.6],[1.05]],
            [[0],[1.2],[1.05],[1.05],[1.2],[0.6],[1.2]],
            [[0.6],[1.2],[1.2],[1.05],[1.2],[0],[1.05]],
            [[0.6],[1.2],[1.05],[1.2],[1.2],[0],[1.05]],
            [[0.6],[1.2],[1.05],[1.05],[1.2],[0],[1.2]],

            [[0],[1.2],[1.2],[0.53],[1.2],[1.2],[0.53]],
            [[0],[1.2],[0.53],[1.2],[1.2],[1.2],[0.53]],
            [[0],[1.2],[0.53],[0.53],[1.2],[1.2],[1.2]],
            [[1.2],[1.2],[1.2],[0.53],[1.2],[0],[0.53]],
            [[1.2],[1.2],[0.53],[1.2],[1.2],[0],[0.53]],
            [[1.2],[1.2],[0.53],[0.53],[1.2],[0],[1.2]],

            [[0],[1.5],[0],[0],[1.5],[1.5],[0]],
            [[0],[0.9],[0],[0],[0.9],[1.5],[0]],
            [[1.5],[1.5],[0],[0],[1.5],[0],[0]],
            [[1.5],[0.9],[0],[0],[0.9],[0],[0]],
            [[0],[1.2],[1.2],[0],[1.2],[0],[0]],
            [[0],[1.2],[0],[1.2],[1.2],[0],[0]],
            [[0],[1.2],[0],[0],[1.2],[0],[1.2]],
            [[0],[0.9],[1.2],[0],[0.9],[0],[0]],
            [[0],[0.9],[0],[1.2],[0.9],[0],[0]],
            [[0],[0.9],[0],[0],[0.9],[0],[1.2]]
            ]

        y1_12=[
            [[2.5],[1.2],[0.5],[0],[0],[0],[0]],
            [[2.5],[0.9],[0],[0],[0],[0],[0]],

            [[2.5],[1.2],[0.5],[0],[1.2],[0],[0]],
            [[2.5],[0.9],[0],[0],[0.9],[0],[0]]
            ]

        y2=[
            [[0],[1.0],[1.0],[1.0],[0],[0],[1.0]],
            [[0],[1.0],[0.8],[0.8],[0],[0.8],[0.8]],
            [[0.8],[1.0],[0.8],[0.8],[0],[0],[0.8]],
            [[0],[1.0],[0],[0],[0],[1.0],[0]],
            [[1.0],[1.0],[0],[0],[0],[0],[0]],

            [[0],[1.0],[1.0],[1.0],[1.0],[0],[1.0]],
            [[0],[1.0],[0.8],[0.8],[1.0],[0.8],[0.8]],
            [[0.8],[1.0],[0.8],[0.8],[1.0],[0],[0.8]],
            [[0],[1.0],[0],[0],[1.0],[1.0],[0]],
            [[1.0],[1.0],[0],[0],[1.0],[0],[0]]
            ]

        response.writelines("********************************************************************\n")
        response.writelines("*************LOAD COMBINATIONS (IS 800:2007 LSD)********************\n")
        response.writelines("****************LOAD COMBINATIONS - STRENGTH************************\n")
        response.writelines("********************************************************************\n")

        Load_no = 100

        y=0
        while y<len(y1):
            rx1=[]
            rx2=[]
            rx3=[]
            ry1=[]
            x=0
            while x<len(y1[y]):
                if y1[y][x][0]!=0:
                    ry1.append(y1[y][x])
                if y1[y][x][0]!=0:
                    rx3.append(x3[x])
                if y1[y][x][0]!=0:
                    rx2.append(x2[x])
                if y1[y][x][0]!=0:
                    rx1.append(x1[x])
                x=x+1

            if len(rx1)==7:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    f=0
                                    while f < rx3[5][0]:
                                        g=0
                                        while g < rx3[6][0]:
                                            response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]} {'+'} {ry1[5][0]}{rx1[5][f]} {'+'} {ry1[6][0]}{rx1[6][g]}\n")
                                            response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]} {rx2[5][f]} {ry1[5][0]} {rx2[6][g]} {ry1[6][0]}\n")
                                            Load_no = Load_no + 1
                                            g=g+1
                                        f=f+1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==6:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    f=0
                                    while f < rx3[5][0]:
                                        response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]} {'+'} {ry1[5][0]}{rx1[5][f]}\n")
                                        response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]} {rx2[5][f]} {ry1[5][0]}\n")
                                        Load_no = Load_no + 1
                                        f=f+1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==5:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]}\n")
                                    response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]}\n")
                                    Load_no = Load_no + 1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==4:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]}\n")
                                response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]}\n")
                                Load_no = Load_no + 1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==3:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]}\n")
                            response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]}\n")
                            Load_no = Load_no + 1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==2:
                a = 0
                while a < rx3[0][0]:
                    b = 0
                    while b < rx3[1][0]:
                        response.writelines(f"LOAD COMB {Load_no} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]}\n")
                        response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]}\n")
                        Load_no = Load_no + 1
                        b = b + 1
                    a = a + 1

            y=y+1


        ####################################################

        response.writelines("********************************************************************\n")
        response.writelines("*************LOAD COMBINATIONS (IS 800:2007 LSD)********************\n")
        response.writelines("****************LOAD COMBINATIONS - CHAPTER 12************************\n")
        response.writelines("********************************************************************\n")

        Load_no_12 = 900

        y=0
        while y<len(y1_12):
            rx1=[]
            rx2=[]
            rx3=[]
            ry1=[]
            x=0
            while x<len(y1_12[y]):
                if y1_12[y][x][0]!=0:
                    ry1.append(y1_12[y][x])
                if y1_12[y][x][0]!=0:
                    rx3.append(x3[x])
                if y1_12[y][x][0]!=0:
                    rx2.append(x2[x])
                if y1_12[y][x][0]!=0:
                    rx1.append(x1[x])
                x=x+1

            if len(rx1)==7:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    f=0
                                    while f < rx3[5][0]:
                                        g=0
                                        while g < rx3[6][0]:
                                            response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]} {'+'} {ry1[5][0]}{rx1[5][f]} {'+'} {ry1[6][0]}{rx1[6][g]}\n")
                                            response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]} {rx2[5][f]} {ry1[5][0]} {rx2[6][g]} {ry1[6][0]}\n")
                                            Load_no_12 = Load_no_12 + 1
                                            g=g+1
                                        f=f+1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==6:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    f=0
                                    while f < rx3[5][0]:
                                        response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]} {'+'} {ry1[5][0]}{rx1[5][f]}\n")
                                        response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]} {rx2[5][f]} {ry1[5][0]}\n")
                                        Load_no_12 = Load_no_12 + 1
                                        f=f+1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==5:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]}\n")
                                    response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]}\n")
                                    Load_no_12 = Load_no_12 + 1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==4:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]}\n")
                                response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]}\n")
                                Load_no_12 = Load_no_12 + 1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==3:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]}\n")
                            response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]}\n")
                            Load_no_12 = Load_no_12 + 1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==2:
                a = 0
                while a < rx3[0][0]:
                    b = 0
                    while b < rx3[1][0]:
                        response.writelines(f"LOAD COMB {Load_no_12} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]}\n")
                        response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]}\n")
                        Load_no_12 = Load_no_12 + 1
                        b = b + 1
                    a = a + 1

            y=y+1


        ####################################################

        response.writelines("********************************************************************\n")
        response.writelines("****************LOAD COMBINATIONS - SERVICEABILITY******************\n")
        response.writelines("********************************************************************\n")

        Load_no1 = 1000

        y=0
        while y<len(y2):
            rx1=[]
            rx2=[]
            rx3=[]
            ry1=[]
            x=0
            while x<len(y2[y]):
                if y2[y][x][0]!=0:
                    ry1.append(y2[y][x])
                if y2[y][x][0]!=0:
                    rx3.append(x3[x])
                if y2[y][x][0]!=0:
                    rx2.append(x2[x])
                if y2[y][x][0]!=0:
                    rx1.append(x1[x])
                x=x+1

            if len(rx1)==7:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    f=0
                                    while f < rx3[5][0]:
                                        g=0
                                        while g < rx3[6][0]:
                                            response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]} {'+'} {ry1[5][0]}{rx1[5][f]} {'+'} {ry1[6][0]}{rx1[6][g]}\n")
                                            response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]} {rx2[5][f]} {ry1[5][0]} {rx2[6][g]} {ry1[6][0]}\n")
                                            Load_no1 = Load_no1 + 1
                                            g=g+1
                                        f=f+1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==6:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    f=0
                                    while f < rx3[5][0]:
                                        response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]} {'+'} {ry1[5][0]}{rx1[5][f]}\n")
                                        response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]} {rx2[5][f]} {ry1[5][0]}\n")
                                        Load_no1 = Load_no1 + 1
                                        f=f+1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==5:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                e=0
                                while e < rx3[4][0]:
                                    response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]} {'+'} {ry1[4][0]}{rx1[4][e]}\n")
                                    response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]} {rx2[4][e]} {ry1[4][0]}\n")
                                    Load_no1 = Load_no1 + 1
                                    e=e+1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==4:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            d=0
                            while d < rx3[3][0]:
                                response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]} {'+'} {ry1[3][0]}{rx1[3][d]}\n")
                                response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]} {rx2[3][d]} {ry1[3][0]}\n")
                                Load_no1 = Load_no1 + 1
                                d=d+1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==3:
                a=0
                while a < rx3[0][0]:
                    b=0
                    while b < rx3[1][0]:
                        c=0
                        while c < rx3[2][0]:
                            response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]} {'+'} {ry1[2][0]}{rx1[2][c]}\n")
                            response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]} {rx2[2][c]} {ry1[2][0]}\n\n")
                            Load_no1 = Load_no1 + 1
                            c=c+1
                        b=b+1
                    a=a+1

            if len(rx1)==2:
                a = 0
                while a < rx3[0][0]:
                    b = 0
                    while b < rx3[1][0]:
                        response.writelines(f"LOAD COMB {Load_no1} {ry1[0][0]}{rx1[0][a]} {'+'} {ry1[1][0]}{rx1[1][b]}\n")
                        response.writelines(f"{rx2[0][a]} {ry1[0][0]} {rx2[1][b]} {ry1[1][0]}\n")
                        Load_no1 = Load_no1 + 1
                        b = b + 1
                    a = a + 1

            y=y+1

        response.writelines("********************************************************************\n")
        response.writelines("PERFORM ANALYSIS\n")
        response.writelines("DEFINE ENVELOPE\n")
        response.writelines(f"100 TO {Load_no-1} 900 TO {Load_no_12-1} ENVELOPE 1 TYPE STRENGTH\n")
        response.writelines(f"1000 TO {Load_no1-1} ENVELOPE 2 TYPE SERVICEABILITY\n")
        response.writelines("END DEFINE ENVELOPE\n")
        response.writelines(f"LOAD LIST 100 TO {Load_no-1} 900 TO {Load_no_12-1}\n")

    ########################################################################################################
    response.writelines("PARAMETER 1\n")
    response.writelines("CODE IS800 LSD\n")

    Memb_total = ((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(len(Only_WC_Nodes)*2)
    MEMB=[]
    i=0
    while i<=(Memb_total-1):
        MEMB.append(i+1)
        i=i+1
    print(MEMB)
    st=' '.join(map(str,MEMB))
    print(st)

    response.writelines(f"FYLD 345000 MEMB -\n")
    CRETA1=[]
    y=1
    while y<=len(MEMB):
        if len(MEMB)>=15:
            CRETA1.append(MEMB[y-1])
            if y%15==0 or y%len(MEMB)==0:
                st=' '.join(map(str,CRETA1))
                if y==len(MEMB):
                    response.writelines(f"{st}\n")
                else:
                    response.writelines(f"{st} -\n")
                print(CRETA1)
                print(st)
                CRETA1=[]
        else:
            if y==len(MEMB):
                st=' '.join(map(str,MEMB))
                response.writelines(f"{st}\n")
        y=y+1

    response.writelines(f"FU 490000 MEMB -\n")
    CRETA1=[]
    y=1
    while y<=len(MEMB):
        if len(MEMB)>=15:
            CRETA1.append(MEMB[y-1])
            if y%15==0 or y%len(MEMB)==0:
                st=' '.join(map(str,CRETA1))
                if y==len(MEMB):
                    response.writelines(f"{st}\n")
                else:
                    response.writelines(f"{st} -\n")
                print(CRETA1)
                print(st)
                CRETA1=[]
        else:
            if y==len(MEMB):
                st=' '.join(map(str,MEMB))
                response.writelines(f"{st}\n")
        y=y+1

    response.writelines(f"BEAM 1 MEMB -\n")
    CRETA1=[]
    y=1
    while y<=len(MEMB):
        if len(MEMB)>=15:
            CRETA1.append(MEMB[y-1])
            if y%15==0 or y%len(MEMB)==0:
                st=' '.join(map(str,CRETA1))
                if y==len(MEMB):
                    response.writelines(f"{st}\n")
                else:
                    response.writelines(f"{st} -\n")
                print(CRETA1)
                print(st)
                CRETA1=[]
        else:
            if y==len(MEMB):
                st=' '.join(map(str,MEMB))
                response.writelines(f"{st}\n")
        y=y+1

    response.writelines(f"STP 2 MEMB -\n")
    CRETA1=[]
    y=1
    while y<=len(MEMB):
        if len(MEMB)>=15:
            CRETA1.append(MEMB[y-1])
            if y%15==0 or y%len(MEMB)==0:
                st=' '.join(map(str,CRETA1))
                if y==len(MEMB):
                    response.writelines(f"{st}\n")
                else:
                    response.writelines(f"{st} -\n")
                print(CRETA1)
                print(st)
                CRETA1=[]
        else:
            if y==len(MEMB):
                st=' '.join(map(str,MEMB))
                response.writelines(f"{st}\n")
        y=y+1

    response.writelines(f"MAIN 180 MEMB -\n")
    CRETA1=[]
    y=1
    while y<=len(MEMB):
        if len(MEMB)>=15:
            CRETA1.append(MEMB[y-1])
            if y%15==0 or y%len(MEMB)==0:
                st=' '.join(map(str,CRETA1))
                if y==len(MEMB):
                    response.writelines(f"{st}\n")
                else:
                    response.writelines(f"{st} -\n")
                print(CRETA1)
                print(st)
                CRETA1=[]
        else:
            if y==len(MEMB):
                st=' '.join(map(str,MEMB))
                response.writelines(f"{st}\n")
        y=y+1


    i=((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(len(Only_WC_Nodes)*2)+(len(BR_Nodes)*(len(SW1)-1))
    CRET=[]
    while i<(((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(len(Only_WC_Nodes)*2)+(len(BR_Nodes)*(len(SW1)-1))+(len(Braced_bay_location)*(len(BR_Nodes)-1)*2)+(len(Braced_bay_location)*2*2)):
        CRET.append(i+1)
        i=i+1
    print(CRET)
    st=' '.join(map(str,CRET))
    print(st)

    response.writelines(f"FYLD 250000 MEMB -\n")
    CRETA1=[]
    y=1
    while y<=len(CRET):
        if len(CRET)>=15:
            CRETA1.append(CRET[y-1])
            if y%15==0 or y%len(CRET)==0:
                st=' '.join(map(str,CRETA1))
                if y==len(CRET):
                    response.writelines(f"{st}\n")
                else:
                    response.writelines(f"{st} -\n")
                print(CRETA1)
                print(st)
                CRETA1=[]
        else:
            if y==len(CRET):
                st=' '.join(map(str,CRET))
                response.writelines(f"{st}\n")
        y=y+1

    response.writelines(f"FU 410000 MEMB -\n")
    CRETA1=[]
    y=1
    while y<=len(CRET):
        if len(CRET)>=15:
            CRETA1.append(CRET[y-1])
            if y%15==0 or y%len(CRET)==0:
                st=' '.join(map(str,CRETA1))
                if y==len(CRET):
                    response.writelines(f"{st}\n")
                else:
                    response.writelines(f"{st} -\n")
                print(CRETA1)
                print(st)
                CRETA1=[]
        else:
            if y==len(CRET):
                st=' '.join(map(str,CRET))
                response.writelines(f"{st}\n")
        y=y+1

    response.writelines(f"STP 1 MEMB -\n")
    CRETA1=[]
    y=1
    while y<=len(CRET):
        if len(CRET)>=15:
            CRETA1.append(CRET[y-1])
            if y%15==0 or y%len(CRET)==0:
                st=' '.join(map(str,CRETA1))
                if y==len(CRET):
                    response.writelines(f"{st}\n")
                else:
                    response.writelines(f"{st} -\n")
                print(CRETA1)
                print(st)
                CRETA1=[]
        else:
            if y==len(CRET):
                st=' '.join(map(str,CRET))
                response.writelines(f"{st}\n")
        y=y+1

    response.writelines(f"MAIN 250 MEMB -\n")
    CRETA1=[]
    y=1
    while y<=len(CRET):
        if len(CRET)>=15:
            CRETA1.append(CRET[y-1])
            if y%15==0 or y%len(CRET)==0:
                st=' '.join(map(str,CRETA1))
                if y==len(CRET):
                    response.writelines(f"{st}\n")
                else:
                    response.writelines(f"{st} -\n")
                print(CRETA1)
                print(st)
                CRETA1=[]
        else:
            if y==len(CRET):
                st=' '.join(map(str,CRET))
                response.writelines(f"{st}\n")
        y=y+1



    x=0
    CRET=[]
    CRET1=[]
    CRET2=[]
    CRET3=[]
    while x<(len(SW1)):
        i=0
        while i<=(len(EWX)-1):
            if i==0:
                CRET.append(1+((len(EWX)-1)*x))
            if i>0 and i<((len(EWX)-1)/2):
                CRET1.append((i+1)+((len(EWX)-1)*x))
            if i>=((len(EWX)-1)/2) and i<(len(EWX)-2):
                CRET2.append((i+1)+((len(EWX)-1)*x))
            if i==len(EWX)-1:
                CRET3.append((len(EWX)-1)+((len(EWX)-1)*x))
            i=i+1
        print(CRET)
        st=' '.join(map(str,CRET))
        print(CRET1)
        st1=' '.join(map(str,CRET1))
        print(CRET2)
        st2=' '.join(map(str,CRET2))
        print(CRET3)
        st3=' '.join(map(str,CRET3))
        print(st)
        x=x+1
    response.writelines(f"LZ {Height} MEMB -\n")
    CRETA1=[]
    y=1
    while y<=len(CRET):
        if len(CRET)>=15:
            CRETA1.append(CRET[y-1])
            if y%15==0 or y%len(CRET)==0:
                st=' '.join(map(str,CRETA1))
                if y==len(CRET):
                    response.writelines(f"{st}\n")
                else:
                    response.writelines(f"{st} -\n")
                print(CRETA1)
                print(st)
                CRETA1=[]
        else:
            if y==len(CRET):
                st=' '.join(map(str,CRET))
                response.writelines(f"{st}\n")
        y=y+1

    if NSC_SUPPORT[0]=='PINNED':
        response.writelines(f"KZ 2 MEMB -\n")
    else:
        response.writelines(f"KZ 1.2 MEMB -\n")

    CRETA1=[]
    y=1
    while y<=len(CRET):
        if len(CRET)>=15:
            CRETA1.append(CRET[y-1])
            if y%15==0 or y%len(CRET)==0:
                st=' '.join(map(str,CRETA1))
                if y==len(CRET):
                    response.writelines(f"{st}\n")
                else:
                    response.writelines(f"{st} -\n")
                print(CRETA1)
                print(st)
                CRETA1=[]
        else:
            if y==len(CRET):
                st=' '.join(map(str,CRET))
                response.writelines(f"{st}\n")
        y=y+1

    response.writelines(f"LY 1.5 MEMB -\n")
    CRETA1=[]
    y=1
    while y<=len(CRET):
        if len(CRET)>=15:
            CRETA1.append(CRET[y-1])
            if y%15==0 or y%len(CRET)==0:
                st=' '.join(map(str,CRETA1))
                if y==len(CRET):
                    response.writelines(f"{st}\n")
                else:
                    response.writelines(f"{st} -\n")
                print(CRETA1)
                print(st)
                CRETA1=[]
        else:
            if y==len(CRET):
                st=' '.join(map(str,CRET))
                response.writelines(f"{st}\n")
        y=y+1

    response.writelines(f"LX 1.5 MEMB -\n")
    CRETA1=[]
    y=1
    while y<=len(CRET):
        if len(CRET)>=15:
            CRETA1.append(CRET[y-1])
            if y%15==0 or y%len(CRET)==0:
                st=' '.join(map(str,CRETA1))
                if y==len(CRET):
                    response.writelines(f"{st}\n")
                else:
                    response.writelines(f"{st} -\n")
                print(CRETA1)
                print(st)
                CRETA1=[]
        else:
            if y==len(CRET):
                st=' '.join(map(str,CRET))
                response.writelines(f"{st}\n")
        y=y+1


    Ibay=[]
    nodes=0
    while nodes<=len(ICO_Nodes):
        Ibay_1=[]
        y=0
        while y<(len(SW1)):
            x=ICO_nodes_for_Rafter_Lz[nodes]
            while x<ICO_nodes_for_Rafter_Lz[nodes+1]:
                Ibay_1.append(x+(y*(len(EWY)-1)))
                x=x+1
            y=y+1
        print(Ibay_1)
        Ibay.append(Ibay_1)

        nodes = nodes + 1


    x=0
    while x<len(Ibay):
        response.writelines(f"LZ {round((ICO_for_rafter_Lz[x]**2+(ICO_for_rafter_Lz[x]*Slope)**2)**0.5,3)} MEMB -\n")
        CRETA1=[]
        y=1
        while y<=len(Ibay[x]):
            if len(Ibay[x])>=15:
                CRETA1.append(Ibay[x][y-1])
                if y%15==0 or y%len(Ibay[x])==0:
                    st1=' '.join(map(str,CRETA1))
                    if y==len(Ibay[x]):
                        response.writelines(f"{st1}\n")
                    else:
                        response.writelines(f"{st1} -\n")
                    print(CRETA1)
                    print(st1)
                    CRETA1=[]
            else:
                if y==len(Ibay[x]):
                    st1=' '.join(map(str,Ibay[x]))
                    response.writelines(f"{st1}\n")
            y=y+1
        x=x+1

    x=0
    while x<len(Ibay):
        response.writelines(f"LY 1.5 MEMB -\n")
        CRETA1=[]
        y=1
        while y<=len(Ibay[x]):
            if len(Ibay[x])>=15:
                CRETA1.append(Ibay[x][y-1])
                if y%15==0 or y%len(Ibay[x])==0:
                    st1=' '.join(map(str,CRETA1))
                    if y==len(Ibay[x]):
                        response.writelines(f"{st1}\n")
                    else:
                        response.writelines(f"{st1} -\n")
                    print(CRETA1)
                    print(st1)
                    CRETA1=[]
            else:
                if y==len(Ibay[x]):
                    st1=' '.join(map(str,Ibay[x]))
                    response.writelines(f"{st1}\n")
            y=y+1
        x=x+1

    x=0
    while x<len(Ibay):
        response.writelines(f"LX 1.5 MEMB -\n")
        CRETA1=[]
        y=1
        while y<=len(Ibay[x]):
            if len(Ibay[x])>=15:
                CRETA1.append(Ibay[x][y-1])
                if y%15==0 or y%len(Ibay[x])==0:
                    st1=' '.join(map(str,CRETA1))
                    if y==len(Ibay[x]):
                        response.writelines(f"{st1}\n")
                    else:
                        response.writelines(f"{st1} -\n")
                    print(CRETA1)
                    print(st1)
                    CRETA1=[]
            else:
                if y==len(Ibay[x]):
                    st1=' '.join(map(str,Ibay[x]))
                    response.writelines(f"{st1}\n")
            y=y+1
        x=x+1


    response.writelines(f"LZ {FS_Height} MEMB -\n")
    CRETA1=[]
    y=1
    while y<=len(CRET3):
        if len(CRET3)>=15:
            CRETA1.append(CRET3[y-1])
            if y%15==0 or y%len(CRET3)==0:
                st3=' '.join(map(str,CRETA1))
                if y==len(CRET3):
                    response.writelines(f"{st3}\n")
                else:
                    response.writelines(f"{st3} -\n")
                print(CRETA1)
                print(st3)
                CRETA1=[]
        else:
            if y==len(CRET3):
                st3=' '.join(map(str,CRET3))
                response.writelines(f"{st3}\n")
        y=y+1

    response.writelines(f"KZ 2 MEMB -\n")
    CRETA1=[]
    y=1
    while y<=len(CRET3):
        if len(CRET3)>=15:
            CRETA1.append(CRET3[y-1])
            if y%15==0 or y%len(CRET3)==0:
                st3=' '.join(map(str,CRETA1))
                if y==len(CRET3):
                    response.writelines(f"{st3}\n")
                else:
                    response.writelines(f"{st3} -\n")
                print(CRETA1)
                print(st3)
                CRETA1=[]
        else:
            if y==len(CRET3):
                st3=' '.join(map(str,CRET3))
                response.writelines(f"{st3}\n")
        y=y+1

    response.writelines(f"LY 1.5 MEMB -\n")
    CRETA1=[]
    y=1
    while y<=len(CRET3):
        if len(CRET3)>=15:
            CRETA1.append(CRET3[y-1])
            if y%15==0 or y%len(CRET3)==0:
                st3=' '.join(map(str,CRETA1))
                if y==len(CRET3):
                    response.writelines(f"{st3}\n")
                else:
                    response.writelines(f"{st3} -\n")
                print(CRETA1)
                print(st3)
                CRETA1=[]
        else:
            if y==len(CRET3):
                st3=' '.join(map(str,CRET3))
                response.writelines(f"{st3}\n")
        y=y+1

    response.writelines(f"LX 1.5 MEMB -\n")
    CRETA1=[]
    y=1
    while y<=len(CRET3):
        if len(CRET3)>=15:
            CRETA1.append(CRET3[y-1])
            if y%15==0 or y%len(CRET3)==0:
                st3=' '.join(map(str,CRETA1))
                if y==len(CRET3):
                    response.writelines(f"{st3}\n")
                else:
                    response.writelines(f"{st3} -\n")
                print(CRETA1)
                print(st3)
                CRETA1=[]
        else:
            if y==len(CRET3):
                st3=' '.join(map(str,CRET3))
                response.writelines(f"{st3}\n")
        y=y+1


    x=0
    while x<len(EW_for_WC_Lz):
        response.writelines(f"LZ {(EW_for_WC_Lz[x]*Slope)+Height} MEMB -\n")
        CRETA1=[]
        CRETA1.append(((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+1+x)
        CRETA1.append(((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+1+x+len(EW_for_WC_Lz))
        st1=' '.join(map(str,CRETA1))
        response.writelines(f"{st1}\n")
        x=x+1

    x=0
    while x<len(EW_for_WC_Lz):
        response.writelines(f"LY 1.5 MEMB -\n")
        CRETA1=[]
        CRETA1.append(((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+1+x)
        CRETA1.append(((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+1+x+len(EW_for_WC_Lz))
        st1=' '.join(map(str,CRETA1))
        response.writelines(f"{st1}\n")
        x=x+1

    x=0
    while x<len(EW_for_WC_Lz):
        response.writelines(f"LX 1.5 MEMB -\n")
        CRETA1=[]
        CRETA1.append(((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+1+x)
        CRETA1.append(((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+1+x+len(EW_for_WC_Lz))
        st1=' '.join(map(str,CRETA1))
        response.writelines(f"{st1}\n")
        x=x+1

    MEMB=[]
    i=0
    while i<=(Memb_total-1):
        MEMB.append(i+1)
        i=i+1
    print(MEMB)
    st=' '.join(map(str,MEMB))
    print(st)
    response.writelines(f"CHECK CODE MEMB -\n")
    CRETA1=[]
    y=1
    while y<=len(MEMB):
        if len(MEMB)>=15:
            CRETA1.append(MEMB[y-1])
            if y%15==0 or y%len(MEMB)==0:
                st=' '.join(map(str,CRETA1))
                if y==len(MEMB):
                    response.writelines(f"{st}\n")
                else:
                    response.writelines(f"{st} -\n")
                print(CRETA1)
                print(st)
                CRETA1=[]
        else:
            if y==len(MEMB):
                st=' '.join(map(str,MEMB))
                response.writelines(f"{st}\n")
        y=y+1

    response.writelines(f"STEEL MEMBER TAKE OFF LIST -\n")
    CRETA1=[]
    y=1
    while y<=len(MEMB):
        if len(MEMB)>=15:
            CRETA1.append(MEMB[y-1])
            if y%15==0 or y%len(MEMB)==0:
                st=' '.join(map(str,CRETA1))
                if y==len(MEMB):
                    response.writelines(f"{st}\n")
                else:
                    response.writelines(f"{st} -\n")
                print(CRETA1)
                print(st)
                CRETA1=[]
        else:
            if y==len(MEMB):
                st=' '.join(map(str,MEMB))
                response.writelines(f"{st}\n")
        y=y+1

    i=((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(len(Only_WC_Nodes)*2)+(len(BR_Nodes)*(len(SW1)-1))
    CRET=[]
    while i<(((len(EWX)-1)*len(SW1))+(len(ICO)*len(SW1))+(len(Only_WC_Nodes)*2)+(len(BR_Nodes)*(len(SW1)-1))+(len(Braced_bay_location)*(len(BR_Nodes)-1)*2)+(len(Braced_bay_location)*2*2)):
        CRET.append(i+1)
        i=i+1
    print(CRET)
    st=' '.join(map(str,CRET))
    print(st)
    response.writelines(f"CHECK CODE MEMB -\n")
    CRETA1=[]
    y=1
    while y<=len(CRET):
        if len(CRET)>=15:
            CRETA1.append(CRET[y-1])
            if y%15==0 or y%len(CRET)==0:
                st=' '.join(map(str,CRETA1))
                if y==len(CRET):
                    response.writelines(f"{st}\n")
                else:
                    response.writelines(f"{st} -\n")
                print(CRETA1)
                print(st)
                CRETA1=[]
        else:
            if y==len(CRET):
                st=' '.join(map(str,CRET))
                response.writelines(f"{st}\n")
        y=y+1

    response.writelines(f"STEEL MEMBER TAKE OFF LIST -\n")
    CRETA1=[]
    y=1
    while y<=len(CRET):
        if len(CRET)>=15:
            CRETA1.append(CRET[y-1])
            if y%15==0 or y%len(CRET)==0:
                st=' '.join(map(str,CRETA1))
                if y==len(CRET):
                    response.writelines(f"{st}\n")
                else:
                    response.writelines(f"{st} -\n")
                print(CRETA1)
                print(st)
                CRETA1=[]
        else:
            if y==len(CRET):
                st=' '.join(map(str,CRET))
                response.writelines(f"{st}\n")
        y=y+1



    
    # END
    response.writelines("FINISH")

    return response
    
