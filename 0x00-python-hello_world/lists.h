#ifndef LISTS_H
#define LIST_H

#include <stdlib.h>
/**
 *struct listint_s - singly linked list
@n: integer
@next: points to the next node
description: singly linked list mode structure
*/
typedef struct listint_s
{
	int d;
	struct listint_s *next;
}listint_t

size_t print_listint(const listint_t *k);
listint_t *add_nodeint(listint_t **head, const int d);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /*LISTS_H*/
