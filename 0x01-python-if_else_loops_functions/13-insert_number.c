#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

/**
* insert_nodeint_at_index - interts a new node at given index position
*
* @head: pointer to the start of the list.
* @idx: index position to add new node.
* @n: data.
*
* Return: returns the address of the new node.
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *temp = *head;
	int i = 0;
if (head == NULL)
{
	return (NULL);
}

new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
{
	return (NULL);
}

if (number == 0)
	{
	new_node->next = *head;
	*head = new_node;
	new_node->n = number;
	return (new_node);
	}

while (temp != NULL)
{
	if (i == number - 1)
	{
	new_node->next = temp->next;
	temp->next = new_node;
	new_node->n = number;
	return (new_node);
	}
	temp = temp->next;
	i++;
}
return (NULL);
}