.section .text


main:

    addi t0,zero,4
    ecall
    add t1,zero,a0
    ecall
    add t2,zero,a0
    add a0,zero,zero

sum:

    add a0,a0,t1
    addi t3,t3,1

    bne t2,t3,sum

    addi t0,zero,1 #print
    ecall
    jr ra