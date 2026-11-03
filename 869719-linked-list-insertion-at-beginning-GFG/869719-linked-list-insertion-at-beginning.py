class Solution:
    def insertAtFront(self, head, x):
        newNode = Node(x)
        newNode.next = head
        return newNode


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna