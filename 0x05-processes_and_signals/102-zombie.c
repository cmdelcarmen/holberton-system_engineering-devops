#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <unistd.h>

int infinite_while(void);

/**
 * main - function creates 5 zombie processes
 * Return: 0
 */
int main(void)
{
	int id, count, status;

	for (count = 0; count < 5; count++)
	{
		id = fork();

		if (id != 0 || id == -1)
			printf("Zombie process created, PID: %i\n", id);
		wait(&status);
	}

	infinite_while();

	return (0);
}

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
