#include <stdio.h>
#include <unistd.h>

/*
This method is old. It cannot work in recent enviroment.
*/

int main(){
    FILE* fd = fopen("/tmp", "r");
    if(fileno(fd) > 3){
        printf("fuck you gdb !!\n");
        _exit(1);
    }
    printf("outside gdb.\n");
    return 0;
}