#include <stdio.h>
#include <unistd.h>
#include <string.h>

#define MAXSIZE 100

int main(){

    int p2c[2], c2p[2];
    pid_t pid;
    char msg[MAXSIZE], reply[MAXSIZE];

    if (pipe(p2c) == -1 || pipe(c2p) == -1 || (pid = fork()) < 0){
        perror("Error!");
        return 1;
    }

    if (pid){
        close(p2c[0]); close(c2p[1]);
        printf("Parent, Enter your message: ")
        fgets(msg, MAXSIZE, stdin);
        write(p2c[1], msg, strlen(msg) + 1);
        read(c2p[0], reply, MAXSIZE);
        printf("Parent Received: %s\n", reply);
    }
    else{
        close([p2c[1]]); close(c2p[0]);
        read(p2c[0], reply, MAXSIZE);
        printf("Child Received: 5s\n", reply);
        printf("Child, Entre your response: ");
        fgets(msg, MAXSIZE, stdin);
        write(c2p[1], msg, strlen(msg) + 1);
    }
    return 0;
}