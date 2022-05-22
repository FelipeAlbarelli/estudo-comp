.section .text


main:

    addi t0,zero,25
    addi t1,zero,3

sum:

    add a0,a0,t0
    addi t2,t2,1

    bne t2,t1,sum

    addi t0,zero,1 #print
    ecall
    jr ra