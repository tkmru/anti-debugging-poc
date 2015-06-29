# include <stdio.h>

int main(void) {

    unsigned int time1 = 0;
    unsigned int time2 = 0;
    
    __asm__(
        "RDTSC\n\t"
        "MOV %0, %%EAX\n\t"
        "RDTSC\n\t"
        "MOV %1, %%EAX\n\t"
        : "=&r" (time1)
        : "r" (time2)
    );

    if ((time2 - time1) > 100) {
        printf("%s", "VM detected");
        _exit(-1);
    }

    printf("%s", "VM not present");

    return 0;
}