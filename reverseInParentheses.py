def reverseInParentheses(s):
    length = len(s)
    stack = []
    list = []
    for i in range(length):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            list.append(stack.pop())
            list.append(i)
    i = 0
    length_list = len(list)
    print
    while i < length_list:
        s = s[:list[i]] +"  " + s[(list[i] + 1 ): list[i + 1]][::-1] + s[(list[i + 1])+1:]
        i += 2
    return s.replace("  ","")
    
    
 
 def reverseInParentheses(s):
    return eval('"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')
    
    
 
 
  def reverseInParentheses(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
        if s[i] == ")":
            end = i
            return reverseInParentheses(s[:start] + s[start+1:end][::-1] + s[end+1:])
    return s


def reverseInParentheses(inputString):
    stack = []
    for x in inputString:
        if x == ")":
            tmp = ""
            while stack[-1] != "(":
                tmp += stack.pop()
            stack.pop() # pop the (
            for item in tmp:
                stack.append(item)
        else:
            stack.append(x)
    
    return "".join(stack)
