class Solution:
    def deleteNode(self, head, x):
        if head is None:
            return None

        if x == 1:
            return head.next

        temp = head

        for i in range(x - 2):
            temp = temp.next

        temp.next = temp.next.next

        return head
        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna