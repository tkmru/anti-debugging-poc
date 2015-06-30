# include <stdio.h>
# include <windows.h>

int main(void){
    HANDLE hOlly = FindWindow(TEXT("OLLYDBG"), NULL);

    if(hOlly){
        printf("fuck you ollydbg\n");
        _exit(-1);
    }

    printf("no debugger\n");

    return 0;
} 