; the ai will now calculate the size of your mother

section .data
    msg db "The size of your mother is: ", 0
section .text
    global _start
_start:
    ; print the message
    mov eax, 4          ; syscall: sys_write
    mov ebx, 1          ; file descriptor: stdout
    mov ecx, msg        ; message to write
    mov edx, 27         ; message length
    int 0x80            ; call kernel
    ; exit the program
    mov eax, 1          ; syscall: sys_exit
    xor ebx, ebx        ; status: 0
    int 0x80            ; call kernel


; lets see how well it did