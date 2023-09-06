#include "lists.h"


/**
 * insert_mode - inserts a number into a singly -linked list
 * @head: pointer to the head
 * @number:  number to insert
 *
 * @Return: NULL if function fails otherwise pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *node = *head, *new;
*new = malloc(sizeof(listint_t));
if (!new)
return (NULL);

new->n = number;
new->next = NULL;

if(!node || new->n < node->n)
{
new->next = node;
return (*head = new;);
}
while (!node)
{
if (!node->next || new->n < node->next->n)
{
new->next = node->next;
node->next = new;
return (node);
}
node = node->next;
}
return (NULL);
}
