# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 09:18:19 2021

@author: thibaut

Inversions: num of (i, j) in A where i<j and A[i]>A[j]"""


def sortAndCountInv(A):
    if len(A)<=1:
        return A, 0
    else:
        mid = len(A)//2
        C = A[:mid]
        D = A[mid:]
# Recursively call sortAndCountInv on B and C
        C, leftInv = sortAndCountInv(C)
        D, rightInv = sortAndCountInv(D)
        B, splitInv = mergeAndCountsplitInv(C, D)
        return B, leftInv + rightInv + splitInv
    
def mergeAndCountsplitInv(C, D):
    i=0
    j=0
    k=0
    splitInv = 0
    B = []
    while i < len(C) and j < len(D):
        if C[i] < D[j]:
           B.append(C[i]) 
           i+=1
        else:
            B.append(D[j])
            j+=1
# B is sorted then if D[j] is less than C[i] it'll be less than the len(C)-i elements
            splitInv = splitInv +(len(C) - i) 
        k+=1
    while i < len(C):
        B.append(C[i])
        i+=1
        k+=1
    while j < len(D):
        B.append(D[j])
        j+=1
        k+=1
    return B, splitInv
# test      
# A=[1, 20, 6, 4, 5]        
# B, n = sortAndCountInv(A)
# print( B, n)
#output 
#[1, 4, 5, 6, 20] 5
arr=[]
with open("inversion.txt", "r") as fichiertext:
    for ligne in fichiertext:
        A=ligne.split()
        a =int (A[0])
        arr.append(a)        
        
B, n = sortAndCountInv(arr)
print('number of inversions', n)
#result:2407905288
