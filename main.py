from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations 
    like insertion, recursion-based sum, search, and reverse.
    """

    # TODO: 1) Create a LinkedList instance
    linked_list = LinkedList()

    # TODO: 2) Insert some sample data using insert_at_front or insert_at_end
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)
        # - Consider a helper function that:
        #   1. Takes the current node and previous node as arguments.
        #   2. If the current node is None, sets head to previous node.
        #   3. Otherwise, recursively calls itself with current.next and current.next set to previous.
        """""
        self.head = self._reverse_recursive(self.head, None)

    def _reverse_recursive(self, current, previous):
        if current is None:
            return previous
        next_node = current.next
        current.next = previous
        return self._reverse_recursive(next_node, current)

    # TODO: 3) Display the list to verify insertion
    linked_list.display()

    # TODO: 4) Call recursive_sum and print the result
    print("Sum:", linked_list.recursive_sum())

    # TODO: 5) Call recursive_search with a target and print result
    target = 2
    print("Search:", linked_list.recursive_search(target))
        """

    # TODO: 6) Call recursive_reverse, then display the reversed list
    linked_list.recursive_reverse()
    linked_list.display()


# 