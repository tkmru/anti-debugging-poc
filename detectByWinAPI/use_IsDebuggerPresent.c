# include <stdio.h>
# include <windows.h>

int main(void){
    if (IsDebuggerPresent()){
        printf("fuck you debugger");
        _exit(-1);
    }

    printf("no debugger\n");

    return 0;
}