#include <stdio.h>
#include <sys/ptrace.h>

int main() {
    if (ptrace(PTRACE_TRACEME, 0, 1, 0) == -1) {
        printf("fuck you gdb !!\n");
        return 1;
    }

    printf("outside gdb.\n");

    return 0;
}