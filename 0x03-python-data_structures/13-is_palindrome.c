#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - function to call verify_pal to see if list is palindrome
 * @head: ptr to the beginning of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);

	if ((*head)->next == NULL)
		return (1);

	return (verify_pal(head, *head));
}

/**
 * verify_pal - function to verify if the list is palindrome
 * @head: beginning of the list
 * @last: end of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int verify_pal(listint_t **head, listint_t *last)
{
	if (last == NULL)
		return (1);
	if (verify_pal(head, last->next) && (*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
