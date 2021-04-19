def validation(card):
    n = len(card)
    if('-' not in card and n!=16):
        return False
    elif('-' in card and n!=19):
        return False
    elif(card[0] not in '456'):
        return False
    else:
        if('-' in card):
            numb = card.split('-')
            if(len(numb)!=4):
                return False
            else:
                vali = []
                for n in numb:
                    if( not n.isnumeric() ):
                        return False
                    if(len(n)!=4):
                        return False
                    else:
                        vali.extend(n)
                
                st = []
                for i in vali:
                    if(i in st):
                        st.append(i)
                        if(len(st)>=4):
                            return False
                    else:
                        st = []
                        st.append(i)
                return True
                
        else:
            if(not card.isnumeric()):
                return False
            st = []
            for i in card:
                if(i in st):
                    st.append(i)
                    if(len(st)>=4):
                        return False
                else:
                    st = []
                    st.append(i)
                    
            return True
                
card = input()
print( validation(card) )