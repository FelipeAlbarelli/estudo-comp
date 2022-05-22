.section .text

main:

    addi t0,zero,5
    addi t1,zero,5

    add a0,t0,t1

    addi t0,zero,1

    ecall

    jr ra