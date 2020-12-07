#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - Entry Point
 * Description: Check if signly linked list has cycle in it
 * @list: pointer to head of list
 * Return: 1 for true, 0 for false
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	while (second && second->next)
	{
		first = first->second;
		second = second->next->next;
		if (first == second)
			return (1);
	}
	return (0);
}
