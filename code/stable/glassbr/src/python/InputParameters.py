## \file InputParameters.py
# \author Nikitha Krithnan and W. Spencer Smith
# \brief Provides the structure for holding input values, the function for reading inputs, the function for calculating derived values, and the function for checking the physical constraints and software constraints on the input
# \note Generated by Drasil v0.1-alpha

import math

## \brief Structure for holding the input values and derived values
class InputParameters:
    ## \brief Initializes input object by reading inputs, calculating derived values, and checking physical constraints and software constraints on the input
    # \param filename name of the input file
    def __init__(self, filename):
        outfile = open("log.txt", "a")
        print("function InputParameters called with inputs: {", file=outfile)
        print("  filename = ", end="", file=outfile)
        print(filename, file=outfile)
        print("  }", file=outfile)
        outfile.close()
        
        self.get_input(filename)
        self.derived_values()
        self.input_constraints()
    
    ## \brief Reads input from a file with the given file name
    # \param filename name of the input file
    def get_input(self, filename):
        outfile = open("log.txt", "a")
        print("function get_input called with inputs: {", file=outfile)
        print("  filename = ", end="", file=outfile)
        print(filename, file=outfile)
        print("  }", file=outfile)
        outfile.close()
        
        infile = open(filename, "r")
        infile.readline()
        self.a = float(infile.readline())
        outfile = open("log.txt", "a")
        print("var 'self.a' assigned ", end="", file=outfile)
        print(self.a, end="", file=outfile)
        print(" in module InputParameters", file=outfile)
        outfile.close()
        infile.readline()
        self.b = float(infile.readline())
        outfile = open("log.txt", "a")
        print("var 'self.b' assigned ", end="", file=outfile)
        print(self.b, end="", file=outfile)
        print(" in module InputParameters", file=outfile)
        outfile.close()
        infile.readline()
        self.w = float(infile.readline())
        outfile = open("log.txt", "a")
        print("var 'self.w' assigned ", end="", file=outfile)
        print(self.w, end="", file=outfile)
        print(" in module InputParameters", file=outfile)
        outfile.close()
        infile.readline()
        self.P_btol = float(infile.readline())
        outfile = open("log.txt", "a")
        print("var 'self.P_btol' assigned ", end="", file=outfile)
        print(self.P_btol, end="", file=outfile)
        print(" in module InputParameters", file=outfile)
        outfile.close()
        infile.readline()
        self.TNT = float(infile.readline())
        outfile = open("log.txt", "a")
        print("var 'self.TNT' assigned ", end="", file=outfile)
        print(self.TNT, end="", file=outfile)
        print(" in module InputParameters", file=outfile)
        outfile.close()
        infile.readline()
        self.g = infile.readline().rstrip()
        outfile = open("log.txt", "a")
        print("var 'self.g' assigned ", end="", file=outfile)
        print(self.g, end="", file=outfile)
        print(" in module InputParameters", file=outfile)
        outfile.close()
        infile.readline()
        self.t = float(infile.readline())
        outfile = open("log.txt", "a")
        print("var 'self.t' assigned ", end="", file=outfile)
        print(self.t, end="", file=outfile)
        print(" in module InputParameters", file=outfile)
        outfile.close()
        infile.readline()
        self.SD_x = float(infile.readline())
        outfile = open("log.txt", "a")
        print("var 'self.SD_x' assigned ", end="", file=outfile)
        print(self.SD_x, end="", file=outfile)
        print(" in module InputParameters", file=outfile)
        outfile.close()
        infile.readline()
        self.SD_y = float(infile.readline())
        outfile = open("log.txt", "a")
        print("var 'self.SD_y' assigned ", end="", file=outfile)
        print(self.SD_y, end="", file=outfile)
        print(" in module InputParameters", file=outfile)
        outfile.close()
        infile.readline()
        self.SD_z = float(infile.readline())
        outfile = open("log.txt", "a")
        print("var 'self.SD_z' assigned ", end="", file=outfile)
        print(self.SD_z, end="", file=outfile)
        print(" in module InputParameters", file=outfile)
        outfile.close()
        infile.close()
    
    ## \brief Calculates values that can be immediately derived from the inputs
    def derived_values(self):
        outfile = open("log.txt", "a")
        print("function derived_values called with inputs: {", file=outfile)
        print("  }", file=outfile)
        outfile.close()
        
        self.h = 1.0 / 1000.0 * (2.16 if self.t == 2.5 else 2.59 if self.t == 2.7 else 2.92 if self.t == 3.0 else 3.78 if self.t == 4.0 else 4.57 if self.t == 5.0 else 5.56 if self.t == 6.0 else 7.42 if self.t == 8.0 else 9.02 if self.t == 10.0 else 11.91 if self.t == 12.0 else 15.09 if self.t == 16.0 else 18.26 if self.t == 19.0 else 21.44)
        outfile = open("log.txt", "a")
        print("var 'self.h' assigned ", end="", file=outfile)
        print(self.h, end="", file=outfile)
        print(" in module InputParameters", file=outfile)
        outfile.close()
        
        self.LDF = (3.0 / 60.0) ** (7.0 / 16.0)
        outfile = open("log.txt", "a")
        print("var 'self.LDF' assigned ", end="", file=outfile)
        print(self.LDF, end="", file=outfile)
        print(" in module InputParameters", file=outfile)
        outfile.close()
        
        if self.g == "AN":
            self.GTF = 1
            outfile = open("log.txt", "a")
            print("var 'self.GTF' assigned ", end="", file=outfile)
            print(self.GTF, end="", file=outfile)
            print(" in module InputParameters", file=outfile)
            outfile.close()
        elif self.g == "FT":
            self.GTF = 4
            outfile = open("log.txt", "a")
            print("var 'self.GTF' assigned ", end="", file=outfile)
            print(self.GTF, end="", file=outfile)
            print(" in module InputParameters", file=outfile)
            outfile.close()
        elif self.g == "HS":
            self.GTF = 2
            outfile = open("log.txt", "a")
            print("var 'self.GTF' assigned ", end="", file=outfile)
            print(self.GTF, end="", file=outfile)
            print(" in module InputParameters", file=outfile)
            outfile.close()
        else:
            raise Exception("Undefined case encountered in function GTF")
        
        self.SD = math.sqrt(self.SD_x ** 2.0 + self.SD_y ** 2.0 + self.SD_z ** 2.0)
        outfile = open("log.txt", "a")
        print("var 'self.SD' assigned ", end="", file=outfile)
        print(self.SD, end="", file=outfile)
        print(" in module InputParameters", file=outfile)
        outfile.close()
        
        self.AR = self.a / self.b
        outfile = open("log.txt", "a")
        print("var 'self.AR' assigned ", end="", file=outfile)
        print(self.AR, end="", file=outfile)
        print(" in module InputParameters", file=outfile)
        outfile.close()
        
        self.w_TNT = self.w * self.TNT
        outfile = open("log.txt", "a")
        print("var 'self.w_TNT' assigned ", end="", file=outfile)
        print(self.w_TNT, end="", file=outfile)
        print(" in module InputParameters", file=outfile)
        outfile.close()
    
    ## \brief Verifies that input values satisfy the physical constraints and software constraints
    def input_constraints(self):
        outfile = open("log.txt", "a")
        print("function input_constraints called with inputs: {", file=outfile)
        print("  }", file=outfile)
        outfile.close()
        
        if not(0.1 <= self.a and self.a <= 5.0):
            print("a has value ", end="")
            print(self.a, end="")
            print(", but is expected to be ", end="")
            print("between ", end="")
            print(0.1, end="")
            print(" (d_min)", end="")
            print(" and ", end="")
            print(5.0, end="")
            print(" (d_max)", end="")
            print(".")
            raise Exception("InputError")
        if not(0.1 <= self.b and self.b <= 5.0):
            print("b has value ", end="")
            print(self.b, end="")
            print(", but is expected to be ", end="")
            print("between ", end="")
            print(0.1, end="")
            print(" (d_min)", end="")
            print(" and ", end="")
            print(5.0, end="")
            print(" (d_max)", end="")
            print(".")
            raise Exception("InputError")
        if not(4.5 <= self.w and self.w <= 910.0):
            print("w has value ", end="")
            print(self.w, end="")
            print(", but is expected to be ", end="")
            print("between ", end="")
            print(4.5, end="")
            print(" (w_min)", end="")
            print(" and ", end="")
            print(910.0, end="")
            print(" (w_max)", end="")
            print(".")
            raise Exception("InputError")
        set_g = {"AN", "FT", "HS"}
        if not(self.g in set_g):
            print("g has value ", end="")
            print(self.g, end="")
            print(", but is expected to be ", end="")
            print("an element of the set ", end="")
            print("{ ", end="")
            for set_i1 in set_g:
                print(set_i1, end="")
                print(" ", end="")
            print("}", end="")
            print(".")
            raise Exception("InputError")
        set_t = {2.5, 2.7, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0, 16.0, 19.0, 22.0}
        if not(self.t in set_t):
            print("t has value ", end="")
            print(self.t, end="")
            print(", but is expected to be ", end="")
            print("an element of the set ", end="")
            print("{ ", end="")
            for set_i1 in set_t:
                print(set_i1, end="")
                print(" ", end="")
            print("}", end="")
            print(".")
            raise Exception("InputError")
        if not(6.0 <= self.SD and self.SD <= 130.0):
            print("SD has value ", end="")
            print(self.SD, end="")
            print(", but is expected to be ", end="")
            print("between ", end="")
            print(6.0, end="")
            print(" (SD_min)", end="")
            print(" and ", end="")
            print(130.0, end="")
            print(" (SD_max)", end="")
            print(".")
            raise Exception("InputError")
        if not(self.AR <= 5.0):
            print("AR has value ", end="")
            print(self.AR, end="")
            print(", but is expected to be ", end="")
            print("below ", end="")
            print(5.0, end="")
            print(" (AR_max)", end="")
            print(".")
            raise Exception("InputError")
        
        if not(self.a > 0.0):
            print("a has value ", end="")
            print(self.a, end="")
            print(", but is expected to be ", end="")
            print("above ", end="")
            print(0.0, end="")
            print(".")
            raise Exception("InputError")
        if not(self.a >= self.b):
            print("a has value ", end="")
            print(self.a, end="")
            print(", but is expected to be ", end="")
            print("above ", end="")
            print(self.b, end="")
            print(" (b)", end="")
            print(".")
            raise Exception("InputError")
        if not(0.0 < self.b and self.b <= self.a):
            print("b has value ", end="")
            print(self.b, end="")
            print(", but is expected to be ", end="")
            print("between ", end="")
            print(0.0, end="")
            print(" and ", end="")
            print(self.a, end="")
            print(" (a)", end="")
            print(".")
            raise Exception("InputError")
        if not(self.w > 0.0):
            print("w has value ", end="")
            print(self.w, end="")
            print(", but is expected to be ", end="")
            print("above ", end="")
            print(0.0, end="")
            print(".")
            raise Exception("InputError")
        if not(0.0 <= self.P_btol and self.P_btol <= 1.0):
            print("P_btol has value ", end="")
            print(self.P_btol, end="")
            print(", but is expected to be ", end="")
            print("between ", end="")
            print(0.0, end="")
            print(" and ", end="")
            print(1.0, end="")
            print(".")
            raise Exception("InputError")
        if not(self.TNT > 0.0):
            print("TNT has value ", end="")
            print(self.TNT, end="")
            print(", but is expected to be ", end="")
            print("above ", end="")
            print(0.0, end="")
            print(".")
            raise Exception("InputError")
        if not(self.SD > 0.0):
            print("SD has value ", end="")
            print(self.SD, end="")
            print(", but is expected to be ", end="")
            print("above ", end="")
            print(0.0, end="")
            print(".")
            raise Exception("InputError")
        if not(self.AR >= 1.0):
            print("AR has value ", end="")
            print(self.AR, end="")
            print(", but is expected to be ", end="")
            print("above ", end="")
            print(1.0, end="")
            print(".")
            raise Exception("InputError")
