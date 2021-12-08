#Created by Ryan Villarreal

class Netlist:
    def init(self, expr, findComp, findNodes, genNetlist):

        self.expr = expr
        self.complist = self.findComp(expr)
        self.nodelist = self.findNodes(self.complist)
        self.netlist = genNetlist(self.nodelist)

    def switch(argument):
        switcher = {
            1: "AND",
            2: "OR",
            3: "NOT",
        }
        print(switcher.get(argument, "Invalid gate"))  

    def findComp(expr):
        components = []
        gates = []
        st = []
        last = []

        gates.append("F")
        for i in expr:
            if((not st.includes(expr[i])) and expr.isalpha(expr[i])):
                st.append(expr[i])

        for i in range(len(st)):
            item = st[i]
        st = []

        for i in expr:
            gate = ''
            if(expr.isalpha(expr[i])):
                st.append(expr[i])
            else:
                op1 = st.pop()
                op2 = st[len(st) - 1]

                if(expr[i] == "'"):
                    gate = op1 + expr[i]
                    st.append(gate)
                    break
                elif(expr[i] == "*"):
                    gate = op1

                    if (last == expr[i]):            #Handle successive operations ie. Multi input OR
                        while (len(st) > 0):
                            gate += st.pop()
                    else:
                        gate += st.pop() + expr[i];                                                                                
                        st.push(gate)
                    break
                else:
                    print("Invalid input")

            if(expr[i] == last):
                gates.pop()
                gates.push(gate)
                last = expr[i]

        for i in range(len(gates)):
            item, index = components.append(new component)(item, index))