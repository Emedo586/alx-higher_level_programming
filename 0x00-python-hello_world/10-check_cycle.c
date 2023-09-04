#include "lists.h"

/***
 * check_cycle - checks for linked list contained in a cycle.
 * @list: linked list to check
 * Return: 0 if list has a cycle, 1 if doesn't.
 */
int check_cycle(listint_t *list)
{
listint_t *steady = list;
listint_t *rapid = list;

if (!list)
return(0);
while (steady && rapid && rapid->next)
{
steady = steady->next;
rapid = rapid->next->next;
if (steady == rapid)
return (1);
}
return (0);
}
