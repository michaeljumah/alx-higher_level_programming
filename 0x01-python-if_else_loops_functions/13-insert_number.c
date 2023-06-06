#include "lists.h"
#include <stdlib.h>

/**
  * insert_node - Inserts a number into a sorted singly linked list
  * @head: The head of the sorted singly linked list
  * @number: The number to inserts in the singly linked list
  *
  * Return: The singly linked list with the new number added
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = NULL, *newnode = NULL, *temp = NULL;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);

	newnode->n = number;
	if (*head)
	{
		current = *head;
		if (number <= current->n)
		{
			newnode->next = current;
			*head = newnode;
		}
		else
		{
			while (current->next)
			{
				if (number <= current->next->n)
				{
					temp = current->next;
					current->next = newnode;
					newnode->next = temp;
					return (*head);
				}

				current = current->next;
			}
			temp = current->next;
			current->next = newnode;
			newnode->next = temp;
		}
		return (*head);
	}
	newnode->next = NULL;
	*head = newnode;
	return (*head);
}
