#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

/**
* insert_node - interts a new node
*
* @head: pointer to the start of the list.
* @number: data.
*
* Return: returns the address of the new node.
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *temp = *head;

new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
{
	return (NULL);
}

	new_node->n = number;
	new_node->next = NULL;
if (*head == NULL || temp->n > new_node->n)
{
	new_node->next = *head;
	*head = new_node;
	return (new_node);
}

while (temp->next != NULL)
{
	if (((temp->next->n > new_node->n) && (temp->n < new_node->n))
	|| (new_node->n == temp->n))
	{
	new_node->next = temp->next;
	temp->next = new_node;
	return (new_node);
	}
	temp = temp->next;
}
new_node->next = temp->next;
temp->next = new_node;
return (new_node);
}
