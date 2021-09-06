#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
  * check_cycle - checkes whether there is a loop or not
  * @list: head of the linked list
  * Return: 1 if cycle found else 0
  */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast  = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
