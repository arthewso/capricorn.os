section .bss
    memory resb 32 * 1024 * 1024 * 1024 
section .text
global _start

_start:
    mov rdi, memory
    mov rcx, 32 * 1024 * 1024 * 1024
    xor rax, rax ; Set all bytes to 0
    rep stosb

    
    mov rax, 60 ; syscall: exit
    xor rdi, rdi ; status: 0
    syscall
    
