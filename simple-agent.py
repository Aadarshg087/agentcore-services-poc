def add_numbers(a, b):
    return a + b

class SimpleAgent:
    def __init__(self, name="HelperAgent"):
        self.name = name

    def think(self, user_message):
        """
        The agent decides what to do based on user input
        """

        if "add" in user_message.lower():
            return "USE_TOOL"
        else:
            return "RESPOND"

    def use_tool(self, user_message):
        """
        Extract numbers from the text and use the tool.
        Very simple logic just for demonstration.
        """
        words = user_message.split()
        numbers = []
        for w in words:
            if w.isdigit():
                numbers.append(int(w))

        if len(numbers) >= 2:
            result = add_numbers(numbers[0], numbers[1])
            return f"The answer is {result}"
        else:
            return "I couldn't find the two numbers to add."
        
    def respond(self, user_message):
        """
        The agent gives simple language response
        """
        return f"You said: {user_message}. I'm here to help!"
    
    def run(self, user_message):
        """
        Main agent loop
        """
        decision = self.think(user_message)

        if(decision == "USE_TOOL"):
            return self.use_tool(user_message)
        else:
            return self.respond(user_message)
        
    
agent = SimpleAgent()

print(agent.run("Hello Agent"))
print(agent.run("Please add 4 and 6"))

