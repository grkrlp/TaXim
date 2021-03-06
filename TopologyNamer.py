'''
    Taxim: A Toolchain for Automated and Configurable Simulation for Embedded Multiprocessor Design 
    Copyright (C) 2016  Deniz Candas (dnzcandas@gmail.com), Gorker Alp Malazgirt (gorkeralp@gmail.com), Arda Yurdakul (yurdakul@boun.edu.tr)

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
'''



f = open('TopologyList', 'a')
def regularMakerNoCheck(f,a,b,c,d):
    for i in range(a):
        for j in range(b):
            for k in range(c):
                f.write(str(i+1) + "C_" + str(j+1) + "L1_" + str(k+1) + "L2\n")
                for l in range(d):
                    f.write(str(i+1) + "C_" + str(j+1) + "L1_" + str(k+1) + "L2_" + str(l+1) + "L3\n")
def semiHybridMakerNoCheck(f,a,b,c,d,e):
    for i in range(a):
        for j in range(b):
            for k in range(c):
                for m in range(d):
                    f.write(str(i+1) + "C_" + str(j+1) + "DL1_" + str(k+1) + "IL1_" + str(m+1) + "L2\n")
                    for l in range(e):
                        f.write(str(i+1) + "C_" + str(j+1) + "DL1_" + str(k+1) + "IL1_" + str(m+1) + "L2_" + str(l+1) + "L3\n")                
def hybridMakerNoCheck(f,a,b,c,d,e,g):
    for i in range(a):
        for j in range(b):
            for k in range(c):
                for m in range(d):
                    for n in range(g):
                        f.write(str(i+1) + "C_" + str(j+1) + "DL1_" + str(k+1) + "IL1_" + str(m+1) + "DL2_" + str(n+1) + "IL2\n")
                        for l in range(e):
                            f.write(str(i+1) + "C_" + str(j+1) + "DL1_" + str(k+1) + "IL1_" + str(m+1) + "DL2_" + str(n+1) + "IL2_" + str(l+1) + "L3\n")                  
def secondLevelMakerNoCheck(f,a,b,c,d,e):
    for i in range(a):
        for j in range(b):
            for k in range(c):
                for m in range(d):
                    f.write(str(i+1) + "C_" + str(j+1) + "DL1_" + str(k+1) + "IL1_" + str(m+1) + "DL2_BP\n")
                    for l in range(e):
                        f.write(str(i+1) + "C_" + str(j+1) + "DL1_" + str(k+1) + "IL1_" + str(m+1) + "DL2_" + str(l+1) + "L3_BP\n")                
def thirdLevelMakerNoCheck(f,a,b,c,d,e,g):
    for i in range(a):
        for j in range(b):
            for k in range(c):
                for m in range(d):
                    for n in range(g):
                        f.write(str(i+1) + "C_" + str(j+1) + "DL1_" + str(k+1) + "IL1_" + str(m+1) + "DL2_" + str(n+1) + "IL2_BP\n")
                        for l in range(e):
                            f.write(str(i+1) + "C_" + str(j+1) + "DL1_" + str(k+1) + "IL1_" + str(m+1) + "DL2_" + str(n+1) + "IL2_" + str(l+1) + "L3_BP\n")
                            
def regularMaker(f,a,b,c,d):
    for i in range(a):
        for j in range(b):
            for k in range(c):
                if i >= j >= k:
                    f.write(str(i+1) + "C_" + str(j+1) + "L1_" + str(k+1) + "L2\n")
                    for l in range(d):
                        if i >= j >= k >= l:
                            f.write(str(i+1) + "C_" + str(j+1) + "L1_" + str(k+1) + "L2_" + str(l+1) + "L3\n")
def semiHybridMaker(f,a,b,c,d,e):
    for i in range(a):
        for j in range(b):
            for k in range(c):
                for m in range(d):
                    if i >= j >= m and i >= k >= m:
                        f.write(str(i+1) + "C_" + str(j+1) + "DL1_" + str(k+1) + "IL1_" + str(m+1) + "L2\n")
                        for l in range(e):
                            if i >= j >= m >= l and i >= k >= m >= l:
                                f.write(str(i+1) + "C_" + str(j+1) + "DL1_" + str(k+1) + "IL1_" + str(m+1) + "L2_" + str(l+1) + "L3\n")                
def hybridMaker(f,a,b,c,d,e,g):
    for i in range(a):
        for j in range(b):
            for k in range(c):
                for m in range(d):
                    for n in range(g):
                        if i >= j >= m and i >= k >= n:
                            f.write(str(i+1) + "C_" + str(j+1) + "DL1_" + str(k+1) + "IL1_" + str(m+1) + "DL2_" + str(n+1) + "IL2\n")
                            for l in range(e):
                                if i >= j >= m >= l and i >= k >= n >= l:
                                    f.write(str(i+1) + "C_" + str(j+1) + "DL1_" + str(k+1) + "IL1_" + str(m+1) + "DL2_" + str(n+1) + "IL2_" + str(l+1) + "L3\n")                  
def secondLevelMaker(f,a,b,c,d,e):
    for i in range(a):
        for j in range(b):
            for k in range(c):
                for m in range(d):
                    if i >= j >= m and i >= k:
                        f.write(str(i+1) + "C_" + str(j+1) + "DL1_" + str(k+1) + "IL1_" + str(m+1) + "DL2_BP\n")
                    for l in range(e):
                        if i >= j >= m >= l and i >= k >= l:
                            f.write(str(i+1) + "C_" + str(j+1) + "DL1_" + str(k+1) + "IL1_" + str(m+1) + "DL2_" + str(l+1) + "L3_BP\n")                
def thirdLevelMaker(f,a,b,c,d,e,g):
    for i in range(a):
        for j in range(b):
            for k in range(c):
                for m in range(d):
                    for n in range(g):
                        for l in range(e):
                            if i >= j >= m >= l and i >= k >= n >= l:
                                f.write(str(i+1) + "C_" + str(j+1) + "DL1_" + str(k+1) + "IL1_" + str(m+1) + "DL2_" + str(n+1) + "IL2_" + str(l+1) + "L3_BP\n")                                                   


regularMaker(f,5,5,5,5)
semiHybridMaker(f,5,5,5,5,5)
hybridMaker(f,5,5,5,5,5,5)
secondLevelMaker(f,5,5,5,5,5)
thirdLevelMaker(f,5,5,5,5,5,5)

f.close()
